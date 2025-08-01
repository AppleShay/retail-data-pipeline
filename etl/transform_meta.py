import pandas as pd
import os

# File paths
RAW_FILE = os.path.join(os.path.dirname(__file__), '../data/META stocks.csv')
TRANSFORMED_FILE = os.path.join(os.path.dirname(__file__), '../data/transformed_meta.csv')

print("📂 Reading raw data...")
df = pd.read_csv(RAW_FILE)

# Convert Date to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Ensure Volume is integer
df['Volume'] = df['Volume'].astype(int)

# Calculate Daily Return %
df['Daily Return (%)'] = ((df['Close'] - df['Open']) / df['Open']) * 100

# 7-day Moving Average of Close
df['7d MA Close'] = df['Close'].rolling(window=7).mean()

print("🔄 Transformation complete!")

# Save transformed data
df.to_csv(TRANSFORMED_FILE, index=False)
print(f"✅ Transformed data saved to {TRANSFORMED_FILE}")
