class CardPile:
    def __init__(self):
    def add_top(self, item):
    def add_bottom(self, item):
    def remove_top(self):
    def remove_bottom(self):
    def size(self):
    def peek_top(self):
    def peek_bottom(self):
    def print_all(self, index):
 
class Solitaire:
    def __init__(self, cards):
        self.__piles = []
        self.__num_cards = len(cards)
        self.__num_piles = (self.__num_cards // 8) + 3
        self.__max_num_moves = self.__num_cards * 2
        for i in range(self.__num_piles):
            self.__piles.append(CardPile())
        for i in range(self.__num_cards):
            self.__piles[0].add_bottom(cards[i])

    def get_pile(self, i):
        return self.__piles[i]
    
    def display(self):
 
    def move(self, p1, p2):

    def is_complete(self):

    def play(self):
        print("********************** NEW GAME *****************************")
        move_number = 1
        while move_number <= self.__max_num_moves and not self.is_complete():
            self.display()
            print("Round", move_number, "out of", self.__max_num_moves, end = ": ")
            row1 = int(input("Move from row no.:"),10)
            print("Round", move_number, "out of", self.__max_num_moves, end = ": ")
            row2 = int(input("Move to row no.:"),10)
            if row1 >= 0 and row2 >= 0 and row1 < self.__num_piles and row2 < self.__num_piles:
                self.move(row1, row2)
            move_number += 1
            
        if self.is_complete():
            print("You Win in", move_number - 1, "steps!\n")
        else:
            print("You Lose!\n")
