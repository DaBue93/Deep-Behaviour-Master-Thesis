###DATA###
#use data from data_preprocessing.py

###show data
df.head()

###SHOW COLUMNS###
df.columns

###PLOT HEATMAP
plt.figure(figsize=(10,10))
matrix = np.triu(df.corr())
ax = sns.heatmap(df.corr(), annot=True, fmt='.1g',  cmap= 'coolwarm', mask=matrix, square=True, linewidths=.5)
ax.set_title("Correlation Plot")
plt.xticks(rotation=70)
plt.tight_layout()

