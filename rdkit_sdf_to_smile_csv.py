#conda env list
#conda activate my-rdkit-env 
from rdkit import Chem
from rdkit.Chem.ChemUtils import SDFToCSV
import os
import pandas as pd 
names=[]
smile_format=[]
file_names=os.listdir("directory_name")
for file_name in file_names:
    sdf = Chem.SDMolSupplier('directory_name/%s'%file_name)
    for mol in sdf:
        smi = Chem.MolToSmiles(mol)
        print(file_name, smi)
        names.append(file_name)
        smile_format.append(smi)
df_results=pd.DataFrame()
df_results["molecules_names"]=names
df_results["smiles_formats"]=smile_format
df_results.to_csv("all_csmiles_format.csv")

