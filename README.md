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