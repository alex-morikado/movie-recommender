import requests
import keys
import json

LINK_FILE_PATH = "ml-latest-small/links.csv"
OUTPUT_FILENAME = "omdb.krf"
BASE_URL = "https://www.omdbapi.com/?apikey=" + keys.omdb

LINES_TO_READ = 5

omdbCycMapping = {
    "Title":"movieTitleString",
    "Year":"movieReleaseYear",
    "Rated":"movieAdvisoryRating",
    "Genre":"movieGenres",
    "Director":"movieDirector",
    "Actors":"movieActors",
    "Runtime":"movieRuntime",
    "Language":"movieLanguage",
    "Country":"movieCountry",
    "Metascore":"movieMetascore",
    "Writer":"movieWriter"
    }

def make_omdb_request(id):
    return requests.get(BASE_URL, params={'i':"tt" + id})

def reduce_data(movie, fields=["Title", "Year", "Rated", "Runtime", "Genre", "Director", "Writer", "Actors", "Language", "Country", "Metascore"]):
    reduced = dict()
    for field in fields:
        reduced[field] = movie[field]

    if reduced.get("Title", False):
        reduced["Title"] = '"' + reduced["Title"].replace('"', "'") + '"'
    if reduced.get("Genre", False):
        reduced["Genre"] = reduced["Genre"].split(", ")
    if reduced.get("Writer", False):
        reduced["Writer"] = list(set([writer[0:writer.find('(')].strip() for writer in reduced["Writer"].split(", ")]))
    if reduced.get("Director", False):
        reduced["Director"] = reduced["Director"].split(", ")
    if reduced.get("Actors", False):
        reduced["Actors"] = reduced["Actors"].split(", ")
    if reduced.get("Language", False):
        reduced["Language"] = reduced["Language"].split(", ")
    if reduced.get("Runtime", False):
        reduced["Runtime"] = reduced["Runtime"][0:reduced["Runtime"].find(' ')]
    if reduced.get("Country", False):
        reduced["Country"] = reduced["Country"].split(', ')

    return reduced

def format_attribute(attribute):
    return attribute.replace(' ', '') if attribute.find('"') == -1 else attribute

def write_krf(entity, id, file):
    file.write('(isa ' + 'tt' + id + ' Movie-CW)\n')
    for key in entity:
        pred_and_id = '(' + omdbCycMapping.get(key, "movie" + key) + ' tt' + str(id)
        if type(entity[key]) == list:
            for attribute in entity[key]:
                file.write(pred_and_id + ' ' + format_attribute(attribute) + ')\n')
        else:
            file.write(pred_and_id + ' ' + format_attribute(entity[key]) + ')\n')
    file.write('\n')

def write_file(max_lines):

    link_file = open(LINK_FILE_PATH, 'r')
    output_file = open(OUTPUT_FILENAME, 'w')

    output_file.write('(in-microtheory Movie-Recommender)\n\n\n')
    #skip the first line as it has the headers
    link_file.readline()

    data = []

    for i in range(max_lines):
        line = link_file.readline()
        if line == '':
            break
        id = line.split(',')[1]
        r = make_omdb_request(id)
        write_krf(reduce_data(r.json()), id, output_file)

    link_file.close()
    output_file.close()


if __name__ == "__main__":
    write_file(LINES_TO_READ)
