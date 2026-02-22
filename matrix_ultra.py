import pygame as p
from random import *
p.init()
s = p.display.set_mode((0, 0), p.FULLSCREEN)
W, H = s.get_size()
C = 16
N = W//C
M = H//C
f = p.font.SysFont(0, C)
Z = "0123456789ABCDEF"
P = [[f.render(c, 0, (b*4, min(255, b*8+50), b))for b in range(32)]for c in Z]
D = [[random()*M, random()*.5+.3, randint(8, 18)]for _ in range(N)]
while not any(e.type == p.KEYDOWN and e.key == 27 for e in p.event.get()):
    s.fill(0)
    for i, d in enumerate(D):
        d[0] += d[1]
        y = int(d[0])
        if y-d[2] > M:
            d[0] = -randint(5, 15)
            d[1] = random()*.5+.3
        for j in range(d[2]):
            r = y-j
            if 0 <= r < M:
                s.blit(P[randint(0, 15)][31-j*31//d[2]], (i*C, r*C))
    p.display.flip()
    p.time.delay(42)
