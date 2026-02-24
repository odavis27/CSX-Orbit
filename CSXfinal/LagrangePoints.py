from calc_position import *
from simulation_class import *
from math import sqrt
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

new_sim = simulation()      # create new simulation object

sun = planet(mass=1.989e30, X=0, Y=0, Vx=0, Vy=0)
vy = 29780
earth = planet(mass=5.972e24, X=1.496e11, Y=0, Vx=0, Vy=vy)         

# L4 Asteriod (60 degrees ahead)
ast = planet(mass=4.6e17, X=7.47914e10, Y=1.29543e11, Vx=-((sqrt(3)/2)*vy), Vy=(1/2)*vy)
# L5 Asteroid (60 degrees behind)
ast_l5 = planet(mass=4.6e17, X=7.47914e10, Y=-1.29543e11, Vx=((sqrt(3)/2)*vy), Vy=(1/2)*vy)      # By the way, these positions are very slightly wrong as they did not account for the focci, and so they may drift apart given time.

# Adjust the time step for the scale of the solar system. delta t is really big to make simulation run faster
earth.T = 100000
sun.T = 100000
ast.T = 100000
ast_l5.T = 100000

planet_X, planet_Y = [], []
host_X, host_Y = [], []
ast_x, ast_y = [], []
ast_l5_x, ast_l5_y = [], []

def anim(i):
    # Earth pulled by Sun; leaving out the asteroids but because their masses are so small, they would have a negligable impact on the earth
    earth.X, earth.Y = earth.calc_pos([sun])
    # Sun pulled by Earth, barely moves but included for accuracy anyways
    sun.X, sun.Y = sun.calc_pos([earth])
    
    # Asteroids pulled by Sun and Earth (ignoring other asteroid)
    ast.X, ast.Y = ast.calc_pos([sun, earth])
    ast_l5.X, ast_l5.Y = ast_l5.calc_pos([sun, earth])

    # track their positions
    planet_X.append(earth.X)
    planet_Y.append(earth.Y)
    host_X.append(sun.X)
    host_Y.append(sun.Y)
    ast_x.append(ast.X)
    ast_y.append(ast.Y)
    ast_l5_x.append(ast_l5.X)
    ast_l5_y.append(ast_l5.Y)

    # Draw the bodies
    new_sim.draw((
        (earth.X, earth.Y, 5, "blue"), 
        (sun.X, sun.Y, 15, "green"),
        (ast.X, ast.Y, 5, "red"),
        (ast_l5.X, ast_l5.Y, 5, "orange")))
    
    new_sim.trail(planet_X, planet_Y, col="blue")       # add trails
    #new_sim.trail(ast_x, ast_y, col="red")
    #new_sim.trail(ast_l5_x, ast_l5_y, col="orange")

fig, ax = plt.subplots()
ani = FuncAnimation(fig, anim, interval=0.00001)
plt.show()