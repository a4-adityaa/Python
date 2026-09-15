# methods of dictionary

Dictionary={"Name:":"Aadi","age:":22, "marks":95}

print(Dictionary.keys()) # Prints the keys i.e {Name:, age:, marks:}
print(Dictionary.values()) # will prints the values i.e {aadi, 22, 95}
print(Dictionary.items()) # will prints the grouped item i.e {name: Aadi}

Dictionary.pop("age:") # pops out the slected keys
Dictionary.clear() # clears all the data from dictionary
print(Dictionary)