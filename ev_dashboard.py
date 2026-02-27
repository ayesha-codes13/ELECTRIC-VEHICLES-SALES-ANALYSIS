import pandas as pd

# ✅ Step 1: Enter the EXACT file path of your Excel file here:
file_path = r"C:\Users\Public\electric vehicle sales\Cleaned_Electric_Vehicle_Sales.xlsx"

# ✅ Step 2: Load the Excel file
df = pd.read_excel(file_path)

# ✅ Step 3: Display success message and first rows
print("✅ Excel File Loaded Successfully!")
print(df.head())
print("\n✅ Columns in the dataset:")
print(df.columns)
# ✅ Step 4: Feature Engineering (Adding useful time-based columns)

# 1. Ensure 'Date' is in datetime format
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# 2. Add Month_Number (1-12) using Date column
df['Month_Number'] = df['Date'].dt.month

# 3. Add Quarter (Q1, Q2, Q3, Q4)
df['Quarter'] = df['Date'].dt.quarter

# 4. Ensure Year is integer
df['Year'] = df['Year'].astype(int)

# 5. Show updated dataset sample
print("\n✅ Step 4 Completed: Added Month_Number and Quarter")
print(df[['Year', 'Month_Name', 'Month_Number', 'Quarter', 'EV_Sales_Quantity']].head())
# ✅ Step 5: Basic Data Exploration & Summary

# 1. Total EV sales overall
total_sales = df['EV_Sales_Quantity'].sum()
print(f"\n✅ Total EV Sales in Dataset: {total_sales:,}")

# 2. Years covered in dataset
print("\n✅ Years in dataset:", df['Year'].unique())

# 3. States in dataset
print("\n✅ Number of States:", df['State'].nunique())
print("✅ Sample States:", df['State'].unique()[:10])

# 4. Total EV Sales by Year
yearly_sales = df.groupby('Year')['EV_Sales_Quantity'].sum()
print("\n✅ Year-wise EV Sales:")
print(yearly_sales)

# 5. Total EV Sales by State
state_sales = df.groupby('State')['EV_Sales_Quantity'].sum().sort_values(ascending=False)
print("\n✅ Top 10 States by EV Sales:")
print(state_sales.head(10))

# 6. Total EV Sales by Vehicle Type
vehicle_sales = df.groupby('Vehicle_Type')['EV_Sales_Quantity'].sum()
print("\n✅ EV Sales by Vehicle Type:")
print(vehicle_sales)
# ✅ Step 6: Data Visualization (Dashboard - Basic Graphs)

import matplotlib.pyplot as plt
import seaborn as sns

# 1. Year-wise EV Sales Trend (Line Chart)
plt.figure(figsize=(10,5))
plt.plot(yearly_sales.index, yearly_sales.values, marker='o')
plt.title("Year-wise Electric Vehicle Sales in India")
plt.xlabel("Year")
plt.ylabel("Total EV Sales")
plt.grid(True)
plt.show()

# 2. Top 10 States by EV Sales (Bar Chart)
plt.figure(figsize=(12,6))
state_sales.head(10).plot(kind='bar')
plt.title("Top 10 States by EV Sales")
plt.xlabel("States")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.show()

# 3. EV Sales by Vehicle Type (Horizontal Bar Chart)
plt.figure(figsize=(10,6))
vehicle_sales.sort_values().plot(kind='barh')
plt.title("Electric Vehicle Sales by Vehicle Type")
plt.xlabel("Total Sales")
plt.ylabel("Vehicle Type")
plt.show()
# ✅ STEP 7.1 – Month-wise EV Sales Trend
# Group by Month_Number and calculate total sales
monthly_sales = df.groupby("Month_Number")["EV_Sales_Quantity"].sum()

plt.figure(figsize=(10,5))
plt.plot(monthly_sales.index, monthly_sales.values, marker='o')
plt.title("Month-wise Electric Vehicle Sales (Across All Years)")
plt.xlabel("Month Number (1 = Jan, 12 = Dec)")
plt.ylabel("Total EV Sales")
plt.xticks(range(1, 13))
plt.grid(True)
plt.show()
plt.pause(2)
# ✅ STEP 7.2 – Quarter-wise EV Sales Trend
quarterly_sales = df.groupby("Quarter")["EV_Sales_Quantity"].sum()

plt.figure(figsize=(8,5))
sns.barplot(x=quarterly_sales.index, y=quarterly_sales.values)
plt.title("Quarter-wise EV Sales")
plt.xlabel("Quarter")
plt.ylabel("Total EV Sales")
plt.show()
plt.pause(2)
# ✅ STEP 7.3 – 2W vs 3W vs 4W EV Sales by Year
vehicle_filtered = df[df['Vehicle_Type'].isin(['2W_Personal', '3W_Shared', '4W_Personal'])]

sales_compare = vehicle_filtered.groupby(['Year', 'Vehicle_Type'])['EV_Sales_Quantity'].sum().unstack()

sales_compare.plot(kind='bar', figsize=(12,6))
plt.title("2W vs 3W vs 4W EV Sales by Year")
plt.xlabel("Year")
plt.ylabel("Total Sales")
plt.legend(title="Vehicle Type")
plt.xticks(rotation=45)
plt.show()
plt.pause(2)
# ✅ STEP 7.4 – Heatmap: EV Sales by State vs Year
import seaborn as sns
import matplotlib.pyplot as plt

