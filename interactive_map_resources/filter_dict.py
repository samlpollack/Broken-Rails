import csv

data = {'Track':[1,2,3,4],'PlateType':['Container','cut spikes','hook','Pandrol','Racor','Resilient Fastener','Switch','transit'],'RailType':['BOLTED','CWR']}

filename = 'map_data.csv'
filter_headers = ['Priority','DvCd','TrackType','Div','LineName','Line','Track','DefectType','PlateType','RailWeight','RailType','Manufacturer']
numerical = ['FoundDate','ProducedDate','Million Gross Tons','RailAge','latitude','longitude']
ignore = ['DefectID','StationName','DefectSize','RepairDate','assetID']
with open(filename,'r') as f:
	csvReader = csv.reader(f)
	headers = csvReader.next()
	for i in headers:
		if i in numerical or i in ignore or i in data:
			continue
		data[i] = []
	for row in csvReader:
		for i in range(len(row)):
			if headers[i] in numerical or headers[i] in ignore:
				continue
			if headers[i] == 'Track' or headers[i]=='PlateType' or headers[i]=='RailType':
				continue
			if row[i] in data[headers[i]] or row[i] == '':
				continue
			else:
				data[headers[i]].append(row[i])

print data
print filter_headers
print numerical