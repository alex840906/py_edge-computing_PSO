import random
import numpy as np
import copy
def update_Pbest(Particle_list,Pbest_Particle_list):
    for i in range(len(Particle_list)):
        if Particle_list[i].consumption > Pbest_Particle_list[i].consumption:
            Pbest_Particle_list[i] = copy.deepcopy(Particle_list[i])
    return Pbest_Particle_list

def update_Gbest(Pbest_Particle_list , Gbest_Particle):
    for i in range(len(Pbest_Particle_list)):
        if Pbest_Particle_list[i].consumption > Gbest_Particle.consumption:
            Gbest_Particle = copy.deepcopy(Pbest_Particle_list[i])
    return Gbest_Particle


def subtraction(array_x,array_y):
    subtraction = array_x ^ array_y
    #print(subtraction)
    return subtraction.astype(int)
    

def addition(p1,p2,p3,velocity,Pbest_position,Gbest_position):
    uncertain_index = np.zeros([len(velocity)])
    for i in range(len(velocity)):
        uncertain_index[i] = \
            p1 * velocity[i] + p2 * Pbest_position[i] + p3 * Gbest_position[i]
    #print(uncertain_index)
    for i in range(len(uncertain_index)):
            r = random.uniform(0,1)
            if uncertain_index[i] > r:
                uncertain_index[i] = 1
            else:
                uncertain_index[i] = 0
    #print(uncertain_index)
    
    return uncertain_index.astype(int)

def evaluate_coefficient_p(consumption,Pbest_consumption,Gbest_consumption):
    coefficient_p1 = consumption / \
        (consumption +  Pbest_consumption + Gbest_consumption)
    coefficient_p2 = Pbest_consumption / \
        (consumption +  Pbest_consumption + Gbest_consumption)
    coefficient_p3 = Gbest_consumption / \
        (consumption +  Pbest_consumption + Gbest_consumption)
    #print (coefficient_p1,coefficient_p2,coefficient_p3)
    return coefficient_p1,coefficient_p2,coefficient_p3

def multiplication(Particle):
    for i in range(len(Particle.position)):
        if Particle.velocity[i] == 1:
            Particle.position[i] = not Particle.position[i]
    
    return Particle.position.astype(int)


