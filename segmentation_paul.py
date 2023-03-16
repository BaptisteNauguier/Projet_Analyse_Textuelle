import matplotlib.pyplot as plt

with open("../fichier_sans_lignes_vides.txt", "r", encoding="utf8") as f:
    lines = f.readlines()

lines = [line.strip() for line in lines if line.strip()]

d_title = {}
for i in range(len(lines)):
    if lines[i][0:5] == "<text":
        p = ""
        boo = False
        for j in range(len(lines[i])):
            if lines[i][j-7:j] == 'title="':
                boo = True
            if lines[i][j] == '"':
                boo = False
            if boo != False:
                p += lines[i][j]
        if p in d_title:  #ajoute dans un dictionnaire le thème et son itération correspondante dans une liste
            d_title[p].append(i)
        else:
            d_title[p] = [i]
    if i > 50:
        break 
# print(d_title)

# for elt in d_title:
#     if len(d_title[elt]) > 1:
#         print(elt,"---",len(d_title[elt]))  
#affiche le nombre de thèmes qui apparaisse + de 2 fois, et c'est souvent 2 fois max donc pas fou de faire une analyse sur les thèmes sauf si on les généralise mais c'est risqué sur des questions précises


d_dept = {}
for i in range(len(lines)):
    if lines[i][0:5] == "<text":
        p = ""
        boo = False
        for j in range(len(lines[i])):
            # if lines[i][j-12:j] == 'department="': #par nom de departement
            # if lines[i][j-8:j] == 'region="':  #par region
            if lines[i][j-15:j] == 'departmentiso="':  #par numéro de departement
                boo = True
            if lines[i][j] == '"':
                boo = False
            if boo != False:
                p += lines[i][j]
        if p in d_dept:  #ajoute dans un dictionnaire le thème et son itération correspondante dans une liste
            d_dept[p].append(i)
        else:
            d_dept[p] = [i]
    # if i > 100000:
    #     break
# print(d_dept)

for elt in d_dept:
    d_dept[elt] = len(d_dept[elt])
    print(elt,"---",d_dept[elt]) 
#par départment c'est déjà mieux (données sur 100 départements)

#trier de manière décroissante
sorted_d = dict(sorted(d_dept.items(), key=lambda x: x[1], reverse=True))
print(sorted_d)
