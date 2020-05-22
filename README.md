<h1>A-package-for-optimizing-the DNA-fragment-assembly</h1>

<b> PythoFragam: A Python-based Optimization Tool for DNA Fragment </b>

This repository contains the code for DNA fragment assembly based on a metaheuristic Overlap Layout Consensus Approach: Restarting recentering hybrid genetic algorithm (RRHGA). Complete code is written in Python 3.

<h2 style="font-family:verdana;">System requirements </h2>

1.	Python 3.4+
2.	Swalign
3.	Pandas
4.	Numpy


<h2 style="font-family:verdana;">Datasets </h2>

http://chac.sis.uia.mx/fragbench/
1.	GenFrag Instances
2.	DNAgen instances

The Documentation is avalible at [paper.md](https://github.com/uzmakhann/paper.md/blob/master/paper.md)
<h3 style="font-family:verdana;">Main.py </h3>

This script contains the main functions for solving the problem of DNA fragment assembly.  These are givens below. 

<h4 style="font-family:verdana;">	Importing the dataset </h4>


First, import a FASTA format file. The file is open and appends the fragments into a list name is sequences. The second is the CSV file includes the matrix, the value of the cell, is overlapping scores among the sequences.

<h4 style="font-family:verdana;">Setting the parameters </h4>


The parameters such as Population size, Mutation rate, Number of Trans, and Cutoff value, the percentage of Trans is increased or decreased in case of improvement and no improvement. 

<h4 style="font-family:verdana;">run_2opt </h4>


This function takes the overlapping score matrix is an input, and find the initial Centre (optimal path- order of the fragments) for the genetic algorithm. 

<h4 style="font-family:verdana;">D_Rep </h4>


This function gets the Centre is an input, and generate the populations based on directed transpositions.

<h4 style="font-family:verdana;">Genetic_alg </h4>


Once the populations are generated. The called function genetic_alg gets the <b> populations, num_parents_mating, n_generation, mutation_rate </b>is an inputs. 
The genetic_algo import <b>partially_cross </b> function for evolutionary operators such as crossover and mutation. 
However, the <b>array_contig</b> function used PALS as an evolutionary operator to order the fragments while minimizing the number of contigs. The <b>init_pop_score</b> function used the local alignment algorithm for the fitness value evaluation.

<h4 style="font-family:verdana;">last_fit_score </h4>



This function gives the final output, by calculating the sum of overlap score, and the number of contigs of the best solution generated from RRHGA.  

<b>Contact:</b> In case of any query, feel free to drop an email at uzma@giki.edu.pk

                                                          
