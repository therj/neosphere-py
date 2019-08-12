import math
pos = [0, 0]
while True:
    s = input("Up, down, left or right <SPACE> steps (Enter to exit): ")
    if not s:
        break
    movement = s.split(" ")
    direction = movement[0]
    try:
        steps = int(movement[1])
    except (IndexError, ValueError):
        steps = 0
    direction = direction.upper()
    if direction == "UP":
        pos[0] += steps
    elif direction == "DOWN":
        pos[0] -= steps
    elif direction == "LEFT":
        pos[1] -= steps
    elif direction == "RIGHT":
        pos[1] += steps
    else:
        pass

print((math.sqrt(pos[1]**2+pos[0]**2)))
# print(int(round(math.sqrt(pos[1]**2+pos[0]**2))))
