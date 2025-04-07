import matplotlib.pyplot as plt
import numpy as np

# Model names and metric values
models = ['Random Forest', 'SVM', 'MLP']
accuracy = [0.9828, 0.8408, 0.9716]
macro_precision = [0.85, 0.13, 0.79]
macro_recall = [0.71, 0.13, 0.66]
macro_f1 = [0.75, 0.13, 0.66]
weighted_f1 = [0.98, 0.79, 0.97]

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(12, 7))

# Bar width and positions
bar_width = 0.15
index = np.arange(len(models))

# Plot each metric
ax.bar(index - 2*bar_width, accuracy, bar_width, label='Accuracy', color='#1f77b4')
ax.bar(index - bar_width, macro_precision, bar_width, label='Macro Precision', color='#ff7f0e')
ax.bar(index, macro_recall, bar_width, label='Macro Recall', color='#2ca02c')
ax.bar(index + bar_width, macro_f1, bar_width, label='Macro F1-Score', color='#d62728')
ax.bar(index + 2*bar_width, weighted_f1, bar_width, label='Weighted F1-Score', color='#9467bd')

# Labeling
ax.set_xlabel('Models')
ax.set_ylabel('Scores')
ax.set_title('Comprehensive Model Comparison')
ax.set_xticks(index)
ax.set_xticklabels(models)
ax.set_ylim(0, 1.1)
ax.legend()
ax.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Show the plot
plt.show()
