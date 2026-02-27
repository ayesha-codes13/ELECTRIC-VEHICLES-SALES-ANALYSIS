import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# ====================== LOAD CLEANED DATA ======================
file_path = r"C:\Users\Public\electric vehicle sales\Cleaned_Electric_Vehicle_Sales.xlsx"
df = pd.read_excel(file_path)

# ====================== FIX DATE COLUMNS ======================
if "Month_Number" not in df.columns:
    month_map = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,
                 'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}
    df["Month_Number"] = df["Month_Name"].map(month_map)

df["Quarter"] = ((df["Month_Number"] - 1) // 3) + 1

# ====================== KPI ======================
total_sales = df["EV_Sales_Quantity"].sum()

state_sales = df.groupby("State")["EV_Sales_Quantity"].sum()
highest_state = state_sales.idxmax()
highest_state_sales = state_sales.max()

yearly_sales = df.groupby("Year")["EV_Sales_Quantity"].sum()
highest_year = yearly_sales.idxmax()
highest_year_sales = yearly_sales.max()

# Short grouping for 2W / 3W / 4W
df["Vehicle_Group"] = df["Vehicle_Type"].replace({
    '2W_Personal': '2W', '2W_Shared': '2W',
    '3W_Personal': '3W', '3W_Shared': '3W', '3W_Shared_LowSpeed': '3W',
    '3W_Goods': '3W', '3W_Goods_LowSpeed': '3W',
    '4W_Personal': '4W', '4W_Shared': '4W'
})

vehicle_group_sales = df.groupby("Vehicle_Group")["EV_Sales_Quantity"].sum().loc[["2W","3W","4W"]]

# ====================== DASHBOARD LAYOUT ======================
plt.figure(figsize=(18, 8))
gs = GridSpec(2, 3, wspace=0.4, hspace=0.7)

# ====================== KPI TEXT ======================
plt.suptitle("EV Market Dashboard (2014–2024)", fontsize=20, fontweight="bold")

kpi_text = (
    f"• Total EV Sales: {total_sales:,}\n"
    f"• Highest Selling State: {highest_state} ({highest_state_sales:,})\n"
    f"• Best Year: {highest_year} ({highest_year_sales:,})"
)

plt.figtext(0.02, 0.94, kpi_text, fontsize=12)

# ====================== CHARTS ======================

charts = [
    (0, 0, yearly_sales, "Year-wise EV Sales"),
    (0, 1, state_sales.nlargest(10), "Top 10 States"),
    (0, 2, df.groupby("Quarter")["EV_Sales_Quantity"].sum(), "Quarterly Sales (Q1–Q4)"),
    (1, 0, df.groupby("Month_Number")["EV_Sales_Quantity"].sum(), "Month-wise Sales"),
    (1, 1, vehicle_group_sales, "2W vs 3W vs 4W"),
    (1, 2, df.groupby("State")["EV_Sales_Quantity"].sum().sample(6), "Random 6 States Comparison")
]

for r, c, data, title in charts:
    ax = plt.subplot(gs[r, c])
    data.plot(kind="bar", ax=ax)
    ax.set_title(title)
    ax.tick_params(axis='x', labelrotation=45, labelsize=8)

plt.show()
