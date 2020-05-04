# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 06:17:46 2018

@author: UZMA
"""

def partially_cross(best_chromosomes,parent1,parent2,mutated_child,mutation_rate):
    import numpy as np;
    import copy
    individual_1=[]
    individual_2=[]
    p1=[]
    p2=[]
    indices1=[]
    indices2=[]
    individual_1=best_chromosomes[parent1]
    individual_2=best_chromosomes[parent2]
    child_individual = ['d' for x in range(min(len(individual_1),len(individual_2)))]
    init_step_crossover=sorted(np.random.choice(len(child_individual), 2, replace=False)) # for selecting a substring from parent to swap
    start=init_step_crossover[0]
    end=init_step_crossover[1]
    crossover_child=copy.deepcopy(individual_2)
    crossover_child=list(crossover_child)
    crossover_child[start:end+1]=child_individual[start:end+1]
    mutation_rate=mutation_rate
 
    p1=individual_1[start:end+1]
    p2=individual_2[start:end+1]
    substring=individual_1[start:end+1]
    
    def mapp_loop(ind1):
        Mapp_array3.append(ind1)
        if ind1 in p2:
            indices = [i for i,x in enumerate(p2) if x == ind1]
            index=indices[0]
            p1[i]=''
            p2[i]=''
            p2[index]=''
            ind2=p1[index]
            p1[index]=''
            mapp_loop(ind2)
            return Mapp_array3

#******************************************************************************#
    Mapp_array1=[]
    Mapp_array2=[]
    Mapp_array3=[]
    for i in range(len(p2)):    #""" if p2[i] not in substring"""
        if(p2[i]!=p1[i] and (p2[i] not in substring)):
            if(p1[i] not in p2):
                
                Mapp_array2.append(p1[i])
                Mapp_array1.append(p2[i])
                ind1=p1[i]
                p1[i]=''
                p2[i]=''
            else:
                ind1=p1[i]
                ind2=p2[i]
                Mapp_array3.append(ind2)
                y=mapp_loop(ind1)
                if(y[0]==y[len(Mapp_array3)-1]):
                    while(y[0]==y[len(Mapp_array3)-1]):
                        del y[len(Mapp_array3)-1]
                    ind=y[0]
                    indd=y[len(Mapp_array3)-1]
                    Mapp_array1.append(ind)
                    Mapp_array2.append(indd)
                else:
                    Mapp_array1.append(y[0])
                    Mapp_array2.append(y[len(Mapp_array3)-1])
                
   
    
    lenMapp_array2=len(Mapp_array2)-1
    k=0
    while(k<=lenMapp_array2):
    
        indx1=Mapp_array2[k] 
       
        if(indx1 !=''):
            D=Mapp_array2.count(indx1)
            if(D>1):
                indices=[i for i,x in enumerate(Mapp_array2) if x == indx1]
                for i in range(len(indices)):
                    if(i==0):
                        continue           
                    
                    Mapp_array1[i]=''       
                    Mapp_array2[i]=''
                    lenMapp_array2=lenMapp_array2-1
        k=k+1
    for i in range(len(Mapp_array1)):
        if(Mapp_array2[i]!='' and Mapp_array1[i]!=''):
            lok=Mapp_array2[i]
            
            lok1=Mapp_array1[i]
           
            Mapp_array1[i]=''
            Mapp_array2[i]=''
            if lok in crossover_child: 
                indices1=[i for i,x in enumerate(crossover_child) if x ==lok]
             
                if len(indices1) > 1:   
                    for j in range(len(indices1)):
                        child_individual[indices1[j]]=lok1
                        crossover_child[indices1[j]]='d'
                else:
                    if(len(indices1)==1):
                        
                        child_individual[indices1[0]]=lok1
                        crossover_child[indices1[0]]='d'
    child_individual[start:end+1]=individual_1[start:end+1]
    indices2=[i for i,x in enumerate(child_individual) if x =='d'] 
    if(len(indices2)>1):
        for l in range(len(indices2)):
            child_individual[indices2[l]]=individual_1[indices2[l]]
    else:
        if(len(indices2)==1):
            child_individual[indices2[0]]=individual_1[indices2[0]]
#********************** Now mutation of child chromosomes# **********************#
    import math
    mutated_child=[]
    child_ind_swap=np.array(len(child_individual));
    mutation=math.ceil((mutation_rate/100)*len(child_individual));
    mutated_child=copy.deepcopy(child_individual);
    for m in range(int(mutation)):
        swap_ind=sorted(np.random.choice(child_ind_swap, 2, replace=False))
        temp=mutated_child[swap_ind[0]];
        mutated_child[swap_ind[0]]=mutated_child[swap_ind[1]]; 
        mutated_child[swap_ind[1]]=temp;
    return mutated_child



        