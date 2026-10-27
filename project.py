import matplotlib.pyplot as plt
from randwalk import RandomWalk

rw = RandomWalk()
rw.fill_walk()
plt.scatter(rw.x, rw.y, c=rw.y, cmap=plt.cm.Greens, edgecolor='none')
plt.show()

