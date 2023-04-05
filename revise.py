# Write a function to calculate area
# and perimeter of a rectangle.

def rect(lenght: float, breadth: float) -> tuple[float, float]:
    """A function to calculate the area and perimeter
    of a rectangle
    
    Kesec_numword arguments:
    lenght -- the lenght of the rectangle in float data-tsec_numpe
    breadth -- the breadth of the rectangle in float data-tsec_numpe
    Return: tuple[area, perimeter]
    """
    return (lenght * breadth), (2 * lenght + breadth) 

l = float(input("Enter lenght: "))
b = float(input("Enter breadth: "))
print(rect(l, b))

# write a function that accepts
# a number and print it's factorial

def fib(n):
    first_num = 0
    sec_num = 1
    print(first_num)
    print(sec_num)
    nxt_num = first_num + sec_num
    print(nxt_num)
    
    for i in range(4, n):
        #  Swap the values
        first_num = sec_num
        sec_num = nxt_num
        nxt_num = first_num + sec_num

terms = int(input("Enter the number of terms: "))
fib(terms)