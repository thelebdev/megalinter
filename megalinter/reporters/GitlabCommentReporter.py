#!/usr/bin/env python3
"""
Gitlab Comment reporter
Post a comment on Gitlab Merge Requests
"""
import logging

import gitlab
from megalinter import Reporter, config
from megalinter.pre_post_factory import run_command
from megalinter.utils_reporter import build_markdown_summary


class GitlabCommentReporter(Reporter):
    name = "GITLAB_COMMENT"
    scope = "mega-linter"

    gitlab_server_url = "https://gitlab.com"

    def manage_activation(self):
        if config.get("GITLAB_COMMENT_REPORTER", "true") != "true":
            self.is_active = False
        elif (
            config.get("POST_GITLAB_COMMENT", "true") == "true"
        ):  # Legacy - true by default
            self.is_active = True

    def produce_report(self):
        # Post comment on Gitlab pull request
        if config.get("CI_JOB_TOKEN", "") != "":
            gitlab_repo = config.get("CI_PROJECT_NAME")
            gitlab_project_id = config.get("CI_PROJECT_ID")
            gitlab_merge_request_id = config.get("CI_MERGE_REQUEST_ID", "")
            if gitlab_merge_request_id == "":
                if config.get("CI_OPEN_MERGE_REQUESTS", "") != "":
                    gitlab_merge_request_id = (
                        config.get("CI_OPEN_MERGE_REQUESTS", "missing!missing")
                        .split(",")[0]
                        .split("!")[1]
                    )
                else:
                    logging.info(
                        "[Gitlab Comment Reporter] No merge request has been found, so no comment has been posted"
                    )
                    return

            gitlab_server_url = config.get("CI_SERVER_URL", self.gitlab_server_url)
            action_run_url = config.get("CI_JOB_URL", "")
            p_r_msg = build_markdown_summary(self, action_run_url)

            # Build gitlab options
            gitlab_options = {}
            # auth token
            if config.get("GITLAB_ACCESS_TOKEN_MEGALINTER", "") != "":
                gitlab_options["private_token"] = config.get(
                    "GITLAB_ACCESS_TOKEN_MEGALINTER"
                )
            else:
                gitlab_options["job_token"] = config.get("CI_JOB_TOKEN")
            # Certificate management
            gitlab_certificate_path = config.get("GITLAB_CERTIFICATE_PATH", "")
            if config.get("GITLAB_CUSTOM_CERTIFICATE", "") != "":
                # Certificate value defined in an ENV variable
                cert_value = config.get("GITLAB_CUSTOM_CERTIFICATE")
                gitlab_certificate_path = "/etc/ssl/certs/gitlab-cert.crt"
                with open(gitlab_certificate_path, "w", encoding="utf-8") as cert_file:
                    cert_file.write(cert_value)
                    logging.debug(
                        f"Updated {gitlab_certificate_path} with certificate value {cert_value}"
                    )
            if gitlab_certificate_path != "":
                # Update certificates and set cert path in gitlab options
                run_command(
                    {"cwd": "root", "command": "update-ca-certificates"},
                    "GitlabCommentReporter",
                    self.master,
                )
                gitlab_options["ssl_verify"] = gitlab_certificate_path
            # Create gitlab connection
            logging.debug(
                f"[GitlabCommentReporter] Logging to {gitlab_server_url} with {str(gitlab_options)}"
            )
            gl = gitlab.Gitlab(gitlab_server_url, **gitlab_options)
            # Get gitlab project
            try:
                project = gl.projects.get(gitlab_project_id)
            except gitlab.GitlabGetError as e:
                logging.warning(
                    "[Gitlab Comment Reporter] No project has been found with "
                    f"id {gitlab_project_id}, so no comment has been posted\n"
                )
                self.display_auth_error(e)
                return
            except Exception as e:
                self.display_auth_error(e)
                return

            # Get merge request
            try:
                mr = project.mergerequests.get(gitlab_merge_request_id)
            except gitlab.GitlabGetError:
                gitlab_merge_request_id = config.get("CI_MERGE_REQUEST_IID", "none")
                try:
                    mr = project.mergerequests.get(gitlab_merge_request_id)
                except gitlab.GitlabGetError as e:
                    logging.warning(
                        "[Gitlab Comment Reporter] No merge request has been found with "
                        f"id {gitlab_merge_request_id}, so no comment has been posted\n"
                    )
                    self.display_auth_error(e)
                    return
                except Exception as e:
                    self.display_auth_error(e)
                    return

            # Ignore if PR is already merged
            if mr.state == "merged":
                return

            # List comments on merge request
            existing_comment = None
            try:
                existing_comments = mr.notes.list()
            except gitlab.GitlabAuthenticationError as e:
                self.display_auth_error(e)
                return
            except Exception as e:
                self.display_auth_error(e)
                return

            # Check if there is already a MegaLinter comment
            for comment in existing_comments:
                if (
                    "See detailed report in [MegaLinter reports" in comment.body
                    or "See detailed report in MegaLinter reports" in comment.body
                ):
                    existing_comment = comment

            # Process comment
            try:
                # Edit if there is already a Mega-Linter comment
                if existing_comment is not None:
                    existing_comment.body = p_r_msg
                    existing_comment.save()
                # Or create a new PR comment
                else:
                    mr.notes.create({"body": p_r_msg})
                logging.debug(f"Posted Gitlab comment: {p_r_msg}")
                logging.info(
                    f"[Gitlab Comment Reporter] Posted summary as comment on {gitlab_repo} #MR{mr.id}"
                )
            except gitlab.GitlabError as e:
                logging.warning(
                    "[Gitlab Comment Reporter] Unable to post merge request comment"
                )
                self.display_auth_error(e)
            except Exception as e:
                logging.warning("[Gitlab Comment Reporter] Error while posting comment")
                self.display_auth_error(e)
        # Not in gitlab context
        else:
            logging.debug(
                "[Gitlab Comment Reporter] No Gitlab Token found, so skipped post of MR comment"
            )

    def display_auth_error(self, e):
        logging.error(
            "[Gitlab Comment Reporter] You may need to define a masked Gitlab CI/CD variable "
            "GITLAB_MEGALINTER_ACCESS_TOKEN containing a personal token with scope 'api'\n"
            "(if already defined, your token is probably invalid)\n"
            "If you are using local certificate, you also may need to define variables "
            "GITLAB_CUSTOM_CERTIFICATE or GITLAB_CERTIFICATE_PATH" + str(e)
        )
