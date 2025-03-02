
How to best transfer notes from Gramps to FS?
And vice versa?

# In Gramps:
* A Note can be referenced by:
  * a person
  * a family
  * an event
  * an event reference
  * a name
  * …
* the same note can be referenced in multiple places.
* a note consists of:
  * an id
  * a type
  * text
  * tags

# In FS:
* A Note can be attached to:
  * a person
  * a family
  * …
* a note cannot be reused.
* a note consists of:
  * an id
  * a title
  * text
  * "attribution" (= author and last modified date)
  *  if it's a person's note: an alert tag (boolean) (only one person note can be an alert note)
* "Explanations" (= changeMessage) can be considered notes. They can be attached to:
  * an event/fact
  * a spouse
  * a name
  * …
* the "Brief biological narrative" could be considered a note, but FS treats it as a fact.

# transfer process
* for person and family notes:
  * Gramps type <--> FS title
  * Gramps text <--> FS text
  * assumption is made that type/title is unique per person or family (though this is often not true in either Gramps or FS…)
* for event/event reference and name notes
  * concatenate Gramps (type+texte), sorted by type <--> FS changeMessage.
