#!/usr/bin/env python3
# ----------------------------------------------------------------------------
#
# Copyright 2018 EMVA
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# ----------------------------------------------------------------------------


# Standard library imports

# Related third party imports
from PySide6.QtGui import QFont

# Local application/library specific imports
from harvesters._private.core.helper.system import is_running_on_macos, \
    is_running_on_windows


def get_system_font():
    if is_running_on_windows():
        font, size = 'Calibri', 12
    else:
        if is_running_on_macos():
            font, size = 'Lucida Sans Unicode', 14
        else:
            font, size = 'Sans-serif', 11
    return QFont(font, size)
