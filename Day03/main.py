if __name__ == '__main__':
    lines = []
    with open('input.txt', 'r') as file:
        for line in file:
            line = line.strip().split("\n")[0]
            lines.append(list('.' + line + '.'))

    lines.insert(0, list(len(lines[0]) * '.'))
    lines.insert(len(lines), list(len(lines[0]) * '.'))
    for line in lines:
        print(line)

    # print(lines)
    sum_of_parts = 0

    for i, line in enumerate(lines):
        for j, letter in enumerate(line):
            number = 0
            if(letter.isdigit() and not lines[i][j-1].isdigit()):
                number = int(letter)
                tmp = 1
                while(lines[i][j+tmp].isdigit()):
                    number = int(str(number) + lines[i][j+tmp])
                    tmp += 1
                skip = False
                temp = -1
                while(temp < (tmp + 1)):
                    if(lines[i - 1][j + temp] !=  '.' and not lines[i - 1][j + temp].isdigit() and not skip):
                        sum_of_parts += number
                        skip = True
                        break
                    temp += 1
                if(lines[i][j - 1] !=  '.' and not lines[i][j - 1].isdigit() and not skip):
                    sum_of_parts += number
                    skip = True
                    break
                if(lines[i][j + tmp] !=  '.' and not lines[i][j + tmp].isdigit() and not skip):
                    sum_of_parts += number
                    skip = True
                    break
                temp = -1
                while (temp < (tmp + 1)):
                    if (lines[i + 1][j + temp] != '.' and not lines[i + 1][j + temp].isdigit() and not skip):
                        sum_of_parts += number
                        skip = True
                        break
                    temp += 1

    print(sum_of_parts)
