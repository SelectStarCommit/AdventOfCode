file = open('input.txt', 'r')
data = file.read()
sample = '^>v<^^<v>'

current_location = [0, 0]
present_dropped = []
present_count = 0
santa_location = [0, 0]
robo_santa_location = [0, 0]

def make_position(location):
    global present_count
    position = str(location[0]) + '.' + str(location[1])
    if position not in present_dropped:
        present_dropped.append(position)
        present_count += 1
    else:
        return None

def navigate():
    global current_location
    make_position(current_location)
    for char in data:
        if char == '^':
            current_location[1] += 1
            make_position(current_location)
        elif char == 'v':
            current_location[1] -= 1
            make_position(current_location)
        elif char == '>':
            current_location[0] += 1
            make_position(current_location)
        else:
            current_location[0] -= 1
            make_position(current_location)

#navigate()
#print('Answer 1:', present_count)

def navigate_alternate():
    global current_location, santa_location, robo_santa_location
    make_position(current_location)
    santa_switch = 1
    for char in data:
        if char == '^':
            current_location[1] += 1
            if santa_switch == 1:
                make_position(santa_location)
                santa_switch = 0
            else:
                make_position(robo_santa_location)
                santa_switch = 1
        elif char == 'v':
            current_location[1] -= 1
            if santa_switch == 1:
                make_position(santa_location)
                santa_switch = 0
            else:
                make_position(robo_santa_location)
                santa_switch = 1
        elif char == '>':
            current_location[0] += 1
            if santa_switch == 1:
                make_position(santa_location)
                santa_switch = 0
            else:
                make_position(robo_santa_location)
                santa_switch = 1
        else:
            current_location[0] -= 1
            if santa_switch == 1:
                make_position(santa_location)
                santa_switch = 0
            else:
                make_position(robo_santa_location)
                santa_switch = 1

navigate_alternate()
print('Answer 2:', present_count)