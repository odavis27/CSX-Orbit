from simulation_class import *

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