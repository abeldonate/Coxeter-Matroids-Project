use application "matroid";

declare $M=new Matroid(VECTORS=>[[1,0,0],[1,0,1],[1,1,0],[1,0,2]]);

print "Number of bases\n", $M->N_BASES, "\n";
print "Number of elements\n", $M->N_ELEMENTS, "\n";
print "Rank\n", $M->RANK, "\n";
print "Bases\n", $M->BASES, "\n";

print $M->VECTORS;
#$M->LATTICE_OF_FLATS->VISUAL;


#Conversion into a polytope --------------
declare $p = $M->POLYTOPE;
print $p->VERTICES;