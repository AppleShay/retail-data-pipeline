# load_meta.py
import pandas as pd
import psycopg2
from io import StringIO

# 1) Read your transformed CSV
csv_path = "../data/transformed_meta.csv"
print(f"📂 Loading transformed data from {csv_path}…")
df = pd.read_csv(csv_path)

# 2) Open a psycopg2 connection to your local Postgres container
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="postgres",
    host="localhost",
    port=5432,
)
cur = conn.cursor()

# 3) (Re)create the target table
cur.execute("DROP TABLE IF EXISTS meta_stocks;")
cur.execute("""
CREATE TABLE meta_stocks (
    Date          DATE,
    Open          FLOAT,
    High          FLOAT,
    Low           FLOAT,
    Close         FLOAT,
    "Adj Close"   FLOAT,
    Volume        BIGINT,
    "Daily Return (%)" FLOAT,
    "7d MA Close" FLOAT
);
""")
conn.commit()

# 4) Use COPY to bulk-load from an in-memory buffer
print("🔌 COPY bulk-loading into Postgres…")
buffer = StringIO()
# write without header, align columns to table DDL order
df.to_csv(buffer, sep='\t', header=False, index=False)
buffer.seek(0)

cur.copy_from(buffer, 'meta_stocks', sep='\t', null="")
conn.commit()

print("✅ Data loaded into Postgres table: meta_stocks")

cur.close()
conn.close()
