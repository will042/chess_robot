import numpy as np 

class chess_board:
    def __init__(self, x0, y0, x7, y7):
        self.board_state = np.array([[1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1]])
        # self.coordinates_x = np.linspace(x0 + sidelength/8/2, x0 - 7*sidelength/8, 8)
        # self.coordinates_y = np.linspace(y0 + 7*sidelength/8, y0 + sidelength/8/2, 8)
        self.coordinates_x = np.linspace(x0, x7, 8)
        self.coordinates_y = np.linspace(y0, y7, 8)
        print(self.coordinates_x)
        print(self.coordinates_y)
        # [self.coordinates_x, self.coordinates_y] = np.meshgrid(x0 + self.sidelength_dummy, y0 + self.sidelength_dummy)


    def check_occupied(self, Row2, Col2):
        self.Row2 = Row2
        self.Col2 = Col2
        self.occupied = 0

        if self.board_state[self.Row2,self.Col2] == 1 :
            self.occupied = 1
        
        return self.occupied


    def get_xy(self, Row, Col):
        return [self.coordinates_x[Col],self.coordinates_y[Row]]


    def update_board(self, Row1, Col1, Row2, Col2):
        self.Row1 = Row1
        self.Col1 = Col1
        self.Row2 = Row2
        self.Col2 = Col2

        self.board_state[self.Row1, self.Col1] = 0
        self.board_state[self.Row2, self.Col2] = 1


    def generate_movestring(self, Row1, Col1, Row2, Col2):
        self.occupied_flag = str(self.check_occupied(Row2, Col2))
        self.point1 = self.get_xy(Row1, Col1)
        self.point2 = self.get_xy(Row2, Col2)
        self.update_board(Row1, Col1, Row2, Col2)
        self.point1x = str(self.point1[0])
        self.point1y = str(self.point1[1])
        self.point2x = str(self.point2[0])
        self.point2y = str(self.point2[1])
        self.tuple = self.occupied_flag, self.point1x, self.point1y, self.point2x, self.point2y
        self.string = '(' + ', '.join(self.tuple) + ')'
        return self.string
 