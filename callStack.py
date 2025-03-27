def three():
    print("three")

def two():
    three()
    print("two")

def one():
    two()
    print("one") 

one()