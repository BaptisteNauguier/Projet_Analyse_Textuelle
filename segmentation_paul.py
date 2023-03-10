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
    # if i > 50:
    #     break
    
# print(d_title)

for elt in d_title:
    if len(d_title[elt]) > 1:
        print(elt,"---",len(d_title[elt]))  
#affiche le nombre de thèmes qui apparaisse + de 2 fois, et c'est souvent 2 fois max donc pas fou de faire une analyse sur les thèmes sauf si on les généralise mais c'est risqué sur des questions précises

