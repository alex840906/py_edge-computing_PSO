import random
import numpy as np
import csv
import Particle
import fitness
import initialize as init
import evaluation
import dataset
import pso_operator
import copy

particle_num = 10
device = dataset.generate_device_list()
data_size = 1094

Particle_list = init.create_Particle_list(particle_num,data_size)

for paticle in Particle_list:
    paticle.consumption = evaluation.evaluate(paticle.position,device)

Pbest_particle_list = copy.deepcopy(Particle_list)

minimum = 0.0
for i in range(len(Pbest_particle_list)):
    if Pbest_particle_list[i].consumption >= minimum:
        minimum = Pbest_particle_list[i].consumption
        flag = i

Gbest_particle = Pbest_particle_list[flag]

iteration = 0
while iteration < 10:
    for paticle in Particle_list:
        paticle.consumption = evaluation.evaluate(paticle.position,device)
    for i in range(len(Particle_list)):
        Particle_list[i].update(Pbest_particle_list[i],Gbest_particle)

    Pbest_particle_list = pso_operator.update_Pbest(Particle_list,Pbest_particle_list)
    Gbest_particle = pso_operator.update_Gbest(Pbest_particle_list,Gbest_particle)
    print(Gbest_particle.consumption)
    iteration += 1












