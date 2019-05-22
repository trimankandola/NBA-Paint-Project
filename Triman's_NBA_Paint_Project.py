#Triman Singh Kandola
#This PAINT Program is an NBA theme based program. It allows the user ot play wiht many different types of tools
#and it allows a user to make a picture and save it on thier device.
from pygame import *
from random import *
from math import *
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter.messagebox import *
root = Tk() 
root.withdraw()
screen=display.set_mode((1200,900))
display.set_caption("NBA PAINT PROGRAM")  #Program name
backPic = image.load("splashscreen.png")    #first splash screen
team="none"
screen.blit(backPic,(0,0))    #blitting firt splash screen
#-------------------------------------Program starts-----------------------------------------------
running=True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type==MOUSEBUTTONDOWN:
            backPic = image.load("splashscreen2.png")  #second splash screen
            screen.blit(backPic,(0,0))
            mpos=mouse.get_pos()
#--------------Rect for choosing whatever team you prefer---------
            PHI=Rect(180,200,140,140)
            MIL=Rect(320,200,140,140)
            CHI=Rect(460,200,140,140)
            CLE=Rect(600,200,140,140)
            BOS=Rect(740,200,140,140)
            LAC=Rect(880,200,140,140)
            MEM=Rect(180,340,140,140)
            ATL=Rect(320,340,140,140)
            MIA=Rect(460,340,140,140)
            CHA=Rect(600,340,140,140)
            UTA=Rect(740,340,140,140)
            SAC=Rect(880,340,140,140)
            NYK=Rect(180,480,140,140)
            LAL=Rect(320,480,140,140)
            ORL=Rect(460,480,140,140)
            DAL=Rect(600,480,140,140)
            BKN=Rect(740,480,140,140)
            DEN=Rect(880,480,140,140)
            IND=Rect(180,620,140,140)
            NOP=Rect(320,620,140,140)
            DET=Rect(460,620,140,140)
            TOR=Rect(600,620,140,140)
            HOU=Rect(740,620,140,140)
            SAS=Rect(880,620,140,140)
            PHO=Rect(180,760,140,140)
            OKC=Rect(320,760,140,140)
            MIN=Rect(460,760,140,140)
            POR=Rect(600,760,140,140)
            GSW=Rect(740,760,140,140)
            WAS=Rect(880,760,140,140)
#------------your program layout is based on the NBA team that you have chosen-------------
            if WAS.collidepoint(mpos) and e.type==MOUSEBUTTONDOWN:
                team="Wizards"
                running=False
            elif GSW.collidepoint(mpos) and e.type==MOUSEBUTTONDOWN:
                team="Warriors"
                running=False
            elif POR.collidepoint(mpos) and e.type==MOUSEBUTTONDOWN:
                team="Trailblazers"
                running=False
            elif MIN.collidepoint(mpos) and e.type==MOUSEBUTTONDOWN:
                team="Timberwolves"
                running=False
            elif PHI.collidepoint(mpos) and e.type==MOUSEBUTTONDOWN:
                team="76ers"
                running=False
            elif CHI.collidepoint(mpos) and e.type==MOUSEBUTTONDOWN:
                team="Bulls"
                running=False
            elif OKC.collidepoint(mpos) and e.type==MOUSEBUTTONDOWN:
                team="Thunder"
                running=False
            elif PHO.collidepoint(mpos) and e.type==MOUSEBUTTONDOWN:
                team="Suns"
                running=False
            elif SAS.collidepoint(mpos) and e.type==MOUSEBUTTONDOWN:
                team="Spurs"
                running=False
            elif HOU.collidepoint(mpos) and e.type==MOUSEBUTTONDOWN:
                team="Rockets"
                running=False
            elif TOR.collidepoint(mpos) and e.type==MOUSEBUTTONDOWN:
                team="Raptors"
                running=False
            elif DET.collidepoint(mpos) and e.type==MOUSEBUTTONDOWN:
                team="Pistons"
                running=False
            elif NOP.collidepoint(mpos) and e.type==MOUSEBUTTONDOWN:
                team="Pelicans"
                running=False
            elif IND.collidepoint(mpos) and e.type==MOUSEBUTTONDOWN:
                team="Pacers"
                running=False
            elif DEN.collidepoint(mpos) and e.type==MOUSEBUTTONDOWN:
                team="Nuggets"
                running=False
            elif BKN.collidepoint(mpos) and e.type==MOUSEBUTTONDOWN:
                team="Nets"
                running=False
            elif DAL.collidepoint(mpos) and e.type==MOUSEBUTTONDOWN:
                team="Mavericks"
                running=False
            elif ORL.collidepoint(mpos) and e.type==MOUSEBUTTONDOWN:
                team="Magic"
                running=False
            elif LAL.collidepoint(mpos) and e.type==MOUSEBUTTONDOWN:
                team="Lakers"
                running=False
            elif NYK.collidepoint(mpos) and e.type==MOUSEBUTTONDOWN:
                team="Knicks"
                running=False
            elif SAC.collidepoint(mpos) and e.type==MOUSEBUTTONDOWN:
                team="Kings"
                running=False
            elif UTA.collidepoint(mpos) and e.type==MOUSEBUTTONDOWN:
                team="Jazz"
                running=False
            elif CHA.collidepoint(mpos) and e.type==MOUSEBUTTONDOWN:
                team="Hornets"
                running=False
            elif MIA.collidepoint(mpos) and e.type==MOUSEBUTTONDOWN:
                team="Heat"
                running=False
            elif ATL.collidepoint(mpos) and e.type==MOUSEBUTTONDOWN:
                team="Hawks"
                running=False
            elif MEM.collidepoint(mpos) and e.type==MOUSEBUTTONDOWN:
                team="Grizzlies"
                running=False
            elif LAC.collidepoint(mpos) and e.type==MOUSEBUTTONDOWN:
                team="Clippers"
                running=False
            elif CLE.collidepoint(mpos) and e.type==MOUSEBUTTONDOWN:
                team="Cavaliers"
                running=False
            elif BOS.collidepoint(mpos) and e.type==MOUSEBUTTONDOWN:
                team="Celtics"
                running=False
            elif MIL.collidepoint(mpos) and e.type==MOUSEBUTTONDOWN:
                team="Bucks"
                running=False
    display.flip()
