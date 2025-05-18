import mysql.connector

# --- Step 1: Your MySQL connection details ---
db_config = {
    "host": "localhost",
    "user": "root",         
    "password": "SamSQL!00",     
    "database": "weather_app"
}

# --- Step 2: Fetch data from MySQL ---
try:
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Query to get the weather data
    select_query = "SELECT * FROM weather"
    cursor.execute(select_query)

    # Fetch all rows from the result
    rows = cursor.fetchall()

    # Display the rows
    for row in rows:
        print(f"ID: {row[0]} | City: {row[1]} | Country: {row[2]} | Temp: {row[3]}°C | Feels Like: {row[4]}°C | Humidity: {row[5]}% | Condition: {row[6]} | Wind Speed: {row[7]} m/s | Timestamp: {row[8]}")

except mysql.connector.Error as err:
    print(f"❌ MySQL Error: {err}")

finally:
    if cursor is not None:
        cursor.close()
    if conn is not None:
        conn.close()
