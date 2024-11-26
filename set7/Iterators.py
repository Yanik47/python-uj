from itertools import cycle
from random import choice

print("(a) zwracajacy 0, 1, 0, 1, 0, 1, ...:")
BinaryIterator = cycle([0, 1])
for i in range(10):
    print(next(BinaryIterator))
print()


print("(b) zwracajacy przypadkowo jedna wartosc z (\"N\", \"E\", \"S\", \"W\") [bladzenie przypadkowe na sieci kwadratowej 2D]:")
RandomNESW = (choice(['N', 'E', 'S', 'W']) for _ in iter(int, 1))
for i in range(15):
    print(next(RandomNESW))
print()


print("(c) zwracajacy 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, ... [numery dni tygodnia]:")
WeekIterator = cycle([0, 1, 2, 3, 4, 5, 6])
for i in range(18):
    print(next(WeekIterator))
print()
