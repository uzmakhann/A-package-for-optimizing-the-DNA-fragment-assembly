
"""
Created on Fri Apr 27 12:18:13 2018

@author: Uzma  (Main file)

"""

import time
import re
import numpy as np
import Genetic as GA
import directed_representation as directed
import score_RRGA as RRGA
import Resultant_layout as RL_fit
#import swalign_score as align;
import tsp_2op as opt
import math
import copy
import pandas as pd



start=time.clock() 

PALWS=[]
mut=[]
arrayscore=[]
seq=[]
array_score=[]
bol=1
string=''
#**************** set parameter ****************#
sel_par=5            # number of population
n_generation=10    # number of generation
muatation_rate=5   # mutation rate

#**************** text file for saving results ****************#
BLF = open('Best_layout_fitness.txt',"a")
BL = open('Best_layout.txt',"a")
ITER = open('solution_iteration.txt',"a")


#****************Reading file****************#
pattern=re.compile("[^\w]")
fname='f25_305.txt'
with open(fname) as f:
    for line in f:
        if line[0]=='>':
            seq.append(string)
            string=''
        if line[0]!='>':
            string+=line
    seq.append(string)
sequence=list()
for a in seq:
    sequence.append(pattern.sub('',a))
while '' in sequence:
    sequence.remove('')

#****************Function for finding ovelap matrix(swalign.LocalAlignment(scoring))****************#
#matrix = np.zeros((len(sequence),len(sequence)));
#matrix=align.scores(sequence,matrix)
#print(matrix)
myFile = 'f25_305.csv'  # read the overlape score matrix
df =pd.read_csv(myFile,skiprows=2) 
matrix=df.values

#**************** Apply 2_opt heuristic on overlap score Matrix to generate initial solution****************#
init_center=list()

tsp_solution = [i for i in range(len(matrix))]
matrix1= -1*np.array(matrix)

tsp_solution=opt.run_2opt(tsp_solution,matrix1)
for i in range(len(tsp_solution)):
    init_center.append(sequence[tsp_solution[i]])
                


#****************RRHGA  genetic algorithm ****************#

Flag=1
iteration=1
pop_size=20
b=1
chromosomes=list()
init_center  # initial center generated by 2_opt

while(iteration<=5):
    print(iteration,'itrations')
    ITER.write(str(iteration)+" ")
    ITER.write("\n")
#**************** initialize popolation through transpositions(directed method) ****************#
    solution_ta=[]
#    chromosomes=indirected.indirect_represent(init_center,chromosomes,pop_size)
    chromosomes=directed.D_Rep(init_center,chromosomes,pop_size) 
    
    genartion_best_solution,generation_fit,generation_Bc_ind,new_populations,fits_pops=GA.Genetic_alg(chromosomes,sel_par,n_generation,muatation_rate);
    
    Best_layout= genartion_best_solution[len(generation_fit)-1]  # best layout of fragment generate after GA

    Best_layout_fitness=generation_fit[len(generation_fit)-1]
    BL.write(str(Best_layout))
    BL.write("\n")
    BLF.write(str(Best_layout_fitness))
    BLF.write("\n")
  
    #************ FITNESS VALUE OF INITIAL SOLUTION ************#
    init_cen_fitness=RRGA.RRGA_score(init_center)
    if(Best_layout_fitness>init_cen_fitness):
        
            init_center=copy.deepcopy(Best_layout)
            decrease=math.ceil(pop_size-(pop_size*0.05))
            pop_size=decrease
            if(decrease>decrease/10):
                pop_size=pop_size
            else:
                pop_size=decrease
    else:
            increase=math.ceil(pop_size+(pop_size*0.1))
            if(increase>increase/10):
                pop_size=pop_size
            else:
                pop_size=increase
    iteration=iteration+1
    chromosomes=[]
    
BL.close()
BLF.close()
ITER.close()
fitness_value,contg=RL_fit.last_fit_score(Best_layout)
print(fitness_value,contg,'fitness_value')

elapsed=(time.time()-start)  
print(elapsed,'time')
    

#mutation_rate=20 or 50
#cross_over_rate=80
#selection_operator=50
#number_of_chromosomes=2*solution_length
#number_of_generation=100
# number of generation for RRGA
############







	