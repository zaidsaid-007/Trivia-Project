from dotenv import load_dotenv
import os
load_dotenv()
database_name = os.environ.get("database_name")
database_path = os.environ.get("database_path")
