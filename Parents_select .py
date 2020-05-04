import numpy as np
def tournament_selection(chromosomes, k,pop_fitness):
    fit_scor_chroms=[]

#   best = 0
#    for i in range(k):
#        r_selection=np.random.choice(len(chromosomes), size=5, replace=False)

#        if (best == 0) or pop_fitness(r_selection[0]) > pop_fitness(best):
#            best = r_selection[0]
    r_selection=np.random.choice(len(chromosomes), size=5, replace=False)
    fit_scor_chroms.append(pop_fitness[r_selection[0]])
    fit_scor_chroms.append(pop_fitness[r_selection[1]])
    fit_scor_chroms.append(pop_fitness[r_selection[2]])
    fit_scor_chroms.append(pop_fitness[r_selection[3]])
    fit_scor_chroms.append(pop_fitness[r_selection[4]])
    
    best_chrom=max(fit_scor_chroms)
    best_index=fit_scor_chroms.index(best_chrom)
    
    #best_chromosomes.append(chromosomes[r_selection[best_index]])
            
    #fitness_cromosomes.append(best_chrom)
            
    best_chrom_index=r_selection[best_index]
    return best_chrom_index 

def selection(pop_fitness,chromosomes,parents):
    select_chroms1=[]
    select_chroms2=[]
    k=5
    for k in range(parents):
        
        best_chromosomes1=tournament_selection(chromosomes, k,pop_fitness)
        
        best_chromosomes2=tournament_selection(chromosomes, k,pop_fitness)
        
        select_chroms1.append(chromosomes[best_chromosomes1])
        select_chroms2.append(chromosomes[best_chromosomes2])
        
    return select_chroms1,select_chroms2
        

def next_gen_parents(mutation_croms,fitness_mutated_array,top_parents,top_parents_fit,num_parents_mating):
    top_parents.extend(mutation_croms)
    new_population=top_parents
    top_parents_fit.extend(fitness_mutated_array)
    fits_pop=top_parents_fit
    
    best_chromosome_fit=max(top_parents_fit)
    best_chromosome_ind=top_parents_fit.index(max(top_parents_fit))
    best_chromosomes=new_population[best_chromosome_ind]
    
    
    fit_pop_sort_ind=sorted(range(len(fits_pop)), key=lambda k: fits_pop[k])
    top_parents_fits_ind=fit_pop_sort_ind[:num_parents_mating]
    
    select_parents=[new_population[i] for i in top_parents_fits_ind]
    select_parents_fit=[fits_pop[i] for i in top_parents_fits_ind]
    
    return select_parents,select_parents_fit,best_chromosome_fit,best_chromosome_ind,best_chromosomes,new_population,fits_pop
    
          