import random
import Tkinter

def shift(c):
        return list([i for i in c if i>0] + [0]*c.count(0))

def swipe(l):
        l=shift(l)
        for i in range(len(l)-1):
                if l[i+1]==l[i]:
                        l[i], l[i+1] = 2*l[i], 0
        return shift(l)

class game(Tkinter.Tk):
        
        matrix = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        
        def __init__(self,parent):
                
                Tkinter.Tk.__init__(self,parent)
                self.parent = parent
                self.grid()
                self.matrixl = [Tkinter.Button(self, height=2, width=4, state=Tkinter.DISABLED, font=("Helvetica", 24)) for i in range(16)]
                for i in range(16): self.matrixl[i].grid(row=i//4, column=i%4)
                self.createWidget()
                self.bind_all('<Key>', self.startMove)
                self.mainloop()
                
        def rot(self):
                self.matrix = list(map(list, zip(*self.matrix[::-1])))
                
        def move(self, n):
                
                diff = self.matrix[:]
                
                for i in range(n):
                        self.rot()
                for i in range(4):
                        self.matrix[i] = swipe(self.matrix[i])
                for i in range(4-n):
                        self.rot()
                return 1 if self.matrix != diff else 0
        
        def createWidget(self):
                
                k = [(i//4, i%4)
                     for i,j in enumerate(sum(self.matrix, []))
                     if j == 0][random.randint(0, sum(self.matrix, []).count(0)-1)]
                
                self.matrix[k[0]][k[1]] = random.randint(1,2)*2
                
                for i in range(16):
                        
                        dist = self.matrix[i//4][i%4]
                        self.matrixl[i].config(text=dist if dist else ' ', bg='#%06x'% ((2**24-1) - (dist*1500) ))
                        
        def startMove(self, event):
                
                direction={'Left': 0, 'Down': 1, 'Right': 2, 'Up': 3}
                
                if self.move(direction[event.keysym]): self.createWidget()
                
                oldMatrix = self.matrix[:]
                
                for i in range(4):
                        
                        self.move(i)
                        
                        if self.matrix != oldMatrix:
                                self.matrix = oldMatrix[:]
                                return
                        
                for i in range(16):
                        self.matrixl[i].config(bg='red', text=':(')
show = game(None)
