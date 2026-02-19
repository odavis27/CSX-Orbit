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
    def draw(self, X1, Y1):
        plt.cla()
        plt.plot(X1, Y1, marker="o", color='black', markersize=8)
    def trail(self, Xs, Ys):
        Xs = [i for i in Xs]
        Ys = [i for i in Ys]
        plt.plot(Xs, Ys, color=self.trail_color)
