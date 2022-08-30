import time
import pyautogui as pag

playtime = 2000
time_delay = 7

gugpan = (1,1)
salse_code = (1,1)
df_click = (1,1)

pag.click(gugpan)
time.sleep(0.5)
pag.click(df_click)

pag.press('end')
pag.press('pgdn')
time.sleep(time_delay)

salse_list = 1
while salse_list < playtime:
    salse_list = salse_list + 1
    pag.press('end')
    pag.press('pgdn')
    time.sleep(time_delay)

print("OK")