import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('sqliteconnect.db')
cursor = conn.cursor()

# Create a new table named "Facility"
cursor.execute('''
    CREATE TABLE Facility (
        FacilityID INTEGER PRIMARY KEY,
        FacilityType TEXT,
        AddressLine1 TEXT,
        AddressLine2 TEXT,
        City TEXT,
        Zip TEXT,
        Latitude REAL,
        Longitude REAL
    )
''')

# Example data for inserting into the 'Facility' table
data = (1, 'Hospital', '123 Main St', '', 'City', '12345', 12.345, -67.890)

# Insert data into the 'Facility' table
cursor.execute("INSERT INTO Facility (FacilityID, FacilityType, AddressLine1, AddressLine2, City, Zip, Latitude, Longitude) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", data)

# Commit the changes
conn.commit()

# Close the database connection
conn.close()
