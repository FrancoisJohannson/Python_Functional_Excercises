# receiving a function as parameter and returning it
def highest_order(f):
    return f()


# receiving a function as parameter and passing it to another
def higher_order(f):
    return highest_order(f)


# a function used as parameter for higher order functions
def low_order(s):
    return "low_order: " + s


print("starting")
print(low_order("ben"))
print(higher_order(lambda: low_order("😜")))
