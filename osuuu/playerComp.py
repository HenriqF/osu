from ossapi import Ossapi
api = Ossapi(0, "") #idcliente e senha. pra cirar vai no site do osu configuracoes da conta (leia docs)

playerNome1 = input("Nome1 -->")
playerNome2 = input("Nome2 -->")

user1 = api.user(playerNome1)
user2 = api.user(playerNome2)

pp1 = user1.statistics.pp
pp2 = user2.statistics.pp

print(playerNome1 + " é melhor com " + str(pp1) + "pp" ) if pp1>pp2 else print("empate") if pp1==pp2 else print(playerNome2 + " é melhor com " + str(pp2) + "pp")

print("done")