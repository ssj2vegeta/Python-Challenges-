v = int(input("number of vertical pixels?"))
h = int(input("number of horizonatal pixels?"))
b = int(input("bit depth?"))
print(f"image size is {v*h*b/(8*1024)} KB")
