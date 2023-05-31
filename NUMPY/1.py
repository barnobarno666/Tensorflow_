import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()
x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(x, np.sin(x))

def animate(i):
    line.set_ydata(np.sin(x + i/10.0))
    ax.scatter(1)
    return line

ani = animation.FuncAnimation(fig, animate, np.arange(1, 200), interval=25)
plt.show()
