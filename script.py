import pandas as pd
import matplotlib.pyplot as plt
import calplot
import matplotlib.ticker as mticker

# Read the dataset
df = pd.read_csv('COVID_US_cases.csv', parse_dates=['date'])

# Aggregate daily cases
daily_cases = df.groupby('date')['new_confirmed'].sum()

# Create the calendar heatmap
fig, axes = calplot.calplot(
    daily_cases,
    cmap='YlOrRd',
    fillcolor='lightgrey',
    figsize=(15, 8),
    colorbar=True,
    yearlabel_kws={'fontsize': 14},
    linewidth=0.5,
)

# Add title
fig.suptitle(
    "New Confirmed COVID-19 Cases in the United States (2020-2022)",
    fontsize=18,
    fontweight="bold",
)

# Access the colorbar and update labels
cbar = fig.axes[-1]  # The last axis is the colorbar
cbar.set_ylabel("Daily Confirmed Cases", fontsize=12)

# Format the colorbar ticks with 'M' instead of scientific notation
def millions(x, pos):
    return f"{x*1e-6:.1f}M"

cbar.yaxis.set_major_formatter(mticker.FuncFormatter(millions))

plt.show()
