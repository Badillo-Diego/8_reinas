#Alan Daniel Sigala Morales
#Diego Fernando Badillo Vega
#Luis Felipe Tarelo Ramírez
#Irving Rodriguez Rodriguez
#Raúl Alajandro Moreno Camargo

from queue import PriorityQueue

def is_valid(board, row, col):
    # Comprueba si es seguro colocar una reina en la posición (row, col) en el tablero.
    # Verifica las filas, columnas y diagonales.
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def queens_a_star():
    n = 8  # Tamaño del tablero de ajedrez (8x8)
    open_list = PriorityQueue()
    open_list.put((0, []))  # (Costo, Tablero)
    
    while not open_list.empty():
        _, board = open_list.get()
        row = len(board)
        
        if row == n:  # Si hemos colocado las 8 reinas, hemos encontrado una solución.
            return board
        
        for col in range(n):
            if is_valid(board, row, col):
                new_board = board + [col]
                cost = len(new_board)  # Costo es simplemente el número de reinas colocadas.
                open_list.put((cost, new_board))
    
    return None  # No se encontró una solución

def print_solution(board):
    for row in range(8):
        line = ""
        for col in range(8):
            if col == board[row]:
                line += "Q "
            else:
                line += ". "
        print(line)

if _name_ == "_main_":
    solution = queens_a_star()
    if solution:
        print("Solución encontrada:")
        print_solution(solution)
    else:
        print("No se encontró solución.")
