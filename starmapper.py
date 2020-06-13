import numpy
import csv
import prettytable
import json
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-l", "--limited", help="only display stars in one direction", action="store_true")
args = parser.parse_args()

column_names = ['StarID','Hip','HD','HR','Gliese','BayerFlamsteed','ProperName','RA','Dec','Distance','Mag','AbsMag','Spectrum','ColorIndex']



reader = csv.reader(open("hygfull.csv", "r"), delimiter=",")
r = list(reader)

r.pop(0) # Remove label row

stars = sorted(r, reverse=False, key=lambda x: float(x[column_names.index('Mag')]));


subset = stars[:1000]

table = prettytable.PrettyTable(column_names)
for row in subset[0:90]:

    table.add_row(row)

print(table)



cleaned = []
for row in subset:
    if args.limited and (((float(row[7]) > 10 or float(row[7]) < 4)) and float(row[8]) < 45):
        continue


    cleaned.append({'Mag': row[10], 'Name': row[6], 'RA': row[7], 'Dec': row[8], 'ColorIndex': row[13]})


with open('stars.json', 'w') as json_file:
    json.dump(cleaned,  json_file)


with open('stars.js', 'w') as js_file:
    dumps = json.dumps(cleaned)
    js_file.write("var stars = " + dumps + "\nexport default stars;")




#imported = numpy.genfromtxt('hygfull.csv', delimiter=',', names=True, case_sensitive=True)
#print(imported)
#stars = numpy.argsort(imported, axis=column_names.index('AbsMag'))
#result = numpy.array(x).astype("float")
#stars = numpy.argsort(r, axis=column_names.index('AbsMag'))
