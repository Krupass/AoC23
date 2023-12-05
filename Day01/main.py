words = [["one", 1], ["two", 2], ["three", 3], ["four", 4], ["five", 5], ["six", 6], ["seven", 7], ["eight", 8], ["nine", 9]]
def first_number(line):
    first_word = 10
    first_num = 10
    temp_word = 9999
    temp_num = 9999
    position = 9999

    for char in line:
        if (char.isdigit()):
            first_num = char
            temp_num = line.find(first_num)
            break

    for word in words:
        temp_word = line.lower().find((word[0]))
        if(temp_word > -1 and temp_word < position):
            position = temp_word
            first_word = word[1]

    if(temp_num < position):
        first = first_num
    else:
        first = first_word

    return first

def last_number(line):
    last_word = 0
    last_num = 0
    temp_word = -1
    temp_num = -1
    position = -1

    for char in line:
        if (char.isdigit()):
            last_num = char
            temp_num = line.rfind(char)

    for word in words:
        temp_word = line.lower().rfind((word[0]))
        if(temp_word > -1 and temp_word > position):
            position = temp_word
            last_word = word[1]

    if(temp_num < position):
        last = last_word
    else:
        last = last_num

    return last


if __name__ == '__main__':

    lines = []
    with open('input.txt', 'r') as file:
        for line in file:
            lines.append(line.strip())

    cal_sum = 0

    # print(lines)

    for line in lines:

        first = first_number(line)
        last = last_number(line)


        print("Line: " + line + ", first: " + str(first) + ", last: " + str(last))
        cal_sum += int(str(first) + str(last))

    print("Calculated corection: " + str(cal_sum))