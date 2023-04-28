import matplotlib.pyplot as plt

with open("Projet_Analyse_Textuelle/occitanie.txt", "r", encoding="utf8") as f:
    lines = f.readlines()

lines = [line.strip() for line in lines if line.strip()]


