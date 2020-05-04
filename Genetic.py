
#*******************  genetic algorithm function ********************* #
def Genetic_alg(chromosomes,num_parents_mating,n_generation,muatation_rate):
    import partially_cross_o as cross
    import pop_scorss as popfit
    import ALGO_PALWS as contigg
    import Parentsselect as ns

    PALWS=[]
    mutated_child=[]
    pop_fitness=[]
    PALWS_fitness=[]
    mutated_chromosomes=[]
    
    mutated_child=[]
    PALWS_fitness=[]
    generation_fit=[]
    generation_Bc_ind=[]
    genartion_best_solution=[]
    pop_contig=[]

    muatation=muatation_rate

    pop_fitness=popfit.init_pop_score(chromosomes)
    
    generation_fit.append(max(pop_fitness))
    generation_Bc_ind.append(pop_fitness.index(max(pop_fitness)))
    
    genartion_best_solution.append(chromosomes[pop_fitness.index(max(pop_fitness))])

    # sort fitness of population
    fit_pop_sort_ind=sorted(range(len(pop_fitness)), key=lambda k: pop_fitness[k])
    top_parents_fits_ind=fit_pop_sort_ind[:num_parents_mating]
    
    # top n parents for crossover with their fitness
    top_parents=[chromosomes[i] for i in top_parents_fits_ind]
    top_parents_fit=[pop_fitness[i] for i in top_parents_fits_ind]
    
     
    Gf = open('fit_value_in_generation.txt',"a")
    
#******************* GA *******************#
    for g in range(n_generation):
        
#******************* partially mapped crossover and mutation *******************#

         
        parent1_set, parent2_set = ns.selection(top_parents,top_parents_fit)
        
        for i in range(len(parent1_set)):
            parent1=parent1_set[i]
            parent2=parent2_set[i]
            mutated_child=cross.partially_cross(chromosomes,parent1,parent2,mutated_child,muatation) 
            mutated_chromosomes.append(mutated_child,)

   
        #parents,parents_fit=ns.selection(pop_fitness,chromosomes,Nparents)   
#******************* POWER AWARE LOCAL SEARCH ALGORITHM *******************#

        PALWS,contig=contigg.array_contig(mutated_chromosomes)
        pop_contig.append(contig)
        PALWS_fitness=popfit.init_pop_score(PALWS)
        top_parents,top_parents_fit,best_chromosome_fit,best_chromosome_ind,best_chromosomes,new_populations,fits_pops=ns.next_gen_parents(PALWS,PALWS_fitness,top_parents,top_parents_fit,num_parents_mating)
        generation_fit.append(max(fits_pops))
        generation_Bc_ind.append(fits_pops.index(max(fits_pops)))
        
        genartion_best_solution.append(new_populations[fits_pops.index(max(fits_pops))])
        
        Gf.write(str(generation_fit[g]))
    Gf.close()    
    return genartion_best_solution,generation_fit,generation_Bc_ind,new_populations,fits_pops
    
    
        
