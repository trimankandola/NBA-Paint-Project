from pygame import *
screen = display.set_mode((1200,900))
canvasRect = Rect(0,0,1000,700)
running =True
screen.fill((255,255,255))
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        img=image.load("Cavaliers\\BP2.jpg")
        img2=transform.scale(img,(1000,700))
        image.save(img2,"Cavaliers\\BP2.png")
    
    running=False


    display.flip()
quit()
