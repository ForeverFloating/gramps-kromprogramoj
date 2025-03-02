	; FSID with non-standardized place: LR24-CQK

# places in FamilySearch:

search: <https://www.familysearch.org/research/places/>

can be classified in two ways:
* PlaceDescription : the "places" attribute of the gedcomx class.
	describes standardized places.
  * the ID retrieves the full description from <https://api.familysearch.org/platform/places/description/ID>
    * from there, the FamilySearch place link can be retrieved: <https://api.familysearch.org/platform/places/ID2>
  * names: localized names.
* PlaceReference: used in all other cases. For example, the place attribute of the Fact class.
	important attributes:
  * description: contains the standardized place ID in the format #ID (if the place is standardized)
  * original: the text as entered
  * normalized: the standardized name (note the language), for France it is usually (but not always) in the format "commune, department, region, country"
  * names: localized names.

Standardized places usually only have commune-level precision. To specify a more precise location, use the "original" field. For example, using the Geneanet recommendation for French locations, enter in the "original" field: "[place-name or precision] - commune, code_insee, departement, region, country."
 Verification: Enter "#ID" in the description field.
 A place from <https://www.familysearch.org/research/places/> can also be created
 Only the following types can be created:
 * 115: School
 *  20: Cemetery
 * 308: Neighborhood
 *  38: Farm
 *  23: Place of worship (excluding temples of The Church of Jesus Christ of Latter-Day Saints!!!)
 * 391: Village = smaller than type 376, has a shop.
 * 376: Town = A local division of human settlement often incorporated administratively, larger than a village but smaller than a city. An official designation for township in several of the United States including New England and parts of the midwest.
 * 201: Commune
 * 186: City = A more or less extensive and permanent artificial settlement with developed systems for land use, housing, transportation, and government.
 * 266: Hamlet
 * 378: Canton (Township)
 * 142: Hospital
The following types can only be created by FamilySearch:
 * County
 * Country
 * Province
 * Region
 * State

list of place types: <https://www.familysearch.org/platform/places/types>.
Some descriptions are not translated into French. See <https://www.familysearch.org/platform/places/types?lang=en> for English descriptions.
Some relevant place types in France:
 * type 580 = Country
 * type 337 = Region
 * type 209 = County (pre-Revolution)
 * type 215 = Department

 * type 172 = Canton
 * type 201 = Commune
 * type 186 = City
 * type 171 = Municipal Arrondissement
 * type 140 = Populated Places
 * 115: School
 *  20: Cemetery
 * 308: Neighborhood
 *  38: Farm
 *  23: Place of worship (excluding temples of The Church of Jesus Christ of Latter-Day Saints!!!)
 * 391: Village = smaller than type 376, has a shop.
 * 266: Hamlet
 * 142: Hospital


Important: there are two types of IDs:
 * place-description ID = used for  https://api.familysearch.org/platform/places/description/ID. Used in the "Gedcomx" and "Fact" classes. Corresponds to the gedcomx.PlaceDescription class.
 * place ID = used for https://api.familysearch.org/platform/places/ID
   * multiple place-description IDs can point to the same place ID.
   * <https://api.familysearch.org/platform/places/ID> retrieves a list of "place-descriptions", which may include temporla variations.
   * no corresponding gedcomx class found.


A place can have duplicates. Example for Angoulême:
 * ID = 10978745 (Commune, certified); type=201; fullname = "Angoulême, Charente, Nouvelle-Aquitaine, France"
 * ID = 5953317 (Commune, acepted); type=201; fullname = "Angoulême, Charente, Nouvelle-Aquitaine, France"
   Has canton-type children???:
   * 9517845; type = 172; fullname = "Aubeterre-sur-Dronne, Angoulême, Charente, Nouvelle-Aquitaine, France"
   * 9517842; type = 172; fullname = "Blanzac-Porcheresse, Angoulême, Charente, Nouvelle-Aquitaine, France"
 * ID = 10905243 (Commune, accepted); type=201 ; fullname = "Angoulême, Charente, Poitou-Charentes, France"
 * ID = 6824318 (Populated places, accepted)
 * ID = 10743639 (City, certified) ; type=186
   * part of 10709047; type=209; name = "Angoumois"

Question: what do non-standardized places look like?

# correspondance with Gramps
## Problem 1: sorting the Gramps ID <--> FamilySearch ID.
 * chosen solution = use Internet links: create a link, type="FamilySearch", addr = https://api.familysearch.org/platform/places/description/ID. A place can have multiple links.

## Problem 2: places where the "original" property is more precise than "normalized"
Creating a child place of the normalized place would be necessary, but only when "original" provides more detail than "normalized."
To be addressed later. For now, the normalized place will be used.


## equivalence of FamilySearch and Gramps types
| code        | Name         | FS code          | notes |
| ----------- | ------------ | ---------------- | ----- |
|COUNTRY      | Country      | 580              | sovereign state
|STATE        | State        | 362              | federal state
|COUNTY       | County       | 209,521          | 209 = ruled by a county, 521 = English, Swedish, Romanian county
|CITY         | City         | 186              |
|PARISH       | Parish       | 312              |
|LOCALITY     | Locality     |                  |
|STREET       | Street       |                  |
|PROVINCE     | Province     | 323              |
|REGION       | Region       | 337              |
|DEPARTMENT   | Departement  | 215              |
|NEIGHBORHOOD | Neighborhood | 308              |
|DISTRICT     | District     | 221              | American district, Arrondissement départemental
|BOROUGH      | Borough      | 171              | Municipal arrondissement
|MUNICIPALITY | Municipality | 201              | = French commune
|TOWN         | Town         | 376              |
|VILLAGE      | Village      | 391              |
|HAMLET       | Hamlet       | 266              |
|FARM         | Farm         | 38               |
|BUILDING     | Building     | 23, 61, 115, 142 |
|NUMBER       | Number       |                  |

Usual FS types without clear equivalents:
 * 172 = Canton
 * 140 = Populated places
 *  20 : Cemetery



# correspondance with INSEE codes
API address: https://adresse.data.gouv.fr/api-doc/adresse
API COG: https://www.data.gouv.fr/fr/datasets/code-officiel-geographique-cog/
  note: former communes are not included.
COG files: https://www.insee.fr/fr/information/2560452

Administrative divisions:
* country = COUNTRY = 580
* region = REGION = 337
* department = DEPARTMENT = 215
	, part of a region
* territorial collectivity
	, part of a region
    e.g.: departmental councils
* arrondissement ~ DISTRICT ~ 221
	, part of a department
* canton, part of a department
* commune = MUNICIPALITY = 201

# correspondence with GeoNames