#---------basic back pictures----------------
backPic = image.load(team+"\\Back.png") 
screen.blit(backPic,(0,0))
logoPic = image.load("NBALogo.png")
pg1Pic = image.load("page1.png")
colPic = image.load("colours.png")
bottompage= image.load("bottompage.png")
#-------for each tool there is a show picture which shows up on the top left corner of the program----------
#-------which show the user what tool they are using and what colour is being used for the tool in the program-----------
#-------the tool being used and the colour being used is located at eh top left corner of the program----------
pencil_s = image.load("Tools\\pencil.png")
eraser_s = image.load("Tools\\eraser.png")
paintbrush_s = image.load("Tools\\paintbrush.png")
spraypaint_s = image.load("Tools\\spraypaint.png")
filloval_s = image.load("Tools\\filloval.png")
fillrect_s = image.load("Tools\\fillrect.png")
drawoval_s = image.load("Tools\\drawoval.png")
drawrect_s = image.load("Tools\\drawrect.png")
drawline_s = image.load("Tools\\drawline.png")
floodfill_s = image.load("Tools\\fill.png")
highlighter_s = image.load("Tools\\highlighter.png")
eyedropper_s = image.load("Tools\\eyedropper.png")
clear_s = image.load("Tools\\clear.png")
bchanger_s = image.load("Tools\\bchanger.png")
inverted_s = image.load("Tools\\inverted.png")
pixelated_s = image.load("Tools\\pixelated.png")
bandw_s = image.load("Tools\\b&w.png")
sepia_s = image.load("Tools\\sepia.png")
drawpic_s = image.load("Tools\\drawpic.png")
#-------------Backgorunds-------------------
b1=image.load(team+"\\BP1.png")
b2=image.load(team+"\\BP2.png")
b3=image.load("BP3.png")
b4=image.load("BP4.png")
#--------------Stamps----------------
p1=image.load(team+"\\Pic1.png")
p2=image.load(team+"\\Pic2.png")
p3=image.load(team+"\\Pic3.png")
p4=image.load(team+"\\Pic4.png")
p5=image.load("Pic5.png")
p6=image.load("Pic6.png")
p7=image.load("Pic7.png")
p8=image.load("Pic8.png")
p9=image.load("Pic9.png")
p10=image.load("Pic10.png")
#-------stamplists and rects------------
picrects=[]
pictool=["Pic1","Pic2","Pic3","Pic4","Pic5","Pic6","Pic7","Pic8","Pic9","Pic10"]
pics=[p1,p2,p3,p4,p5,p6,p7,p8,p9,p10]
bpics=[b1,b2,b3,b4]
bspics=[]
bpicrects=[]
bpicx=[]
bpicy=[]
b=["BP1","BP2","BP3","BP4"]
stampic=[]
stampicordx=[]
stampicordy=[]
for backshow in range(len(bpics)):                     #this loop transforms that scale of the image so that it can
    bspic=transform.scale(bpics[backshow],(100,55))    #fit in the display box, and it make the rect for each image
    bspics.append(bspic)                               #there are ten stamps so ther rects, their coordinates are all being stored into sifferent lists accordingly
    if backshow>1:
        bpicx.append(((backshow-2)*100))
        bpicy.append(590)
        bpicrect=Rect(bpicx[backshow],bpicy[backshow],100,55)
        bpicrects.append(bpicrect)
    else:
        bpicx.append(backshow*100)
        bpicy.append(645)
        bpicrect=Rect(bpicx[backshow],bpicy[backshow],100,55)
        bpicrects.append(bpicrect)
for stamp in range(len(pics)):                    #the same thing is done for the Bachgkround images to transform their scale and to put them on display
    stimg=transform.scale(pics[stamp],(89,85))
    stampic.append(stimg)
    if stamp>4:
        stampicordx.append(((stamp-5)*89)+215)
        stampicordy.append(800)
        picrect=Rect(stampicordx[stamp],stampicordy[stamp],89,85)
        picrects.append(picrect)
    else:
        stampicordx.append((stamp*89)+215)
        stampicordy.append(715)
        picrect=Rect(stampicordx[stamp],stampicordy[stamp],89,85)
        picrects.append(picrect)
font.init()
comicFont = font.SysFont("Comic Sans MS", 20)
#---------bltiing all images----------------------
screen.blit(logoPic,(0,0))
screen.blit(pg1Pic,(0,157))
screen.blit(colPic,(0,700))
screen.blit(bottompage,(205,705))
for st in range(len(stampic)):                                   #these two loops puts the different stamps and backgorunds on dsiplay
    screen.blit(stampic[st],(stampicordx[st],stampicordy[st]))
for bt in range (len(bspics)):
    screen.blit(bspics[bt],(bpicx[bt],bpicy[bt]))
running=True
#-----------two functions, both for making sure that the brush/eraser and alpha tool don't produce random cricles----------
def trail(mmx,mmy,oox,ooy,thick,colour):
    dist=hypot(mmx-oox,mmy-ooy)
    dist=int(dist)
    for i in range(dist):
        sx=i*(mmx-oox)//dist
        sy=i*(mmy-ooy)//dist
        draw.circle(screen,colour,(oox+sx,ooy+sy),thick)
def alphatrail(mmx,mmy,oox,ooy,thick,colour):
    dist=hypot(mmx-oox,mmy-ooy)
    dist=int(dist)
    for i in range(dist):
        sx=i*(mmx-oox)//dist
        sy=i*(mmy-ooy)//dist
        draw.circle(cover,colour,(oox+sx,ooy+sy),thick)
'''def fill():
    fx,fy=mouse.get_pos()
    while '''
