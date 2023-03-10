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
        d_title[i] = p
print(d_title)

