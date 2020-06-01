import numpy
import csv
import prettytable

column_names = ['StarID','Hip','HD','HR','Gliese','BayerFlamsteed','ProperName','RA','Dec','Distance','Mag','AbsMag','Spectrum','ColorIndex']



reader = csv.reader(open("hygfull.csv", "r"), delimiter=",")
r = list(reader)

r.pop(0) # Remove label row

stars = sorted(r, reverse=True, key=lambda x: x[column_names.index('ProperName')])


table = prettytable.PrettyTable(column_names)
for row in stars[0:90]:
    table.add_row(row)

print(table)





#imported = numpy.genfromtxt('hygfull.csv', delimiter=',', names=True, case_sensitive=True)
#print(imported)
#stars = numpy.argsort(imported, axis=column_names.index('AbsMag'))
#result = numpy.array(x).astype("float")
#stars = numpy.argsort(r, axis=column_names.index('AbsMag'))
