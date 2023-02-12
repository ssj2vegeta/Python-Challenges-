def f():
    try:
        print("a")
    except:
        print("b")
    else:
        print("c")
    finally:
        print("d")

f()

#ex1: A B | A B
#ex2: a,c,d
#ex3: a,b,d
#ex4: a,d
