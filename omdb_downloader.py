import requests
import keys
import json

LINK_FILE_PATH = "ml-latest-small/links.csv"
OUTPUT_FILENAME = "omdb.json"
BASE_URL = "https://www.omdbapi.com/?apikey=" + keys.omdb

LINES_TO_READ = 3

def make_omdb_request(id):
    return requests.get(BASE_URL, params={'i':"tt" + id})

if __name__ == "__main__":

    link_file = open(LINK_FILE_PATH, 'r')
    output_file = open(OUTPUT_FILENAME, 'w')

    #skip the first line as it has the headers
    link_file.readline()

    for i in range(LINES_TO_READ):
        id = link_file.readline().split(',')[1]
        r = make_omdb_request(id)
        body = r.json()
        output_file.write(json.dumps(body) + '\n')

    link_file.close()
    output_file.close()
