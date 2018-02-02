
class board():
    def __init__(self):
        self.cell=['-','-','-','-','-','-','-','-','-']
        self.player='O'
        self.num=1

    def display(self):
        x=0
        c= self.cell
        for i in range(0,3):
            for j in range(0,3):
                if(j is 0):
                    print(' ',end='')
                print(c[x],end='')
                x+=1
                if(j<2):
                    print(' | ',end='')
            if(i<2):
                print('\n-----------')
        print()
        
    def update_cell(self,cell_in,player):
        if(self.cell[(cell_in-1)]=='-'):
            self.cell[(cell_in-1)]= player
        else:
            print(':cell already occupied:')
            cell_in = int(input("player "+player+" turn: enter cell between 1 and 9: "))
            while((cell_in<1)|(cell_in>9)):
                print("input  cell is  out of range:")
                cell_in = int(input("player "+player+" turn: enter cell between 1 and 9: "))
            self.update_cell(cell_in, player)

    def change_player(self,):
        play= self.player
        if(play=='X'):
            self.player='O'
            return 'O'
        else:
            self.player='X'
            return 'X'
    def won(self):
        #horizontal check!
        x=0
        c= self.cell
        v=0
        p= self.player
        for i in range(0,3):
            for j in range(0,3):
                if(c[x]==p):
                    v=v+1
                x=x+1
            if(v==3):
                return p
            v=0
        #ver check!
        index=0
        ce= self.cell
        v=0
        pl= self.player
        l=0
        for i in range(0,3):
            for j in range(0,3):
                if(ce[index]==pl):
                    v=v+1
                index=index+3
            if(v==3):
                return pl
            
            v=0
            l=l+1
            index=l
        #diagonal check
        #ce= self.cell
        #pl= self.player
        if((ce[0]==pl)&(ce[4]==pl)&(ce[8]==pl)):
            return pl
        elif((ce[2]==pl)&(ce[4]==pl)&(ce[6]==pl)):
            return pl
        
        return '0'
    def cls(self):
            import os
            os.system("CLS")    
        
    def itr(self):
        self.num=((self.num)+1)
        return self.num
    def header(self):
            print("-TicTacToe-")
    def ref_scr(self):
            self.cls()
            self.header()
            self.display()
            return self.change_player()
    def run(self):
        w = self.won()
        while (True):

            player=self.ref_scr()
            cell_in = int(input("player "+player+" turn: enter cell between 1 and 9: "))
            while((cell_in<1)|(cell_in>9)):
                print("input  cell is  out of range:")

                cell_in = int(input("player "+player+" turn: enter cell between 1 and 9: "))


            self.update_cell(cell_in, player)
            w = self.won()
            n= (self.itr())-1
            if((n==9)&(w=='0')):
                self.cls()
                self.header()
                self.display()
                print('its draw')
                break
            if(w==player):
                self.cls()
                self.header()
                self.display()
                print(player+' won!')
                break


if __name__ == '__main__':
    board().run()
        




