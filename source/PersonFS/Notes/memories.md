
How to compare FS memories with Gramps media?

note: using the service interface is easier for getting information:
https://www.familysearch.org/service/memories/presentation/artifacts/197051022?includeAssociatedArtifacts=true&includeDatesPlaces=true&includeContactName=true&_=1726156704965&profile=skeleton


# Gramps media properties:
 * visible properties:
   * Identifier(gramps\_id), title(desc), date, path(path), tags, type(mime)
   * attributes
   * citations
   * notes
 * hidden properties: checksum.
the "thumbnail" needs to be stored, otherwise previews might display an outdated version.

# Gramps media reference properties:
 * visible properties:
   * media
   * reference: type, handle
   * private?
   * rectangle
   * attributes
   * citations
   * notes
 * hidden properties: none.

# FS memory properties:
 * Evidence class
   * id
   * resourceId: the part before '-' represents the SourceDescription ID.
   * resource
   * links
 * SourceDescription class
   * id
   * about: link to the image
   * descriptions (set)
   * artifactMetadata (set)
   * links: links to:
     * artifact, comments, coverage, image, image-deep-zoom-lite, image-icon, image-thumbnail, memory, persons, …
   * mediaType (e.g.: 'image/jpeg')
   * titles: title(s)
   * coverage: set of Coverage:
     * spatial: PlaceReference = place
     * temporal: Date
   * …
 * artifactMetaData class
   * filename, width, height, size

