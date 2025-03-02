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

from typing import Union

import sys
import re
import asyncio
import email.utils
import time
from urllib.parse import unquote

# gedcomx_v1 biblioteko. Instalu kun `pip install gedcomx_v1`
import gedcomx_v1

# local imports
from constants import (
    MAX_PERSONS,
)
from gedcomx_v1.dateformal import DateFormal

import gettext
_ = gettext.gettext

# ununura sesio uzata por ĉiuj «Tree»
_FsSeanco = None


class Tree(gedcomx_v1.Gedcomx):
  """ gedcomx_v1 tree class
  """
  def __init__(self):
    gedcomx_v1._utila.klaso_ini(self)
    self._fam = dict()
    self._places = dict()
    self._persons = dict()
    self._getsources = True
    self._sources = dict()
    self._notes = list()

  def add_persono(self, fid):
    r = _FsSeanco.get_url( "/platform/tree/persons/" + fid)
    if not r:
      return
    try:
      data = r.json()
    except Exception as e:
      print("WARNING: corrupted file from %s, error: %s" % (url, e))
      print(r.content)
      data = None

    if data:
      gedcomx_v1.maljsonigi(self,data)
      fsPersono = gedcomx_v1.Person._indekso[fid]
      if 'Last-Modified' in r.headers :
        fsPersono._last_modified = int(time.mktime(email.utils.parsedate(r.headers['Last-Modified'])))
      if 'Etag' in r.headers :
        fsPersono._etag = r.headers['Etag']
      self._persons[fid]=gedcomx_v1.Person._indekso[fid]

  def add_persons(self, fids):
    """add individuals to the family tree
    :param fids: an iterable of fid
    """
    async def sxargi_personoj(loop,fids):
      farindajxoj = set()
      for fid in fids :
        if fid not in self._persons.keys() :
          farindajxoj.add(loop.run_in_executor(None,self.add_persono,fid))
      for farindajxo in farindajxoj :
        await farindajxo
        
    loop = asyncio.get_event_loop()
    loop.run_until_complete( sxargi_personoj(loop,fids))

    for fid in fids :
      if fid in gedcomx_v1.Person._indekso :
        self._persons[fid]=gedcomx_v1.Person._indekso[fid]

  def add_parents(self, fids):
    """add parents relationships
    :param fids: a set of fids
    """
    rels = set()
    for fid in fids & self._persons.keys():
      for paro in self._persons[fid]._gepatroj :
        if paro.person1 : rels.add(paro.person1.resourceId)
        if paro.person2 : rels.add(paro.person2.resourceId)
      for cp in self._persons[fid]._gepatrojCP :
        if cp.parent1 : rels.add(cp.parent1.resourceId)
        if cp.parent2 : rels.add(cp.parent2.resourceId)
    rels.difference_update(fids)
    self.add_persons(rels)
    return set(filter(None, rels))

  def add_spouses(self, fids):
    """add spouse relationships
    :param fids: a set of fid
    """
    rels = set()
    for fid in fids & self._persons.keys():
      fsPersono = self._persons[fid]
      if hasattr(fsPersono,'_paroj') and fsPersono._paroj :
        for paro in fsPersono._paroj :
          if paro.person1 : rels |= {paro.person1.resourceId}
          if paro.person2 : rels |= {paro.person2.resourceId}
    rels.difference_update(fids)
    self.add_persons(rels)
    return set(filter(None, rels))

  def add_children(self, fids):
    """add children relationships
    :param fids: a set of fid
    """
    rels = set()
    for fid in fids & self._persons.keys():
      fsPersono = self._persons[fid]
      if hasattr(fsPersono,'_infanoj') and fsPersono._infanoj :
        for paro in fsPersono._infanoj :
          rels |= {paro.person1.resourceId , paro.person2.resourceId }
    rels.difference_update(fids)
    self.add_persons(rels)
    return set(filter(None, rels))

  #def get_marriage_notes(self,ids):
    #"""retrieve marriage notes"""
    #if self.fid:
    #    notes = _FsSeanco.get_jsonurl(
    #        "/platform/tree/couple-relationships/%s/notes" % self.fid
    #    )
    #    if notes:

  #def add_marriage(self, fid):
    #"""retrieve and add marriage information
    #:param fid: the marriage fid
    #"""
    #if not self.fid:
    #    self.fid = fid
    #    url = "/platform/tree/couple-relationships/%s" % self.fid
    #    data = _FsSeanco.get_jsonurl(url)
  #def get_notes(self,id):
    #"""retrieve individual notes"""
    #notes = _FsSeanco.get_jsonurl("/platform/tree/persons/%s/notes" % self.id)
    #if notes:
  #def get_person_contributors(self,id):
    #"""retrieve contributors"""
    #temp = set()
    #url = "/platform/tree/persons/%s/changes" % self.id
    #data = _FsSeanco.get_jsonurl(url, {"Accept": "application/x-gedcomx-atom+json"})
    #if data:
  #def
    #    # FARINDAĴO : portrait
    #    #if "links" in data:
    #    #    req = _FsSeanco.get_jsonurl(
    #    #        "/platform/tree/persons/%s/portrait" % self.id
    #    #        , {"Accept": "image/*"}
    #    #    )
    #    #    if req and req.text:
  #def
    #    if "evidence" in data:
    #        url = "/platform/tree/persons/%s/memories" % self.id
    #        memorie = _FsSeanco.get_jsonurl(url)
    #        if memorie and "sourceDescriptions" in memorie:
  #def get_person_contributors(self):
    #"""retrieve contributors"""
    #temp = set()
    #url = "/platform/tree/persons/%s/changes" % self.id
    #data = _FsSeanco.get_jsonurl(url, {"Accept": "application/x-gedcomx-atom+json"})
  #def add_marriage(self, fid):
    #"""retrieve and add marriage information
    #:param fid: the marriage fid
    #"""
    #if not self.fid:
    #    self.fid = fid
    #    url = "/platform/tree/couple-relationships/%s" % self.fid
    #    data = _FsSeanco.get_jsonurl(url)
    #    if data:
