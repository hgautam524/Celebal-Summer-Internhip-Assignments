
# As it is not mentioned correctly in the question how many rows are there in the triangle pattern, I am assuming it to be 5 rows.
# or 15 start Triangle pattern.

def print_triangle_pattern(rows):
    for i in range(1, rows + 1):

        if i == 1:
            print()

        print( '* ' * i)
        

def upper_triangle(rows):
    print("Upper Triangular :")
    for i in range(rows, 0, -1):
        print('* ' * i)
    print()

def pyramid(rows):
    print("Pyramid :")
    for i in range(1, rows + 1):
        print(' ' * (rows - i) + '* ' * i)
    print()

rows = 5
print("Lower Triangular :") 
print_triangle_pattern(rows)
upper_triangle(rows)
pyramid(rows)
