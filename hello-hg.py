#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

__author__ = 'luckydonald'

import logging

logger = logging.getLogger(__name__)

import re
from mercurial import error


ISSUE_REGEX = re.compile(r'#\d+')


def check_commit_message_has_issue_number_hook(ui, repo, **kwargs):
    """
    Checks a single commit message for to have a issue number (Format: `#\d+`) in it.

    To use add the following to your project .hg/hgrc for each
    project you want to check, or to your (global( user hgrc to apply to all projects.

    [hooks]
    precommit = python:path/to/script/hello-hg.py:check_commit_message_has_issue_number_hook
    """
    hg_commit_message = repo['tip'].description()

    if not check_commit_message_has_issue_number(hg_commit_message):
        raise error.Abort("Commit description is Missing Hacknpan task ID (e.g. #123)")
    else:
        return True


def check_commit_message_has_issue_number(commit_message_text):
    """
    Check if the message contains a issue reference somewhere.

    >>> check_commit_message_has_issue_number('foo bar #1234 bar foo')
    True

    >>> check_commit_message_has_issue_number('#1234 bar foo')
    True

    >>> check_commit_message_has_issue_number('#1234 bar foo')
    True

    >>> check_commit_message_has_issue_number("First line\\nSecond line\\nLast line with #1234 reference.")
    True

    >>> check_commit_message_has_issue_number("#1234.")
    True

    >>> check_commit_message_has_issue_number("#1234a")
    False

    >>> check_commit_message_has_issue_number("#.1234")
    False

    >>> check_commit_message_has_issue_number("# 1234")
    False

    >>> check_commit_message_has_issue_number("Issue #a")
    False

    :param commit_message_text: The commit message to check
    :type  commit_message_text: str
    :return:
    """
    match = ISSUE_REGEX.search(commit_message_text)
    return bool(match)
# end def
