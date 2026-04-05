import unittest #тест#

def snake_travelse(matrix):
    result = []
    for i, row in enumerate(matrix):                 #проходиться про кожному елемену рядка
        if i % 2 == 0:           #парність/непарність рядка
            result.extend(row)
        else:                # непарний рядок -  зворотність послідовності елементів    
            result.extend(row[::-1])
    return result

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
print(snake_travelse(matrix))

class bot_way(unittest.TestCase):           #шлях робота
    def test_square_5x5(self):  
        matrix = [
            [1, 2, 3, 4, 5,],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ]
        extendet = [          #додає кілька елементів до списку. функція.
            1, 2, 3, 4, 5, 
            10, 9, 8, 7, 6,
            11, 12, 13, 14, 15,
            20, 19, 18, 17, 16,
            21, 22, 23, 24, 25
        ]
        self.assertEqual(snake_travelse(matrix), extendet)

    def test_rectangle_2x4(self):
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8]
        ]
        extendet = [1, 2, 3, 4, 8, 7, 6, 5]
        self.assertEqual(snake_travelse(matrix), extendet)

    def test_column_6x1(self):
        matrix = [
            [1],
            [2],
            [3],
            [4],
            [5],
            [6]
        ]
        extendet = [1, 2, 3, 4 ,5 ,6]
        self.assertEqual(snake_travelse(matrix), extendet)
    def test_row_1x6(self):
        matrix = [[1, 2, 3, 4, 5, 6]]
        extendet = [1, 2, 3, 4, 5, 6]
        self.assertEqual(snake_travelse(matrix), extendet)

if __name__ == '__main__':
    unittest.main()