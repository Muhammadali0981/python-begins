#using sep
#for no seperator
print('I','J','K', sep = "")

#for seprating with comma
print('I','J','K', sep = ",")

#whatever works apparently
print('I','J','K', sep = "FE")
print('I','J','K', sep = 's')
print('I','J','K', sep = "*")

#nice 

#using format()
#rounds off depeneding on the .f value
amount = 156.887
print("${:.2f}".format(amount))
print("${:.3f}".format(amount))
print("${:.4f}".format(amount))

#testing something
name = "Ali"
age = 19

print("name is" ,name ,"age is" ,age)

#this langauge has no shame
#can use f and put curly brackets on variables
#> is used for padding > for before < for after
print(f"name is {name:>10} age is {age:<10}.")

