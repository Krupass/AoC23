# from functions import s2s
import sys

import functions

if __name__ == '__main__':
    inputs = []
    with open('input.txt', 'r') as file:
        for input in file:
            inputs.append(input)

    inputs[-1] = inputs[-1] + "\n"
    #print(inputs)

    seeds = []
    seed_to_soil = []
    soil_to_fert = []
    fert_to_water = []
    water_to_light = []
    light_to_temp = []
    temp_to_humid = []
    humid_to_loc = []

    temp = ""
    sw = 1
    for input in inputs:
        temp += input
        if(input.endswith("\n")):
            if(sw == 1):
                if (temp != "\n"):
                    seeds = (temp.split(":")[1].split())
                    temp = ""
                elif(temp == "\n"):
                    sw += 1
                    temp = ""
            elif(sw == 2):
                if ":" in temp:
                    temp = ""
                elif(temp != "\n"):
                    seed_to_soil.append(temp.strip().split())
                    temp = ""
                else:
                    temp = ""
                    sw += 1
            elif(sw == 3):
                if ":" in temp:
                    temp = ""
                elif(temp != '\n'):
                    soil_to_fert.append(temp.strip().split())
                    temp = ""
                else:
                    temp = ""
                    sw += 1
            elif(sw == 4):
                if ":" in temp:
                    temp = ""
                elif(temp != '\n'):
                    fert_to_water.append(temp.strip().split())
                    temp = ""
                else:
                    temp = ""
                    sw += 1
            elif(sw == 5):
                if ":" in temp:
                    temp = ""
                elif(temp != '\n'):
                    water_to_light.append(temp.strip().split())
                    temp = ""
                else:
                    temp = ""
                    sw += 1
            elif(sw == 6):
                if ":" in temp:
                    temp = ""
                elif(temp != '\n'):
                    light_to_temp.append(temp.strip().split())
                    temp = ""
                else:
                    temp = ""
                    sw += 1
            elif(sw == 7):
                if ":" in temp:
                    temp = ""
                elif(temp != '\n'):
                    temp_to_humid.append(temp.strip().split())
                    temp = ""
                else:
                    temp = ""
                    sw += 1
            elif(sw == 8):
                if ":" in temp:
                    temp = ""
                elif(temp != '\n'):
                    humid_to_loc.append(temp.strip().split())
                    temp = ""
                else:
                    temp = ""
                    sw += 1
            else:
                print("Error")
                raise EnvironmentError

    # print(seeds)
    # print(seed_to_soil)
    # print(soil_to_fert)
    # print(fert_to_water)
    # print(water_to_light)
    # print(light_to_temp)
    # print(temp_to_humid)
    # print(humid_to_loc)

    results = []
    for seed in seeds:
        soil = functions.e2e(seed, seed_to_soil)
        fert = functions.e2e(soil, soil_to_fert)
        water = functions.e2e(fert, fert_to_water)
        light = functions.e2e(water, water_to_light)
        temperature = functions.e2e(light, light_to_temp)
        humidity = functions.e2e(temperature, temp_to_humid)
        location = functions.e2e(humidity, humid_to_loc)

        result = []
        result.append(seed)
        result.append(soil)
        result.append(fert)
        result.append(water)
        result.append(light)
        result.append(temperature)
        result.append(humidity)
        result.append(location)
        results.append(result)

        # print("Seed:  " + seed + ", soil: " + str(soil) + ", fert: " + str(fert) + ", water: " + str(water) + ", light: " + str(light) + ", temp: " + str(temperature) + ", humidity: " + str(humidity) + ", location: " + str(location))

    lowest = sys.maxsize
    for result in results:
        if(result[7] < lowest):
            lowest = result[7]

    print("Lowest location number: " + str(lowest))