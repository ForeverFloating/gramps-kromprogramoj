#
# Copyright (C) 2023 Jean Michault
# GNU General Public License v3.0 or later
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the license, or
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


"""
Lokpurigado Gramplet.
"""

register(
    GRAMPLET,
    id = "Lokpurigado",
    name = _("Lokpurigado"),
    description = _("Lokpurigado helpas kompletigi lokojn uzante OpenStreetMap."),
    status = STABLE,
    version = '1.0.21',
    gramps_target_version = '5.2',
    fname = "lokpurigado.py",
    gramplet = 'Lokpurigado',
    navtypes=["Place"],
    height = 375,
    detached_width = 510,
    detached_height = 480,
    expand = True,
    gramplet_title = _("Lokpurigado"),
    help_url="Addon:Lokpurigado",
    include_in_listing = True,
    )
