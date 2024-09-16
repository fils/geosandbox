import duckdb
import pandas as pd

# Assume you have a pandas DataFrame named 'df' with a column 'wkt_column' containing WKT data

# Connect to DuckDB and load the spatial extension
con = duckdb.connect('your_database.db')
con.execute("INSTALL spatial;")
con.execute("LOAD spatial;")

# Create a table to store the data
con.execute("""
    CREATE TABLE spatial_data (
        id INTEGER,
        name VARCHAR,
        geom GEOMETRY
    )
""")

# Insert data from the DataFrame into the DuckDB table
con.execute("""
    INSERT INTO spatial_data (id, name, geom)
    SELECT
        id,
        name,
        ST_GeomFromText(wkt_column) AS geom
    FROM df
""")

# Verify the data
result = con.execute("SELECT * FROM spatial_data LIMIT 5").fetchall()
print(result)

con.close()

