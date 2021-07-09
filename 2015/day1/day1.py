file = open('input.txt', 'r')
floor = 0
position = 0

def elevator():
    global floor, position
    
    for i in file.read():
        if i == '(':
            floor += 1
        else:
            floor -= 1
    print('Final floor:', floor)
    
def elevator_basement_stop():
    global floor, position
    
    for i in file.read():
        if i == '(':
            floor += 1
            position += 1
            if floor == -1:
                break
        else:
            floor -= 1
            position += 1
            if floor == -1:
                break
    print('current floor:', floor)
    print('current position:', position)

#elevator()
#elevator_basement_stop()
