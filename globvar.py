globvar = 0

def set_globvar_to_one():
    global globvar    # Needed to modify global copy of globvar
    globvar = 1

def print_globvar():
    print(globvar)     # No need for global declaration to read value of globvar

set_globvar_to_one()
print_globvar()

"""
    a   b   c   d   e   f   g   h   i   j   k   l   m   n   o   p 
a   0   4   5   6   11  13  20  2   60  16  15  23  65  27  32  56
b   4   0   3   6   7   11  34  23  6   90  20  38  51  60  33  17
c   5   3   0   3   8   8   40  17  22  21  16  82  71  44  18  6
d   6   6   3   0   11  9   33  2   1   15  5   2   3   9   8   10 
e   11  7   8   11  0   4   88  77  93  11  3   2   5   8   7   7
f   13  11  8   9   4   0   12  14  22  1   1   15  16  23  64  80
g   20  34  40  33  88  12  0   81  20  17  9   4   5   1   2   9
h   2   23  17  2   77  14  81  0   27  54  6   22  3   1   44  10
i   60  6   22  1   93  22  20  27  0   99  7   40  20  10  11  12
j   16  90  21  15  11  1   17  54  99  0   13  20  2   50  1   2
k   15  20  16  5   3   1   9   6   7   13  0   15  2   7   8   9
l   23  38  82  2   2   15  4   22  40  20  15  0   3   11  15  90
m   65  51  71  3   5   16  5   3   20  2   2   3   0   70  80  45
n   27  60  44  9   8   23  1   1   10  50  7   11  70  0   9   8
o   32  33  18  8   7   64  2   44  11  1   8   14  80  9   0   2
p   56  17  6   10  7   80  9   10  12  2   9   90  45  8   2   0
"""