            #*******  find overlap score of center by using smith-waterman algorithm *******##
def RRGA_score(init_center):
    print(init_center)
    arrayscore=list();
    import swalign;
    match = 1
    mismatch = -3
    scoring = swalign.NucleotideScoringMatrix(match,mismatch)
    sw = swalign.LocalAlignment(scoring)
    for j in range(len(init_center)-1):
        
        alignment = sw.align(init_center[j],init_center[j+1]);
        #alignment = sw.align('ACACACTA','AGCACACA');
        alignment.dump();
        var = alignment.score;
        arrayscore.append(var);
    init_cen_fitness=sum(arrayscore);
    
    return init_cen_fitness