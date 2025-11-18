import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Data
data = pd.DataFrame({
    "Answer": ["maybe", "probCant", "defCan", "probCan"],
    "Percent": [39, 7, 23, 25],
    "Score": [231, 225, 247, 247]
})

# Scale percents into reasonable widths
scale = 0.1
widths = data["Percent"] * scale

# Compute left edges so bars don’t overlap
left_edges = np.cumsum([0] + list(widths[:-1]))

# Use a nice color palette
colors = sns.color_palette("Set3", len(data)) # Spectral, mako, viridis

fig, ax = plt.subplots(figsize=(9,6))

## Draw bars
#for left, width, score, ans, pct, color in zip(left_edges, widths, data["Score"], data["Answer"], data["Percent"], colors):
#    ax.bar(left, score, width=width, color=color, edgecolor="black", align="edge")
#    ax.text(left + width/2, score + 1, f"{ans}\n{score}\n{pct}%", 
#            ha="center", va="bottom", fontsize=9, weight="bold")

# Draw bars
for left, width, score, ans, pct, color in zip(left_edges, widths, data["Score"], data["Answer"], data["Percent"], colors):
    ax.bar(left, score, width=width, color=color, edgecolor="black", align="edge")
    # Label only the answer (bigger and bold)
    ax.text(left + width/2, score + 2, ans, ha="center", va="bottom", fontsize=12, weight="bold")
    # Label percent INSIDE bar, centered
    ax.text(left + width/2, 210, f"{pct}%", ha="center", va="center", fontsize=12)
    #ax.text(left + width/2, score/2, f"{pct}%", ha="center", va="center", fontsize=11, weight="bold", color="black")


# Reference line at score = 235
ax.axhline(235, linestyle="--", color="gray", label="Average Score of All Students")


ax.set_ylabel("Average Score by Answer")
ax.set_title("Remote Math: Recognize when don't understand", fontsize=14)

# Start y at 190
ax.set_ylim(190, max(data["Score"]) + 10)

# Remove default x-ticks (since x is now cumulative percent widths)
ax.set_xticks([])
ax.set_xlabel("Student Response")

#ax.set_xticklabels(data["Answer"])
ax.legend()

plt.show()
