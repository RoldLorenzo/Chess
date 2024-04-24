import tkinter as tk
from PIL import Image, ImageTk
from typing import Literal, TypeAlias

Team : TypeAlias = Literal["White", "Black"]

class Piece:
    def __init__(self, team : Team) -> None:
        self.team = team
        self.sprite = None
        
    def loadSprite(self) -> None:
        if self.sprite == None:
            pieceImgPIL = Image.open("images/" + self.team + self.__class__.__name__ + ".png")
            self.sprite = ImageTk.PhotoImage(pieceImgPIL.convert(mode="RGBA"))

class King(Piece):
    def __init__(self, team: Team) -> None:
        super().__init__(team)

class Queen(Piece):
    def __init__(self, team: Team) -> None:
        super().__init__(team)

class Rook(Piece):
    def __init__(self, team: Team) -> None:
        super().__init__(team)

class Bishop(Piece):
    def __init__(self, team: Team) -> None:
        super().__init__(team)
        
class Knight(Piece):
    def __init__(self, team: Team) -> None:
        super().__init__(team)

class Pawn(Piece):
    def __init__(self, team: Team) -> None:
        super().__init__(team)



BoardTile : TypeAlias = Piece | None

class Board:
    def __init__(self) -> None:
        self.tiles : list[list[BoardTile]] 
        self.setPieces()
        
        self.tileSize = 50
        
    def setPieces(self):
        self.tiles = [[None for _ in range(8)] for _ in range(8)]
        
        self.tiles[3][0] = King("White")
        self.tiles[4][0] = Queen("White")
        self.tiles[0][0] = Rook("White")
        self.tiles[7][0] = Rook("White")
        self.tiles[1][0] = Knight("White")
        self.tiles[6][0] = Knight("White")
        self.tiles[2][0] = Bishop("White")
        self.tiles[5][0] = Bishop("White")
        
        for i in range(8):
            self.tiles[i][1] = Pawn("White")
        
        self.tiles[3][7] = King("Black")
        self.tiles[4][7] = Queen("Black")
        self.tiles[0][7] = Rook("Black")
        self.tiles[7][7] = Rook("Black")
        self.tiles[1][7] = Knight("Black")
        self.tiles[6][7] = Knight("Black")
        self.tiles[2][7] = Bishop("Black")
        self.tiles[5][7] = Bishop("Black")
        
        for i in range(8):
            self.tiles[i][6] = Pawn("Black")


class GUI:
    def __init__(self, board : Board) -> None:
        self.root = tk.Tk()
        self.root.title("Chess")
        self.root.geometry("500x500")
        
        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.place(relx=0.5, rely=0.5, anchor = tk.CENTER)
        
        self.loadPieceImages(board)
        self.drawBoard(board)
    
    # The pieces sprites must be loaded in the GUI class because images cannot be loaded before the TK root.
    def loadPieceImages(self, board : Board):
        for row in board.tiles:
            for piece in row:
                if piece != None:
                    piece.loadSprite()
    
    def drawBoard(self, board : Board) -> None:
        for i, row in enumerate(board.tiles):
            for j, piece in enumerate(row):
                color = "#ecd4b4" if (i + j) % 2 == 0 else "#bc8464"
                
                x, y = i * board.tileSize, j * board.tileSize
                
                self.canvas.create_rectangle(x, y, x + board.tileSize, y + board.tileSize, fill=color)
                
                if piece != None:                    
                    self.canvas.create_image(x + 2.5, y + 2.5, image=piece.sprite, anchor=tk.NW)
    
    def loop(self):
        self.root.mainloop()



if __name__ == "__main__":
    board = Board()
    
    gui = GUI(board)
    gui.loop()