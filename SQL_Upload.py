import os
import pandas as pd
from sqlalchemy import create_engine, text
import urllib.parse

# =====================================================
# SQL SERVER CONNECTION CONFIG (custom for your setup)
# =====================================================

SERVER = r"ADII\SQLEXPRESS"                 # as shown in SSMS
DATABASE = "AirbnbMarketAnalytics"
BASE_PATH = r"E:\Airbnb_Project\data_clean"

# Use one of the installed drivers (you have both 17 & 18)
DRIVER = "ODBC Driver 18 for SQL Server"
# If this ever complains, you can switch to:
# DRIVER = "ODBC Driver 17 for SQL Server"

# Build ODBC connection string
odbc_str = (
    f"DRIVER={{{DRIVER}}};"
    f"SERVER={SERVER};"
    f"DATABASE={DATABASE};"
    "Trusted_Connection=yes;"
    "Encrypt=no;"
    "TrustServerCertificate=yes;"
)

# URL-encode for SQLAlchemy
odbc_str_encoded = urllib.parse.quote_plus(odbc_str)

connection_string = f"mssql+pyodbc:///?odbc_connect={odbc_str_encoded}"

engine = create_engine(connection_string, fast_executemany=True)

print("Engine created, testing connection...")
with engine.connect() as conn:
    conn.execute(text("SELECT 1"))
print("Connection OK. Ready to load data.")

# =====================================================
# CSV → SQL TABLE MAPPING (based on your actual files)
# =====================================================

FILES_AND_TABLES = [
    ("Listings_table.csv",        "listings"),
    ("Listing_Reviews.csv",       "reviews"),
    ("reviews_score.csv",         "review_scores"),
    ("amenities_table.csv",       "amenities"),
    ("listing_amenities.csv",     "listing_amenities"),
]

# =====================================================
# CHUNKED LOADER FUNCTION
# =====================================================

def load_csv_to_sql(csv_path, table_name, chunksize=100000, if_exists="replace"):
    print(f"\nLoading {csv_path} → {table_name}")

    if not os.path.exists(csv_path):
        print(f"⚠ File not found: {csv_path}")
        return

    # 👇 IMPORTANT: handle weird characters safely
    chunk_iter = pd.read_csv(
        csv_path,
        chunksize=chunksize,
        encoding="latin1",      # more permissive than utf-8
        on_bad_lines="warn"     # if some rows are broken, just warn
    )

    first = True
    total = 0

    for chunk in chunk_iter:
        mode = "replace" if first else "append"

        chunk.to_sql(
            name=table_name,
            con=engine,
            if_exists=mode,
            index=False,
        )

        total += len(chunk)
        print(f"   + {len(chunk)} rows inserted (total so far: {total})")

        first = False

    print(f"✔ Finished loading table: {table_name} — Total rows: {total}")

# =====================================================
# MAIN EXECUTION
# =====================================================

def main():
    # 1) Load each CSV into its table
    for filename, table_name in FILES_AND_TABLES:
        csv_full_path = os.path.join(BASE_PATH, filename)
        load_csv_to_sql(csv_full_path, table_name)

    # 2) Show row counts from SQL Server
    print("\n========== ROW COUNTS (SQL SERVER) ==========")
    with engine.connect() as conn:
        for _, table_name in FILES_AND_TABLES:
            try:
                count = conn.execute(text(f"SELECT COUNT(*) FROM {table_name};")).scalar()
                print(f"{table_name:20s} : {count} rows")
            except Exception as e:
                print(f"{table_name:20s} : ERROR → {e}")

if __name__ == "__main__":
    main()
