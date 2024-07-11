def closest_mod_5():
    x = int(input())
    if x % 5 == 0:
        return x
    else:
        return(x+(5-x%5))