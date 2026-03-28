import pandas as pd
import matplotlib.pyplot as plt


#1. Loading Data
try:
    df = pd.read_csv("netflix_titles.csv")
    print("✅ Data successfully loaded.\n")
except FileNotFoundError:
    print("❌ Error: 'netflix_titles.csv' file not found!")
    exit()

# 2. Initial Data Look and Cleaning
print("--- Data Set Summary ---")
print(f"Total Rows: {df.shape[0]}, Total Columns: {df.shape[1]}")
print("\nMissing Value Check:")
print(df.isnull().sum()) # Which column has how many missing values?

# 3. Content Type Analysis (Movie vs. Series)
plt.figure(figsize=(8, 5))
plt.style.use('ggplot') #modern look

type_counts = df["type"].value_counts()
type_counts.plot(kind="bar", color=['skyblue', 'salmon'])

plt.title("Netflix: Movie and Series Distribution", fontsize=14)
plt.ylabel("Content Count")
plt.xticks(rotation=0) 
plt.show()

# 4. Country-Based Analysis (Top 10 Content-Producing Countries)
plt.figure(figsize=(10, 6))
top_countries = df["country"].value_counts().head(10)
top_countries.plot(kind="barh", color='teal') # Yatay bar grafiği daha şıktır

plt.title("Top 10 Content-Producing Countries", fontsize=14)
plt.xlabel("Content Count")
plt.gca().invert_yaxis() # Brings the highest to the top
plt.show()

# 5. Extra Analysis: Yearly Content Addition (Bonus)
# Convert 'date_added' column to datetime and extract the year
df['year_added'] = pd.to_datetime(df['date_added'].str.strip()).dt.year
yearly_growth = df['year_added'].value_counts().sort_index()

plt.figure(figsize=(10, 5))
yearly_growth.plot(kind="line", marker='o', color='red')
plt.title("Yearly Content Addition", fontsize=14)
plt.ylabel("Added Content")
plt.grid(True)
plt.show()
