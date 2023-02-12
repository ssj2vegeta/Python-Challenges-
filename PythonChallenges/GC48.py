while True:
    try:
        k = int(input("integers only!"))
    except ValueError:
        pass 
        continue
    finally:
        print("input accepted")
        break
