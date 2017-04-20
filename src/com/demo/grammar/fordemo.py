#!/usr/bin/python
# Filename: fordemo.py

for i in range(2, 5):
    if i == 3:
        continue
    print(i)
#    if i==3:
#        break
else:
    print("Loop is End!")
