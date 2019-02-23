import requests
import keys
import json

LINK_FILE_PATH = "ml-latest-small/links.csv"
OUTPUT_FILENAME = "omdb.json"
BASE_URL = "https://www.omdbapi.com/?apikey=" + keys.omdb

LINES_TO_READ = 10

def make_omdb_request(id):
    return requests.get(BASE_URL, params={'i':"tt" + id})

def write_file(max_lines):

    link_file = open(LINK_FILE_PATH, 'r')
    output_file = open(OUTPUT_FILENAME, 'w')

    #skip the first line as it has the headers
    link_file.readline()

    data = []

    for i in range(max_lines):
        line = link_file.readline()
        if line == '':
            break
        id = line.split(',')[1]
        r = make_omdb_request(id)
        data.append(r.json())

    output_file.write(json.dumps(data) + '\n')

    link_file.close()
    output_file.close()


if __name__ == "__main__":
    write_file(LINES_TO_READ)
