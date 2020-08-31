filename = input("enter the file name: ")
fextns = filename.split(".")
print("The extension of the file is :" + repr(fextns[-1]))
