# Automated Weather Data Pipeline 

##  Key Features
- **Automation:** The pipeline runs automatically every day at 06:00 UTC using GitHub Actions.
- **ETL Logic:**
    - **Extract:** Fetches raw data from the [Open-Meteo API](https://open-meteo.com/).
    - **Transform:** Cleans and filters the data using Python (e.g., keeping only hours where the temperature is above 15°C).
    - **Load:** Inserts the processed data into a version-controlled `weather.db` (SQLite) database.
- **CI/CD:** Utilizes a GitHub Actions workflow to spin up an Ubuntu runner, set up the Python environment, install dependencies, and commit the updated database back to the repository.

##  Tech Stack
- **Language:** Python 3.10+
- **Database:** SQLite3
- **Infrastructure:** GitHub Actions (Automated Workflows)
- **Libraries:** `requests`, `sqlite3`, `json`
