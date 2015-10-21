
import csv

BR_file = 'All Defects with edits.csv'
stations_file = 'stations_modified2.csv'

stations = {}
unmatched = {}

data = []

match = 0
n = 0

with open(stations_file, 'rU') as f:
	csvReader = csv.reader(f)
	headers = csvReader.next()
	for row in csvReader:
		station_name_index = headers.index('StaNam')
		station_name = row[station_name_index].upper()
		station_name2 = row[headers.index('Station Name')].upper()

		line_index = headers.index('LineName')
		line = row[line_index].strip().upper()

		div_index = headers.index('Div')
		div = row[div_index].strip().upper()

		id_index = headers.index('AssetID')
		assetID = row[id_index].strip()

		latitude_index = headers.index('Latitude')
		latitude = row[latitude_index].strip()

		longitude_index = headers.index('Longitude')
		longitude = row[longitude_index].strip()

		station = station_name + ',' + line + ',' + div
		station2 = station_name2 + ',' + line + ',' + div
		stations[station] = {'assetID': assetID, 'latitude': latitude, 'longitude':longitude}
		stations[station2] = {'assetID': assetID, 'latitude': latitude, 'longitude':longitude}
		# if station_name == 'DeKalb Av': 
		# 	print station
		# if station_name2 == 'DeKalb Av':
		# 	print station2

