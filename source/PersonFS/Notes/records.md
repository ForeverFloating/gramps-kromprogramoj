

# query the 1836 Dordogne census


## using a web browser

### general form for the collection:
https://www.familysearch.org/search/collection/2821307
### by film number:

### search for Champagne-et-Fontaine:
https://www.familysearch.org/search/record/results?count=20&q.anyPlace=Champagne-et-Fontaine%2C%20Dordogne%2C%20Nouvelle-Aquitaine%2C%20France&q.anyPlace.exact=on&f.collectionId=2821307


## using the collection API:
https://api.familysearch.org/platform/records/collections/2821307
--> returns the description + the list of fields
note: Champagne-et-Fontaine: EVENT_PLACE=
"place" : {
        "original" : "Champagne-et-Fontaine, Dordogne, Aquitaine, France",
        "description" : "#place_6816919",
        "fields" : [ {
          "type" : "http://gedcomx.org/Place",
          "values" : [ {
            "confidence" : "http://confidence/85",
            "type" : "http://gedcomx.org/Interpreted",
            "labelId" : "EVENT_PLACE",
            "text" : "Champagne-et-Fontaine, Dordogne, Aquitaine, France",
            "resource" : "https://www.familysearch.org/platform/places/description/6816919",
            "qualifiers" : [ {
              "value" : "1011;1010;1013",
              "name" : "StdQualifier"
            }, {
              "value" : "France, Dordogne, Champagne-et-Fontaine",
              "name" : "Context"
            } ]
          } ]
        } ]}

# searching for a collection by its title:
https://www.familysearch.org/service/search/catalog/v2/search?count=20&query=%2Btitle%3AFrance%20%2Btitle%3ADordogne%20%2Btitle%3ARegistres%20%2Btitle%3AParoissiaux%20%2Btitle%3Aet%20%2Btitle%3AEtat%20%2Btitle%3ACivil%20%2Btitle%3A1540%20%2Btitle%3A1896%20%2Bavailability%3AOnline
