import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("tips.csv")

# Pie Chart Gender
gender = data['sex'].value_counts()
plt.title("Persentase Gender")
plt.pie(gender, labels=gender.index, autopct='%1.1f%%')
plt.show()

# Bar Chart Tips per Hari
avg_tip = data.groupby('day')['tip'].mean()
avg_tip.plot(kind='bar')
plt.title("Rata-rata Tips per Hari")
plt.xlabel("Hari")
plt.ylabel("Tip")
plt.show()
