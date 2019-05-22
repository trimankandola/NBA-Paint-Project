canvas
height
width
old # color to change
new # new color to fill
mx,my

if old != new:
    coords = [[mx,my]]
    while len(coords) > 0:
        x,y coods.pop()
        if x>0 and y>0 and x<width and y<height and canvas.get_at((x,y))==old:
            canvas.set_at((x,y), new)
            coords.append((x-1,y))
            coords.append((x+1,y))
            coords.append((x,y-1))
            coords.append((x,y+1))
    
