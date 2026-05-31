import pandas as pd
import numpy as np

# ── 1. Load ───────────────────────────────────────────────────────────────────
df = pd.read_csv('dataset/netflix_titles.csv')
original_shape = df.shape
print(f"Original shape: {original_shape}")

# ── 2. Rename columns (lowercase, underscores) ────────────────────────────────
df.columns = [c.strip().lower().replace(' ', '_') for c in df.columns]

# ── 3. Remove duplicates ──────────────────────────────────────────────────────
before_dup = len(df)
df = df.drop_duplicates()
print(f"Duplicates removed: {before_dup - len(df)}")

# ── 4. Fix misplaced rating/duration rows ─────────────────────────────────────
mask = df['rating'].str.contains('min', na=False)
df.loc[mask, 'duration'] = df.loc[mask, 'rating']
df.loc[mask, 'rating'] = np.nan
print(f"Fixed misplaced rating/duration: {mask.sum()} rows")

# ── 5. Handle missing values ──────────────────────────────────────────────────
df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Unknown')
df['country'] = df['country'].fillna('Unknown')

mode_rating = df['rating'].mode()[0]
df['rating'] = df['rating'].fillna(mode_rating)
print(f"Rating NaNs filled with mode: '{mode_rating}'")

before_drop = len(df)
df = df.dropna(subset=['duration'])
print(f"Rows dropped due to missing duration: {before_drop - len(df)}")

df['date_added'] = df['date_added'].fillna('Unknown')

# ── 6. Standardise & convert date_added ──────────────────────────────────────
df['date_added'] = df['date_added'].str.strip()
date_parsed = pd.to_datetime(df['date_added'], format='%B %d, %Y', errors='coerce')
df['date_added'] = date_parsed.dt.strftime('%d-%m-%Y').fillna('Unknown')

# ── 7. Fix data types ─────────────────────────────────────────────────────────
df['release_year'] = df['release_year'].astype(int)
df['duration_value'] = df['duration'].str.extract(r'(\d+)')[0].astype(float).astype('Int64')
df['duration_unit'] = df['duration'].str.extract(r'([A-Za-z ]+)')[0].str.strip()

# ── 8. Standardise text columns ───────────────────────────────────────────────
df['type'] = df['type'].str.strip().str.title()
df['rating'] = df['rating'].str.strip().str.upper()
df['country'] = df['country'].str.strip().str.title()

# ── 9. Sort & save ────────────────────────────────────────────────────────────
df = df.sort_values(by=['type', 'release_year'], ascending=[True, False]).reset_index(drop=True)
df.to_csv('netflix_cleaned.csv', index=False)

print(f"\n✅ Cleaning complete!")
print(f"  Original rows : {original_shape[0]}")
print(f"  Cleaned rows  : {len(df)}")
print(f"  Columns       : {list(df.columns)}")
print(f"\nMissing values after cleaning:\n{df.isnull().sum()}")
