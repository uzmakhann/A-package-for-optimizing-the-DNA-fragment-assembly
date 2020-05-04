#def sappend(s11,s22):
#matrix=ss(s11,s22)
   # s11.append(2);
   # s22.append(3)
   # return s11,s22
#import numpy as np;
import swalign;
arry=list();
def scores(sequence1,matrix1):
    match = 1
    mismatch = -3
    scoring = swalign.NucleotideScoringMatrix(match,mismatch)
    sw = swalign.LocalAlignment(scoring)
    #matrix = np.zeros((len(sequence1),len(sequence1)));
    for i in range(len(sequence1)):
        for j in range(len(sequence1)):
            j=j+i;
            if(i==j):
                continue;
            if(j>len(sequence1)-1):
                break;
            
            alignment = sw.align(sequence1[i],sequence1[j]);
        #alignment = sw.align('ACACACTA','AGCACACA');
            alignment.dump();
            var = alignment.score;
            matrix1[i][j] =var;
            matrix1[j][i] =var;
                 #arry.append(var); 
#print(matrix) 
    return matrix1


#def fitness_chromose(chromes_array):
#     
#     match = 2
#     mismatch = -1
##     fitness_scor=list();
#     fitness_scor=[]
#     fit_scor_chroms=[]
##     fit_scor_chroms=list();
#     fitness_scor='';
#     fit_scor_chroms='';
#     for kk in range(len(chromes_array)):
#         for k in range(len(chromes_array[kk])-1):
#             scoring = swalign.NucleotideScoringMatrix(match,mismatch)
#             sw = swalign.LocalAlignment(scoring)
#             alignment = sw.align(chromes_array[k],chromes_array[k+1]);
#             alignment.dump();
#             var = alignment.score;
##             fitness_scor.append (var)
#             import numpy as np
#             fitness_scor=np.array([var])
#         fitness_scor=sum(fitness_scor)
##             print(fitness_scor,'varrrrrrrrr')
##             fitness_scor.append(var)
#             #dddddddddddd
#         fit_scor_chroms=np.array([ fitness_scor])
##         fit_scor_chroms.append([fitness_scor])
#         fitness_scor=[];
#     print(fit_scor_chroms,'uzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz')
#     return fit_scor_chroms
#          










##*****************************************************************###
#import numpy as np
#import copy; 
#def center(center1,chromosomes):
##center=['TTAA','CCGA','CTTA','AAAT','TTCG','GGCA','AAATC'];
#    rand_order=np.random.randint(4,size=(len(center1)+1));
##print(rand_order,'random')
#    len_pop=2
##    chromosomes=list();
#    chrom=list();
#    chrom=copy.deepcopy(center1);     # center use swaping order to generate chromosomes
##print(chrom,('init chrom'))
#    for k in range(len_pop):
#        for z in range(len(center1)):
#            print(rand_order,'random order')
#            print(type(rand_order),'typerandom order')
#            print(z,'L')
#            ind=rand_order[0,z]
#            print(ind,'ind')
#            #if(ind!=len(center1)):
#            print(type(chrom),'uzma')
#            s=chrom[ind]
#            print(chrom,'chromee')
#            print(ind,'ind')
#            print(rand_order,'order')
#            chrom[ind]=chrom[ind+1]           # swap order to generate chromosomes
#            chrom[ind+1]=s
##            else:
##              s=chrom[len(center)]
##              print(chrom,'chromee')
##              print(ind,'ind')
##              chrom[ind]=chrom[1]           # swap order to generate chromosomes
##              chrom[1]=s  
#    #print(chrom,('updat chorm'))
#        chromosomes.append(chrom);
#    #print(chromosom,('append chorm'));
#   # print(chrom,(' charm'))
#        chrom=[];
#        chrom=copy.deepcopy(center1);
##    print(center,('checking chrom'));
##    print(chrom,('new center'));
#        rand_order='';
#        rand_order=np.random.randint(5, size=(1,len(center1)+1))
#    #print(rand_order)
#    return chromosomes