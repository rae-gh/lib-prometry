

######### TEST THE DATAFRAME ##############################





## Ensure code is imported in path
import sys
from pathlib import Path
CODEDIR = str(Path(__file__).resolve().parent.parent)
sys.path.append(CODEDIR)
DATADIR = "src/data/"

from prometry import pdbloader as pl
from prometry import pdbgeometry as pg

pdbs = ["1ejg","6eex","7uly","3nir","5d8v"]
pobjs = []

print(pg.ret_get())

print("---")
for pdb in pdbs:    
    pla = pl.PdbLoader(pdb,DATADIR,cif=False)    
    po = pla.load_pdb()
    #print(po,len(po.lines()))
    #print("---")
    pobjs.append(po)

gm = pg.GeometryMaker(pobjs)

geoss = []
geoss.append(['N:CA','C:O'])
geoss.append(['N:CA:C:N+1','N:CA:C'])
geoss.append(['N+1:CA','C:O+1'])
geoss.append(['N+1:CA-1','C+1:O-1'])
geoss.append(['CA-1:CA:CA+1'])

for geos in geoss:
    df = gm.calculateGeometry(geos)
    print(df.columns)
    for col in df.columns:        
        if "motif" in col:
            print(df[col])
    





    


