import mouse
import pandas as pd
import os
import time
import subprocess
import sys

file_number = 8

def draw_csv(file_number):
    df = pd.read_csv(f'{os.getcwd()}\\CSV\\mouse_{file_number}.csv')
    events = df.to_dict('records')

    os.system('taskkill /F /IM mspaint.exe')
    subprocess.Popen('mspaint')
    time.sleep(2)
    for i, e in enumerate(events):
        # print(f'{i}: {e}')
        if i%1 == 0 :
            if e["hold"] == 0:
                mouse.move(e["x"], e["y"], True, 0)
                time.sleep(0.00000000000001)
            else:
                mouse.drag(events[i - 1]["x"], events[i - 1]["y"], e["x"], e["y"])
                time.sleep(0.00000000000001)

draw_csv(file_number)            