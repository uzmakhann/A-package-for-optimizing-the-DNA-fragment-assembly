
import numpy as np;
def array_contig(mutated_child):
    import copy;
    def clculatedelta(s,i,j):
        import swalign;
        dc=0;
        match = 1
        mismatch = -3
        scoring = swalign.NucleotideScoringMatrix(match,mismatch)
        sw = swalign.LocalAlignment(scoring)
        ali1 = sw.align(s[i-1],s[j]);
        ali1.dump();
        ali2 = sw.align(s[i],s[j+1]);
        ali2.dump();
        delt_f = ali1.score + ali2.score;
        f1=ali1.score;
        f2=ali2.score;
        ali1 = sw.align(s[i-1],s[i]);
        ali1.dump();
        ali2 = sw.align(s[j],s[j+1]);
        ali2.dump();
        delt_f = delt_f - (ali1.score + ali2.score);
        f3=ali1.score;
        f4=ali2.score;
        if(f3>30):
            dc=dc+1;
        if(f4>30):
            dc=dc+1;
        if(f1>30):
            dc=dc-1;
        if(f2>30):
            dc=dc-1;
        
        return delt_f,dc;    

##********************************************************************##
						#*****PALWS *****#
    index1=np.zeros(4);
    index1=index1.astype(int)
    ss=mutated_child;
    import math;
    palws_rate=5;
    PALWS=list();
    contig=list();
    palwsrate=list()
#    palwsrate=math.ceil((palws_rate/100)*len(ss));
    for k in range(len(ss)): 
        s=copy.deepcopy(ss[k])
        palwsrate=math.ceil((palws_rate/100)*len(s))
        for m in range(palwsrate):
            indexes=sorted(np.random.choice([i+1 for i in range(len(s)-2)], 2, replace=False))
            a=indexes[0];
            b=indexes[1];
            if(len(s)!=0):
                df,dc=clculatedelta(s,indexes[0],indexes[1])
                if(dc<index1[3] or (dc==index1[3] and df>index1[2])):
                    index1[0] = a;
                    index1[1] = b;
                    index1[2] = df;
                    index1[3] = dc;
                s[index1[0]:(index1[1]+1)] = reversed(s[index1[0]:(index1[1]+1)]);
                index1=np.zeros(4);
                index1=index1.astype(int)
                indexes=[];
                
                
        contig.append(index1[3])
        PALWS.append(s);
            
    return  PALWS,contig