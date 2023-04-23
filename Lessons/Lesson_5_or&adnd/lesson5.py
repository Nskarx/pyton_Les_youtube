# Логические операторы

print(True or False)  # True
print(False or True)  # True

print(1 or 0)  # 1
print(1 or 2 or 3)  # 1
print(True or hahaha)  # True
print(None or False or 0)  # 0

print(False and True)  # false
print(1 and 0)  # 0

print(0 and None and False)  # 0

print(0 and hahaha)  # 0

print( -1 and 2 and 3) # 3

print( 1 > 0 and 10 < 100) # True

print( 1 > 0 or 5 > 10) # True

print( 1 > 0 or None and '0') # True