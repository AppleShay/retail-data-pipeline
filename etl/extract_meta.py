import os
import pandas as pd

# Path to data file
DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "META stocks.csv")

def extract_meta_stock_data():
    """Extracts Meta stock data from CSV and returns as DataFrame."""
    try:
        print(f"📂 Reading data from {DATA_PATH}...")
        df = pd.read_csv(DATA_PATH)
        print(f"✅ Successfully loaded {len(df)} rows and {len(df.columns)} columns.")
        return df
    except FileNotFoundError:
        print("❌ Error: META stocks.csv not found in /data directory.")
    except Exception as e:
        print(f"❌ Error loading file: {e}")

if __name__ == "__main__":
    df = extract_meta_stock_data()
    if df is not None:
        print(df.head())
