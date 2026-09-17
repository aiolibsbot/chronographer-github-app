"""Shared test helpers."""

from io import StringIO

import pytest
from unidiff import PatchSet


@pytest.fixture()
def make_diff():
    """Return a factory turning unified diff text into a patch set."""
    return lambda diff_text: PatchSet(StringIO(diff_text))


ADDED_FRAGMENT_DIFF = """\
diff --git a/news/123.bugfix b/news/123.bugfix
new file mode 100644
--- /dev/null
+++ b/news/123.bugfix
@@ -0,0 +1 @@
+Fixed a thing
"""


REMOVED_FRAGMENT_DIFF = """\
diff --git a/news/123.bugfix b/news/123.bugfix
deleted file mode 100644
--- a/news/123.bugfix
+++ /dev/null
@@ -1 +0,0 @@
-Fixed a thing
"""


CHANGELOG_ADDITION_DIFF = """\
diff --git a/NEWS.rst b/NEWS.rst
--- a/NEWS.rst
+++ b/NEWS.rst
@@ -1,2 +1,4 @@
 Changelog
 =========
+
+Fixed a thing
"""


SOURCE_CHANGE_DIFF = """\
diff --git a/src/app.py b/src/app.py
--- a/src/app.py
+++ b/src/app.py
@@ -1,2 +1,2 @@
 import os
-x = 1
+x = 2
"""
