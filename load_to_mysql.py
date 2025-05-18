import mysql.connector
from datetime import datetime

# --- Step 1: Your MySQL connection details ---
db_config = {
    "host": "localhost",
    "user": "root",         
    "password": "SamSQL!00",    
    "database": "weather_app"
}

# --- Step 2: Transformed weather data ---
weather_data = {
    "city": "London",
    "country": "GB",
    "temperature": 11.66,
    "feels_like": 10.89,
    "humidity": 77,
    "condition": "broken clouds",
    "wind_speed": 2.24,
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}

# --- Step 3: Connect to MySQL and insert data safely ---
conn = None
cursor = None

try:
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    insert_query = """
        INSERT INTO weather (city, country, temperature, feels_like, humidity, `condition`, wind_speed, timestamp)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    cursor.execute(insert_query, (
        weather_data["city"],
        weather_data["country"],
        weather_data["temperature"],
        weather_data["feels_like"],
        weather_data["humidity"],
        weather_data["condition"],
        weather_data["wind_speed"],
        weather_data["timestamp"]
    ))

    conn.commit()
    print("✅ Weather data successfully loaded into MySQL!")

except mysql.connector.Error as err:
    print(f"❌ MySQL Error: {err}")

finally:
    if cursor is not None:
        cursor.close()
    if conn is not None:
        conn.close()
