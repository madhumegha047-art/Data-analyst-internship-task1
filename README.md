 Task 1: Data Cleaning and Preprocessing — Netflix Movies & TV Shows

## 📌 Objective
Clean and prepare the raw Netflix titles dataset (sourced from Kaggle) by handling missing values, fixing data type issues, correcting misplaced data, and standardising formats — making it ready for analysis or modelling.

---

## 📁 Files
| File | Description |
|------|-------------|
| `netflix_titles.csv` | Original raw dataset from Kaggle |
| `netflix_cleaned.csv` | Fully cleaned and preprocessed dataset |
| `clean_netflix.py` | Python script with all cleaning steps |

---

## 🛠 Tools Used
- Python 3
- Pandas
- NumPy

---

## 🔍 Dataset Overview
- **Source:** [Netflix Movies and TV Shows – Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows)
- **Original shape:** 8807 rows × 12 columns
- **Cleaned shape:** 8807 rows × 14 columns (2 new derived columns added)

---

## 🧹 Cleaning Steps Performed

### 1. Column Renaming
- Renamed all columns to lowercase with underscores (e.g., `date_added` stays consistent).

### 2. Duplicate Removal
- Checked for and removed duplicate rows using `.drop_duplicates()`.
- **Result:** 0 duplicates found.

### 3. Misplaced Data Fix (Rating ↔ Duration)
- 3 rows had duration values (e.g., `"74 min"`) incorrectly stored in the `rating` column with `NaN` in `duration`.
- **Fix:** Swapped values to the correct columns.

### 4. Missing Value Treatment

| Column | Missing Count | Strategy |
|--------|--------------|----------|
| `director` | 2634 | Filled with `'Unknown'` |
| `cast` | 825 | Filled with `'Unknown'` |
| `country` | 831 | Filled with `'Unknown'` |
| `rating` | 4 | Filled with mode (`TV-MA`) |
| `date_added` | 10 | Filled with `'Unknown'` |
| `duration` | 0 after fix | No action needed |

### 5. Date Format Standardisation
- Converted `date_added` from `"Month DD, YYYY"` (e.g., `September 25, 2021`) to `DD-MM-YYYY` format (e.g., `25-09-2021`).
- Unparseable dates left as `'Unknown'`.

### 6. Data Type Fixes
- `release_year` confirmed as `int`.
- Extracted `duration_value` (numeric) and `duration_unit` (`min` / `Season(s)`) as separate columns for easier analysis.

### 7. Text Standardisation
- `type`: Title Case (e.g., `Movie`, `TV Show`)
- `rating`: UPPERCASE (e.g., `TV-MA`, `PG-13`)
- `country`: Title Case (e.g., `United States`)

### 8. Final Sort
- Sorted by `type` (ascending) then `release_year` (descending) for logical ordering.

---

## 📊 Before vs After

| Metric | Before | After |
|--------|--------|-------|
| Total rows | 8807 | 8807 |
| Total columns | 12 | 14 |
| Missing values | 4307 | 0 |
| Misplaced rating/duration | 3 | 0 (fixed) |
| Date format | Inconsistent string | `DD-MM-YYYY` |
| Column names | Mixed case | Lowercase + underscores |

---

## ▶️ How to Run

```bash
pip install pandas numpy
python clean_netflix.py
```

This will read `netflix_titles.csv` from a `dataset/` folder and produce `netflix_cleaned.csv`.

---

## 💡 Key Learnings
- Real datasets often have data in the **wrong column** — always cross-check.
- **Director and cast** fields being empty doesn't mean bad data; it's a legitimate unknown.
- Separating `duration` into value + unit makes downstream analysis (e.g., average movie length) much easier.
- Pandas Copy-on-Write (pandas ≥
