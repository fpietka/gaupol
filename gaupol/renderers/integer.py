# -*- coding: utf-8 -*-

# Copyright (C) 2009-2010 Osmo Salomaa
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

"""Cell renderer for integer data."""

import aeidon

from gi.repository import GObject
from gi.repository import Gtk

__all__ = ("IntegerCellRenderer",)


class IntegerCellRenderer(Gtk.CellRendererText):

    """Cell renderer for integer data."""

    __gtype_name__ = "IntegerCellRenderer"

    def __init__(self):
        """Initialize a :class:`IntegerCellRenderer` object."""
        GObject.GObject.__init__(self)
        aeidon.util.connect(self, self, "editing-started")

    def _on_editing_started(self, renderer, editor, path):
        """Set `editor` to use same font as `self`."""
        editor.modify_font(self.props.font_desc)
