import mouse
import keyboard
import numpy as np
import pandas as pd
import os
import re
import subprocess
import math

def find_csv_ind():
    csv_ind = 0
    path = os.getcwd() + '\\CSV'
    filenames = os.listdir(path)
    csv = [int(re.findall('\d', file)[0]) for file in filenames if file.endswith('.csv')]
    if len(csv) != 0:
        csv_ind = np.max(csv) + 1
    else:
        csv_ind = csv_ind
    
    return csv_ind

def record_mouse():
    subprocess.Popen('mspaint')
    events = []                 
    mouse.hook(events.append)   
    keyboard.wait("Alt") 
    mouse.unhook(events.append)
    os.system('taskkill /F /IM mspaint.exe')

    return events

def m_hold(move, buttons):
    if len([b for b in buttons if b["ind"] == move["ind"] - 1]) == 0:
        return 0
    else:
        return 1

def movement(moves, buttons):
    return map(lambda m:{"x": m["atr1"], "y": m["atr2"], "hold": m_hold(m, buttons)}, moves)


def events_to_csv(events, csv_ind):
    evm = map(lambda e: {"t": e.__class__.__name__, "atr1": e[0], "atr2": e[1], "time": e[2], "ind": events.index(e)}, events)
    evb = map(lambda e: {"t": e.__class__.__name__, "atr1": e[0], "atr2": e[1], "time": e[2], "ind": events.index(e)}, events)
    eMoves = [e for e in evm if e["t"] == "MoveEvent"]
    eBtns = [e for e in evb if e["t"] == "ButtonEvent"]
    mouse_moves = movement(eMoves, eBtns)

    df = pd.DataFrame(mouse_moves)
    btn_presses = np.array_split(df[df["hold"] == 1].index.to_list(), math.ceil(len(df[df["hold"] == 1].index.to_list())/2))
    print(btn_presses)

    for i in btn_presses:
        for j in range(i[0], i[1], 1):
            df.at[j, 'hold'] = 1

    df.to_csv(f'CSV/mouse_{csv_ind}.csv')

events_to_csv(record_mouse(), find_csv_ind())