##### Lesson 05: Control Flow & Loops #########

### 1.If Statement ###
x = 10
if x > 5:
    print("x is greater than 5")

### 2.Elif Statement ###
x = 10
if x > 20:
    print("x is greater than 20")
elif x > 5:
    print("x is greater than 5 but less than or equal to 20")

### 3.Else Statement ###
x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")

### 4.Nested If Statements ###
x = 10
if x > 5:
    if x < 15:
        print("x is between 5 and 15")

### 5. Logical Operators ###
x = 10
y = 20
if x > 5 and y > 15:
    print("Both conditions are true")

### 6. Ternary Operator (Conditional Expression) ###
if x > 5:
    value = "Greater"
else:
    value = "Smaller"

### 7. For Loops ###
for i in range(5):
    print(i)

### 8. While Loops ###
x = 0
while x < 5:
    print(x)
    x += 1  # Increment to avoid infinite loop

### 9. Break and Continue ###
for i in range(10):
    if i == 5:
        break  # Breaks the loop when i equals 5
    print(i)

for i in range(5):
    if i == 2:
        continue  # Skips the print statement when i equals 2
    print(i)

####### ************ ##########