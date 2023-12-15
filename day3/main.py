import tools

schematic = tools.fetch_input('https://adventofcode.com/2023/day/3/input')

lines_of_schematic = tools.split_by_line(schematic)


def has_symbol_adj(x: int, y: int, l: int) -> bool:
    # print('x:' + str(x) + ' y:' + str(y))
    if y == 0:
        if x == 0:
            if (lines_of_schematic[y][x + 1] != '.' and not lines_of_schematic[y][x + 1].isnumeric() or
                    lines_of_schematic[y + 1][x] != '.' and not lines_of_schematic[y + 1][x].isnumeric() or
                    lines_of_schematic[y + 1][x + 1] != '.' and not lines_of_schematic[y + 1][x + 1].isnumeric()):
                return True
        elif x == l:
            if (lines_of_schematic[y][x - 1] != '.' and not lines_of_schematic[y][x - 1].isnumeric() or
                    lines_of_schematic[y + 1][x - 1] != '.' and not lines_of_schematic[y + 1][x - 1].isnumeric() or
                    lines_of_schematic[y + 1][x] != '.' and not lines_of_schematic[y + 1][x].isnumeric()):
                return True
        elif (lines_of_schematic[y][x - 1] != '.' and not lines_of_schematic[y][x - 1].isnumeric() or
              lines_of_schematic[y][x + 1] != '.' and not lines_of_schematic[y][x + 1].isnumeric() or
              lines_of_schematic[y + 1][x - 1] != '.' and not lines_of_schematic[y + 1][x - 1].isnumeric() or
              lines_of_schematic[y + 1][x] != '.' and not lines_of_schematic[y + 1][x].isnumeric() or
              lines_of_schematic[y + 1][x + 1] != '.' and not lines_of_schematic[y + 1][x + 1].isnumeric()):
            return True
    elif y == len(lines_of_schematic) - 1:
        if x == 0:
            if (lines_of_schematic[y][x + 1] != '.' and not lines_of_schematic[y][x + 1].isnumeric() or
                    lines_of_schematic[y - 1][x] != '.' and not lines_of_schematic[y - 1][x].isnumeric() or
                    lines_of_schematic[y - 1][x + 1] != '.' and not lines_of_schematic[y - 1][x + 1].isnumeric()):
                return True
        elif x == l:
            if (lines_of_schematic[y][x - 1] != '.' and not lines_of_schematic[y][x - 1].isnumeric() or
                    lines_of_schematic[y - 1][x - 1] != '.' and not lines_of_schematic[y - 1][x - 1].isnumeric() or
                    lines_of_schematic[y - 1][x] != '.' and not lines_of_schematic[y - 1][x].isnumeric()):
                return True
        elif (lines_of_schematic[y][x - 1] != '.' and not lines_of_schematic[y][x - 1].isnumeric() or
              lines_of_schematic[y][x + 1] != '.' and not lines_of_schematic[y][x + 1].isnumeric() or
              lines_of_schematic[y - 1][x - 1] != '.' and not lines_of_schematic[y - 1][x - 1].isnumeric() or
              lines_of_schematic[y - 1][x] != '.' and not lines_of_schematic[y - 1][x].isnumeric() or
              lines_of_schematic[y - 1][x + 1] != '.' and not lines_of_schematic[y - 1][x + 1].isnumeric()):
            return True
    elif x == 0:
        if (lines_of_schematic[y][x + 1] != '.' and not lines_of_schematic[y][x + 1].isnumeric() or
                lines_of_schematic[y - 1][x] != '.' and not lines_of_schematic[y - 1][x].isnumeric() or
                lines_of_schematic[y - 1][x + 1] != '.' and not lines_of_schematic[y - 1][x + 1].isnumeric() or
                lines_of_schematic[y + 1][x] != '.' and not lines_of_schematic[y + 1][x].isnumeric() or
                lines_of_schematic[y + 1][x + 1] != '.' and not lines_of_schematic[y + 1][x + 1].isnumeric()):
            return True
    elif x == l:
        if (lines_of_schematic[y][x - 1] != '.' and not lines_of_schematic[y][x - 1].isnumeric() or
                lines_of_schematic[y - 1][x - 1] != '.' and not lines_of_schematic[y - 1][x - 1].isnumeric() or
                lines_of_schematic[y - 1][x] != '.' and not lines_of_schematic[y - 1][x].isnumeric() or
                lines_of_schematic[y + 1][x - 1] != '.' and not lines_of_schematic[y + 1][x - 1].isnumeric() or
                lines_of_schematic[y + 1][x] != '.' and not lines_of_schematic[y + 1][x].isnumeric()):
            return True
    elif (lines_of_schematic[y][x - 1] != '.' and not lines_of_schematic[y][x - 1].isnumeric() or
          lines_of_schematic[y][x + 1] != '.' and not lines_of_schematic[y][x + 1].isnumeric() or
          lines_of_schematic[y - 1][x - 1] != '.' and not lines_of_schematic[y - 1][x - 1].isnumeric() or
          lines_of_schematic[y - 1][x] != '.' and not lines_of_schematic[y - 1][x].isnumeric() or
          lines_of_schematic[y - 1][x + 1] != '.' and not lines_of_schematic[y - 1][x + 1].isnumeric() or
          lines_of_schematic[y + 1][x - 1] != '.' and not lines_of_schematic[y + 1][x - 1].isnumeric() or
          lines_of_schematic[y + 1][x] != '.' and not lines_of_schematic[y + 1][x].isnumeric() or
          lines_of_schematic[y + 1][x + 1] != '.' and not lines_of_schematic[y + 1][x + 1].isnumeric()):
        return True


