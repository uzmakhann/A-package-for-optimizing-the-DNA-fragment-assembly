"""
Created on Fri Feb 23 02:48:56 2018

@author: UZMA
"""
#********************* fitness value of a resultant layout ********************* #
def last_fit_score(sequence):
    print(sequence,len(sequence))
    import swalign;
    contg=0;
    arrayscore=list();
    match = 1
    mismatch = -3
    scoring = swalign.NucleotideScoringMatrix(match,mismatch)
    sw = swalign.LocalAlignment(scoring)
    for j in range(len(sequence)-1):
        
        alignment = sw.align(sequence[j],sequence[j+1]);
        alignment.dump();
        var = alignment.score;
        if(var>30):
            contg=contg-1;
        else:
            contg=contg+1;
        arrayscore.append(var);
    fitness_value=sum(arrayscore);
    return fitness_value,contg
