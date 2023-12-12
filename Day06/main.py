import math

def number_of_ways(records):
    result = []

    for record in records:
        time = int(record[0])
        dist = record[1]
        ways = 0
        time_hold = 1
        while(time_hold < time):
            dist_hold = time_hold * (time - time_hold)
            if(dist_hold > dist):
                ways += 1
            time_hold += 1

        result.append(ways)


    return result

if __name__ == '__main__':
    inputs = []
    with open('input.txt', 'r') as file:
        for i, input in enumerate(file):
            if((i % 2) == 0):
                tmp = (input.split(":")[1].strip().split())
                for time in tmp:
                    inputs.append(time.split())
            else:
                tmp = (input.split(":")[1].strip().split())
                for j, dist in enumerate(tmp):
                    inputs[j].append(int(dist))

    ways = number_of_ways(inputs)
    result = 1
    print(ways)

    for way in ways:
        result *= way

    print(result)

