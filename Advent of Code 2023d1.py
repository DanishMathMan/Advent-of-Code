"""
Solution program for Advent of Code Day 1
"""

with open("AoC2023Day1.txt","r") as file:
    sum_a = 0
    sum_b = 0
    converted_digits = {"one":"1",
                        "two":"2",
                        "three":"3",
                        "four":"4",
                        "five":"5",
                        "six":"6",
                        "seven":"7",
                        "eight":"8",
                        "nine":"9",
                        "zero":"0"}
    
    for line_in_file in file:
        
        #pre-process
        line_processed = line_in_file
        for i in converted_digits:
            if i in line_in_file:
                line_processing_i = line_in_file
                while line_processing_i.find(i) != -1: #find returns -1 if i doesn't occur in line anymore.
                    line_processing_i = line_processing_i.replace(i,"*") #replace occurence with a safe character such that loop finds all occurences of i.
                    line_processed = line_processed.replace(i,i+converted_digits[i]+i) #replace occurence in line_processed with the converted value surounded by i's,
                                                                                       #such that overlaps in spelled out numbers are detected in loop over converted_digits.
                    
        #run through processed
        digits_a = ""
        digits_b = ""
        for i in line_in_file: #must loop over unprocessed line for part a.
            if i in list(converted_digits.values()):
                digits_a = digits_a + i 
        for i in line_processed:
            if i in list(converted_digits.values()):
                digits_b = digits_b + i
        sum_a += 10*int(digits_a[0])+int(digits_a[-1])
        sum_b += 10*int(digits_b[0])+int(digits_b[-1])

print(sum_a,sum_b)

                
        
    
