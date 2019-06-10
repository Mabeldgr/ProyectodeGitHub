print('Third quartile = ',np.percentile(trim_data,75))
iqr = np.percentile(trim_data,75)-np.percentile(trim_data,25)
print('IQR = ',iqr)
plt.boxplot(trim_data)