#----------------making rects for all other tools except for the images and backgrounds--------------------
colshowRect=(102,90,58,47)
pencilRect=Rect(0,188,50,45)
eraserRect=Rect(50,188,50,45)
brushRect=Rect(0,241,50,45)
sprayRect=Rect(50,241,50,45)
fillovalRect=Rect(100,188,50,45)
fillrectRect=Rect(150,188,50,45)
drawovalRect=Rect(100,241,50,45)
drawrectRect=Rect(150,241,50,45)
drawlineRect=Rect(0,296,50,45)
floodfillRect=Rect(50,296,50,45)
eyedropperRect=Rect(150,296,50,45)
highlighterRect=Rect(100,296,50,45)
clearRect=Rect(0,380,100,60)
colorbackRect=Rect(100,380,100,60)
invertedRect=Rect(0,440,100,60)
pixelatedRect=Rect(100,440,100,60)
bandwRect=Rect(0,500,100,60)
sepiaRect=Rect(100,500,100,60)
backRect=Rect(0,590,200,110)
canvasRect=Rect(200,0,1000,700)
colRect=Rect(0,700,200,200)
picboxrect=Rect(215,715,445,170)
saverect=Rect(855,715,60,75)
uploadrect=Rect(915,715,60,75)
undorect=Rect(855,805,60,75)
redorect=Rect(915,805,60,75)
#starting tool is obviously the pencil tool
tool="pencil"
toolpic=pencil_s
#staritng colour is balck
drawColour=(0,0,0)
#undo and redo lists and flags
undolist=[]
redolist=[]
undoredoflag=False
#setting the x and y cordinates for the trail function and pencil tools
oldx,oldy=mouse.get_pos()
thickness=1         #thickness starts at 1
picupflag=False          #upload flag
saveflag=False       #save flag
draw.rect(screen,(255,255,255),canvasRect)   #drawing actual canvas rect
mx,my=mouse.get_pos()
mb=mouse.get_pressed()
#sets the first copy of the undolist as a blank copy, which will be a part of the list
screencopy=screen.subsurface(canvasRect).copy()
undolist.append(screencopy)

#----------real event loop starts
while running:
    for e in event.get():
        if e.type==QUIT:
            running=False
#-----------------I used the event loop only for their selection, and once they are selected, the event loop is exited and it goes through all the tools-------------
#----------------When I say that the event loop is exitted, I don't mean permanently, beacuse it temporarliy exits when the tool is being used---------------------
#---------------Also the tools can only be used if once the tool is selected, use press on the actual canvas-----------------------
        if e.type==MOUSEBUTTONDOWN and e.button==1 and canvasRect.collidepoint(mx,my):
            undoredoflag=True
        if e.type==MOUSEBUTTONUP and canvasRect.collidepoint(mx,my)and undoredoflag==True:
            undolist.append(screen.subsurface(canvasRect).copy())  
            redolist=[]
            undoredoflag=False
        if e.type==MOUSEBUTTONDOWN and e.button==1 and fillovalRect.collidepoint(mx,my):   #oval fill tool selection
            tool="filloval"
            toolpic=filloval_s   #the toolpic variable is used to the select tool feature beacuse when you slect the tool,
            fillovalflag=True    # the toolpic shows up at the top left corner of the program
        if e.type==MOUSEBUTTONDOWN and tool=="filloval":
            fillovalcopy=screen.copy()
        if e.type==MOUSEBUTTONUP and tool=="filloval":
            fillovalflag=True
        if e.type==MOUSEBUTTONDOWN and e.button==1 and fillrectRect.collidepoint(mx,my):    #rectangle fill tool selection
            tool="fillrect"
            toolpic=fillrect_s
            fillrectflag=True
        if e.type==MOUSEBUTTONDOWN and tool=="fillrect":
            fillrectcopy=screen.copy()
        if e.type==MOUSEBUTTONUP and tool=="fillrect":
            fillrectflag=True
        if e.type==MOUSEBUTTONDOWN and e.button==1 and drawovalRect.collidepoint(mx,my):    #oval draw tool selection
            tool="drawoval"
            toolpic=drawoval_s
            drawovalflag=True
        if e.type==MOUSEBUTTONDOWN and tool=="drawoval":
            drawovalcopy=screen.copy()
        if e.type==MOUSEBUTTONUP and tool=="drawoval":
            drawovalflag=True
        if e.type==MOUSEBUTTONDOWN and e.button==1 and drawrectRect.collidepoint(mx,my):    #rect draw tool selection
            tool="drawrect"
            toolpic=drawrect_s
            drawrectflag=True
        if e.type==MOUSEBUTTONDOWN and tool=="drawrect":
            drawrectcopy=screen.copy()
        if e.type==MOUSEBUTTONUP and tool=="drawrect":
            drawrectflag=True
        if clearRect.collidepoint(mx,my) and e.type==MOUSEBUTTONDOWN and e.button==1:      #clear screen tool selection
            tool="clear"
            toolpic=clear_s
        if colorbackRect.collidepoint(mx,my) and e.type==MOUSEBUTTONDOWN and e.button==1:   #change the background to any colour (i know sir, too many words) 
            tool="bchanger"                                                                 #tool selection 
            toolpic=bchanger_s
        if invertedRect.collidepoint(mx,my) and e.type==MOUSEBUTTONDOWN and e.button==1:         #inverted tool slection
            tool="inverted"
            toolpic=inverted_s
        if pixelatedRect.collidepoint(mx,my) and e.type==MOUSEBUTTONDOWN and e.button==1:     #pixelated tool selection
            tool="pixelated"
            toolpic=pixelated_s
        if bandwRect.collidepoint(mx,my) and e.type==MOUSEBUTTONDOWN and e.button==1:    #black and white tool selection
            tool="bandw"
            toolpic=bandw_s
        if sepiaRect.collidepoint(mx,my) and e.type==MOUSEBUTTONDOWN and e.button==1:   #sepia tool selection
            tool="sepia"
            toolpic=sepia_s
        if pencilRect.collidepoint(mx,my) and e.type==MOUSEBUTTONDOWN and e.button==1:   #pencil tool selection
            tool="pencil"
            toolpic=pencil_s
        if eraserRect.collidepoint(mx,my) and e.type==MOUSEBUTTONDOWN and e.button==1:    #eraser tool selection
            tool="eraser"
            toolpic=eraser_s
        if brushRect.collidepoint(mx,my) and e.type==MOUSEBUTTONDOWN and e.button==1:   #brush tool selection
            tool="brush"
            toolpic=paintbrush_s
        if sprayRect.collidepoint(mx,my) and e.type==MOUSEBUTTONDOWN and e.button==1:   #spray tool selection
            tool="spray"
            toolpic=spraypaint_s
        if drawlineRect.collidepoint(mx,my) and e.type==MOUSEBUTTONDOWN and e.button==1:     #line tool selection
            tool="drawline"
            toolpic=drawline_s
            drawlineflag=True
        if e.type==MOUSEBUTTONDOWN and tool=="drawline":
            drawlinecopy=screen.copy()
        if e.type==MOUSEBUTTONUP and tool=="drawline":
            drawlineflag=True
        if floodfillRect.collidepoint(mx,my) and e.type==MOUSEBUTTONDOWN and e.button==1:  # fill tool slection
            tool="floodfill"
            toolpic=floodfill_s
        if eyedropperRect.collidepoint(mx,my) and e.type==MOUSEBUTTONDOWN and e.button==1:   #eyedropper tool selection
            tool="eyedropper"
            toolpic=eyedropper_s
        if highlighterRect.collidepoint(mx,my) and e.type==MOUSEBUTTONDOWN and e.button==1:   #higlighter tool selection
            tool="highlighter"
            toolpic=highlighter_s
            cover = Surface((1200,675)).convert()
            cover.set_alpha(55)
            cover.set_colorkey((255,0,255))
        if tool=="highlighter" and e.type==MOUSEBUTTONUP:
            copy = screen.copy()
            cover.fill((255,0,255))
        if saverect.collidepoint(mx,my) and e.type==MOUSEBUTTONDOWN and e.button==1 and saveflag==False:  #save picture feature selection
            saveflag=True
        if saverect.collidepoint(mx,my) and e.type==MOUSEBUTTONUP and saveflag==True:
            saveflag=False
            fileName = asksaveasfilename(parent=root,title="Save the image as...")
            image.save(screen.subsurface(canvasRect),fileName+".png")
        if uploadrect.collidepoint(mx,my) and e.type==MOUSEBUTTONDOWN and e.button==1 and picupflag==False:  #upload picture feature slection
            picupflag=True
        if uploadrect.collidepoint(mx,my) and e.type==MOUSEBUTTONUP and picupflag==True:
            fileName = askopenfilename(parent=root,title="Open Image:")
            picup=image.load(fileName)
            tool="upload"
            toolpic=drawpic_s
            picupflag=False
            drawpicupflag=True
        if e.type==MOUSEBUTTONDOWN and tool=="upload":
            drawpicupcopy=screen.copy()
        if e.type==MOUSEBUTTONUP and tool=="upload":
            drawpicupflag=True
        if backRect.collidepoint(mx,my):        #all backgorund pictures tool selection, this if statement in the event loop, goes through another
            for l in range(len(bpicrects)):     #for loop which goes thorugh all of the backgorund rect, and if you select any, than it will selct the background
                if bpicrects[l].collidepoint(mx,my) and e.type==MOUSEBUTTONDOWN and e.button==1:
                    tool=b[l]
                    toolpic=drawpic_s
                    print(tool)
        if picboxrect.collidepoint(mx,my):   #basically same thing as the backgorund loop above, but it goes through the fro loop 10 times because there are ten stamps
            for l in range(len(picrects)):
                if picrects[l].collidepoint(mx,my) and e.type==MOUSEBUTTONDOWN and e.button==1:
                    tool=pictool[l]
                    toolpic=drawpic_s
                    drawpicflag=True
                if e.type==MOUSEBUTTONDOWN and tool==pictool[l]:
                    drawpiccopy=screen.copy()
                if e.type==MOUSEBUTTONUP and tool==pictool[l]:
                    drawpicflag=True
        if e.type==MOUSEBUTTONDOWN and e.button==1 and undorect.collidepoint(mx,my):   #undo feature slection
            if len(undolist)>1: #if the undo list has more then 1 copythen 
                redolist.append(undolist.pop())  #then it will append the current copy to the redo list 
                screen.blit((undolist[-1]),(200,0)) #it will blit the last copy in the undo list 
        if e.type==MOUSEBUTTONDOWN and e.button==1 and redorect.collidepoint(mx,my):  #redo featur selection
            if len(redolist)>0:   #if the redo list has at least one copy then
                screen.blit((redolist[-1]),(200,0)) #it blits the last copy in th redo list and append the current copy in the undo list
                undolist.append(redolist.pop())     # it will append the current cpy to the undo list
        if e.type== MOUSEBUTTONDOWN:
            if e.button==4:   #if the mouse scroll button goes up then
                thickness+=1 #increase the thickness by one pixel
            if e.button==5:   #if the scroll button goes down then 
                if thickness>2:  #if the thickness is greater the 2 pixels than 
                    thickness-=1 #decrease the thickness
                else:
                    thickness=1 # and if it is 2 or 1, then keep it as the thickness of 1
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
    screen.blit(toolpic,(40,90))
