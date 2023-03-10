from tkinter import *
import random
r = Tk()
c = Canvas(r,background='black',height='600',width='600')
c.pack()
cords_x = [x for x in range(20,580,10)]
cords_y = [y for y in range(20,580,10)]

class Cell:
    def __init__(self):
        self.squares = []
        self.lst = []
        self.count = []
        while True:
            x = random.choice(cords_x)
            y = random.choice(cords_y)
            xy = list()
            xy.append(x)
            xy.append(y)
            if xy not in self.lst:
                self.lst.insert(0,xy)
                square = c.create_rectangle(x,y,x+10,y+10,fill='white')
                self.squares.insert(0,square)
            if len(self.lst) == 100:
                break

a = Cell()

def check_existing():
    a.count = []
    for coord in a.lst:
        coun = 0
        x0 = coord[0]
        y0 = coord[1]
        ll = list()
        ll.extend([[x0+10,y0],[x0+10,y0+10],[x0+10,y0-10],
                   [x0-10,y0],[x0-10,y0+10],[x0-10,y0-10],
                   [x0,y0+10],[x0,y0-10]])
        for z in ll:
            if z in a.lst:
                coun+=1
        a.count.append(coun)

    for cou in a.count:
        if cou >= 4 or cou <= 1:
            lol = a.count.index(cou)
            c.delete(a.squares[lol])
            a.count.remove(cou)
            a.squares.pop(lol)
            a.lst.pop(lol)

def check_non():
    global cords_x,cords_y
    new_squares = list()
    new_lst = list()
    new_count = list()
    x = [i for i in cords_x]
    y = [i for i in cords_y]
    lll = list()
    for m in x:
        for n in y:
            if [m,n] not in a.lst:
                lll.append([m,n])
    
    for coord in lll:
        count = 0
        x0 = coord[0]
        y0 = coord[1]
        ll = list()
        ll.extend([[x0+10,y0],[x0+10,y0+10],[x0+10,y0-10],
                   [x0-10,y0],[x0-10,y0+10],[x0-10,y0-10],
                   [x0,y0+10],[x0,y0-10]])
        for z in ll:
            if z in a.lst:
                count+=1
        if count >= 3:
            #print('yea')
            sq = c.create_rectangle(x0,y0,x0+10,y0+10,fill='white')
            new_squares.insert(0,sq)
            new_count.insert(0,count)
            new_lst.insert(0,coord)
    
    a.squares.extend(new_squares)
    a.count.extend(new_count)
    a.lst.extend(new_lst)

def running():
    check_non()
    tim = r.after(300,check_existing)
    tim2 = r.after(300,running)

running()
r.mainloop()