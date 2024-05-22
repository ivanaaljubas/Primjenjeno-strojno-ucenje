
import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,3,3,2,1])
y = np.array([1,1,2,2,1])

plt.plot(x,y, linewidth=1,marker=".",markersize=5)
plt.axis([0,5,0,5])
plt.xlabel("x")
plt.ylabel("y")
plt.title("Zadatak 1")

plt.show()

