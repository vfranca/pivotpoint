from _pp import *
import sys

h = float(sys.argv[1])
l = float(sys.argv[2])
c = float(sys.argv[3])

pp = pp(h, l, c)
r1 = r1(pp, l)
s1 = s1(pp, h)
r2 = r2(pp, h, l)
s2 = s2(pp, h, l)

print("ponto pivô: %.2f" % pp)
print("resistências: %.2f %.2f" % (r1, r2))
print("suportes: %.2f %.2f" % (s1, s2))




