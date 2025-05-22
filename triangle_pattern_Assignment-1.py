
# As it is not mentioned correctly in the question how many rows are there in the triangle pattern, I am assuming it to be 5 rows.
# or 15 start Triangle pattern.

def print_triangle_pattern(rows):
    for i in range(1, rows + 1):

        if i == 1:
            print()

        print( '* ' * i)
        
        
print_triangle_pattern(5)
