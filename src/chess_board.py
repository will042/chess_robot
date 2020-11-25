import chess
import numpy as np

class chess_board:

    def __init__(self, x0, y0, x7, y7):
        self.coordinates_x = np.linspace(x0, x7, 8)
        self.coordinates_y = np.linspace(y0, y7, 8)
        # print(self.coordinates_x)
        # print(self.coordinates_y)
        self.board = chess.Board()


    def get_xy(self, Row, Col):
        return [self.coordinates_x[Col], self.coordinates_y[Row]]


    def check_occupied(self, target_square):

        if not self.board.piece_at(target_square):
            self.occupied = 0
        else:
            self.occupied = 1

        return self.occupied

    def convert_square(self, Row, Col):

        self.numbered_squares = np.arange(64).reshape(8, 8)
        self.square_number = self.numbered_squares[Row,Col]

        return self.square_number

    def move(self, Row1, Col1, Row2, Col2):

        self.source_square = self.convert_square(Row1,Col1)
        self.target_square = self.convert_square(Row2,Col2)

        self.occupied_flag = str(self.check_occupied(self.target_square))

        self.source_xy = self.get_xy(Row1, Col1)
        self.target_xy = self.get_xy(Row2, Col2)
        self.source_x = str(self.source_xy[0])
        self.source_y = str(self.source_xy[1])
        self.target_x = str(self.target_xy[0])
        self.target_y = str(self.target_xy[1])
        self.tuple = self.occupied_flag, self.source_x, self.source_y, self.target_x, self.target_y
        self.move_string = '(' + ', '.join(self.tuple) + ')'

        self.desired_move = chess.Move(self.source_square, self.target_square)
        self.board.push(self.desired_move)

        print(self.desired_move)
        print(self.move_string+"\n")
        print(self.board.unicode()+"\n")

        return self.move_string