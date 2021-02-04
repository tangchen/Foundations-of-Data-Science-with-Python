labels=['probability/statistics','linear algebra','visualization','simulation']

percentages=[0.4,0.2,0.2,0.4]

import matplotlib.pyplot as plt

plt.pie(percentages,labels=labels)
plt.savefig("tools.pdf")



