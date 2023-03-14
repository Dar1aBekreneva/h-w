"lab3"
def q0():
    m = int(input())
    n = []
    for i in range(m):
        n.append(input())
    w = ' '.join(n)
    print(w)

def q1():
    n = []
    m = str(input())
    while m != 'stop':
        m = str(input())
        n.append(m)
    w = ' '.join(n)
    print(w)

def q2():
    n = str(input())
    l = "ф"
    x = l in n
    if x == True:
        print("редкое слово")
    else:
        print("обычное слово")

q0()
q1()
q2()
