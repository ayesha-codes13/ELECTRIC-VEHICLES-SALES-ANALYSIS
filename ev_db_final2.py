# ✅ EV Dashboard — Clean Final Version (No Overlap, Formatted Numbers)
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# ✅ Always clear old figures to avoid multiple dashboards
plt.close('all')

# ✅ Theme setup
green = '#388E3C'
light_green = '#A5D6A7'
bg_color = '#F9FAF9'
plt.style.use('ggplot')
plt.rcParams['axes.facecolor'] = bg_color
plt.rcParams['figure.facecolor'] = 'white'

# ✅ Load Excel File
file_path = r"C:\Users\Public\electric vehicle sales\Cleaned_Electric_Vehicle_Sales.xlsx"
df = pd.read_excel(file_path)

# ✅ Fix missing Month_Number or Quarter
if "Month_Number" not in df.columns:
    month_map = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,
                 'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}
    df["Month_Number"] = df["Month_Name"].map(month_map)
df["Quarter"] = ((df["Month_Number"] - 1)//3) + 1

# ✅ KPI calculations
total_sales = df["EV_Sales_Quantity"].sum()
state_sales = df.groupby("State")["EV_Sales_Quantity"].sum()
highest_state = state_sales.idxmax()
highest_state_sales = state_sales.max()
yearly_sales = df.groupby("Year")["EV_Sales_Quantity"].sum()
highest_year = yearly_sales.idxmax()
highest_year_sales = yearly_sales.max()

vehicle_class_sales = df.groupby("Vehicle_Class")["EV_Sales_Quantity"].sum().sort_values(ascending=False)
top_classes = vehicle_class_sales.head(8).sort_values(ascending=True)

vehicle_type_sales = df[df["Vehicle_Type"].isin(["2W_Personal","3W_Shared","4W_Personal"])]
vehicle_type_sales = vehicle_type_sales.groupby("Vehicle_Type")["EV_Sales_Quantity"].sum()

quarterly_sales = df.groupby("Quarter")["EV_Sales_Quantity"].sum()
month_sales = df.groupby("Month_Number")["EV_Sales_Quantity"].sum()

# ✅ Create Dashboard Layout
fig = plt.figure(figsize=(18, 10), constrained_layout=True)
gs = GridSpec(3, 3, height_ratios=[0.4, 1, 1], figure=fig)

# ✅ KPI Section
kpi_ax = plt.subplot(gs[0, :])
kpi_ax.axis('off')
kpi_ax.text(0, 1.0, f"• Total EV Sales: {total_sales:,.0f}", fontsize=13, color=green)
kpi_ax.text(0, 0.8, f"• Top State: {highest_state} ({highest_state_sales:,.0f})", fontsize=13, color=green)
kpi_ax.text(0, 0.6, f"• Highest Year: {highest_year} ({highest_year_sales:,.0f})", fontsize=13, color=green)
kpi_ax.text(0, 0.4, "• Top Vehicle Types: 2W / 3W / 4W", fontsize=13, color=green)
kpi_ax.set_title("⚡ Electric Vehicle Market Dashboard (2014–2024)", fontsize=18, fontweight='bold', color=green, pad=30)

# ✅ Chart 1 — Yearly Sales
ax1 = plt.subplot(gs[1, 0])
ax1.plot(yearly_sales.index, yearly_sales.values, marker='o', color=green)
ax1.set_title("Year-wise EV Sales")
ax1.set_xlabel("Year")
ax1.set_ylabel("Sales Count")
ax1.ticklabel_format(style='plain', axis='y')
ax1.grid(True, linestyle='--', alpha=0.5)

# ✅ Chart 2 — Top 10 States (Formatted Axis + Labels)
ax2 = plt.subplot(gs[1, 1])
top_states = state_sales.nlargest(10)
bars = ax2.barh(top_states.index, top_states.values, color=light_green, edgecolor=green)
ax2.set_title("Top 10 States by EV Sales")
ax2.set_xlabel("Sales Count")
ax2.invert_yaxis()
ax2.ticklabel_format(style='plain', axis='x')

# Add commas and labels at end of each bar
for bar in bars:
    ax2.text(bar.get_width() + (bar.get_width() * 0.01),
             bar.get_y() + bar.get_height()/2,
             f"{int(bar.get_width()):,}",
             va='center', fontsize=9, color='black')

# ✅ Chart 3 — Vehicle Class (Top 8)
ax3 = plt.subplot(gs[1, 2])
ax3.barh(top_classes.index, top_classes.values, color='#81C784', edgecolor=green)
ax3.set_title("Top 8 Vehicle Classes by EV Sales")
ax3.set_xlabel("Sales Count")
ax3.ticklabel_format(style='plain', axis='x')
for i, v in enumerate(top_classes.values):
    ax3.text(v + (v * 0.01), i, f"{int(v):,}", va='center', fontsize=9)

# ✅ Chart 4 — Quarterly Sales
ax4 = plt.subplot(gs[2, 0])
ax4.fill_between(quarterly_sales.index, quarterly_sales.values, color=light_green, alpha=0.8)
ax4.plot(quarterly_sales.index, quarterly_sales.values, color=green)
ax4.set_title("Quarterly Sales Trend")
ax4.set_xlabel("Quarter")
ax4.set_ylabel("Sales Count")
ax4.grid(True, linestyle='--', alpha=0.5)

# ✅ Chart 5 — Month-wise Sales
ax5 = plt.subplot(gs[2, 1])
ax5.bar(month_sales.index, month_sales.values, color=green)
ax5.set_title("Month-wise Sales Trend")
ax5.set_xlabel("Month")
ax5.set_ylabel("Sales Count")
ax5.grid(True, linestyle='--', alpha=0.5)

# ✅ Chart 6 — Vehicle Type Comparison
ax6 = plt.subplot(gs[2, 2])
bars = ax6.barh(vehicle_type_sales.index, vehicle_type_sales.values, color=['#2E7D32', '#66BB6A', '#A5D6A7'], edgecolor=green)
ax6.set_title("2W vs 3W vs 4W Sales Distribution")
ax6.set_xlabel("Sales Count")
ax6.ticklabel_format(style='plain', axis='x')
for bar in bars:
    ax6.text(bar.get_width() + (bar.get_width() * 0.01),
             bar.get_y() + bar.get_height()/2,
             f"{int(bar.get_width()):,}",
             va='center', fontsize=9, color='black')

# ✅ Save and Display
output = r"C:\Users\Shaikh Ayesha\Desktop\EV_Dashboard_Final_Fixed.png"
plt.savefig(output, dpi=300, bbox_inches='tight')
plt.show()
plt.close('all')

print("✅ Dashboard Created Successfully!")
print(f"✅ Saved to Desktop: {output}")
