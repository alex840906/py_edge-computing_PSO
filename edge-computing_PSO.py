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
import convergence_graph

mutation_rate = 0.1
particle_num = 50
device = dataset.generate_device_list()
data_size = dataset.candidate_station_quantity()

Particle_list = init.create_Particle_list(particle_num,data_size)

for paticle in Particle_list:
    paticle.consumption = evaluation.evaluate(paticle.position)

Pbest_particle_list = copy.deepcopy(Particle_list)

minimum = 0.0
for i in range(len(Pbest_particle_list)):
    if Pbest_particle_list[i].consumption >= minimum:
        minimum = Pbest_particle_list[i].consumption
        flag = i

Gbest_particle = copy.deepcopy(Pbest_particle_list[flag])
count = 0
iteration = 0

draw_Gbest = []
while count < 30000:
    for i in range(len(Particle_list)):
        Particle_list[i].update(Pbest_particle_list[i],Gbest_particle)
    for paticle in Particle_list:
        paticle.consumption = evaluation.evaluate(paticle.position)
        count += 1
    
    Pbest_particle_list = pso_operator.update_Pbest(Particle_list,Pbest_particle_list)
    Gbest_particle = pso_operator.update_Gbest(Pbest_particle_list,Gbest_particle)

    # for particle in Particle_list:
    #     particle.mutation(mutation_rate)

    print(count, end='')
    print(',', end='')
    print(Gbest_particle.consumption)




convergence_graph.draw(draw_Gbest,iteration)
