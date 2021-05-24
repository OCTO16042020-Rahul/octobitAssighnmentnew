# _author_='Rahul kharatmol'

from matplotlib import pyplot as plt

plt.bar([0.25, 1.25, 2.25, 3.25, 4.25], [50, 40, 70, 80, 20],
        label="Hero cycle", width=.5)
plt.bar([.75, 1.75, 2.75, 3.75, 4.75], [80, 20, 20, 50, 60],
        label="Cycle cycle", color='r', width=.5)
plt.legend()
plt.xlabel('Days')
plt.ylabel('Distance (kms)')
plt.title('Information')
plt.show()
import matplotlib.pyplot as plt
population_age = [22,55,62,45,21,22,34,42,42,4,2,102,95,85,55,110,120,70,65,55,111,115,80,75,65,54,44,43,42,48]
bins = [0,10,20,30,40,50,60,70,80,90,100]
plt.hist(population_age, bins, histtype='bar', rwidth=0.8)

plt.xlabel('age groups')
plt.ylabel('Number of people')

plt.title('Histogram')
plt.show()

import matplotlib.pyplot as plt
# importing the required libraries
import matplotlib.pyplot as plt
import numpy as np

# define data values
x = np.array([5, 6, 7, 8]) # X-axis points
y = x*2 # Y-axis points

plt.plot(x, y) # Plot the chart
plt.show() # display

import matplotlib.pyplot as plt
import numpy as np

n = 10
x = np.random.rand(n)
y = np.random.rand(n)

plt.scatter(x, y)
plt.show()
import matplotlib.pyplot as plt
import numpy as np

x = [100, 200, 300, 400, 500]
labels = ['first', 'second', 'third', 'fourth', 'fifth']

plt.pie(x, labels=labels, autopct='%1.1f%%')