#-----------------------------------------------features and tools dow real work here, and are not lazy----------------------------------------------------
    if colRect.collidepoint(mx,my) and mb[0]==1:  #colour pallette tool
        drawColour=screen.get_at((mx,my))      #choose any colour and it will show up at the top left corner of the screen
        draw.ellipse(screen,drawColour,colshowRect,0)
    if canvasRect.collidepoint(mx,my) and mb[0]==1: #if your mouse is on the canvas and you are pressing the left button
        screen.set_clip(canvasRect)  #set the screen as the canvas, so that the tools don't go outside of the canvasRect
        if tool=="clear" and mb[0]==1:        #the clear screen tool basically draws a white rectangle on the screen
            draw.rect(screen,(255,255,255),canvasRect)
        elif tool=="bchanger" and mb[0]==1:    #the backgorund changer tool basically lets you select any colour and the backgorund of your canvas becomes that colour
            draw.rect(screen,drawColour,canvasRect)
        elif tool=="inverted" and mb[0]==1: #the inverted colour tool goes through 2 for loops which goes through every single pixels on the screen and  
            for ix in range(200,1200):      #gets the colour value in RGB form  what it does is it sets that pixel as the difference of 255 and the 
                for iy in range(0,700):     #value for the RGB spot
                    icol=screen.get_at((ix,iy))
                    ncol=(255-icol[0],255-icol[1],255-icol[2])
                    screen.set_at((ix,iy),ncol)
                    
        elif tool=="pixelated" and mb[0]==1:  #the pixelated feature is complicated and the number 10 is going to be important because my pixelated effect is 10x10 
            for iy in range(0,690,10):      #goes through 1000 y-axis of pixels by ten pixels each time
               for ix in range(200,1190,10): #goes through the 700 x-axis of pixels by ten each time 
                   icolrs=[]  #r list
                   icolgs=[]  #g list
                   icolbs=[]  #b list
                   for iiy in range(1,11):  #we need the colour at every pixels so we go through
                       for iix in range(1,11): #every pixel and get the RGB values at store it in the lists above
                           icol=screen.get_at((ix+iix,iy+iiy)) 
                           icolrs.append(icol[0])
                           icolgs.append(icol[1])
                           icolbs.append(icol[2])
                           if iiy==10 and iix==10:
                               icolr=int(sum(icolrs)/len(icolrs))    #once it reaches the end of the list it gets the collected values and 
                               icolg=int(sum(icolgs)/len(icolgs))    #it calculates the average and make a rect and sets that rect to those RGB values
                               icolb=int(sum(icolbs)/len(icolbs))
                               draw.rect(screen,(icolr,icolg,icolb),Rect(ix,iy,10,10)) 
        elif tool=="sepia" and mb[0]==1:   #the sepia tool is a tool, but to calculate the RGB values, I had to do some research and find out the formulas to ge them
            for ix in range(200,1200):
                for iy in range(0,700):
                    icol=screen.get_at((ix,iy)) #goes through each pixel
                    oRed = int((icol[0]*0.393) + (icol[1]*0.769) + (icol[2]*0.189))  #formula for red
                    oGreen = int((icol[0]*0.349) + (icol[1]*0.686) + (icol[2]*0.168)) #formula for green
                    oBlue = int((icol[0]*0.272) + (icol[1]*0.534) + (icol[2]*0.131))  #formual for b;ue
                    if oRed>255:  #if any of these values are over 255 (which is max), then it sets it to 255
                        oRed=255
                    if oGreen>255: 
                        oGreen=255
                    if oRed>255:
                        oRed=255
                    screen.set_at((ix,iy),(oRed,oGreen,oBlue)) #and then it sets that pixel ot the value
        elif tool=="bandw" and mb[0]==1:  #the black and white feature is similar and in this feature it goes trough every pixel and finds the average of 
            for ix in range(200,1200):    #the RGB values and sets all three values as the same
                for iy in range(0,700):
                    icol=screen.get_at((ix,iy))
                    imean=int((icol[0]+icol[1]+icol[2])/3)
                    screen.set_at((ix,iy),(imean,imean,imean))
        elif tool=="pencil" and mb[0]==1:      #basic pencil tool using the draw.line feature
            draw.line(screen,drawColour,(oldx,oldy),(mx,my))
        elif tool=="eraser" and mb[0]==1:     #eraser tool using the trail funtion created above
            trail(mx,my,oldx,oldy,thickness,(255,255,255))
        elif tool=="brush" and mb[0]==1:      #brush tool using the trail funtion created above
            trail(mx,my,oldx,oldy,thickness,drawColour)
        elif tool=="eyedropper" and mb[0]==1:  #eyedropper tool is used and the screen.get_at feature is the feature used
            screen.set_clip(None)
            ecol=screen.get_at((mx,my))
            drawColour=ecol
            draw.ellipse(screen,drawColour,colshowRect,0)
            screen.set_clip(canvasRect)
        elif tool=="highlighter" and mb[0]==1:  #the highlighter tool uses the alpha trail function
            alphatrail(mx,my,oldx,oldy,thickness,drawColour)
            screen.blit(copy,(0,0))
            screen.blit(cover,(0,0))
        elif tool=="spray" and mb[0]==1:     #spray paint feature just makes sure that the random points are put within a cicle
            spx=randint(mx-int(thickness),mx+int(thickness))
            spy=randint(my-int(thickness),my+int(thickness))
            if hypot(mx-spx,my-spy)<thickness:
                draw.circle(screen,drawColour,(spx,spy),int(0.9))
        elif tool=="BP1" and mb[0]==1:      #all four backgorunds just blit on the screen at the same place
            screen.blit(bpics[0],(200,0))
        elif tool=="BP2" and mb[0]==1:
            screen.blit(bpics[1],(200,0))
        elif tool=="BP3" and mb[0]==1:
            screen.blit(bpics[2],(200,0))
        elif tool=="BP4" and mb[0]==1:
            screen.blit(bpics[3],(200,0))
