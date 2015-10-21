import csv

filename = 'stations_modified.csv'
newfile = 'stations_modified2.csv'
w = open(newfile, 'w')
csvWriter = csv.writer(w)
with open(filename,'rU') as f:
	csvReader = csv.reader(f)
	headers = csvReader.next()
	csvWriter.writerow(headers)
	for row in csvReader:
		lat = row[headers.index('Latitude')]
		lon = row[headers.index('Longitude')]

		try:
			lat = float(lat)
			lon = float(lon)
			csvWriter.writerow(row)
		except:
			continue

w.close()