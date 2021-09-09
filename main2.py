c = 0
while c < 5:
    print(c)
    c = c + 1

while c < 5:
    c = c + 1
    if c == 3:
        break
    print(c)


# try and except
name = "h"
try:
    if name > "3":
        print('hi')
finally:     # except isn't working
    print("There is an error here")

# functions

