#!/usr/local/bin/python3

import csv


with open('/Users/stan/Documents/Uranium_Database_Support_Files/DRUM_db/DRM_Utah.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        print(row[2], ' ', row[3],' ', row[4],' ', row[7],' ', row[8],' ', row[9],' ', row[10],' ', row[15],' ', row[16],' ', row[22],' ', row[23],' ', row[24])
        line_count += 1
    print(f'Processed {line_count} lines.')
