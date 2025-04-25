from random import randint

class Rock_paper_scissors:
    wins = {'computer': 0}
    u = 0
    c = 0

    def __init__(self, name):
        Rock_paper_scissors.wins.update({name: 0})
        self.name = name

    def __compMove(self):
        a = randint(1, 3)
        if a == 1:
            return 'St'
        elif a == 2:
            return 'P'
        else:
            return 'Sc'

    def play(self, rounds):
        print(self.name, "Vs Computer")
        for i in range(rounds):
            user = input("Enter 'St' to select stone, 'P' to select paper or 'Sc' to select scissors: ")
            comp = self.__compMove()
            self.compute_result(user, comp)
        self.__matchWinner()

    def compute_result(self, user, comp):
        if user == comp:
            print('Computer chose', comp, 'and you also chose', user)
            print('Round drawn')
        elif user == 'St' and comp == 'P':
            print('Computer chose paper and you chose stone')
            print('You lose')
            Rock_paper_scissors.c += 1
        elif user == 'St' and comp == 'Sc':
            print('Computer chose scissors and you chose stone')
            print('You win')
            Rock_paper_scissors.u += 1
        elif user == 'P' and comp == 'St':
            print('Computer chose stone and you chose paper')
            print('You win')
            Rock_paper_scissors.u += 1
        elif user == 'P' and comp == 'Sc':
            print('Computer chose scissors and you chose paper')
            print('You lose')
            Rock_paper_scissors.c += 1
        elif user == 'Sc' and comp == 'St':
            print('Computer chose stone and you chose scissors')
            print('You lose')
            Rock_paper_scissors.c += 1
        elif user == 'Sc' and comp == 'P':
            print('Computer chose paper and you chose scissors')
            print('You win')
            Rock_paper_scissors.u += 1

    def __matchWinner(self):
        if Rock_paper_scissors.u > Rock_paper_scissors.c:
            print(self.name, "is the match winner")
            Rock_paper_scissors.wins[self.name] += 1
        elif Rock_paper_scissors.u < Rock_paper_scissors.c:
            print("Computer is the match winner")
            Rock_paper_scissors.wins['computer'] += 1
        else:
            print("Match drawn")
        Rock_paper_scissors.c = 0
        Rock_paper_scissors.u = 0

f = Rock_paper_scissors("Rajdeep")
f.play(5)