# -*- coding: utf-8 -*-

# Copyright (C) 2005-2008,2010 Osmo Salomaa
#
# This file is part of Gaupol.
#
# Gaupol is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# Gaupol is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# Gaupol. If not, see <http://www.gnu.org/licenses/>.

import aeidon
import gaupol

from gi.repository import Gtk

from .test_file import _TestFileDialog


class TestMultiSaveDialog(_TestFileDialog):

    @aeidon.deco.silent(gaupol.Default)
    def run__show_overwrite_question_dialog(self):
        self.dialog._show_overwrite_question_dialog(3, "test")

    def run_dialog(self):
        self.dialog.run()
        self.dialog.destroy()

    def setup_method(self, method):
        self.application = self.new_application()
        self.application.add_page(self.new_page())
        self.application.add_page(self.new_page())
        self.dialog = gaupol.MultiSaveDialog(Gtk.Window(), self.application)
        self.dialog.show()

    def test__on_response__cancel(self):
        self.dialog.response(Gtk.ResponseType.CANCEL)

    @aeidon.deco.monkey_patch(gaupol.util, "flash_dialog")
    def test__show_overwrite_question_dialog(self):
        gaupol.util.flash_dialog = lambda dialog: Gtk.ResponseType.YES
        self.dialog._show_overwrite_question_dialog(3, "test")

    def test_get_format(self):
        for format in aeidon.formats:
            self.dialog.set_format(format)
            value = self.dialog.get_format()
            assert value == format

    def test_get_newline(self):
        for newline in aeidon.newlines:
            self.dialog.set_newline(newline)
            value = self.dialog.get_newline()
            assert value == newline

    def test_set_format(self):
        for format in aeidon.formats:
            self.dialog.set_format(format)
            value = self.dialog.get_format()
            assert value == format

    def test_set_newline(self):
        for newline in aeidon.newlines:
            self.dialog.set_newline(newline)
            value = self.dialog.get_newline()
            assert value == newline
