import matplotlib.pyplot as plt
def plotting(value1, value2):
    plt.scatter(value1, value2,edgecolor = 'none',c=y,cmap=plt.cm.Reds, s=100)
    return plt.show()

x = list(range(1,5))
y = list(range(1,8,2))

plotting(x,y)