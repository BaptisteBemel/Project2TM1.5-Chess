class Piece:
    def __init__(self, name, color, dead):
        self.color = color
        self.name = name
        self.dead = dead


class Pawn(Piece):
    def __init__(self, color):
        super().__init__("P", color, 0)

    @staticmethod
    def move(move_list):
        if len(move_list) != 2:
            return 'error, try again'


class Rook(Piece):
    def __init__(self, color):
        super().__init__("R", color, 0)


class Bishop(Piece):
    def __init__(self, color):
        super().__init__("B", color, 0)


class Queen(Piece):
    def __init__(self, color):
        super().__init__("Q", color, 0)


class Knight(Piece):
    def __init__(self, color):
        super().__init__("Kn", color, 0)


class King(Piece):
    def __init__(self, color):
        super().__init__("K", color, 0)

    def is_dead(self):
        if self.dead == 1:
            pass


pieces = {'rook': {}, 'bishop': {}, 'pawn': {}, 'king': {}, 'knight': {}, 'queen': {}}


def creation_pieces():
    for i in range(16):
        if i == 0:
            pieces['rook'][i] = Rook('white')
            pieces['bishop'][i] = Bishop('white')
            pieces['pawn'][i] = Pawn('white')
            pieces['knight'][i] = Knight('white')
            pieces['king'][i] = King('white')
            pieces['queen'][i] = Queen('white')
        elif i == 1:
            pieces['rook'][i] = Rook('white')
            pieces['bishop'][i] = Bishop('white')
            pieces['pawn'][i] = Pawn('white')
            pieces['knight'][i] = Knight('white')
            pieces['king'][i] = King('black')
            pieces['queen'][i] = Queen('black')
        elif i < 4:
            pieces['rook'][i] = Rook('black')
            pieces['bishop'][i] = Bishop('black')
            pieces['pawn'][i] = Pawn('white')
            pieces['knight'][i] = Knight('black')
        elif i < 8:
            pieces['pawn'][i] = Pawn('white')
        else:
            pieces['pawn'][i] = Pawn('black')
