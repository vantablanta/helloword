print('Hello World')
age = 20
name = "Michelle"
""
print("My name is " + name + "."  "I am turning " + str(age))

name2, age2 = "I am Michelle", 20
print(name2)
print(age2)

x = 2
y = 10
print(y - x)
print(x * y)
print(y % x)
print(y / x)

sent1 = "Today is a good day. "
print(sent1 * 2)
sent2 = "I will go fishing"
print(sent1 + sent2)

sent = "Michelle is playing  cricket"
print(sent[0:9])
print(sent[-3])

# placeholders
person = "Ochi "
text = "%s is 15 years old"
print(text)
print(text % person)

boy = "Chris"
text = "%s is a good boy"
print(text % boy)
print(text % "Nico")

girl = "Shiko"
text = "%s loves to walk"
print(text % girl)
print(text % "Njeri")

sent = "%s %s is the President of the united States"
print(sent % ("Barack", "Obama"))
sent = "%s is %d years old"
print(sent % ("Obama", 50))

# lists
shopList = ["Apples", "Oranges", "Bananas", "Mangoes", "Bread"]
print(shopList[4])
print(shopList[1:3])
shopList.append("Melon")
print(shopList)
del shopList[1]
print(shopList)
print(len(shopList))
shopList2 = ["Shoes", "Dresses", "Cars"]
newList = shopList2 + shopList
print(newList)

Nums = [2, 5, 10, 89, 17]
print(max(Nums))


# Dictionaries
students = {
    "Bob": 15,
    "Emily": 13,
    "Rachel": 12
}
print(students["Bob"])
students["Bob"] = 20
print(students["Bob"])
del students['Bob']
print(students)

# tuples are immutable... cant be updated
tup1 = ("oranges", "apples", "bananas")
print(tup1[0])
tup2 = ('boots', 'ginger', 'eyes')
tup3 = tup1 + tup2
print(tup3)

# conditional statements
if 5 > 10:
    print("the condition 5 > 10 is true")
else:
    print('the condition 5 > 10 was not true')

age = 10
if age < 25:
    print('you are young')
elif age >= 25 and age <= 28:
    print('you are a young adult')
else:
    print('you are old')
