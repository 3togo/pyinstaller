# Copyright (C) 2007, Matteo Bertini
# Based on previous work under copyright (c) 2001, 2002 McMillan Enterprises, Inc.
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA


# Compare attributes of cElementTree module from frozen executable
# with cElementTree module from standard python.

print "Used to fail if _xmlplus is installed"


import sys
import subprocess
import xml.etree.ElementTree as ET

print "#" * 50
print "xml.etree.ElementTree", dir(ET)
print "#" * 50
import xml.etree.cElementTree as cET

pyexe = open("python_exe.build").readline().strip()

out = subprocess.Popen([pyexe, '-c',
        'import xml.etree.cElementTree as cET; print dir(cET)'],
        stdout=subprocess.PIPE, shell=False).stdout.read().strip()

assert str(dir(cET)) == out, (str(dir(cET)), out)
