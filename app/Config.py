#!/usr/bin/python2
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
#
# This file is part of bumblebee-ui.
#
# bumblebee-ui is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# bumblebee-ui is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with bumblebee-ui. If not, see <http://www.gnu.org/licenses/>.
#
### END LICENSE

import os
import gtk

#ICONS FILE PATH
icon_file_directory = '/usr/share/icons/hicolor/48x48/apps/'

#BUMBLEBEE DEFAULT CONFIGURATION
config_file_path='/etc/bumblebee/bumblebee.conf'
#GET BUMBLEBEE CONFIGURATION VALUE
def get_config_value(variable_name):
    """Function to get configuration value inside a shell script"""
    for line in open(config_file_path):
        if variable_name in line:
            return line.split('=',1)[1].replace("\n","")

vgl_display= get_config_value('VirtualDisplay').replace(":","")

#CATEGORIES CONFIGURATION

#NOTIFICATION MESSAGES :
#TODO Revert when the possibility to turn off the card is back
attention_label="Discrete GPU: ON"
attention_comment=""
active_label="Discrete GPU: OFF"
active_comment=""

#TODO : There might be a way to use string formatting to simplify the config definition
#FIXME There must be a better way to store config

if __name__=="__main__" : 
    print "Config.py can't run as a standalone application"
    quit()

