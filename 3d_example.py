# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 21:28:27 2018

@author: garci
"""

'in this example the y-axis is a certain "ith" 2d plot from the z(x) = i* cos(x) plots'

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax1 = fig.add_subplot(111,projection='3d')


depth=50
for i in range(depth):
    
    import numpy.random as ran
    x=np.linspace(0,3.14*4,100)
    z=i*np.cos(x)
    ax1.plot(x,np.ones(len(x))*i,z,'-')

plt.show()
