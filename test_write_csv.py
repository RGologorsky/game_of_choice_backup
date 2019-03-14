import csv
with open("hi.csv", 'w') as f:
	    writer = csv.writer(f)
	    writer.writerow([1,2,3])