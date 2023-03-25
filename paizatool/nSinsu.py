#10進数から各進数へ変換
a = int('1001', 2)  # 2進数
b = int('75', 8)  # 8進数
c = int('c3', 16)  # 16進数
print(a)  # 9
print(b)  # 61
print(c)  # 195

#10進数から2進数へ変換
a = format(6, 'b')
b = format(7, 'b')
c = format(8, 'b')
d = format(9, 'b')
print(a)  # 110
print(b)  # 111
print(c)  # 1000
print(d)  # 1001
print(type(a))  # <class 'str'>