
print('IQR = ',iqr)
plt.boxplot(dataCol)

plt.figure()
per = 0.1
trim_data = stats.trimboth(data[col],per)
print('Statics for ',col,'Trimmed at ',per)
print('Minimun = ',np.min(trim_data))