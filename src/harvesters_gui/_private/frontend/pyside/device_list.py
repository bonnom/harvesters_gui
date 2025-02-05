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
from PySide6.QtWidgets import QComboBox

# Local application/library specific imports
from harvesters._private.core.observer import Observer
from harvesters_gui._private.frontend.pyside.helper import get_system_font


class ComboBoxDeviceList(QComboBox, Observer):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFont(get_system_font())

    def update(self):
        if self.parent().parent().harvester_core.has_revised_device_info_list:
            self.clear()
            separator = '::'
            for d in self.parent().parent().harvester_core.device_info_list:
                name = d.vendor
                name += separator
                name += d.model

                try:
                    _ = d.serial_number
                except:  # We know it's too broad:
                    pass
                else:
                    if d.serial_number != '':
                        name += separator
                        name += d.serial_number

                try:
                    _ = d.user_defined_name
                except:  # We know it's too broad:
                    pass
                else:
                    if d.user_defined_name != '':
                        name += separator
                        name += d.user_defined_name

                self.addItem(name)
        #
        self.parent().parent().harvester_core.has_revised_device_info_list = False

        #
        enable = False
        if self.parent().parent().cti_files:
            if self.parent().parent().ia is None:
                enable = True
        self.setEnabled(enable)
