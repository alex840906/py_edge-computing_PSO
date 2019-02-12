import random
import numpy as np
from Particle import Particle

def init_deployment_table(deployment_table,data_size):
    for i in range(data_size):
        r = random.randint(0,data_size-1)
        deployment_table[i][r] = 1
    return deployment_table

def create_Particle_list(particle_num,data_size):
    Particle_list = []

    for i in range(particle_num):
        ###初始化位置(table的對角線)
        position = np.zeros([data_size])
        for j in range(data_size):
            r = random.randint(0,1)
            position[j] = r

        ###初始化速度
        velocity = np.zeros([data_size])
        for j in range(data_size):
            r = random.randint(0,1)
            velocity[j] = r
        
        Particle_list.append(Particle(position.astype(int),velocity.astype(int),None))

    return Particle_list