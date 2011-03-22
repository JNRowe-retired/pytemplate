#
"""Per-package configuration data"""
# Copyright (C) 2008-2011  James Rowe <jnrowe@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import {{ module }}
MODULE = {{ module }}

import {{ script}}
SCRIPTS = [{{ script }}, ]

DESCRIPTION = MODULE.__doc__.splitlines()[0][:-1]
LONG_DESCRIPTION = "\n\n".join(MODULE.__doc__.split("\n\n")[1:3])

KEYWORDS = []
CLASSIFIERS = []

OBSOLETES = []

GRAPH_TYPE = None

TEST_EXTRAGLOBS = {}

SCM = "git"
