import random
import numpy as np
import pso_operator

class Particle(object):
    def __init__(self,position,velocity,consumption):   
        self.position = position
        self.velocity = velocity
        self.consumption = consumption

    def update(self,Pbest_particle,Gbest_particle):
        p1,p2,p3 = pso_operator.evaluate_coefficient_p(self.consumption,Pbest_particle.consumption,Gbest_particle.consumption)
        tmp_Pbest = pso_operator.subtraction(self,Pbest_particle)
        tmp_Gbest = pso_operator.subtraction(self,Gbest_particle)
        self.velocity = pso_operator.addition(p1,p2,p3,self.velocity,tmp_Pbest,tmp_Gbest)
        self.position = pso_operator.multiplication(self)


        
        


                


