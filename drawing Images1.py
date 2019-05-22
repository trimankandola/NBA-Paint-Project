from pygame import *
screen = display.set_mode((1200,900))
backPic = image.load("Celtics\\Back.png")
logoPic = image.load("NBALogo.png")
pg1Pic = image.load("page1.png")
colPic = image.load("colours.png")
pencil_s = image.load("Tools\pencil.png")
bottompage= image.load("bottompage.png")
b1=image.load("76ers\\BP1.png")
b2=image.load("76ers\\BP2.png")
b3=image.load("BP3.png")
b4=image.load("BP4.png")
p1=image.load("76ers\\Pic1.png")
p2=image.load("76ers\\Pic2.png")
p3=image.load("76ers\\Pic3.png")
p4=image.load("76ers\\Pic4.png")
p5=image.load("Pic5.png")
p6=image.load("Pic6.png")
p7=image.load("Pic7.png")
p8=image.load("Pic8.png")
p9=image.load("Pic9.png")
p10=image.load("Pic10.png")
bpics=[b1,b2,b3,b4]
bspics=[]
bpicx=[]
bpicy=[]
pics=[p1,p2,p3,p4,p5,p6,p7,p8,p9,p10]
stampic=[]
stampicordx=[]
stampicordy=[]
for backshow in range(len(bpics)):
    bspic=transform.scale(bpics[backshow],(100,55))
    bspics.append(bspic)
    if backshow>1:
        bpicx.append(((backshow-2)*100))
        bpicy.append(590)
    else:
        bpicx.append(backshow*100)
        bpicy.append(645)
for stamp in range(len(pics)):
    stimg=transform.scale(pics[stamp],(89,85))
    stampic.append(stimg)
    if stamp>4:
        stampicordx.append(((stamp-5)*89)+215)
        stampicordy.append(800)
    else:
        stampicordx.append((stamp*89)+215)
        stampicordy.append(715)
screen.blit(backPic,(0,0))
font.init()
comicFont = font.SysFont("Comic Sans MS", 20)
canvasRect=Rect(200,0,1000,700)
draw.rect(screen,(255,255,255),canvasRect)
screen.blit(backPic,(0,0))
screen.blit(logoPic,(0,0))
screen.blit(pg1Pic,(0,157))
screen.blit(colPic,(0,700))
screen.blit(pencil_s,(40,90))
screen.blit(bottompage,(205,705))
for st in range(len(stampic)):
    screen.blit(stampic[st],(stampicordx[st],stampicordy[st]))
for bt in range (len(bspics)):
    screen.blit(bspics[bt],(bpicx[bt],bpicy[bt]))
running =True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        mx,my = mouse.get_pos()
        
        draw.rect(screen,(255,255,255),canvasRect)
        txtPic1 = comicFont.render(str(mx), True, (255,0,0))
        txtPic2 = comicFont.render(str(my), True, (255,0,0))
        screen.blit(txtPic1,(200,0))
        screen.blit(txtPic2,(200,200))
    display.flip()
quit()
'''
dist=hypot(mx-oldx,my-oldy)
            dist=int(dist)
            for i in range(dist):
                sx=i*(mx-oldx)//dist
                sy=i*(my-oldy)//dist
                draw.circle(screen,(255,255,255),(oldx+sx,oldy+sy),thickness)
'''
