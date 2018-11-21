import numpy as np
import matplotlib as plt
import matplotlib.pyplot as plt
%matplotlib inline
labels='Red','Green','Yellow','Blue'
sizes=[50,20,10,20]
colours=['Red','Green','Yellow','Blue']
plt.pie(sizes,labels=labels)
plt.axis('equal')
plt.show()