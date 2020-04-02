import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = np.array(pd.read_csv('data.csv'))

if True:
    # Plot positions
    plt.figure(1)
    plt.title('Position Estimate')
    filterName=['True Position', 'Prediction only','EKF Estimate', 'UKF Estimate']
    for i in range(4):
        plt.plot(data[:,0 + i*3],data[:,1 + i*3], label=filterName[i])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()

# Estimation error (euclidian distance)

plt.figure(2)
plt.title('Estimate errors from true position (Euclidian distance)')
errorName=['EKF Error', 'UKF Error']
for i in range(2):
    error = np.sqrt((data[:,0]-data[:,6 + i * 3])**2 + (data[:,1]-data[:,7 + i * 3])**2)
    plt.plot(error, label=errorName[i])
plt.legend()
plt.xlabel('Iteration')
plt.ylabel('Error')

# Plot cov
kfName=['True','Pred','EKF', 'UKF']
#plt.figure(3)
#plt.title('covariance')
for j in range(2):
    plt.figure(3+j)
    plt.title("%scov" % kfName[j+2])
    for i in range(9):
        if i / 3 >= i % 3:
            plt.plot(data[:,12 + i + 9 * j], label="%scov %d,%d" % (kfName[j+2], i / 3, i % 3))
    plt.legend()
    plt.xlabel('Iteration')
    plt.ylim([-10,10])

# Plot t-y
plt.figure(5)
plt.title('t-position')
axis=['x','y']
for i in range(4):
    for j in range(2):
        plt.plot(data[:,j+i*3], label="%s%s" % (kfName[i],axis[j]))
plt.legend()
plt.xlabel('Iteration')
plt.ylabel('pos')

plt.show()
