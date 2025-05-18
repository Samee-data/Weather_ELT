🌦️ Weather_ELT: Weather Data ELT Pipeline
Weather_ELT is a robust ELT (Extract, Load, Transform) pipeline designed to collect real-time weather data from a public API and store it in a structured SQL database. This project demonstrates the core principles of data engineering by handling data ingestion, storage, and post-load transformation.

🔧 Features
Extract: Connects to a weather API to retrieve current weather data for specified cities.

Load: Writes the raw data directly into a SQL table with timestamped records.

Transform: (Optional phase) Performs cleaning or aggregation queries within the database post-load.

Automated Execution: Can be scheduled for regular updates using Apache Airflow or a cron job.

🧰 Tech Stack
Python – API requests and database integration

MySQL – Target SQL database

Requests – For HTTP communication with the weather API

MySQL Connector – For database connectivity

📦 Table Schema
Column	Type	Description
id	INT	Auto-increment primary key
city	VARCHAR	Name of the city
country	VARCHAR	Country code
temperature	FLOAT	Current temperature
feels_like	FLOAT	Feels like temperature
humidity	INT	Humidity percentage
weather_desc	VARCHAR	Weather condition (e.g., Clear)
wind_speed	FLOAT	Wind speed in km/h
timestamp	DATETIME	Time of data collection

🚀 Use Cases
Weather monitoring dashboards

Historical weather analytics

ETL practice for aspiring data engineers

📈 Future Enhancements
Integrate with Apache Spark for data transformation

Load into a cloud data warehouse (Snowflake/BigQuery)

Add alerting based on weather thresholds
