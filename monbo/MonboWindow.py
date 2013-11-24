# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

from locale import gettext as _

from gi.repository import Gtk # pylint: disable=E0611
import logging
logger = logging.getLogger('monbo')

from monbo_lib import Window
from monbo.AboutMonboDialog import AboutMonboDialog
from monbo.PreferencesMonboDialog import PreferencesMonboDialog

# See monbo_lib.Window.py for more details about how this class works
class MonboWindow(Window):
    __gtype_name__ = "MonboWindow"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the main window"""
        super(MonboWindow, self).finish_initializing(builder)

        self.AboutDialog = AboutMonboDialog
        self.PreferencesDialog = PreferencesMonboDialog

        # Code for other initialization actions should be added here.

