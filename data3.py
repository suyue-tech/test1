import csv

csvfile = open('data-text.csv','rb')
reader = csv.reader(csvfile)

for row in reader:
    print(row)

dogs = ['Jokers','Simons','Ellie','Lishka','Fido']
for dog in dogs:
    print(dog)

