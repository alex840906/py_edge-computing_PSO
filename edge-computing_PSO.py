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

particle_num = 50
device = dataset.generate_device_list()
data_size = 338

Particle_list = init.create_Particle_list(particle_num,data_size)

for paticle in Particle_list:
    paticle.consumption = evaluation.evaluate(paticle.position,device)

Pbest_particle_list = copy.deepcopy(Particle_list)

minimum = 0.0
for i in range(len(Pbest_particle_list)):
    if Pbest_particle_list[i].consumption >= minimum:
        minimum = Pbest_particle_list[i].consumption
        flag = i

Gbest_particle = copy.deepcopy(Pbest_particle_list[flag])

iteration = 0
draw_Gbest = []
while iteration < 100:
    for i in range(len(Particle_list)):
        print(i,' particle',Particle_list[i].consumption)
        Particle_list[i].update(Pbest_particle_list[i],Gbest_particle)
    for paticle in Particle_list:
        paticle.consumption = evaluation.evaluate(paticle.position,device)

    Pbest_particle_list = pso_operator.update_Pbest(Particle_list,Pbest_particle_list)
    Gbest_particle = pso_operator.update_Gbest(Pbest_particle_list,Gbest_particle)
    print('Gbest:',Gbest_particle.consumption)
    draw_Gbest.append(Gbest_particle.consumption)
    iteration += 1

Convergence_garph.draw(draw_Gbest,iteration)












