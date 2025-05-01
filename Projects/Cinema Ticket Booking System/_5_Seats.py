

class Seats:
    def __init__(self):
        self.available_seats = 120
        self.seat_map = [[True] * 12 for _ in range(0, 10)]


    def book_seats(self, no_of_seat):
        print(' --- Enter [Row] [Column] No --- ')
        seat_lst = []
        wrong_input = no_of_seat

        while wrong_input != 0:
            row, col = list(map(int, input().split()))
            col -= 1
            if row > 9 or col > 11:
                print('--- Invalid Seat NO. Try Again ---')
                continue

            elif not self.seat_map[row][col]:
                print('--- This seat already booked. Try Again --- ')
                continue
            
            seat_lst.append([row, col])
            self.seat_map[row][col] = False
            self.available_seats -= 1
            wrong_input -= 1

        
        return seat_lst


    def is_available_seat(self):
        if self.available_seats == 0:
            return False
        else:
            return True
        
    


    def view_seat_map(self):
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
                if self.seat_map[i][j]:
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
