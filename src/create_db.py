import sqlite3
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

csv_path = BASE_DIR / "data" / "globalAirQuality.csv"
db_path  = BASE_DIR / "db" / "air_quality.db"

df = pd.read_csv(csv_path)

conn = sqlite3.connect(db_path)
df.to_sql("air_quality", conn, if_exists="replace", index=False)
conn.close()

print("SQLite DB 생성 완료:", db_path)
