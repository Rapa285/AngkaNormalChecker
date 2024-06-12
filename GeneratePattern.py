def generatePattern(digit :int):
    pattern = []
    upper = ""
    for i in range(digit):
        upper += "9"
    dig_upper = int(upper)
    for i in range (dig_upper+1):
        num = str(i)
        nolstring = ""
        for j in range(digit-len(num)):
            nolstring+="0"
        pattern.append(nolstring+num)
    return pattern

# pattern1 = generatePattern(1)
# pattern2 = generatePattern(2)
# pattern3 = generatePattern(3)

# print(f"pattern1 : {pattern1}")
# print(f"pattern2 : {pattern2}")
# print(f"pattern3 : {pattern3}")
        