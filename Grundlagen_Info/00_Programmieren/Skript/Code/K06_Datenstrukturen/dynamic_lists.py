zahlen = [1, 2, 3]
zahlen.append(4)  # [1, 2, 3, 4]
zahlen.insert(1, 10)  # [1, 10, 2, 3, 4]
letztes = zahlen.pop()  # entfernt 4, jetzt [1, 10, 2, 3]
erstes = zahlen.pop(0)  # entfernt 1, jetzt [10, 2, 3]
print(zahlen)  # [10, 2, 3]
print(letztes)  # 4
print(erstes)  # 1