with open(BR_file, 'r') as f:
	csvReader = csv.reader(f)
	headers = csvReader.next()
	for row in csvReader:
		n += 1
		station_name_index = headers.index('StationName')
		station_name = row[station_name_index].upper()

		line_index = headers.index('LineName')
		line = row[line_index].upper()

		div_index = headers.index('Div')
		div = row[div_index].upper()

		station = station_name + ',' + line + ',' + div
		if station in stations:
			match += 1
			defect = row
			defect.append(stations[station]['assetID'])
			defect.append(stations[station]['latitude'])
			defect.append(stations[station]['longitude'])
			data.append(defect)
		else:
			if line == 'BROADWAY' or line =='4TH AV' or line == 'MANHATTAN BRIDGE':
				line = 'BROADWAY - BRIGHTON'
				station = station_name + ',' + line +',' + div
				if station in stations:
					match += 1
					defect = row
					defect.append(stations[station]['assetID'])
					defect.append(stations[station]['latitude'])
					defect.append(stations[station]['longitude'])
					data.append(defect)
					continue
			if line == 'NOSTRAND AV':
				line = 'NOSTRAND'
				station = station_name + ',' + line +',' + div
				if station in stations:
					match += 1
					defect = row
					defect.append(stations[station]['assetID'])
					defect.append(stations[station]['latitude'])
					defect.append(stations[station]['longitude'])
					data.append(defect)
					continue
				else:
					line = 'EASTERN PKY'
					station = station_name + ',' + line +',' + div
					if station in stations:
						defect = row
						defect.append(stations[station]['assetID'])
						defect.append(stations[station]['latitude'])
						defect.append(stations[station]['longitude'])
						data.append(defect)
						match += 1
						continue
			if line == 'NASSAU LOOP':
				line = 'JAMAICA'
				station = station_name + ',' + line +',' + div
				if station in stations:
					match += 1
					defect = row
					defect.append(stations[station]['assetID'])
					defect.append(stations[station]['latitude'])
					defect.append(stations[station]['longitude'])
					data.append(defect)
					continue
				else:
					print station

			if station == '57 ST,63RD ST,IND':
				line = '6TH AV - CULVER'
			if station == '5 AV,6TH AV - CULVER,IND':
				line = 'QUEENS - ARCHER'
			if station == '59-COLUMBUS,6TH AV - CULVER,IND':
				line = '8TH AV - FULTON ST'
			if station == '57 ST,ASTORIA,BMT':
				line = 'BROADWAY - BRIGHTON'
			if station == 'S FERRY LOOP,BROADWAY - 7AV,IRT':
				line = 'SOUTH FERRY LOOP'
			if station == 'STILLWELL AV,BROADWAY - BRIGHTON,BMT':
				line = 'SEA BEACH'
			if station == 'CANAL ST (LL),BROADWAY - BRIGHTON,BMT':
				line = 'MANHATTAN BRIDGE'
			if station == '5 AV,BROADWAY - BRIGHTON,BMT':
				line = 'ASTORIA'
			if station == 'CHAMBERS ST,CLARK ST,IRT':
				line = 'BROADWAY - 7AV'
			if station == '135 ST,CONCOURSE,IND':
				line = '8TH AV - FULTON ST'
			if station == 'BERGEN ST,CROSSTOWN,IND':
				line = '6TH AV - CULVER'
			if station == '125 ST,JEROME AV,IRT':
				line = 'LEXINGTON - SHUTTLE'
			if station == '96 ST,LENOX - WPR,IRT':
				line ='BROADWAY - 7AV'
			if station == 'BORO HALL,LEXINGTON - SHUTTLE,IRT':
				line = 'EASTERN PKY'
			if station == 'EUCLID AV,LIBERTY AV,IND':
				line = '8TH AV - FULTON ST'
			if station == '125 ST,PELHAM,IRT':
				line = 'LEXINGTON - SHUTTLE'
			if station == 'COURT SQ,QUEENS - ARCHER,IND':
				station_name = 'COURT SQ-23 ST'
			if station == 'ROCKAWAY BLVD,ROCKAWAY,IND':
				line = 'LIBERTY AV'
			if station == '59 ST,SEA BEACH,BMT':
				line = '4TH AV'
			if station == 'BOWLING GREEN,SOUTH FERRY LOOP,IRT':
				line = 'LEXINGTON - SHUTTLE'
			if station == 'STILLWELL AV,WEST END,BMT':
				line = 'SEA BEACH'
			if station == '36 ST,WEST END,BMT':
				line = '4TH AV'
			if station == '21-QUEENSBRIDGE,QUEENS - ARCHER,IND':
				line = '63RD ST'
			if station == 'JEROME TUBE,LEXINGTON - SHUTTLE,IRT':
				line = 'JEROME AV'
			if station == 'LEXINGTON/63,ASTORIA,BMT':
				station_name = 'LEXINGTON/60'
			if station == '57 ST,63RD ST,BMT':
				line = 'BROADWAY - BRIGHTON'
			if station == '36 ST,63RD ST,IND':
				line = 'QUEENS - ARCHER'
			if station == 'NOSTRAND AV,NOSTRAND,IRT':
				line = 'EASTERN PKY'




			station = station_name + ',' + line +',' + div
			if station in stations:
				match += 1
				defect = row
				defect.append(stations[station]['assetID'])
				defect.append(stations[station]['latitude'])
				defect.append(stations[station]['longitude'])
				data.append(defect)
				continue
			# else:
			# 	print station

			if line == 'BROADWAY - BRIGHTON':
				line = 'BROADWAY'
			station = station_name + ',' + line +',' + div
			if station in stations:
				match += 1
				defect = row
				defect.append(stations[station]['assetID'])
				defect.append(stations[station]['latitude'])
				defect.append(stations[station]['longitude'])
				data.append(defect)
				continue

			if station in unmatched:
				unmatched[station] += 1 
			else: 
				unmatched[station] = 1
		

unmatched_sorted = []
for i in unmatched:
	unmatched_sorted.append((unmatched[i], i))
unmatched_sorted.sort(reverse=True)

sorted_stations = []
for i in stations:
	sorted_stations.append(i)
sorted_stations.sort()
print sorted_stations

print('station \t count')
for i in unmatched_sorted:
	print(i[1] + '\t' + str(i[0]))

print('matches: ' + str(match))
print('out of: ' + str(n)) 
print('percentage: ' + str(match*100/n) +'%')
print('unmatched stations: ' + str(len(unmatched)))



headers.append('assetID')
headers.append('latitude')
headers.append('longitude')
new_file = 'map_data.csv'
with open(new_file, 'w') as f:
	csvWriter = csv.writer(f)
	csvWriter.writerow(headers)
	for i in data:
		csvWriter.writerow(i)



