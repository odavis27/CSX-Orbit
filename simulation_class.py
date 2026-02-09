import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class ball:
    def __init__(self,color,x=0,y=0):
        self.x = x
        self.y = y
        self.color = (0,0,0)
    def goto(self,x,y):
        self.x = x
        self.y = y
    def plot(self,radius = 8):
        plt.plot(self.x, self.y, marker="o", markersize=radius, markeredgecolor=self.color, markerfacecolor=self.color)

class simulation:
    # init function runs with class is created
    # self argument is always needed and automatically passed 
    def __init__(self,trail_color = "green"):
        # Defines the class attributes Xs and Ys
        # An attribute is a variable specific to a class
        self.balls = []
        self.trail_color = trail_color
    def clear_balls(self):
        self.balls.clear()
    def add_ball(self,x=0,y=0,col = None):
        if col == None:
            col = self.trail_color
        self.balls.append(ball(col,x,y))
    def draw(self,size=8,with_trails = False):
        for ball in self.balls:
            ball.plot(radius=size)
        if with_trails:
            Xs = [i.x for i in self.balls]
            Ys = [i.y for i in self.balls]
            plt.plot(Xs, Ys, color=self.trail_color)


#========================================================
#========================================================
# example use

col = "blue"
new_sim = simulation(col)


x = 0
def anim(i):
    global x
    x+=1
    new_sim.draw(with_trails=True)
    new_sim.add_ball(x,100)


fig, ax = plt.subplots()
ani = FuncAnimation(plt.gcf(), anim, interval=500)
plt.show()