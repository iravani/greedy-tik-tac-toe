class Table:
    def __init__(self):
        self.table = [['e','e','e'],['e','e','e'],['e','e','e']]
        self.turns = {1:'X' , -1:'O'}
        self.point = 0

    def show(self):
        s=""
        for i in range(3):
            for j in range(3):
                s += self.table[i][j]
            s += "\n"
        print(s)

    def set_cell(self,_x,_y,_turn):
        #for input error
        if not(_x >= 0 and _x <=2):
            return "Error"
        if not(_y >= 0 and _y <=2):
            return "Error"
        if self.table[_y][_x] != 'e':
            return "Error"

        #set the table
        self.table[_y][_x] = self.turns[_turn]
        self.calculate_point()

    def calculate_point(self):
        self.point = 0

        if self.table[1][1] == 'X':
            self.point += 5
        elif self.table[1][1] == 'O':
            self.point -= 5

        #horizontal
        for row in self.table:
            counter = 0
            for c in row:
                if c == 'X':
                    counter += 1
                elif c == 'O':
                    counter -= 1
            if counter == 3:
                self.point = 1000
                return
            elif counter == 1:
                self.point -= 8
            elif counter == 2:
                self.point += 2
            if counter == -3:
                self.point = -1000
                return
            elif counter == -1:
                self.point += 4
            elif counter == -2:
                self.point -= 2

        #vertical
        for j in range(3):
            counter = 0
            for i in range(3):
                if self.table[i][j] == 'X':
                    counter += 1
                elif self.table[i][j] == 'O':
                    counter -= 1
            if counter == 3:
                self.point = 1000
                return
            elif counter == 1:
                self.point -= 8
            elif counter == 2:
                self.point += 2
            if counter == -3:
                self.point = -1000
                return
            elif counter == -1:
                self.point += 4
            elif counter == -2:
                self.point -= 2

        #orib
        if self.table[0][0] == 'X' and self.table[1][1] == 'X' and self.table[2][2] == 'X':
            self.point = 1000
            return
        elif self.table[0][0] == 'O' and self.table[1][1] == 'O' and self.table[2][2] == 'O':
            self.point = -1000
            return
        if self.table[0][2] == 'X' and self.table[1][1] == 'X' and self.table[2][0] == 'X':
            self.point = 1000
            return
        elif self.table[0][2] == 'O' and self.table[1][1] == 'O' and self.table[2][0] == 'O':
            self.point = -1000
            return

    def copy(self):
        t = Table()
        for i in range(3):
            for j in range(3):
                if self.table[i][j] != 'e':
                    if self.table[i][j] == 'X':
                        t.set_cell(j,i,1)
                    else:
                        t.set_cell(j,i,-1)
        return  t

