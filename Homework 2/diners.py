import sqlite3

# Connect to database
con = sqlite3.connect("DINERS.db")
cursor = con.cursor()

# 1) Create PROVIDER and CANTEEN tables 
cursor.execute('CREATE TABLE if not exists PROVIDER (ID integer PRIMARY KEY, ProviderName VARCHAR)')

cursor.execute('CREATE TABLE if not exists CANTEEN (ID INTEGER PRIMARY KEY, ProviderID INTEGER, Name VARCHAR, Location VARCHAR,  time_open TIME, time_closed TIME, FOREIGN KEY (ProviderID) REFERENCES PROVIDER(ID))')


# 2) Insert values into tables
cursor.execute('INSERT INTO PROVIDER(ProviderName) VALUES ("Rahva Toit"), ("Baltic Restaurants Estonia AS"), ("TTÜ Sport"), ("Bitstop Kohvik OÜ")')

# IT college canteen
cursor.execute('INSERT INTO CANTEEN (ProviderID, Name, Location, time_open, time_closed) VALUES (4, "bitStop CAFE", "Raja 4", "09:30", "16:00")')

# all other canteens
cursor.execute('INSERT INTO CANTEEN (ProviderID, Name, Location, time_open, time_closed) VALUES (1, "Economics and social science building canteen", "Akadeemia tee 3", "08:30", "18:30"), (1, "Libary canteen", "Akadeemia tee 1/Ehitajate tee 7", "08:30", "19:00"), (2, "Main building Deli cafe", "Ehitajate tee 5", "09:00", "16:30"), (2, "Main building Daily lunch restaurant", "Ehitajate tee 5", "09:00", "16:30"), (1, "U06 building canteen", "Ehitajate tee 5", "09:00", "16:00"), (2, "Natural Science building canteen", "Akadeemia tee 15", "09:00", "16:00"), (2, "ICT building canteen", "Raja 15/Mäepealse 1", "09:00", "16:00"), (3, "Sports building canteen", "Männiliiva 7", "11:00", "20:00")')


# 3) Query for canteens which are open 16.15-18.00
cursor.execute('SELECT * FROM CANTEEN WHERE time_open <= "16:15" AND time_closed >= "18:00"')
arr1 = cursor.fetchall()


# 4) Query for canteens which are serviced by Rahva Toit
cursor.execute('SELECT * FROM CANTEEN WHERE ProviderID == (SELECT ID FROM PROVIDER WHERE ProviderName == "Rahva Toit")')
arr2 = cursor.fetchall()


print("Canteens which are open 16.15-18.00:")
for i in arr1:
	print(i)

print("\nCanteens which are serviced by Rahva Toit:")
for i in arr2:
	print(i)

con.commit()
con.close()



