import pandas as pd

data = pd.read_csv('results.csv')


#Dados de Vitória (Mandante/Visitante) com %
placarCasa = data["home_score"]         #Pega os resutados da equipe da casa
placarFora = data["away_score"]         #Pega os resultados da equipe visitante
home = []                               #Lista de gols marcados pelo mandante
away = []                               #Lista de gols marcados pelo visitante

for i in placarCasa:        #função para pegar os resultados do "placarCasa" e adicionar na lista "home"
    home.append(i)

for y in placarFora:        #função para pegar os resultados do "placarFora" e adicionar na lista "away"
    away.append(y)

def whoWon(c, f): #função compara os resultados
    casa = 0
    fora = 0
    emp = 0

    for i in range(len(c)):
        if c[i] > f[i]:
            casa += 1
        elif c[i] < f[i]:
            fora += 1
        else:
            emp += 1
    percentH = (casa * 100) / len(c)
    percentA = (fora * 100) / len(c)
    percentE = (emp * 100) / len(c)
    print("Vitória mandante: ", casa, "-", percentH, "%")
    print("Vitória visitante: ", fora, "-", percentA, "%")
    print("Empates: ", emp, "-", percentE, "%")
    print(casa + fora + emp)

whoWon(home, away)


