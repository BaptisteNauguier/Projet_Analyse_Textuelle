import re
import pandas as pd
import numpy
import math
import sklearn
import spacy

# Charger le fichier 
with open("../gd-fiscalite_depenses-utf8-sgml-cwb.txt", "r", encoding="utf8") as f:
    txt = f.read()

# Supprimer toutes les balises div
txt = re.sub(r'<div.*?>', '', txt, flags=re.DOTALL)
txt = re.sub(r'</div>', '', txt, flags=re.DOTALL)

# Écrire le fichier modifié
with open("../fichier_modifie.txt", "w", encoding="utf8") as f:
    f.write(txt)


### supprimer les lignes vides
with open("../fichier_modifie.txt", "r", encoding="utf8") as f:
    lines = f.readlines()

lines = [line.strip() for line in lines if line.strip()]

with open("../fichier_sans_lignes_vides.txt", "w", encoding="utf8") as f:
    f.write("\n".join(lines))
