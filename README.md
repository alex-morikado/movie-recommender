# movie-recommender

Movie recommendation system with a knowledge-based approach.
Designed as a project for EECS 371 Knowledge Representation &amp; Reasoning at Northwestern University.

## Knowledge

The knowledge used for this system is from the MovieLens latest dataset downloaded on 02/20/2019.
We are using the small dataset as it will allow us to develop our project quickly without concern for scalability and performance optimization.
Data from MovieLens is not included in this repository as we do not have the rights to redistribute.
We also used the OMDB (Open Movie Database) to supplement the data from MovieLens.

## Knowledge

We transformed the raw data from the sources mentioned above into krf.
This allowed us to use Companions and the Fire for querying and inference.

## Files

There are three files that compose our microtheory: omdb.krf, movies.krf, and recommendMovies.krf.

`omdb.krf` contains the knowledge we collected from OMDB and MovieLens.
`movies.krf` contains the definitions of predicates that our group defined related to movies that supplement those already found in Cyc.
`recommendMovies.krf` contains the Horn Clauses that define the reasoning for the movie recommendations.


## Horn Clauses

**(recommendMovieName ?inputMovie ?recommendedMovie)** finds movies that are similar and have the same rating where the recommended movie also satisfies at least one of the recommendation types.

**(recommendMovieName ?inputMovieName ?recommendedMovieName ?rating)** finds movies that are similar where the recommended movie has the specified rating and where the recommended movie satisfies at least one of the recommendation types.

### Recommendation Types

**(criticFavorite ?inputMovie ?criticMovie ?rating)** indicates that inputMovie and criticMovie are similar and that criticMovie is a critic favorite on Metacritic.

**(fanFavorite ?inputMovie ?fanFavMovie ?rating)** indicates that inputMovie and fanFavMovie are similar and that fanFavMovie has a large number of ratings on IMDB.

**(academyFavorite ?inputMovie ?academyFavorite)** indicates that inputMovie and academyFavorite are similar and that academyFavorite has won an Academy Award.

**(oldies ?inputMovie ?oldMovie)** indicates that inputMovie and oldMovie are similar and that oldMovie was released before 1980.

**(hiddenGems ?inputMovie ?hiddenGemMovie)** indicates that inputMovie and hiddenGemMovie are similar and that hiddenGemMovie has few IMDB ratings and a high Metacritic score.

**(foreignLanguage ?inputMovie ?foreignLanguageMovie)** indicates that inputMovie and foreignLanguageMovie are similar and that foreignLanguageMovie was not published in English.

## Example Queries

**(recommendMovieName "Toy Story" ?recommended)** will return all movies that are similar to and have the same rating as Toy Story.
Pocahontas is fan favorite movie that is recommended by this query.

**(recommendMovieName "Toy Story ?recommended" PG-13)** will return all PG-13 movies that are similar to Toy Story.
Batman Forever is fan favorite movie that is recommended by this query.

## Notes on the omdb_downloader
The requests library for python must be installed.
Alternatively, one could modify the code to use urllib2 to make the http request.
```
pip install requests
```
Also if you must have a keys.py file with a single line:
```
omdb = YOUR_API_KEY
```
Where you replace YOUR_API_KEY with your OMDB API key.
Use the link below to learn more about the OMDB API and generate an API key.

The MovieLens data, which you can download using the link below, is expected to be unzipped and one directory above the code file.
If you would like to keep the MovieLens data in a different directory as `omdb_downloader.py`, modify the filepath in line 5 of `omdb_downloader.py`
The output filename can also be modified as needed.
Finally, the number of lines to read is also specified in `omdb_downloader.py`.
Running this file will download a krf file of the first LINES_TO_READ - 1 movies in the MovieLens dataset.


## Links

- [MovieLens dataset](http://files.grouplens.org/datasets/movielens/ml-latest-small.zip)
- [OMBD API](http://omdbapi.com)
