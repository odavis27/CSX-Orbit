G = 6.67e-11

class planet:
    def __init__(self, MH, XP, VyP, MP, XH, VyH):
        self.T = .5
        self.MH = MH
        self.XP = XP
        self.MP = MP
        self.XH = XH
        self.YP = 0
        self.YH = 0
        self.VxP = 0
        self.VxH = 0
        self.VyP = VyP
        self.VyH = VyH

    def calc_pos(self):
        global G
        self.DX = self.XP-self.XH
        self.DY = self.YP-self.YH
        #pythag theorem to find straight distance from a to b
        linear_distance = (self.DX**2+self.DY**2)**0.5
        #multiplies gravitational force by their distance (X or Y) divided by linear distance
        #note: the ratio of distance and linear distance is sin for x and cos for y of angle of orbit
        self.X_force = (G*((self.MH*self.MP)/linear_distance**2))*(self.DX/linear_distance)
        self.Y_force = (G*((self.MH*self.MP)/linear_distance**2))*(self.DY/linear_distance)
        #updates velocities using a=f/m with force components as f
        self.VxP -= self.X_force/self.MP*self.T
        self.VxH += self.X_force/self.MH*self.T
        self.VyP -= self.Y_force/self.MP*self.T
        self.VyH += self.Y_force/self.MH*self.T
        #changes position according to updated velocities
        self.XP += self.VxP*self.T
        self.XH += self.VxH*self.T
        self.YP += self.VyP*self.T
        self.YH += self.VyH*self.T
        return (self.XP, self.YP, self.XH, self.YH)
