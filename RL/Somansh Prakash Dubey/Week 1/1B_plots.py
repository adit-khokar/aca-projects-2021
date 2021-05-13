import matplotlib.pyplot as plt
import numpy as np

x_coordinate = int(input("Enter x coordinate :"))
y_coordinate = int(input("Enter y coordinate :"))
size = int(input("Enter Size : "))
x = np.array([np.random.randint(0,x_coordinate) for i in range(size)])
y = np.array([np.random.randint(0,y_coordinate) for i in range(size)])

print(x)
print(y)

plt.plot(x,y)
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.show()


plt.bar(x,y)
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.show()

plt.hist(x)
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.show()


plt.pie(x,explode=[np.random.random() for i in range(size)],shadow=True)
plt.show()

plt.pie(x,shadow=True)
plt.show()