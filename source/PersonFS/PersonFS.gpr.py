#
# Gramplet - fs (familysearch)
#
# Copyright (C) 2022 Jean Michault
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

#------------------------------------------------------------------------
#
# FS Gramplet
#
#------------------------------------------------------------------------

register(GRAMPLET,
         id = "FS Gramplet",
         name = _("PersonFS"),
         description = _("interfaco por FamilySearch"),
         status = STABLE,
         fname="PersonFS.py",
         height=100,
         expand=True,
         gramplet = 'PersonFS',
         gramplet_title=_("FS"),
         detached_width = 500,
         detached_height = 500,
         version = 'beta 2.0.50',
         gramps_target_version= '5.2',
         navtypes=["Person"],
         requires_mod=["gedcomx_v1","packaging","requests"],
         )

register(TOOL,
    id    = 'Importo de FamilySearch',
    name  = _("Importo de FamilySearch datumoj"),
    description =  _("FamilySearch."),
    version = 'beta 2.0.50',
    gramps_target_version = '5.2',
    status = STABLE,
    fname = 'Importo.py',
    category = TOOL_DBPROC,
    toolclass = 'FSImporto',
    optionclass = 'FSImportoOpcionoj',
    tool_modes = [TOOL_MODE_GUI],
    requires_mod=["gedcomx_v1","packaging","requests"],
)

register(TOOL,
    id    = 'FamilySearch komparo',
    name  = _("FamilySearch : kompari"),
    description =  _("FamilySearch : kompari gramps personojn kun FS personojn."),
    version = 'beta 2.0.50',
    gramps_target_version = '5.2',
    status = STABLE,
    fname = 'komparo.py',
    category = TOOL_DBPROC,
    toolclass = 'FSKomparo',
    optionclass = 'FSKomparoOpcionoj',
    tool_modes = [TOOL_MODE_GUI],
    requires_mod=["gedcomx_v1","packaging","requests"],
)
