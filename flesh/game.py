import random
from fastapi import FastAPI, APIRouter

router=APIRouter()

class Game:
    def __init__ (self, users):
        self.users=users
        self.tiles=[]
        self.wordbank=WordBank()
    
    def flip_tile(self):
        tile=self.wordbank.get_next_tile()
        if not tile:
            return None
        self.tiles.append(tile)
        return tile


class WordBank:
    tiles = {
        "A":13,
        "B":3,
        "C":3,
        "D":6,
        "E":18,
        "F":3,
        "G":4,
        "H":3,
        "I":12,
        "J":2,
        "K":2,
        "L":5,
        "M":3,
        "N":8,
        "O":11,
        "P":3,
        "Q":2,
        "R":9,
        "S":6,
        "T":9,
        "U":6,
        "V":3,
        "W":3,
        "X":2,
        "Y":3,
        "Z":2
    }

    def __init__(self):
        self.wordbank = self.generate_wordbank(self.tiles)

    def generate_wordbank(self, tiles):
        queue=[]
        for letter, count in tiles.items():
            queue.extend([letter]*count)
        random.shuffle(queue)
        return queue
    
    def get_next_tile(self):
        if self.wordbank:
            return self.wordbank.pop()
        else:
            return None

# class User:
#     def __init__(self):
#         self=self
#     def addWord():

    
# class Word:
#     def __init_(self, word):
#         self.words_used = set()
#         self.words_used.add(word)
    
#     def anagram():





    



