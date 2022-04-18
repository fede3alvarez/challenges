import csv
import os
import collections

data = []
record = collections.namedtuple(
    'Record',
)

def init():
    base_folder = os.path.dirname(__file__)
    filename = os.path.join(base_folder, 'data', 'seattle.csv')

    with open(filename,'r',encoding='utf') as fin:
        #print(fin.read())

        # Can iterate over reader, and get line per line data
        reader = csv.DictReader(fin)
        print(type(reader))

        for row in reader:
            #print("ROW --> {}".format(row))

            # Everything out of the csv file is a string
            #print(row.get('actual_mean_temp'))

            # Outsource row manipulation to parse_now:
            row = parse_row(row)
            print(type(row.get('actual_mean_temp')),row.get('actual_mean_temp'))

def parse_row(row):
    row['actual_mean_temp'] = int(row['actual_mean_temp'])
    row['actual_min_temp'] = int(row['actual_min_temp'])
    row['actual_max_temp'] = int(row['actual_max_temp'])
    row['average_min_temp'] = int(row['average_min_temp'])
    row['average_max_temp'] = int(row['average_max_temp'])
    row['record_min_temp'] = int(row['record_min_temp'])
    row['record_max_temp'] = int(row['record_max_temp'])

    # How to iterate over the 'columns'
    
        # You have to first iterate over the dict getting each row, and then iterate over the items in each row:

        # for row in d:
        #     for k, v in row.items():
        #         # Do stuff

    return row