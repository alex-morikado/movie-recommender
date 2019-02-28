# movie-recommender

Movie recommendation system with a knowledge-based approach. Designed as a project for EECS 371 Knowledge Representation &amp; Reasoning at Northwestern University.

The knowledge used for this system is from the MovieLens latest dataset downloaded on 02/20/2019. We are using the small dataset as it will allow us to develop our project quickly without concern for scalability and performance optimization. Data is not included in this repository as we do not have the rights to redistribute.

## Workflow

1. Generate RDF
    - download MovieLens data to `./ml-latest-small`
    - run `csv-parser.py` to generate formatted csv file
    - convert formatted csv to rdf
2. Start SPARQL server with RDF
    - `java -jar PATH/TO/fuseki-server.jar --file RDF_FILEPATH /ENDPOINT_NAME`
3. Test queries
4. Save queries in repo
    - save to `.rq` file

## Links

- [MovieLens dataset](files.grouplens.org/datasets/movielens/ml-latest-small.zip)
- [Apache Jena Fuseki](https://jena.apache.org/download/)
- [CSV to RDF converter](http://levelup.networkedplanet.com/)

## Cyc stuff

### Collections

- [Movie-CW](https://gavotte.cs.northwestern.edu/rbrowse/kbb-frameset.html?concept-id=11&kb=1)
  - specs:
    - ActionMovie
    - AdventureMovie
    - AIGoneWrongMovie
    - AnimatedMovie
    - BatmanMovie
    - BiblicalEpicMovie
    - ChildrensMovie
    - ClassicMovie
    - ComedyMovie
    - CrimeMovie
    - CultMovie
    - Documentary-Genre
    - DocumentaryFilm
    - DramaticMovie
    - EducationalMovie
    - ExperimentalMovie
    - FamilyMovie
    - FantasyMovie
    - FilmNoirMovie
    - ForeignMovie
    - GeneralRating
    - HistoricalNarrativeMovie
    - HorrorMovie
    - IMAXMovie
    - IndependentMovie
    - Movie-CW
    - Movie-Silent
    - MysteryMovie
    - NC-17Rating
    - NotYetRatedRating
    - ParentalGuidance13Rating
    - ParentalGuidanceRating
    - PornographicMovie
    - RestrictedRating
    - RomanceMovie
    - SatireMovie
    - ScienceFictionMovie
    - SportsMovie
    - StarWarsMovie
    - SupermanMovie
    - SuspenseMovie
    - TeenMovie
    - ThrillerMovie
    - WarMovie
    - WesternMovie
    - XRating
    - (FreeThingOfTypeFn Movie-CW)
- [ActorInMovies](https://gavotte.cs.northwestern.edu/rbrowse/kbb-frameset.html?concept-id=1285&kb=1)
- [Director-Movie](https://gavotte.cs.northwestern.edu/rbrowse/kbb-frameset.html?concept-id=1372&kb=1)
- [Producer-Movie](https://gavotte.cs.northwestern.edu/rbrowse/kbb-frameset.html?concept-id=1410&kb=1)
- [MPAAAdvisoryClassification-Film](https://gavotte.cs.northwestern.edu/rbrowse/kbb-frameset.html?concept-id=159&kb=1)
  - instances:
    - GeneralRating
    - NC-17Rating
    - NotYetRatedRating
    - ParentalGuidance13Rating
    - ParentalGuidanceRating
    - RestrictedRating
    - XRating

### Relations

- [movieProducer](https://gavotte.cs.northwestern.edu/rbrowse/kbb-frameset.html?concept-id=64&kb=1)
- [movieDirector](https://gavotte.cs.northwestern.edu/rbrowse/kbb-frameset.html?concept-id=62&kb=1)
- [movieReleaseYear](https://gavotte.cs.northwestern.edu/rbrowse/kbb-frameset.html?concept-id=65&kb=1)
- [movieAdvisoryRating](https://gavotte.cs.northwestern.edu/rbrowse/kbb-frameset.html?concept-id=61&kb=1)
- [movieTitleString](https://gavotte.cs.northwestern.edu/rbrowse/kbb-frameset.html?concept-id=71&kb=1)
- [movieGenres](https://gavotte.cs.northwestern.edu/rbrowse/kbb-frameset.html?concept-id=63&kb=1)
- [movieActors](https://gavotte.cs.northwestern.edu/rbrowse/kbb-frameset.html?concept-id=59&kb=1)

### Functions

- [MoviesDirectedByFn](https://gavotte.cs.northwestern.edu/rbrowse/kbb-frameset.html?kb=1)
- [MoviesStarringFn](https://gavotte.cs.northwestern.edu/rbrowse/kbb-frameset.html?concept-id=49&kb=1)
- [MovieNamedFn](https://gavotte.cs.northwestern.edu/rbrowse/kbb-frameset.html?concept-id=46&kb=1)

## Need to Define

### Relations

- movieRuntime
- movieLanguage
- movieCountry
- movieMetascore
- movieWriter