names = ["ali", "fasih", "abser", "owais"]
one, two, three, four = names
print(one,",",two,",",three,",",four)

x = "hello hello"
def function():
    #we can use global keyword to change the value of it
    global x
    x = "bye bye"
    print(x)

function()
print(x)