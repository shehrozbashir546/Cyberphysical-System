#Field is providing a testmap
field = []
trash_cnt = 0
#Initialize field
for i in range(1, 901):
    if(i%20==0):
        field.append("+")
        trash_cnt+=1
    else:
        field.append("#")
    print(field[i-1], end = " ")
    if(i%30==0):
        print()

print(f"Trash: {trash_cnt}")

#Put everything that should stay in here
whitelist = ["#"]
rows, cols = (30, 30)
#Fieldmap: G = pick up that garbage of a plant!, P = will be processed by Remover, F = there was garbage
fieldmap = [[0]*cols]*rows

def Field_Content(x, y):
    #return name of image
    return field[y*30+x]

#start x, start y, finish x, finish y (Remember: The drone flies back and forth!)
def Inspector(sx, sy, fx, fy):
    x = sx
    y = sy
    fly_right = True
    delete_cnt = 0
    go = False
    moved_distance = 1
    while not go:
        if not(Field_Content(x,y) in whitelist):
            fieldmap[x][y]="G"
            delete_cnt+=1
            #print(f"{delete_cnt} x: {x} y: {y}")
        if(fly_right):
            x+=1
            if(x==30):
                x=29
                y+=1
                fly_right = False
        else:
            x-=1
            if(x==-1):
                x=0
                y+=1
                fly_right = True
        moved_distance += 1
        if (x==fx and y==fy):
            go = True

    print(f"Finished at x: {x} y: {y} by moving {moved_distance} fields. {delete_cnt} plants had been marked as trash.")

Inspector(0, 0, 0, 29)