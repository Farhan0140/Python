

class Sits:
    def __init__(self):
        self.available_sits = 120
        self.sit_map = [[True] * 12 for _ in range(0, 10)]


    def book_sits(self, no_of_sit):
        print(' --- Enter [Row] [Column] No --- ')
        sit_lst = []
        wrong_input = no_of_sit

        while wrong_input != 0:
            row, col = list(map(int, input().split()))
            col -= 1
            if row > 9 or col > 11:
                print('--- Invalid Sit NO. Try Again ---')
                continue

            elif not self.sit_map[row][col]:
                print('--- This sit already booked. Try Again --- ')
                continue
            
            sit_lst.append([row, col])
            self.sit_map[row][col] = False
            self.available_sits -= 1
            wrong_input -= 1

        
        return sit_lst


    def is_available_sit(self):
        if self.available_sits == 0:
            return False
        else:
            return True
        
    


    def view_sit_map(self):
        screen = """
---------------------------------------------------------
|                         Screen                        |
---------------------------------------------------------



                 """
        print(screen)

        for i in range(0, 10):
            print(f'{i}->', end=' ')

            for j in range(0, 12):
                if j == 2 or j == 9:
                    print('_', end=" ")
                if self.sit_map[i][j]:
                    print(f'[{j+1}]', end=" ")
                else:
                    print(' * ', end=' ')
            print()


        projector = """

                -----------------------
                |      Projector      |
                -----------------------

"""
        print(projector)
