import matplotlib.pyplot as plt
import numpy as np

x=range(1,100)
# y=[2*v for v in x]
y=range(1,100)
print(x, y)
plt.plot(x, y)
pos=plt.ginput(10000)
print(pos)
