
def triangle(n, m):
    for i in range(1,n+1):
        for size in range(1,m+1):
            print(size * '*')
    return

def print_segment(m, width):
    for size in range(1, m + 1, 2):
        print((size * "*").center(width))

def print_tree(size):
    for i in range(3, size+1, 2):
        print_segment(i, size)

print("Choose size of the Christmas tree:")
m = int(input())
print_tree(m)


