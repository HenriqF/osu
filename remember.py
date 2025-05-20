#aiohttp

import asyncio
from ossapi import OssapiAsync

import tkinter as tk
import random
import time

import webbrowser

janela = tk.Tk()
janela.geometry('830x500')
janela.resizable(False,False)
janela.title("porraloca")
frame = tk.Frame(janela)
frame.pack()

api = OssapiAsync(0, "") #idcliente e senha. pra cirar vai no site do osu configuracoes da conta (leia docs)

list = [] #['nome','id','tentativas']

async def getStuff(player):
    global list
    global api

    user = await api.user(player)
    numMaps = (user.beatmap_playcounts_count)//5

    warning = False
    for i in range(3):
        janela.update()
        alfa = await api.user_beatmaps(user, "most_played", limit=1, offset=random.randint(0, numMaps-1)*5)
        try:
            currentMap = [alfa[0].beatmapset.title, alfa[0].beatmap_id, alfa[0].count]
            print(currentMap)
            if currentMap not in list:
                list.append(currentMap)
        except:
            warning = True
    list = sorted(list, key=lambda x: x[2])[::-1]
    # print("mn vai jogar antes de usar essa porra; tu mal jogou 20 vezes e tá querendo ter nostalgia?... Independente, ai vai:") if warning else print("se liga:")
    # print(list)


    return

def download(index):
    webbrowser.open(f"https://osu.ppy.sh/b/{index}")

def createButtons():
    global list
    for i in range(0,len(list)):
        janela.update()
        bt= tk.Button(janela, text=f"Baixar '{list[i][0]}' | Suas tentativas -> {list[i][2]} ",font=("Cascadia Code", 10) ,command=lambda index=list[i][1]: download(index), width=100, height=2)
        text.window_create("end", window=bt)
        text.insert("end", "\n")

def start():
    global list
    list = []
    nick = ign.get("1.0", tk.END).strip()
    asyncio.run(getStuff(nick))
    createButtons()

text = tk.Text(janela,height=2,width=101)
text.pack(side="left", fill="both")

sb = tk.Scrollbar(janela, command=text.yview)
sb.pack(side="left", fill="y")

ign=tk.Text(janela,font=("Cascadia Code", 15), height=2, width=67)
ign.insert("1.0", "CarlosDeAlmeida")
text.window_create("end", window=ign)
text.insert("end", "\n")


start = tk.Button(janela, text="novo",font=("Cascadia Code", 10) ,command=start, width=100, height=2)
text.window_create("end", window=start)
text.insert("end", "\n")

text.configure(yscrollcommand=sb.set)
sb.configure(command=text.yview)


janela.mainloop()
