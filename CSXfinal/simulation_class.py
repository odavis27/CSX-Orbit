import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class ball:
    def __init__(self,Xs,Ys):
        self.Xs = Xs
        self.Ys = Ys

class simulation:
    # init function runs with class is created
    # self argument is always needed and automatically passed 
    def __init__(self,trail_color = "black"):
        # Defines the class attributes Xs and Ys
        # An attribute is a variable specific to a class
        self.trail_color = trail_color
    def draw(self, points):
        # datastructure for points: [(X,Y,size,color),...]
        plt.cla()
        for p in points:
            plt.plot(p[0], p[1], marker="o", color=p[3], markersize=p[2])
        

    def trail(self, Xs, Ys,col="black"):
        Xs = [i for i in Xs]
        Ys = [i for i in Ys]
        plt.plot(Xs, Ys, color=col)
