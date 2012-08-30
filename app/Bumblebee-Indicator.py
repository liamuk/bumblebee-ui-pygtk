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

# UI MODULE
import pygtk
pygtk.require('2.0')
import gtk
import gobject
import pynotify

# SYSTEM MODULE
import os
import subprocess

# ORIGINAL CLASS
import Config

class BumblebeeIndicator():
    def notify_state(self, title, msg, icon_name):
        pynotify.init("Bumblebee notification")
        self.notification= pynotify.Notification(title, msg)
        self.notification.set_urgency(pynotify.URGENCY_LOW)
        self.notification.set_timeout(5000)
        self.notification.show()

# INITIALIZATION OF INDICATOR AND MENU
    def __init__(self):
        self.indicator = gtk.StatusIcon() 
        self.indicator.set_from_file("%s/bumblebee-indicator.svg" % Config.icon_file_directory )
        self.indicator.set_tooltip(Config.attention_label)        

        self.card_state=False
        self.lock_file = "/tmp/.X%s-lock" % Config.vgl_display
        
    def quit(self, widget, data=None):
        gtk.main_quit()

# FUNCTIONS TO CHECK FOR THE STATE OF THE INDICATOR
    def initial_state_checker(self):
        if self.attention_state_condition(): self.set_attention_state(notify=False)
        else : self.set_active_state(notify=False)

    def state_checker(self):
        if self.attention_state_condition():
            if not self.card_state: self.set_attention_state()
        elif self.card_state: self.set_active_state()	
        return True
	
    def attention_state_condition(self):
        return os.path.exists(self.lock_file)

# FUNCTIONS TO SET THE STATE OF THE INDICATOR AND LAUNCH NOTIFICATION
    def set_attention_state(self, notify=True):
        self.set_status(True, 
                        Config.attention_label, 
                        Config.attention_comment, 
                        "bumblebee-indicator-active", notify)

    def set_active_state(self, notify=True):
        self.set_status(False,
                        Config.active_label, 
                        Config.active_comment,  
                        "bumblebee-indicator", notify)
    
    def set_status(self, status, label, comment, icon, notify):
        self.indicator.set_from_file("%(dir)s/%(file)s.svg" % {"dir": Config.icon_file_directory, "file": icon})
        self.indicator.set_tooltip(label)
        self.card_state = status
        if notify: self.notify_state(label, comment, icon)
        try:
			self.switch.set_label(label)
        	self.switch.set_active(status)
		except AttributeError:
       		pass
 
# MAIN LOOP LAUNCHING A STATE CHECK EVERY TWO SECONDS
    def main(self):
        self.state_checker()
#FIXME It would be nice to avoid this loop : Maybe by using a signal emitted by the system
        #gtk.timeout_add(2000,self.state_checker)
        gobject.timeout_add_seconds(2, self.state_checker)
        gtk.main()

if __name__ == "__main__":
    indicator = BumblebeeIndicator()
    indicator.main()

