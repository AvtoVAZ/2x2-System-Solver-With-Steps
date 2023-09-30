print("=======================================================================================================")
print("---")
print("| ax ± by = c")
print("| a'x ± b'y = c")
print("---")
a1 = int(input("a: "))
b1 = int(input("b: "))
g1 = int(input("c: "))
a2 = int(input("a': "))
b2 = int(input("b': "))
g2 = int(input("c': "))
print("=======================================================================================================")
print("---")
print("| ",a1,"x ± ",b1,"y = ",g1)
print("| ",a2,"x ± ",b2,"y = ",g2)
print("---")
print("=======================================================================================================")
dpart1 = (a1) * (b2)
dpart2 = (a2) * (b1)
dpart3 = (dpart1) - (dpart2)
if b2 < 0:
    b2if = "(" + str(b2) + ")"
else:
    b2if = str(b2)
if b1 < 0:
    b1if = "(" + str(b1) + ")"
else:
    b1if = str(b1)
if dpart2 < 0:
    dpart2if = "(" + str(dpart2) + ")"
else:
    dpart2if = str(dpart2)
if dpart2 < 0:
    dpart2mulmin1 = (dpart2) * (-1)
    dpart2if = "(" + str(dpart2) + ") = " + str(dpart1) + " + " + str(dpart2mulmin1) + " = " + str(dpart3)
else:
    dpart2if = str(dpart2) + " = " + str(dpart3)
print("D = |",a1 ,b2,"| = (" + str(a1) + " * " + str(b2if) + ") - (" + str(a2) + " * " + str(b1if) + ") = " + str(dpart1) + " - " + str(dpart2if))
print("    |",a2 ,b1,"|")
print("=======================================================================================================")

if dpart3 == 0:
    print("The system of 2x2 cannot be solved or it has a number of infinite possible solutions.")
    print("=======================================================================================================")
else:
    dxpart1 = (g1) * (b2)
    dxpart2 = (g2) * (b1)
    dxpart3 = (dxpart1) - (dxpart2)
    blank = str(" ")
    if b2 < 0:
        b2if = "(" + str(b2) + ")"
    else:
        b2if = str(b2)
    if b1 < 0:
        b1if = "(" + str(b1) + ")"
    else:
        b1if = str(b1)
    if dxpart2 < 0:
        dxpart2if = "(" + str(dxpart2) + ")"
    else:
        dxpart2if = str(dxpart2)
    if dxpart2 < 0:
        dxpart2mulmin1 = (dxpart2) * (-1)
        dxpart2if = "(" + str(dxpart2) + ") = " + str(dxpart1) + " + " + str(dxpart2mulmin1) + " = " + str(dxpart3)
    else:
        dxpart2if = str(dxpart2) + " = " + str(dxpart3)
    print("D(x) = |",g1 ,b2,"| = (" + str(g1) + " * " + str(b2if) + ") - (" + str(g2) + " * " + str(b1if) + ") =" + str(dxpart1) + " - " + str(dxpart2if))
    print("D(x) = |",g2 ,b1,"|")
    print("=======================================================================================================")
    dypart1 = (a1) * (g2)
    dypart2 = (a2) * (g1)
    dypart3 = (dypart1) - (dypart2)
    if g2 < 0:
        g2if = "(" + str(g2) + ")"
    else:
        g2if = str(g2)
    if g1 < 0:
        g1if = "(" + str(g1) + ")"
    else:
        g1if = str(g1)
    if dypart2 < 0:
        dypart2mulmin1 = (dypart2) * (-1)
        dypart2if = "(" + str(dypart2) + ") = " + str(dypart1) + " + " + str(dypart2mulmin1) + " = " + str(dypart3)
    else:
        dypart2if = str(dypart2) + " = " + str(dypart3)
    print("D(y) = |",a1 ,g2,"| = " + str(a1) + " * " + str(g2if) + " - (" + str(a2) + " * " + str(g1if) + ") = " + str(dypart1) + " - " + str(dypart2if))
    print("D(y) = |",a2 ,g1,"|")
    print("=======================================================================================================")
    x = (dxpart3) / (dpart3)
    y = (dypart3) / (dpart3)
    print("      D(x)   ",dxpart3                                                                                            )
    print("x = ------- = -------- = ",x)
    print("      D      ",dpart3                                                                                             )
    print("=======================================================================================================")
    print("      D(y)   ", dypart3                                                                                           )
    print("y = ------- = -------- = ",y)
    print("      D      ", dpart3                                                                                            )
    print("=======================================================================================================")
    print("(",x,",",y,")")
    print("=======================================================================================================")

