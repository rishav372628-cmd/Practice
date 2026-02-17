x = 1
y = 3
unit_price = 3
print(x)
course = "Python Programming"
print(course)
print(len(course))
print(course[0])
print(course[-1])
print(course[0:3])
print(course[0:])
print(course[:3])
print(course[:])
print("Python \" ")
print("\\")
print("Python \nProgramming")
first = "chut"
last = "Seshanpyari"
full_name = first + " " + last
print(full_name)
full = f"{first} {last}"
print(full)
a = " python "
print(len(a))
print(a.upper())
print(a.lower())
print(a.title())
print(a.strip())
print(a.lstrip())
print(a.rstrip())
print(a.find("th"))
print(a.find("to"))
print(a.replace("p", "j"))
print(a.replace("j", "p"))
print("py" in a)
print("Py" in a)
print("py" not in a)
print("Py" not in a)
# -------------------------------------------

c = "app" > "apple"
print(c)

c = 0
for i in range(1, 10):
    if i % 2 == 0:
        print(i)
        c += 1
print(f"We have {c} even numbers")
