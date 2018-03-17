"""
copyright (c) 2017 Ricardo Rodrigues All Rights Reserved
"""
import os
from gi.repository import Nautilus, GObject


class VSCodeExtension(GObject.GObject, Nautilus.MenuProvider):
    """ Extension that allows for the quick open of VSCode in a file or folder """

    def __init__(self):
        pass

    def menu_activate_cb(self, menu, input_file):
        """ Method called when menu item is clicked """
        os.system('/usr/share/code/code --new-window ' +
                  input_file.get_location().get_path().replace(" ", "\\ ") + ' &')

    def get_file_items(self, window, files):
        """ Method called when a right click occurs in Nautilus """
        if len(files) != 1:
            return

        input_file = files[0]

        item = Nautilus.MenuItem(
            name="VSCodeExtension::Open_with_VSCode",
            label="Open with VSCode",
            tip="Opens the file or folder with Visual Studio Code"
        )
        item.connect('activate', self.menu_activate_cb, input_file)

        return [item]
