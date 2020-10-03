import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeat
import csv

# read files and move data to list
file1 = open("airports.dat", "r")
reader1 = csv.reader(file1, delimiter=",")
next(reader1) # remove header
airports = list(reader1) # make list

file2 = open("flights_from_tallinn.csv", "r")
reader2 = csv.reader(file2, delimiter=";")
next(reader2)
connected_airports = list(reader2)

src = []
longitude = []
latitude = []
IATA = []

# compare IATA and move matching to src, longitude, latitude and IATA lists respectively
for row1 in airports:
	for row2 in connected_airports:
		if(row1[4]==row2[1]):
			if(row2[1]=="TLL"):
				src = [row1[4], float(row1[7]), float(row1[6])]	
			else:
				longitude.append(float(row1[7]))
				latitude.append(float(row1[6]))
				IATA.append(row1[4])

#################
# map making part
#################

plt.figure(figsize=(15,10))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_title("Flights From Tallinn")

# add coastline, land and borders to the map
ax.add_feature(cfeat.COASTLINE)
ax.add_feature(cfeat.OCEAN)
ax.add_feature(cfeat.LAND)
ax.add_feature(cfeat.BORDERS)

# add airports to map with IATA
for i in range(len(IATA)):
	x = [src[1], longitude[i]]
	y = [src[2], latitude[i]]
	ax.plot(x, y, marker="o", transform=ccrs.Geodetic(), color="blue")
	ax.text(longitude[i]+0.2, latitude[i]+0.2, IATA[i], weight="bold")

# add IATA to tallinn airport
ax.text(src[1], src[2], src[0], weight="bold")

# save figure
plt.savefig("FFT_map.png", dpi=300)
plt.show()

