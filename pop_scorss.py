# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 08:18:06 2018

@author: UZMA
"""
def init_pop_score(chromosomes):
    pop_fitness = list();
    import swalign
    scoring = swalign.NucleotideScoringMatrix(1,-3)
    sw = swalign.LocalAlignment(scoring)
    for i in range(len(chromosomes)):
        arrayscore=list();
        for j in range(len(chromosomes[i])-1):
            alignment = sw.align(chromosomes[i][j],chromosomes[i][j+1]);
            alignment.dump();
            var = alignment.score;
            arrayscore.append(var);
        pop_fitness.append(sum(arrayscore))
#    print(arrayscore);
    print(pop_fitness)
    return pop_fitness
