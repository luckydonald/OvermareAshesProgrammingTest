#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
__author__ = 'luckydonald'

import re
from mercurial import error
from mercurial.ui import ui as MercurialUI


ISSUE_REGEX = re.compile(r'#\d+')
ERROR_MESSAGE = b'Commit description is Missing Hacknplan task ID (e.g. #123)'


def check_commit_message_has_issue_number_hook(ui, repo, **kwargs):
    """
    Checks a single commit message for to have a issue number (Format: `#\d+`) in it.

    To use add the following to your project .hg/hgrc for each
    project you want to check, or to your (global( user hgrc to apply to all projects.

    ```
    [hooks]
    pretxncommit.hello-hg = python:path/to/script/hello-hg.py:check_commit_message_has_issue_number_hook
    ```

    :type ui: MercurialUI
    """
    hg_commit_message = repo['tip'].description()

    if not check_commit_message_has_issue_number(hg_commit_message):
        continue_anyway = ui.promptchoice(ERROR_MESSAGE + b"\nIgnore and continue? (yN)" + repr(hg_commit_message) + "  $$ &Yes $$ &No", default=1) == 0
        if not continue_anyway:
            raise error.Abort(ERROR_MESSAGE + ": User aborted commit.")
        # end if
    # end if
    return 0  # linux error codes, so 0/False/None = ok, True/1 = error
# end def


def check_commit_message_has_issue_number(commit_message_text):
    """
    Check if the message contains a issue reference somewhere.

    >>> check_commit_message_has_issue_number(b'foo bar #1234 bar foo')
    True

    >>> check_commit_message_has_issue_number(b'#1234 bar foo')
    True

    >>> check_commit_message_has_issue_number(b'#1234 bar foo')
    True

    >>> check_commit_message_has_issue_number(b"First line\\nSecond line\\nLast line with #1234 reference.")
    True

    >>> check_commit_message_has_issue_number(b"#1234.")
    True

    >>> check_commit_message_has_issue_number(b"prefix#1234")
    True

    >>> check_commit_message_has_issue_number(b"#1234suffix")
    True

    >>> check_commit_message_has_issue_number(b"#.1234")
    False

    >>> check_commit_message_has_issue_number(b"# 1234")
    False

    >>> check_commit_message_has_issue_number(b"Issue #a")
    False

    :param commit_message_text: The commit message to check
    :type  commit_message_text: bytes
    :return:
    """
    match = ISSUE_REGEX.search(commit_message_text)
    return bool(match)
# end def
