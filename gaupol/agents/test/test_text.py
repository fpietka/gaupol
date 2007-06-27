# Copyright (C) 2007 Osmo Salomaa
#
# This file is part of Gaupol.
#
# Gaupol is free software; you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# Gaupol is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# Gaupol; if not, write to the Free Software Foundation, Inc., 51 Franklin
# Street, Fifth Floor, Boston, MA 02110-1301, USA.


import gaupol
from gaupol import unittest


class TestTextAgent(unittest.TestCase):

    def format_lines(self):

        dialogue_pattern = gaupol.scripts.get_dialogue_separator("latin")
        clause_pattern = gaupol.scripts.get_clause_separator("latin")
        self.project.format_lines(
            indexes=None,
            doc=gaupol.DOCUMENT.MAIN,
            dialogue_pattern=dialogue_pattern,
            clause_pattern=clause_pattern,
            ok_dialogue=3,
            ok_clauses=2,
            max_length=32,
            length_func=len,
            legal_length=46,
            legal_lines=2,
            require_reduction=True)

    def setup_method(self, method):

        self.project = self.get_project()

    def test_capitalize(self):

        self.project.subtitles[0].main_text = "test. test."
        pattern = gaupol.scripts.get_capitalize_after("latin")
        self.project.capitalize(None, gaupol.DOCUMENT.MAIN, pattern)
        assert self.project.subtitles[0].main_text == "Test. Test."

    def test_format_lines__legal_lines_and_legal_length(self):

        # Liner would break this to one clause per line.
        self.project.subtitles[0].main_text = \
            "You have stolen salami from\n" + \
            "me. Be careful what you say."
        self.format_lines()
        assert self.project.subtitles[0].main_text == \
            "You have stolen salami from\n" + \
            "me. Be careful what you say."

    def test_format_lines__require_reduction(self):

        # Liner would break this to one clause per line.
        self.project.subtitles[0].main_text = \
            "You have stolen salami. You\n" + \
            "have stolen salami. You have\n" + \
            "stolen salami."
        self.format_lines()
        assert self.project.subtitles[0].main_text == \
            "You have stolen salami. You\n" + \
            "have stolen salami. You have\n" + \
            "stolen salami."