#! /usr/bin/env python

# Copyright (c) 2011 Victor Terron. All rights reserved.
# Institute of Astrophysics of Andalusia, IAA-CSIC
#
# This file is part of phone.
#
# phone is free software: you can redistribute it and/or modify
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

import distutils.core

distutils.core.setup (name = 'phone',
                      version = '0.9',
                      description = "White pages of the IAA-CSIC",
                      author = 'Victor Terron',
                      author_email = 'vterron@iaa.es',
                      url = 'http://www.iaa.es/~vterron/',
                      license = "GNU General Public License, version 3 (GPLv3)",
                      scripts = ['phone'])
