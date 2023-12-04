with open("AoC2023Day2.txt", "r") as file:
    line_num = 0
    sum_ = 0
    power = 0
    for line in file:
        line_num += 1
        a = "".join(line.split(":")[1].replace(";",",")).split(",")
        valid = True
        min_red = 0
        min_green = 0
        min_blue = 0
        for i in a:
            if (("red" in i and int(i[1:-4])>12) or
            ("green" in i and int(i[1:-6])>13) or
            ("blue" in i and int(i[1:-5])>14)):
                valid = False
            if "red" in i and int(i[1:-4])>min_red:
                min_red = int(i[1:-4])
            elif "green" in i and int(i[1:-6])>min_green:
                min_green = int(i[1:-6])
            elif "blue" in i and int(i[1:-5])>min_blue:
                min_blue = int(i[1:-5])
        if valid:
            sum_ += line_num
        power += min_red*min_green*min_blue
        
print(sum_,power)
