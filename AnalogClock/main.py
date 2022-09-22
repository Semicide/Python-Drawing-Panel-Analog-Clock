
import time
import math
import tkinter
from DrawingPanel import DrawingPanel as dp
def clock():
    width,height=610,610
    x,y=305,305 #center
    x1,y1,x2,y2=x,y,x,10 #second needle
    p = dp(width, height, background="black")
    r1=280 #minute
    r2=230 #hour
    rs=240 #second
    degree=0
    while True:
        dial = p.draw_oval(10, 10, height - 10, width - 10, width=10, fill="black", outline="white")
        center = p.draw_oval(x - 8, y - 8, 8, 8, fill="white")
        for i in range(0, 60):
            in_radiant = math.radians(degree)
            if (i % 5 == 0):
                ratio = 0.85
            else:
                ratio = 0.9
            x1 = x + ratio * r1 * math.sin(in_radiant)
            y1 = y - ratio * r1 * math.cos(in_radiant)
            x2 = x + r1 * math.sin(in_radiant)
            y2 = y - r1 * math.cos(in_radiant)
            p.draw_line(x1, y1, x2, y2, width="1", color="white")
            degree = degree + 6
        in_degree_s = int(time.strftime('%S')) * 6  # local second
        in_degree_m = int(time.strftime('%M')) * 6  # local minutes
        in_degree_h = int(time.strftime('%I')) * 30  # 12 hour format
        in_radianh=math.radians(in_degree_h)
        in_radians = math.radians(in_degree_s)
        in_radianm = math.radians(in_degree_m)
        s1=x+rs*math.sin(in_radians)
        s2=y-rs*math.cos(in_radians)
        m1 = x + r1 * math.sin(in_radianm)*0.85
        m2 = y - r1 * math.cos(in_radianm)*0.85
        h1=x + r2 * math.sin(in_radianh)*0.8
        h2=y - r2 * math.cos(in_radianh)*0.8
        second=p.draw_line(x, y, s1, s2 , fill="tomato", width=2, arrow="last")
        minute = p.draw_line(x, y, m1, m2 , fill="DarkOrchid", width=2, arrow="last")
        hour=p.draw_line(x, y, h1, h2 , fill="white", width=2, arrow="last")
        p.sleep(1)#normally 1 sec is 1000 ms but when i did it it misses some of the seconds so i changed it but its not a biggie
clock()