with open('p01_d.txt') as f:
    w, h = [int(x) for x in next(f).split()]
    array = [[int(x) for x in line.split()] for line in f]
    print(array)
