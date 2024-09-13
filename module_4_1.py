from fake_math import divide as div_fm
from true_math import divide as div_tm

res1 = div_fm(69, 3)
res2 = div_fm(3, 0)
res3 = div_tm(49, 7)
res4 = div_tm(15, 0)

print(res1)
print(res2)
print(res3)
print(res4)