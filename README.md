# **🎶 Data Wrangling: Spotify Charts & Grammy Awards**

## **📌 Project Overview**

This project demonstrates data wrangling and integration by combining two datasets of different formats and structures:

Spotify Charts Dataset (CSV) – Tracks songs that appear on Spotify’s Top 200 and Viral 50 charts.

Grammy Awards Dataset (JSON) – Contains Grammy award winners, categories, and award details.

The main objective was to clean, transform, and merge these datasets to discover insights about the relationship between popular streaming success and Grammy recognition.

## **⚙️ Tools & Technologies**

Python (for data extraction, JSON → CSV conversion, and subsetting large datasets)

Excel / PowerQuery (for merging, cleaning, filtering, and pivot analysis)

## **🛠️ Data Wrangling Process**

1. Audited datasets – checked formats, missing values, duplicates, and inconsistencies.

2. Converted Grammy data – transformed JSON to CSV using Python’s json and csv modules.

3. Cleaned data – removed duplicates and rows with null values in key fields (artist, song).

4. Merged datasets – combined on artist name and song title with fuzzy matching in Excel PowerQuery.

5. Analyzed data – used PivotTables and filters to answer key questions.

## **❓ Key Questions & Insights**

How many artists have appeared on Spotify Charts and won at least one Grammy?
→ 28 artists

Have the artists of the top 10 most streamed songs on Spotify won a Grammy for those songs?
→ No. None of the top 10 most streamed songs are Grammy-winning tracks.

Which Grammy Award category has the most overlap with Spotify charting artists?
→ Song of the Year

## **📊 Final Dataset**

The cleaned and merged dataset is available here:
🔗 Google Sheets – [Final Dataset](https://docs.google.com/spreadsheets/d/1T-B-zeNeBHDEBobzTBUeC7Lk2P0X1dcq/edit?usp=sharing&ouid=109419367565294155278&rtpof=true&sd=true)


## **🚀 Key Takeaways**

Data wrangling often requires working across formats (CSV & JSON).

Cleaning and preparation (handling nulls, duplicates, large file sizes) are crucial before merging.

Merging datasets on common keys (artist, song title) can generate valuable cross-domain insights.

## **📂 Repository Structure**

📄 PythonScript.py     - Python script for extraction & conversion

📄 FinalDataset.xlsx    - Cleaned & merged dataset

📄 ProjectReport.pdf   - Detailed project write-up

📄 README.md    - Project overview

## **✨ Future Improvements**

Automate entire pipeline with Pandas (instead of Excel).

Package as a Jupyter Notebook for reproducibility.

Expand analysis with visualizations (Matplotlib, Excel Visulaisations, Power BI).
