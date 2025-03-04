n = int(input())

def star(n):
    if n == 1:
        print('*')
        return
    print('*' * n)
    return star(n - 1)

star(n)