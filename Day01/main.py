# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    lines = []
    with open('input.txt', 'r') as file:
        for line in file:
            lines.append(line.strip())

    cal_sum = 0

    # print(lines)

    for line in lines:
        first = 10
        last = 0
        for char in line:
            if(char.isdigit()):
                if(first == 10):
                    first = char
                    last = char
                else:
                    last = char
        # print("Line: " + line + ", first: " + first + ", last: " + last)
        cal_sum += int(str(first) + str(last))

    print("Calculated corection: " + str(cal_sum))