import numpy as np
import copy; 
chromosomes=list();
def D_Rep(center1,chromosomes,pop_size):
    rand_order=np.random.randint(1,len(center1)-2,5);
    chrom=[];
    chrom=copy.deepcopy(center1);     # center use swaping order to generate chromosome
    for j in range(int(pop_size)):
        for i in range(len(rand_order)):
            ind=rand_order[i]
            s=chrom[ind]
            print(ind,'ind')
            chrom[ind]=chrom[ind+1]           # swap order to generate chromosomes
            chrom[ind+1]=s
        chromosomes.append(chrom);
        chrom=[];
        chrom=copy.deepcopy(center1);
        rand_order=[];
        rand_order=np.random.randint(1,len(center1)-2,5);
    return chromosomes


## error in (replace 5 by len(center1) )