y = 0
part_nums = []
for line in lines_of_schematic:
    x = 0
    this_part = ''
    is_part_num = False
    print(line)
    # print(len(line))
    # print('x:'+str(x)+' y:'+str(y))
    for letter in line:
        if letter.isnumeric():
            this_part += letter
            if not is_part_num:
                if has_symbol_adj(x, y, len(line) - 1):
                    is_part_num = True
            if x == len(line) - 1 and is_part_num:
                part_nums.append(int(this_part))
        elif not letter.isnumeric():
            if this_part != '':
                if is_part_num:
                    part_nums.append(int(this_part))
                    is_part_num = False
                this_part = ''
        x = x + 1
    y = y + 1
print(part_nums)
print(sum(part_nums))


def find_the_start(x, y) -> int:
    if not lines_of_schematic[y][x].isnumeric():
        return int(x+1)
    elif x == 0:
        return int(x)
    else:
        return find_the_start(x - 1, y)


def find_the_end(x, y) -> int:
    if not lines_of_schematic[y][x].isnumeric():
        return int(x)
    elif x == len(lines_of_schematic) - 1:
        return int(x+1)

    else:
        return find_the_end(x + 1, y)


def find_the_number(x, y) -> int:
    first_digit = find_the_start(x, y)
    last_digit = find_the_end(x, y)
    this_number = lines_of_schematic[y][first_digit:last_digit]
    if this_number != '':
        return int(this_number)
    else:
        return 0


def find_gear_multiples(x: int, y: int, l: int) -> int:
    num1 = 0
    num2 = 0
    if (x > 0 and y > 0 and x < l and y < len(lines_of_schematic)-1):
        # do all sides
        if (lines_of_schematic[y][x - 1].isnumeric()):
            #lhs
            if num1 > 0:
                num2 = find_the_number(x - 1, y)
            else:
                num1 = find_the_number(x - 1, y)
        if (lines_of_schematic[y - 1][x - 1].isnumeric()):
            #tlhs
            if num1 > 0:
                num2 = find_the_number(x - 1, y - 1)
            else:
                num1 = find_the_number(x - 1, y - 1)
            if not lines_of_schematic[y - 1][x].isnumeric():
                # need to check trhs
                if lines_of_schematic[y - 1][x + 1].isnumeric():
                    num2 = find_the_number(x + 1, y - 1)
        elif lines_of_schematic[y - 1][x].isnumeric():
            #top
            if num1 > 0:
                num2 = find_the_number(x, y - 1)
            else:
                num1 = find_the_number(x, y - 1)
        elif lines_of_schematic[y - 1][x + 1].isnumeric():
            #trhs
            if num1 > 0:
                num2 = find_the_number(x + 1, y - 1)
            else:
                num1 = find_the_number(x + 1, y - 1)
        if lines_of_schematic[y][x+1].isnumeric():
            #rhs
            if num1 > 0:
                num2 = find_the_number(x + 1, y)
            else:
                num1 = find_the_number(x + 1, y)
        if (lines_of_schematic[y + 1][x - 1].isnumeric()):
            #blhs
            if num1 > 0:
                num2 = find_the_number(x - 1, y + 1)
            else:
                num1 = find_the_number(x - 1, y + 1)
            if not lines_of_schematic[y + 1][x].isnumeric():
                # need to check brhs
                if lines_of_schematic[y + 1][x + 1].isnumeric():
                    num2 = find_the_number(x + 1, y + 1)
        elif lines_of_schematic[y + 1][x].isnumeric():
            #bottom
            if num1 > 0:
                num2 = find_the_number(x, y + 1)
            else:
                num1 = find_the_number(x, y + 1)
        elif lines_of_schematic[y + 1][x + 1].isnumeric():
            #brhs
            if num1 > 0:
                num2 = find_the_number(x + 1, y + 1)
            else:
                num1 = find_the_number(x + 1, y + 1)
    print("num1:"+str(num1)+" num2:"+str(num2))
    return num1 * num2


y = 0
gear_nums = []
for line in lines_of_schematic:
    x = 0
    for letter in line:
        if letter == '*':
            gear_nums.append(find_gear_multiples(x, y, len(line) - 1))

        x = x + 1
    y = y + 1
print(gear_nums)
print(sum(gear_nums))
