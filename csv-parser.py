import csv

filepath = 'ml-latest-small/movies.csv'

write_filepath = 'edited-movies.csv'

with open(filepath) as f:
    with open(write_filepath, 'w+') as f_w

    lines = f.readlines()
    for i, row in enumerate(lines):
        if i == 0:
            f_w.write(row)
        else:
            cols = row.split(',')
            genres = cols[2].split('|')
            for genre in genres:
                new_line = cols[:2] + genre
                commas = ','.join(new_line)
                f_w.write(commas)


    