# Create pivot table (State vs Year)
state_year_sales = df.pivot_table(
    index='State', 
    columns='Year', 
    values='EV_Sales_Quantity', 
    aggfunc='sum'
)

# Plot Heatmap
plt.figure(figsize=(14, 8))
sns.heatmap(state_year_sales, cmap="YlGnBu", linewidths=0.5)
plt.title("Heatmap of EV Sales (State vs Year)")
plt.xlabel("Year")
plt.ylabel("State")
plt.show()
plt.pause(2)
# ✅ STEP 7.5 – Top 5 EV States per Year
for year in df['Year'].unique():
    top_states = df[df['Year'] == year].groupby('State')['EV_Sales_Quantity'].sum().nlargest(5)
    plt.figure(figsize=(8,4))
    top_states.plot(kind='bar')
    plt.title(f"Top 5 States in {year} by EV Sales")
    plt.xlabel("State")
    plt.ylabel("EV Sales")
    plt.xticks(rotation=45)
    plt.show()
    plt.pause(1)
  
# ✅ STEP 9: Save all existing charts into a single PDF
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt

output_pdf = r"C:\Users\Shaikh Ayesha\Desktop\EV_Dashboard_Report.pdf"

with PdfPages(output_pdf) as pdf:
    # Loop through every figure generated so far
    for fig_num in plt.get_fignums():
        fig = plt.figure(fig_num)
        pdf.savefig(fig)   # Save each figure to PDF

print("✅ All figures saved into EV_Dashboard_Report.pdf on Desktop successfully!")
# STEP 10 CODE — KPI Summary
# ✅ STEP 10: KPI SUMMARY (Key Metrics)

# Total EV Sales
total_sales = df['EV_Sales_Quantity'].sum()

# State with highest EV sales
state_sales = df.groupby('State')['EV_Sales_Quantity'].sum()
highest_state = state_sales.idxmax()
highest_state_sales = state_sales.max()

# Year with highest EV sales
yearly_sales = df.groupby('Year')['EV_Sales_Quantity'].sum()
highest_year = yearly_sales.idxmax()
highest_year_sales = yearly_sales.max()

# Most popular vehicle type
vehicle_sales = df.groupby('Vehicle_Type')['EV_Sales_Quantity'].sum()
top_vehicle_type = vehicle_sales.idxmax()
top_vehicle_sales = vehicle_sales.max()

print("\n📊 EV DASHBOARD SUMMARY")
print("--------------------------------------------------")
print(f"✅ Total EV Sales (2014–2024): {total_sales:,}")
print(f"✅ State with Highest Sales: {highest_state} ({highest_state_sales:,} vehicles)")
print(f"✅ Year with Highest Sales: {highest_year} ({highest_year_sales:,} vehicles)")
print(f"✅ Most Popular Vehicle Type: {top_vehicle_type} ({top_vehicle_sales:,} vehicles)")
print("--------------------------------------------------")
print("✅ Dashboard Analysis Completed Successfully!")
# ✅ STEP 11: Generate KPI Summary Image
import matplotlib.pyplot as plt

# Prepare KPI values
kpi_total_sales = f"{total_sales:,}"
kpi_best_state = f"{highest_state} ({highest_state_sales:,})"
kpi_best_year = f"{highest_year} ({highest_year_sales:,})"
kpi_best_vehicle = f"{top_vehicle_type} ({top_vehicle_sales:,})"

# Create the KPI image
plt.figure(figsize=(10, 6))
plt.suptitle("EV Market KPI Summary (2014–2024)", fontsize=16, fontweight='bold')

plt.text(0.1, 0.75, f"✅ Total EV Sales:\n   {kpi_total_sales}", fontsize=14)
plt.text(0.1, 0.55, f"✅ Highest Selling State:\n   {kpi_best_state}", fontsize=14)
plt.text(0.1, 0.35, f"✅ Highest EV Sales Year:\n   {kpi_best_year}", fontsize=14)
plt.text(0.1, 0.15, f"✅ Most Popular Vehicle Type:\n   {kpi_best_vehicle}", fontsize=14)

plt.axis("off")

# Save image on desktop
plt.savefig(r"C:\Users\Shaikh Ayesha\Desktop\KPI_Summary.png", dpi=300)

plt.show()
# ✅ STEP 11 – Improved KPI Summary Image (Professional Layout)

import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10,6))
fig.patch.set_facecolor("white")

plt.title("EV Market KPI Summary (2014–2024)", fontsize=18, fontweight="bold", pad=20)

kpi_text = (
    f"📌 Total EV Sales:              {total_sales:,}\n\n"
    f"📌 Highest Selling State:       {highest_state} ({highest_state_sales:,})\n\n"
    f"📌 Highest EV Sales Year:       {highest_year} ({highest_year_sales:,})\n\n"
    f"📌 Most Popular Vehicle Type:   {top_vehicle_type} ({top_vehicle_sales:,})"
)

plt.text(0.1, 0.5, kpi_text, fontsize=14, va='center', ha="left", family='monospace')

plt.axis("off")

# ✅ Save final KPI image
plt.savefig(r"C:\Users\Shaikh Ayesha\Desktop\KPI_Summary.png", dpi=300, bbox_inches="tight")

plt.show()