#----------------------------------------------drawing and filling rects and ovals----------------------------------------
        elif tool=="filloval" and mb[0]==1:   #fill oval tool
            screen.blit(fillovalcopy,(0,0))
            if fillovalflag==True:
                ox,oy=mx,my #when the flag above is set to true, it records the very first mouse position
                fillovalflag=False
            else:
                if mx<ox and my<oy and mb[0]==1:   #these if statements basically find which values are bigger between the orginal mouse positions
                    rect=Rect(mx,my,ox-mx,oy-my)   #and the new ones and use those to fidn the distance and draw the rect that certain way
                elif mx>ox and my<oy and mb[0]==1: #all of the features are the same for the rest of the Rects
                    rect=Rect(ox,my,mx-ox,oy-my)
                elif mx<ox and my>oy and mb[0]==1:
                    rect=Rect(mx,oy,ox-mx,my-oy)
                elif mx>ox and my>oy and mb[0]==1:
                    rect=Rect(ox,oy,mx-ox,my-oy)
                elif mb[0]!=1:
                    fillovalflag=True
                    ox,oy=mx,my
                else:
                    rect=Rect(mx,my,0,0)
                draw.ellipse(screen,drawColour,rect,0)
        elif tool=="fillrect" and mb[0]==1:   #fill rect tool
            screen.blit(fillrectcopy,(0,0))
            if fillrectflag==True:
                ox,oy=mx,my
                fillrectflag=False
            else:
                if mx<ox and my<oy and mb[0]==1:
                    rect=Rect(mx,my,ox-mx,oy-my)
                elif mx>ox and my<oy and mb[0]==1:
                    rect=Rect(ox,my,mx-ox,oy-my)
                elif mx<ox and my>oy and mb[0]==1:
                    rect=Rect(mx,oy,ox-mx,my-oy)
                elif mx>ox and my>oy and mb[0]==1:
                    rect=Rect(ox,oy,mx-ox,my-oy)
                elif mb[0]!=1:
                    fillrectflag=True
                    ox,oy=mx,my
                else:
                    rect=Rect(mx,my,0,0)
                draw.rect(screen,drawColour,rect,0)
        elif tool=="drawoval" and mb[0]==1:        #draw oval tool
            screen.blit(drawovalcopy,(0,0))
            if drawovalflag==True:
                ox,oy=mx,my
                drawovalflag=False
            else:
                if mx<ox and my<oy and mb[0]==1:
                    rect=Rect(mx,my,ox-mx,oy-my)
                elif mx>ox and my<oy and mb[0]==1:
                    rect=Rect(ox,my,mx-ox,oy-my)
                elif mx<ox and my>oy and mb[0]==1:
                    rect=Rect(mx,oy,ox-mx,my-oy)
                elif mx>ox and my>oy and mb[0]==1:
                    rect=Rect(ox,oy,mx-ox,my-oy)
                elif mb[0]!=1:
                    drawovalflag=True
                    ox,oy=mx,my
                else:
                    rect=Rect(mx,my,0,0)
                if thickness*2>max(mx,ox)-min(mx,ox) or thickness*2>max(my,oy)-min(mx,oy): #the only difference between the draw feature is setting is to manual
                    draw.ellipse(screen,drawColour,rect,0)                                 #thickness
                else:
                    draw.ellipse(screen,drawColour,rect,thickness)
        elif tool=="drawrect" and mb[0]==1:  #draw rect tool
            screen.blit(drawrectcopy,(0,0))
            if drawrectflag==True:
                ox,oy=mx,my
                drawrectflag=False
            else:
                if mx<ox and my<oy and mb[0]==1:
                    rect=Rect(mx,my,ox-mx,oy-my)
                elif mx>ox and my<oy and mb[0]==1:
                    rect=Rect(ox,my,mx-ox,oy-my)
                elif mx<ox and my>oy and mb[0]==1:
                    rect=Rect(mx,oy,ox-mx,my-oy)
                elif mx>ox and my>oy and mb[0]==1:
                    rect=Rect(ox,oy,mx-ox,my-oy)
                elif mb[0]!=1:
                    drawrectflag=True
                    ox,oy=mx,my
                else:
                    rect=Rect(mx,my,0,0)
                draw.rect(screen,drawColour,rect,thickness)
                draw.line(screen,drawColour,(ox-thickness//2,oy-thickness//2),(ox+max(mx-ox,ox-mx)+thickness//2,oy-thickness//2),thickness)
                draw.line(screen,drawColour,(ox-thickness//2,my+thickness//2),(mx+thickness//2,my+thickness//2),thickness)
        elif tool=="drawline" and mb[0]==1:#draw line tool just draws a trail from the original position to the new, which is a straight line, so i used the trail 
            screen.blit(drawlinecopy,(0,0))#function
            if drawlineflag==True:
                ox,oy=mx,my
                drawlineflag=False
            else:
                draw.line(screen,drawColour,(ox,oy),(mx,my))
                trail(mx,my,ox,oy,thickness,drawColour)
#-----------------------------------------blitting stamps and uploading pics-----------------------------------------------
        elif tool=="Pic1" and mb[0]==1:  #this feature is just like the draw rects feature and you can draw your and resize them all you want
            screen.blit(drawpiccopy,(0,0)) #to use the stamps again you must press on the stamp rect again, because the resize feature is set that specific way
            if drawpicflag==True:
                ox,oy=mx,my
                drawpicflag=False
            else:
                if mx<ox and my<oy and mb[0]==1:
                    picimg=transform.scale(pics[0],(ox-mx,oy-my))
                    picx,picy=mx,my
                    rect=Rect(mx,my,ox-mx,oy-my)
                elif mx>ox and my<oy and mb[0]==1:
                    picimg=transform.scale(pics[0],(mx-ox,oy-my))
                    picx,picy=ox,my
                    rect=Rect(ox,my,mx-ox,oy-my)
                elif mx<ox and my>oy and mb[0]==1:
                    picimg=transform.scale(pics[0],(ox-mx,my-oy))
                    picx,picy=mx,oy
                    rect=Rect(mx,oy,ox-mx,my-oy)
                elif mx>ox and my>oy and mb[0]==1:
                    picimg=transform.scale(pics[0],(mx-ox,my-oy))
                    picx,picy=ox,oy
                    rect=Rect(ox,oy,mx-ox,my-oy)
                elif mb[0]!=1:
                    drawpicflag=True
                    ox,oy=mx,my
                else:
                    picimg=transform.scale(pics[0],(0,0))
                    picx,picy=mx,my
                    rect=Rect(mx,my,0,0)
                screen.blit(picimg,(picx,picy))
        elif tool=="Pic2" and mb[0]==1:
            screen.blit(drawpiccopy,(0,0))
            if drawpicflag==True:
                ox,oy=mx,my
                drawpicflag=False
            else:
                if mx<ox and my<oy and mb[0]==1:
                    picimg=transform.scale(pics[1],(ox-mx,oy-my))
                    picx,picy=mx,my
                    rect=Rect(mx,my,ox-mx,oy-my)
                elif mx>ox and my<oy and mb[0]==1:
                    picimg=transform.scale(pics[1],(mx-ox,oy-my))
                    picx,picy=ox,my
                    rect=Rect(ox,my,mx-ox,oy-my)
                elif mx<ox and my>oy and mb[0]==1:
                    picimg=transform.scale(pics[1],(ox-mx,my-oy))
                    picx,picy=mx,oy
                    rect=Rect(mx,oy,ox-mx,my-oy)
                elif mx>ox and my>oy and mb[0]==1:
                    picimg=transform.scale(pics[1],(mx-ox,my-oy))
                    picx,picy=ox,oy
                    rect=Rect(ox,oy,mx-ox,my-oy)
                elif mb[0]!=1:
                    drawpicflag=True
                    ox,oy=mx,my
                else:
                    picimg=transform.scale(pics[1],(0,0))
                    picx,picy=mx,my
                    rect=Rect(mx,my,0,0)
                screen.blit(picimg,(picx,picy))
        elif tool=="Pic3" and mb[0]==1:
            screen.blit(drawpiccopy,(0,0))
            if drawpicflag==True:
                ox,oy=mx,my
                drawpicflag=False
            else:
                if mx<ox and my<oy and mb[0]==1:
                    picimg=transform.scale(pics[2],(ox-mx,oy-my))
                    picx,picy=mx,my
                    rect=Rect(mx,my,ox-mx,oy-my)
                elif mx>ox and my<oy and mb[0]==1:
                    picimg=transform.scale(pics[2],(mx-ox,oy-my))
                    picx,picy=ox,my
                    rect=Rect(ox,my,mx-ox,oy-my)
                elif mx<ox and my>oy and mb[0]==1:
                    picimg=transform.scale(pics[2],(ox-mx,my-oy))
                    picx,picy=mx,oy
                    rect=Rect(mx,oy,ox-mx,my-oy)
                elif mx>ox and my>oy and mb[0]==1:
                    picimg=transform.scale(pics[2],(mx-ox,my-oy))
                    picx,picy=ox,oy
                    rect=Rect(ox,oy,mx-ox,my-oy)
                elif mb[0]!=1:
                    drawpicflag=True
                    ox,oy=mx,my
                else:
                    picimg=transform.scale(pics[2],(0,0))
                    picx,picy=mx,my
                    rect=Rect(mx,my,0,0)
                screen.blit(picimg,(picx,picy))
        elif tool=="Pic4" and mb[0]==1:
            screen.blit(drawpiccopy,(0,0))
            if drawpicflag==True:
                ox,oy=mx,my
                drawpicflag=False
            else:
                if mx<ox and my<oy and mb[0]==1:
                    picimg=transform.scale(pics[3],(ox-mx,oy-my))
                    picx,picy=mx,my
                    rect=Rect(mx,my,ox-mx,oy-my)
                elif mx>ox and my<oy and mb[0]==1:
                    picimg=transform.scale(pics[3],(mx-ox,oy-my))
                    picx,picy=ox,my
                    rect=Rect(ox,my,mx-ox,oy-my)
                elif mx<ox and my>oy and mb[0]==1:
                    picimg=transform.scale(pics[3],(ox-mx,my-oy))
                    picx,picy=mx,oy
                    rect=Rect(mx,oy,ox-mx,my-oy)
                elif mx>ox and my>oy and mb[0]==1:
                    picimg=transform.scale(pics[3],(mx-ox,my-oy))
                    picx,picy=ox,oy
                    rect=Rect(ox,oy,mx-ox,my-oy)
                elif mb[0]!=1:
                    drawpicflag=True
                    ox,oy=mx,my
                else:
                    picimg=transform.scale(pics[3],(0,0))
                    picx,picy=mx,my
                    rect=Rect(mx,my,0,0)
                screen.blit(picimg,(picx,picy))
        elif tool=="Pic5" and mb[0]==1:
            screen.blit(drawpiccopy,(0,0))
            if drawpicflag==True:
                ox,oy=mx,my
                drawpicflag=False
            else:
                if mx<ox and my<oy and mb[0]==1:
                    picimg=transform.scale(pics[4],(ox-mx,oy-my))
                    picx,picy=mx,my
                    rect=Rect(mx,my,ox-mx,oy-my)
                elif mx>ox and my<oy and mb[0]==1:
                    picimg=transform.scale(pics[4],(mx-ox,oy-my))
                    picx,picy=ox,my
                    rect=Rect(ox,my,mx-ox,oy-my)
                elif mx<ox and my>oy and mb[0]==1:
                    picimg=transform.scale(pics[4],(ox-mx,my-oy))
                    picx,picy=mx,oy
                    rect=Rect(mx,oy,ox-mx,my-oy)
                elif mx>ox and my>oy and mb[0]==1:
                    picimg=transform.scale(pics[4],(mx-ox,my-oy))
                    picx,picy=ox,oy
                    rect=Rect(ox,oy,mx-ox,my-oy)
                elif mb[0]!=1:
                    drawpicflag=True
                    ox,oy=mx,my
                else:
                    picimg=transform.scale(pics[4],(0,0))
                    picx,picy=mx,my
                    rect=Rect(mx,my,0,0)
                screen.blit(picimg,(picx,picy))
        elif tool=="Pic6" and mb[0]==1:
            screen.blit(drawpiccopy,(0,0))
            if drawpicflag==True:
                ox,oy=mx,my
                drawpicflag=False
            else:
                if mx<ox and my<oy and mb[0]==1:
                    picimg=transform.scale(pics[5],(ox-mx,oy-my))
                    picx,picy=mx,my
                    rect=Rect(mx,my,ox-mx,oy-my)
                elif mx>ox and my<oy and mb[0]==1:
                    picimg=transform.scale(pics[5],(mx-ox,oy-my))
                    picx,picy=ox,my
                    rect=Rect(ox,my,mx-ox,oy-my)
                elif mx<ox and my>oy and mb[0]==1:
                    picimg=transform.scale(pics[5],(ox-mx,my-oy))
                    picx,picy=mx,oy
                    rect=Rect(mx,oy,ox-mx,my-oy)
                elif mx>ox and my>oy and mb[0]==1:
                    picimg=transform.scale(pics[5],(mx-ox,my-oy))
                    picx,picy=ox,oy
                    rect=Rect(ox,oy,mx-ox,my-oy)
                elif mb[0]!=1:
                    drawpicflag=True
                    ox,oy=mx,my
                else:
                    picimg=transform.scale(pics[5],(0,0))
                    picx,picy=mx,my
                    rect=Rect(mx,my,0,0)
                screen.blit(picimg,(picx,picy))
        elif tool=="Pic7" and mb[0]==1:
            screen.blit(drawpiccopy,(0,0))
            if drawpicflag==True:
                ox,oy=mx,my
                drawpicflag=False
            else:
                if mx<ox and my<oy and mb[0]==1:
                    picimg=transform.scale(pics[6],(ox-mx,oy-my))
                    picx,picy=mx,my
                    rect=Rect(mx,my,ox-mx,oy-my)
                elif mx>ox and my<oy and mb[0]==1:
                    picimg=transform.scale(pics[6],(mx-ox,oy-my))
                    picx,picy=ox,my
                    rect=Rect(ox,my,mx-ox,oy-my)
                elif mx<ox and my>oy and mb[0]==1:
                    picimg=transform.scale(pics[6],(ox-mx,my-oy))
                    picx,picy=mx,oy
                    rect=Rect(mx,oy,ox-mx,my-oy)
                elif mx>ox and my>oy and mb[0]==1:
                    picimg=transform.scale(pics[6],(mx-ox,my-oy))
                    picx,picy=ox,oy
                    rect=Rect(ox,oy,mx-ox,my-oy)
                elif mb[0]!=1:
                    drawpicflag=True
                    ox,oy=mx,my
                else:
                    picimg=transform.scale(pics[6],(0,0))
                    picx,picy=mx,my
                    rect=Rect(mx,my,0,0)
                screen.blit(picimg,(picx,picy))
        elif tool=="Pic8" and mb[0]==1:
            screen.blit(drawpiccopy,(0,0))
            if drawpicflag==True:
                ox,oy=mx,my
                drawpicflag=False
            else:
                if mx<ox and my<oy and mb[0]==1:
                    picimg=transform.scale(pics[7],(ox-mx,oy-my))
                    picx,picy=mx,my
                    rect=Rect(mx,my,ox-mx,oy-my)
                elif mx>ox and my<oy and mb[0]==1:
                    picimg=transform.scale(pics[7],(mx-ox,oy-my))
                    picx,picy=ox,my
                    rect=Rect(ox,my,mx-ox,oy-my)
                elif mx<ox and my>oy and mb[0]==1:
                    picimg=transform.scale(pics[7],(ox-mx,my-oy))
                    picx,picy=mx,oy
                    rect=Rect(mx,oy,ox-mx,my-oy)
                elif mx>ox and my>oy and mb[0]==1:
                    picimg=transform.scale(pics[7],(mx-ox,my-oy))
                    picx,picy=ox,oy
                    rect=Rect(ox,oy,mx-ox,my-oy)
                elif mb[0]!=1:
                    drawpicflag=True
                    ox,oy=mx,my
                else:
                    picimg=transform.scale(pics[7],(0,0))
                    picx,picy=mx,my
                    rect=Rect(mx,my,0,0)
                screen.blit(picimg,(picx,picy))
        elif tool=="Pic9" and mb[0]==1:
            screen.blit(drawpiccopy,(0,0))
            if drawpicflag==True:
                ox,oy=mx,my
                drawpicflag=False
            else:
                if mx<ox and my<oy and mb[0]==1:
                    picimg=transform.scale(pics[8],(ox-mx,oy-my))
                    picx,picy=mx,my
                    rect=Rect(mx,my,ox-mx,oy-my)
                elif mx>ox and my<oy and mb[0]==1:
                    picimg=transform.scale(pics[8],(mx-ox,oy-my))
                    picx,picy=ox,my
                    rect=Rect(ox,my,mx-ox,oy-my)
                elif mx<ox and my>oy and mb[0]==1:
                    picimg=transform.scale(pics[8],(ox-mx,my-oy))
                    picx,picy=mx,oy
                    rect=Rect(mx,oy,ox-mx,my-oy)
                elif mx>ox and my>oy and mb[0]==1:
                    picimg=transform.scale(pics[8],(mx-ox,my-oy))
                    picx,picy=ox,oy
                    rect=Rect(ox,oy,mx-ox,my-oy)
                elif mb[0]!=1:
                    drawpicflag=True
                    ox,oy=mx,my
                else:
                    picimg=transform.scale(pics[8],(0,0))
                    picx,picy=mx,my
                    rect=Rect(mx,my,0,0)
                screen.blit(picimg,(picx,picy))
        elif tool=="Pic10" and mb[0]==1:
            screen.blit(drawpiccopy,(0,0))
            if drawpicflag==True:
                ox,oy=mx,my
                drawpicflag=False
            else:
                if mx<ox and my<oy and mb[0]==1:
                    picimg=transform.scale(pics[9],(ox-mx,oy-my))
                    picx,picy=mx,my
                    rect=Rect(mx,my,ox-mx,oy-my)
                elif mx>ox and my<oy and mb[0]==1:
                    picimg=transform.scale(pics[9],(mx-ox,oy-my))
                    picx,picy=ox,my
                    rect=Rect(ox,my,mx-ox,oy-my)
                elif mx<ox and my>oy and mb[0]==1:
                    picimg=transform.scale(pics[9],(ox-mx,my-oy))
                    picx,picy=mx,oy
                    rect=Rect(mx,oy,ox-mx,my-oy)
                elif mx>ox and my>oy and mb[0]==1:
                    picimg=transform.scale(pics[9],(mx-ox,my-oy))
                    picx,picy=ox,oy
                    rect=Rect(ox,oy,mx-ox,my-oy)
                elif mb[0]!=1:
                    drawpicflag=True
                    ox,oy=mx,my
                else:
                    picimg=transform.scale(pics[9],(0,0))
                    picx,picy=mx,my
                    rect=Rect(mx,my,0,0)
                screen.blit(picimg,(picx,picy))
#------------------------upload------------------------------------------
        elif tool=="upload" and mb[0]==1:   #same as rect and other pics
            screen.blit(drawpicupcopy,(0,0))
            if drawpicupflag==True:
                ox,oy=mx,my
                drawpicupflag=False
            else:
                if mx<ox and my<oy and mb[0]==1:
                    picimg=transform.scale(picup,(ox-mx,oy-my))
                    picx,picy=mx,my
                    rect=Rect(mx,my,ox-mx,oy-my)
                elif mx>ox and my<oy and mb[0]==1:
                    picimg=transform.scale(picup,(mx-ox,oy-my))
                    picx,picy=ox,my
                    rect=Rect(ox,my,mx-ox,oy-my)
                elif mx<ox and my>oy and mb[0]==1:
                    picimg=transform.scale(picup,(ox-mx,my-oy))
                    picx,picy=mx,oy
                    rect=Rect(mx,oy,ox-mx,my-oy)
                elif mx>ox and my>oy and mb[0]==1:
                    picimg=transform.scale(picup,(mx-ox,my-oy))
                    picx,picy=ox,oy
                    rect=Rect(ox,oy,mx-ox,my-oy)
                elif mb[0]!=1:
                    drawpicupflag=True
                    ox,oy=mx,my
                else:
                    picimg=transform.scale(picup,(0,0))
                    picx,picy=mx,my
                    rect=Rect(mx,my,0,0)
                screen.blit(picimg,(picx,picy))
#--------------------------------flood fill---------------------------------------
        elif tool=="floodfill" and mb[0]==1:
            mx,my=mouse.get_pos() #gets the mouse position
            ncol=drawColour
            ocol=screen.get_at((mx,my)) #gets the old colour
            if ocol != ncol:  
                cords = [[mx,my]] #starts the cord list 
            while len(cords) > 0:
                cx,cy=cords.pop()#takes the last value form the list and returns it
                try:
                    if canvasRect.collidepoint(mx,my) and screen.get_at((cx,cy))==ocol: #checks if you are on the canvas
                        screen.set_at((cx,cy), ncol)
                        cords.append((cx-1,cy)) #adds four cords, the value on top, beside, over and under it
                        cords.append((cx+1,cy))
                        cords.append((cx,cy-1))
                        cords.append((cx,cy+1))
                except IndexError: #if the flood fill toll goes out of the canvas, this fixes the problem 
                   pass 

    screen.set_clip(None)
    oldx,oldy=mx,my
    print(mx,",",my)
    display.flip()
quit()
