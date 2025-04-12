import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# SQLite Database 
DB_URI = "sqlite:///C:/Users/muqeem/OneDrive - Youngstown State University/Desktop/Spring 2025/Data_Capston_Project/db/tpch120k_sqlite3.db"

#  API Key (Store in .env file)
deepseek_api_key = os.getenv("deepseek_api_key")
