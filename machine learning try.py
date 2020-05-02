import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-50,50,10000)
y = np.sin(2*x)*x
plt.plot(x,y)
plt.show()