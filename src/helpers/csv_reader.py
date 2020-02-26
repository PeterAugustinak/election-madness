import csv


def csv_reader(file):
    source = f'..\..\{file}'
    with open(source, encoding='utf-8') as csv_file:
        return csv.reader(csv_file, delimiter=',')


# csv_reader('vol_kal.csv')
