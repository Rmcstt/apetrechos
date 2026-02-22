import pygame
import math
import random

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
W, H = screen.get_width(), screen.get_height()
clock = pygame.time.Clock()

# Criar estrelas/astros: [x, y, vx, vy, massa, cor, raio]
NUM_STARS = 500


def create_star():
    x = random.randint(0, W)
    y = random.randint(0, H)
    mass = random.uniform(1, 3)
    brightness = random.randint(150, 255)
    color = random.choice([
        (brightness, brightness, brightness),           # branca
        (brightness, brightness * 0.8, brightness * 0.6),  # amarelada
        (brightness * 0.7, brightness * 0.8, brightness),  # azulada
        (brightness, brightness * 0.6, brightness * 0.6),  # avermelhada
    ])
    return [x, y, random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5), mass, color, mass]


stars = [create_star() for _ in range(NUM_STARS)]

# Buracos negros ativos: [x, y, força, tempo_de_vida]
blackholes = []

# Partículas de efeito ao sugar
particles = []

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                running = False
            elif e.key == pygame.K_r:
                # Reset: recriar estrelas
                stars = [create_star() for _ in range(NUM_STARS)]
                blackholes.clear()
                particles.clear()
            elif e.key == pygame.K_SPACE:
                # Adicionar mais estrelas
                stars.extend([create_star() for _ in range(100)])

    screen.fill((5, 5, 15))

    mx, my = pygame.mouse.get_pos()
    mb = pygame.mouse.get_pressed()

    # Criar/manter buraco negro enquanto clica
    if mb[0]:  # Clique esquerdo - buraco negro atrativo
        # Verifica se já existe um buraco negro perto
        found = False
        for bh in blackholes:
            if math.hypot(bh[0] - mx, bh[1] - my) < 50:
                bh[2] = min(bh[2] + 0.5, 50)  # Aumenta força
                bh[3] = 60  # Reset tempo de vida
                found = True
                break
        if not found:
            blackholes.append([mx, my, 10, 60])

    if mb[2]:  # Clique direito - explosão repulsiva
        for star in stars:
            dx = star[0] - mx
            dy = star[1] - my
            dist = math.hypot(dx, dy) + 1
            if dist < 300:
                force = 500 / (dist * dist) * 50
                star[2] += (dx / dist) * force
                star[3] += (dy / dist) * force

    # Atualizar buracos negros
    for bh in blackholes[:]:
        bh[3] -= 1  # Diminui tempo de vida
        if bh[3] <= 0:
            bh[2] -= 0.3  # Diminui força gradualmente
            if bh[2] <= 0:
                blackholes.remove(bh)
                continue

        # Desenhar buraco negro com efeito de disco de acreção
        for r in range(int(bh[2] * 3), 5, -3):
            alpha = max(0, min(255, 100 - r * 2))
            color = (min(255, 50 + r * 2),
                     min(255, 20 + r), min(255, 80 + r * 3))
            pygame.draw.circle(screen, color, (int(bh[0]), int(bh[1])), r, 2)

        # Núcleo do buraco negro
        pygame.draw.circle(screen, (0, 0, 0), (int(
            bh[0]), int(bh[1])), max(5, int(bh[2] / 2)))
        pygame.draw.circle(screen, (30, 0, 50), (int(
            bh[0]), int(bh[1])), max(8, int(bh[2] / 1.5)), 2)

    # Atualizar e desenhar estrelas
    stars_to_remove = []
    for i, star in enumerate(stars):
        # Aplicar gravidade de cada buraco negro
        for bh in blackholes:
            dx = bh[0] - star[0]
            dy = bh[1] - star[1]
            dist = math.hypot(dx, dy) + 1

            if dist < 15:  # Estrela foi sugada
                stars_to_remove.append(i)
                # Criar partículas de efeito
                for _ in range(5):
                    angle = random.uniform(0, math.pi * 2)
                    speed = random.uniform(2, 5)
                    particles.append([
                        star[0], star[1],
                        math.cos(angle) * speed,
                        math.sin(angle) * speed,
                        star[5], 30  # cor e vida
                    ])
                break

            # Força gravitacional (inverso do quadrado da distância)
            force = bh[2] * 100 / (dist * dist)
            force = min(force, 5)  # Limitar força máxima

            star[2] += (dx / dist) * force
            star[3] += (dy / dist) * force

        # Aplicar velocidade
        star[0] += star[2]
        star[1] += star[3]

        # Fricção espacial leve
        star[2] *= 0.999
        star[3] *= 0.999

        # Limitar velocidade
        speed = math.hypot(star[2], star[3])
        if speed > 15:
            star[2] = (star[2] / speed) * 15
            star[3] = (star[3] / speed) * 15

        # Wrap around nas bordas
        if star[0] < -50:
            star[0] = W + 50
        if star[0] > W + 50:
            star[0] = -50
        if star[1] < -50:
            star[1] = H + 50
        if star[1] > H + 50:
            star[1] = -50

        # Desenhar estrela com rastro baseado na velocidade
        speed = math.hypot(star[2], star[3])

        # Rastro (trail)
        if speed > 1:
            trail_len = min(speed * 3, 20)
            trail_end = (star[0] - star[2] * trail_len / speed * 2,
                         star[1] - star[3] * trail_len / speed * 2)
            trail_color = tuple(max(0, c // 3) for c in star[5])
            pygame.draw.line(screen, trail_color,
                             (int(star[0]), int(star[1])),
                             (int(trail_end[0]), int(trail_end[1])), 1)

        # Brilho da estrela
        glow_size = int(star[6] + speed / 3)
        if glow_size > 2:
            glow_color = tuple(max(0, c // 4) for c in star[5])
            pygame.draw.circle(screen, glow_color, (int(
                star[0]), int(star[1])), glow_size + 2)

        pygame.draw.circle(screen, star[5], (int(
            star[0]), int(star[1])), max(1, int(star[6])))

    # Remover estrelas sugadas
    for i in sorted(stars_to_remove, reverse=True):
        if i < len(stars):
            stars.pop(i)

    # Atualizar e desenhar partículas
    for p in particles[:]:
        p[0] += p[2]
        p[1] += p[3]
        p[5] -= 1
        if p[5] <= 0:
            particles.remove(p)
        else:
            alpha = p[5] / 30
            color = tuple(int(c * alpha) for c in p[4])
            pygame.draw.circle(screen, color, (int(p[0]), int(p[1])), 2)

    # HUD
    font = pygame.font.Font(None, 30)
    info = [
        f"Estrelas: {len(stars)}",
        f"Buracos negros: {len(blackholes)}",
        "",
        "Clique esquerdo: Criar buraco negro",
        "Clique direito: Explosão repulsiva",
        "ESPAÇO: Adicionar estrelas",
        "R: Reset | ESC: Sair"
    ]

    for i, text in enumerate(info):
        surface = font.render(text, True, (100, 100, 120))
        screen.blit(surface, (20, 20 + i * 25))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
