# Data Quality Report – Netflix Dataset

Overview
This report summarizes the data quality issues identified in the Netflix Movies and TV Shows dataset before cleaning.

1. Missing Values

The following columns contained missing values:

- **director** → 2634 missing values  
- **cast** → 825 missing values  
- **country** → 831 missing values  
- **date_added** → 10 missing values  
- **rating** → 4 missing values  
- **duration** → 3 missing values  

2. Data Type Issues

Date_added was in object (string) format instead of datetime  
- Required conversion for time-based analysis  

3. Inconsistent Data

- **duration column** contained mixed formats:
  - "90 min" (Movies)
  - "2 Seasons" (TV Shows)

- **rating column** had incorrect values such as:
  - "74 min", "84 min", "66 min" (misplaced data)

4. Formatting Issues

- Some values in **date_added** had leading spaces  
  - Example: `" August 4, 2017"`  
- This caused errors during datetime conversion  

5. Duplicate Records

- No duplicate records were found in the dataset  

Summary of Issues

| Issue Type        | Columns Affected                  |
|------------------|----------------------------------|
| Missing Values   | director, cast, country, date_added, rating, duration |
| Data Type Issues | date_added                       |
| Inconsistent Data| duration, rating                 |
| Formatting Issues| date_added                       |
| Duplicates       | None                             |

---

Conclusion

The dataset contained several common real-world data issues such as missing values, inconsistent formats, and incorrect entries. These issues were addressed during the data cleaning phase to prepare the dataset for analysis.