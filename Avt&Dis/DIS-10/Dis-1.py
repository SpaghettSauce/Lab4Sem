def nod(m,n):
    return m if n == 0 else nod (n,m%n)

a = 51111
b = -58973
c=1

assert c!=0
nodAB = nod(abs(a),abs(b))
if c % nodAB:
    print("Нет решений")
else:
    a//= nodAB
    b//= nodAB
    c//= nodAB
    for k in range(abs(a)):
        if (c - b * k) % a == 0:
            y = k
            x = (c - b * y) // a 
            print("x=",x,"y=",y)
            break
    else:
        print("Упси")
