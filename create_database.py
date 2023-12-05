import sqlite3
import pandas as pd

# Read the CSV files
final_data = pd.read_csv('final_data.csv')
climate_data = pd.read_csv('chicago_climate_data.csv')

# Create an SQLite database connection
conn = sqlite3.connect('crime_climate_housing_analysis.db')

# Create a cursor object
cursor = conn.cursor()

# Create a table for final_data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS final_data (
        ID INTEGER,
        CaseNumber TEXT,
        Date TEXT,
        PrimaryType TEXT,
        Description TEXT,
        LocationDescription TEXT,
        Arrest INTEGER,
        Domestic INTEGER,
        Year INTEGER,
        Population INTEGER,
        RegionID INTEGER,
        RegionName TEXT,
        City TEXT,
        ZHVI REAL
    )
''')

# Create a table for chicago_climate_data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS chicago_climate_data (
        climate_index INTEGER,
        dt TEXT,
        day INTEGER,
        month INTEGER,
        year INTEGER,
        City TEXT,
        AverageTemperature REAL,
        AverageTemperatureUncertainty REAL,
        Latitude REAL,
        Longitude REAL
    )
''')

# Commit the changes
conn.commit()

# Insert data into final_data table
final_data.to_sql('final_data', conn, if_exists='replace', index=False)

# Insert data into chicago_climate_data table
climate_data.to_sql('chicago_climate_data', conn, if_exists='replace', index=False)

# Close the database connection
conn.close()
