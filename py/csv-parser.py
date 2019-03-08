import csv

READ_FILEPATH = 'ml-latest-small/movies.csv'
WRITE_FILEPATH = 'edited-movies.csv'

with open(READ_FILEPATH) as f_read:
    with open(WRITE_FILEPATH, 'w+') as f_write:

        reader = csv.reader(f_read, delimiter=',')
        writer = csv.writer(f_write)

        for i, row in enumerate(reader):
            if i == 0:
                writer.writerow(row)
            else:
                genres = row[2].split('|')
                for genre in genres:
                    new_line = row[:2] + [genre]
                    writer.writerow(new_line)
