
* note: merged FSID: GZKW-DLY,GJ7P-84L;
        ; FSID George Washington: KNDX-MKG
	; FSID with multiple parents: 9CSJ-L2D (lacour-pijardière: official and biological father)
	; FSID with non-standardized location: LR24-CQK
	; FSID with date range: LTY2-RSM
	; FSID with date before:  KZCP-RPL (Meints, Roelof)
	; FSID with "Short biographical sketch": LRVF-9YS
    ; FSID with individual note: LRVF-HBK
# issues:
  * copying a marriage contract to FS: this does not work because FS only accepts the following marriage events: "Marriage," "Divorce," "Annulment," "Common-law," "Lived together," "No children."
    * --> create a marriage event with an explanation stating that it is a contract?
	  this is the chosen solution: add the explanation :"http://gedcomx.org/MarriageContract\nMarriage contract."
    * --> create a "Common-law" event with an explanation stating it is a contract?
    * --> link these other events to spouses? (this is how FamilySearch handles it)
    * --> convert other events into notes (problem: notes lack dates, these must be added to the text)?
  * same for: engagement
  * copying person and family notes from Gramps to FS.
  * copying sources to FS: this must be done twice, the first source is created but not linked.
  * setting the language during transfers to FS. Especially for names.

# to do for the next version
## priorities
* bugs:
  * updating a source in FamilySearch: the note is not updated.
  * updating a source in Gramps: to be investigated.
  * copying a source to Gramps: "None" in the citation note if there is no note.
  * copying a source to FS: link to the couple when the source is attached to the couple or a couple's event.
  * individual search: problems with the second search?
  * importing praents: does not consider relationship type
    * e.g.: GP83-PXQ : Athanaze Lamothe, fostered by Jean Nadal x Jeanne Daza.
  * refreshing is needed after transferring a child to FS.
  * years in short dates: convert French Republican dates (see Libaros, Jean: his son Frix is displayed as 0005-1882 instead of 1797-1882)
  * if the FS connection is lost: reconnect properly (currently, a second refresh is required).
  * comparison: FSID G6M3-79W: the spouse does not appear because there is no marital link in FS.
  * comparison: comparing marriages does not use FSFTID
  * importing a date A/+1736 (not supported in Gramps).
  * comparison: the filter list is the one from the initial launch.
  * 1-click import: sometimes not all the children are imported.
  * birth events without dates are not shown in Gramps?
  * syncing a date "to xxxx" becomes "about xxxx-00-00" instead of "about xxxx"
* other Gramplet issues:
  * when transferring to FS, specify the language.
  * copying a marriage contract to FS: instead of "marriage," use "common-law" marriage
     (Alternative marriage in Gramps)
  * copying marriage banns to FS: handle as you would contracts and engagements.
  * during FS creation: after creating the person, transfer the person's events.
  * add the FSFTID for any events missing this identifier during comparison.
  * transfer a child from Gramps to FS.
  * allow manual entry of a person's \_FSTID
  * if a group row is checked: check the entire group.
  * if a parent, child, or spouse is checked:
    * if missing in FS but has an FSFTID: accept.
    * if missing in FS FS and no FSFTID: prompt the user to verify the record and confirm.
    * if absent from Gramps: search for FSFTID in Gramps.
      * if absent: suggest importing.
      * if present: accept.
  * if sex is checked: suggest manual correction.
  * compare locations.
  * if there is a sync error: display a message.
* search:
  * creation in FS:
    * link to parents and children that exist in FS
    * after creation: also transfer facts and names.
  * more criteria (at least death: date + place of death, and general location)
* import:
  * do not start if there is no FSID.
  * standardize first/last names (uppercase and lowercase).
  * import/update object IDs: event, family, source, citation.
  * manage automatic linking of parents, spouses, and children if they already exist, rather than making duplicates.
  * always check "Do not re-import existing people" by default
* French translation
* update documentation
## optional
* import a child, spouse, or parent individually.
* maintain a person.fsid-handle dictionary.
* maintain place.fsid-handle dictionary.
* gedcomx: unknown attributes:
  * Person:Principal, ex.: LR2N-SRM
  * Tag:conclusionId G8FW-VTJ
* run sync in background?
* what if a person has two \_FSFTID attributes?
	those deleted in FS should be deleted.
* Gramplet:
  * refresh without rereading FS data after entry in Gramps?
  * copy the names to FS: ensuring the "preferred" designation is correct.
OA	attention: there sholud always be a preferred name on FS.
  * comparaison: manage the "living" flag on FamilySearch.
  * refresh: only reload the person if they have been modified.
  * linking spouses from FS to Gramps (the spouse must exist in Gramps, otherwise: an error message will be displayed).
* search:
  * import button in the search bar?
  * hide or disable the "Add" button if the \_FSFTID attribute is populated
	otherwise, display a warning.
  * is search accessible from the menu?
  * search: load more results
* identify and manage prerequisites (requests, gedcomx\_v1)
* sync:
  * speed up processing:
    * multi-threaded launch (async?)
  * required information:
    * source to attach.
    * note to attach.
* do not connect to FamilySearch before the DB opens
* import:
  * manage StillBirth events (= stillborn child)?
  * speed up loading notes and sources.

# to do for version 2

* refresh when switching modes.
* Gramps bug if a checkbox in a treeview is checked: `sudo sed -i 's/int(path)/path/' /usr/lib/python3/dist-packages/gramps/gui/listmodel.py`
	--> this needs to be fixed by gramps-project: https://github.com/gramps-project/gramps/pull/1426
	--> I could then delete `mialistmodel.py`
* advanced place management during import, in the Gramplet, in gedcomx\_v1?
  - caution, place management is undergoing a major overhaul for Gramps 2.0…
* management of "memories"
* automatic linking module.
* chained manual linking module.
* duplicate detection module in Gramps based on FSID
* Gramplet:
  * linking a child or spouse on Gramps to a child or spouse in FS
  * source management
    problem: what is the best way to transfer sources from Grmaps to FS?
      - Gramps uses a repository --> source --> citation hierarchy, but this does not exist in FS.
      - see Notes/sources.txt
  * notes management
  * images and portraits management
* during import:
  * handling of "attributes"?
  * importig IDs for places, sources, Relationships, ChildAndParentsRelationship?
* nickname management to be determined
* syncing portraits between FS and gramps.
* syncing images between FS and gramps
* creating person profiles in FS: manage all names, sources, …
* deleting FS data within the Gramplet?
* deleting Gramps data within the Gramplet?
* records handling (= FS "records")
