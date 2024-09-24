n = 2
print (1)
spelet_pågår = True
    
def flippblipp(n):
        if n %3 == 0 and n %5 == 0:
            return "flipp blipp"
        elif n %3 == 0:
            return "flipp"
        elif n %5 == 0:
            return "blipp"
        else:
            return str (n)
        
while (spelet_pågår):
    if (str(input())==flippblipp(n)):
        #print (flippblipp(n))
        n += 1
    else:
        print ("Fel", "-", flippblipp(n) )
        print()
        print("Game Over"2)
        spelet_pågår = False
    



