from lab2 import matrix

def calculate_time(matrix):
    m = len(matrix)
    n = len(matrix[0])

    time_row = m * 10

    time_turn = (m - 1) * 15

    walk_tm = time_row + time_turn

    breaks = walk_tm // 50

    total_tm = walk_tm + breaks * 10

    return total_tm, breaks

if __name__ == "__main__":
    total_tm, breaks = calculate_time(matrix)
    print(f" ЗГ час: {total_tm}хв") 
    print(f" кількість перерв: {breaks}")