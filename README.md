# movie-recommender

Movie recommendation system with a knowledge-based approach.
Designed as a project for EECS 371 Knowledge Representation &amp; Reasoning at Northwestern University.

##Knowledge

The knowledge used for this system is from the MovieLens latest dataset downloaded on 02/20/2019.
We are using the small dataset as it will allow us to develop our project quickly without concern for scalability and performance optimization.
Data from MovieLens is not included in this repository as we do not have the rights to redistribute.
We also used the OMDB (Open Movie Database) to supplement the data from MovieLens.

##Knowledge

We transformed the raw data from the sources mentioned above into krf.
This allowed us to use Companions and the Fire for querying and inference.

##Files

There are three files that compose our microtheory: omdb.krf, movies.krf, and recommendMovies.krf.

`omdb.krf` contains the knowledge we collected from OMDB and MovieLens.
`movies.krf` contains the definitions of predicates that our group defined related to movies that supplement those already found in Cyc.
`recommendMovies.krf` contains the Horn Clauses that define the reasoning for the movie recommendations.


##Horn Clauses

**(recommendMovieName ?inputMovie ?recommendedMovie)** finds movies that are similar and have the same rating where the recommended movie also satisfies at least one of the recommendation types.

**(recommendMovieName ?inputMovieName ?recommendedMovieName ?rating)** finds movies that are similar where the recommended movie has the specified rating and where the recommended movie satisfies at least one of the recommendation types.

#Recommendation Types

**(criticFavorite ?inputMovie ?criticMovie ?rating)** indicates that the inputMovie and criticMovie are similar and that criticMovie is a critic favorite on Metacritic

**(fanFavorite ?movie ?movieToFind ?rating)** indicates that the inputMovie and movieToFind are similar and that movieToFind is a fan favorite on IMDB

**(academyFavorite ?inputMovie ?academyFavorite)** indicates that the inputMovie and academyFavorite are similar and that academyFavorite has won an Academy Award.

##Example Queries

**(recommendMovieName "Toy Story" ?recommended)** will return all movies that are similar to and have the same rating as Toy Story.
Pocahontas is fan favorite movie that is recommended by this query.

**(recommendMovieName "Toy Story ?recommended" PG-13)** will return all PG-13 movies that are similar to Toy Story.
Batman Forever is fan favorite movie that is recommended by this query.

## Links

- [MovieLens dataset](files.grouplens.org/datasets/movielens/ml-latest-small.zip)
- [OMBD API](omdbapi.com)
