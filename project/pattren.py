#Cara membuat pattren dengan teks (python)
print("=== Pattren Text ===")
MyStr = "Python"
x = 0

for i in MyStr:
    x += 1
    print(MyStr[0:x])
    
for i in MyStr:
    x -= 1
    print(MyStr[0:x])