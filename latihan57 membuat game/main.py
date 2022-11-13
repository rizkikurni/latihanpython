import pygame

    # struktur membuat game

        # init
        # user input, database input
        # upadate asset
        # render ke display

# init
pygame.init()

# membuat display surface object
window = pygame.display.set_mode((500,500))

# variable running
isRun = True

# object game
    # posisi 
x = 250
y = 250

    # ukuran
panjang = 20
lebar = 20

    # kecepatan gerak
speed = 0.7

while isRun:
    # user input, database input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False

    # ambil semua keyboard press
    keys = pygame.key.get_pressed()

    #ambil kiri
    if keys[pygame.K_LEFT] and x > 0: 
        x -= speed

    # ambil kanan
    if keys[pygame.K_RIGHT] and x < 480: 
        x += speed

    # ambil atas
    if keys[pygame.K_UP] and y > 0: 
        y -= speed

    # ambil bawah
    if keys[pygame.K_DOWN] and y < 480: 
        y += speed
    # upate asset
    window.fill((255,255,255))
    pygame.draw.rect(window,(120,50,80),(x,y,lebar,panjang))

    # render ke display
    pygame.display.update()
pygame.QUIT


    