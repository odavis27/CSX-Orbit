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
        #self.trail_line, = plt.plot([], [], color=self.trail_color, alpha=0.5)
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
    def draw_last_trails(self):
        plt.plot([i.x for i in self.balls][-2:], [i.y for i in self.balls][-2:], color=self.trail_color)
        #self.trail.set_data(self.history_x, self.history_y)
        #self.trail_line.set_data(self.history_x, self.history_y)
        #self.history_x = self.history_x[-50:]
        #self.history_y = self.history_y[-50:]

        # REWRITE: Update the data instead of calling plt.plot()
        #self.trail_line.set_data([i.x for i in self.balls], [i.x for i in self.balls])
        #self.marker.set_data([self.x], [self.y])
        #pass