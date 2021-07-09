file = open('input.txt', 'r')
data = file.read().split()

total_area = 0
total_ribbon = 0

def get_dimensions(row):
    dimensions = row.split('x')
    return dimensions

def get_area_and_slack(dimensions):
    global total_area
    l = int(dimensions[0])
    w = int(dimensions[1])
    h = int(dimensions[2])
    a1 = 2 * l * w
    a2 = 2 * l * h
    a3 = 2 * w * h
    all_sides = [a1, a2, a3]
    area = sum(all_sides)
    slack = int(sorted(all_sides)[0]/2)
    total_area = total_area + area + slack
    
def get_total_area():
    for f in data:
        get_area_and_slack(get_dimensions(f))

get_total_area()
print('Answer 1:', str(total_area))

def get_ribbon_length(dimensions):
    global total_ribbon
    l = int(dimensions[0])
    w = int(dimensions[1])
    h = int(dimensions[2])
    in_order = sorted([l, w, h])
    ribbon = in_order[0] + in_order[0] + in_order[1] + in_order[1]
    bow = l * w * h
    total_ribbon = total_ribbon + ribbon + bow

def get_total_ribbon():
    for f in data:
        get_ribbon_length(get_dimensions(f))

get_total_ribbon()
print('Answer 2:', str(total_ribbon))