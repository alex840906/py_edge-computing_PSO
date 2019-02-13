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
        #print('p1,p2,p3' , p1,p2,p3)
        tmp_Pbest = pso_operator.subtraction(self.position,Pbest_particle.position)
        tmp_Gbest = pso_operator.subtraction(self.position,Gbest_particle.position)
        self.velocity = pso_operator.addition(p1,p2,p3,self.velocity,tmp_Pbest,tmp_Gbest)
        self.position = pso_operator.multiplication(self)


        
        


                


