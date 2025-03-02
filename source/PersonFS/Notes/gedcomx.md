# sources
"official" doc: (but not up to date)
https://github.com/FamilySearch/gedcomx/blob/master/specifications/json-format-specification.md
https://github.com/FamilySearch/gedcomx/blob/master/specifications/conceptual-model-specification.md

a little more practical, but incomplete (when I looked at it, for example, the Event and Document classes were missing, which are nevertheless "top level":
https://www.familysearch.org/developers/docs/api/gx_json
https://www.familysearch.org/developers/docs/api/fs_json

unsurprisingly familysearch does not follow its own standard, it adds classes and fields, and it ignores some of them…

# convert the types to python type:
boolean                 --> bool
string                  --> str
map of array of string  --> dict[str,set]   (identifiers)
map of Link             --> dict[str,Link]  (links)
array                   --> set
class                   --> class
array of class          --> set[class]

# list of gedcomx classes:

## base class of the gedcomx file:
* Gedcomx(HypermediaEnabledData)

## "top level" classes:
* Person(Subject)
* Relationship(Subject)
* SourceDescription(HypermediaEnabledData)
* Agent(HypermediaEnabledData)
* Event(Subject)
* PlaceDescription(Subject)
* Document(Conclusion)

## classes that are essentially string enumerations:
ConfidenceLevel
FactType
GenderType
NamePartType
NameType
RelationshipType
ResourceType

## classes that do not inherit from another class:
* ExtensibleData	implements id
* HasDateAndPlace (used for ?)
* HasFacts (used for ?)
* HasNotes (used for ?)
* HasText (used for ?)
* Link
* Qualifier
* ReferencesSources (used for ?)
* ResourceReference   (creates and manages an index ?)
* TextValue
* VocabElement
* VocabElementList

## classes inheriting from one other class and serving as the base for other classes:
* HypermediaEnabledData(ExtensibleData)
* Conclusion(HypermediaEnabledData)
* Subject(Conclusion)

## other classes
* Address(ExtensibleData)
* Attribution(ExtensibleData)
* Coverage(HypermediaEnabledData)
* Date(ExtensibleData)
* DisplayProperties(ExtensibleData)
* EvidenceReference(HypermediaEnabledData)
* Fact(Conclusion)
* FamilyView(HypermediaEnabledData)
* Gender(Conclusion)
* Name(Conclusion)
* NameForm(ExtensibleData)
* NamePart(ExtensibleData)
* Note(HypermediaEnabledData)
* OnlineAccount(ExtensibleData)
* PlaceDisplayProperties(ExtensibleData)
* PlaceReference(ExtensibleData)
* SourceCitation(HypermediaEnabledData)
* SourceReference(HypermediaEnabledData)

## FS additions:
* PersonInfo
* CitationField: no documentation ???
