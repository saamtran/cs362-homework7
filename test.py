
def fizzbuzz():
    array = []
    for x in range(1, 101):
        if x % 3 == 0:
            array.append("Fizz")
        
        elif x % 5 == 0:
            array.append("buzz")
        
        else:
            array.append(x)
    print(array)
    return array
fizzbuzz()