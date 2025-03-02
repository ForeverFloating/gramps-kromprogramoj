#
# Gramplet - PlaceFrCog (Place : France : Code Officiel Géographique)
#
# Copyright (C) 2022 Jean Michault
# GNU General Public License v3.0 or later
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#

#------------------------------------------------------------------------
#
# PlaceFrCog Gramplet
#
#------------------------------------------------------------------------

register(GRAMPLET,
         id = "PlaceFrCog Gramplet",
         name = _("Lokoj : Franca Oficiala Geografia Kodo"),
         description = _("Gramplet por preni municipojn de la datumbazo Insee"),
         status = STABLE,
         fname = "placefrcog.py",
         height = 375,
         expand = True,
         gramplet = 'PlaceFrCog',
         gramplet_title = _("Fr COG"),
         detached_width = 510,
         detached_height = 480,
         version = '1.0.34',
         gramps_target_version = '5.2',
         include_in_listing = True,
        )
