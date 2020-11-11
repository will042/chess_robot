import numpy as np 

class chess_board:
    def __init__(self, sidelength, x0, y0):
        self.board_state = np.array([[1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1]])
        self.coordinates = np.linspace(sidelength/8/2, sidelength - sidelength/8/2, 8)
        # [self.coordinates_x, self.coordinates_y] = np.meshgrid(x0 + self.sidelength_dummy, y0 + self.sidelength_dummy)


    def check_occupied(self, Row2, Col2):
        self.Row2 = Row2
        self.Col2 = Col2
        self.occupied = 0

        if self.board_state[self.Row2,self.Col2] == 1 :
            self.occupied = 1
        
        return self.occupied


    def get_xy(self, Row, Col):
        return [self.coordinates[Row], self.coordinates[Col]]


    def update_board(self, Row1, Col1, Row2, Col2):
        self.Row1 = Row1
        self.Col1 = Col1
        self.Row2 = Row2
        self.Col2 = Col2

        self.board_state[self.Row1, self.Col1] = 0
        self.board_state[self.Row2, self.Col2] = 1


    def move(self, Row1, Col1, Row2, Col2):

        self.occupied_flag = self.check_occupied(Row2, Col2)
        self.point1 = self.get_xy(Row1, Col1)
        self.point2 = self.get_xy(Row2, Col2)
        self.update_board(Row1, Col1, Row2, Col2)

        return self.occupied_flag, self.point1, self.point2
