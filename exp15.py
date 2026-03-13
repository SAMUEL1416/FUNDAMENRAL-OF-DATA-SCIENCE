import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

control = np.array([5,6,7,5,6,5,7])
treatment = np.array([8,9,7,8,9,10,8])


t_stat, p_value = stats.ttest_ind(treatment, control)

print("T-Statistic:", t_stat)
print("P-Value:", p_value)


data = [control, treatment]

plt.boxplot(data)
plt.xticks([1,2], ["Control", "Treatment"])
plt.title("Treatment Effect Comparison")
plt.show()
