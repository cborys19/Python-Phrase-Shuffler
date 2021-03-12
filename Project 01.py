"""
Program: Project 1
Name: Christopher Borys
Date: 2/20/21

This is the first Python project of the semester. The goal of this project is to take a given .txt file
(project1.txt) and do a series of tasks with the information on it. These tasks include:
    A. Reading each line and printing both the shortest and longest words in each.
    B. List how many total lines exist and how many words are in each.
    C. Keep a count of the number of words that contain exactly 3 and 6 characters individually and 
         then print the results.
    D. Rewrite the phrases to a new .txt file (called project1-reordered.txt) and do it in descending
       order so that the smallest line is first and the largest is last.
            i. The length is determined by characters in the line, not words.
    E. Rewrite the lines so that the authors do not appear, then print this list to the screen.
    F. Create a new file that prints just the authors to a new .txt file (called project1-authors.txt)
       and do it in ascending order.
    G. Take the first 2 words in each phrase and replace the, with the first two words of the previous
         line.
            i. In the case of the first line, swap with the last line.
"""

# Task A
print("Task A")
print("------------------------")
with open("project1.txt", 'r') as file: # runs processes while file is open and being read
    lines = [] # creates list named lines
    for line in file: # used to loop through file's contents
        lines.append(line.rstrip()) # each line will be appended to the end of the list and trimmed at the end for trailing characters

    firstLine = lines[0].split(" ") # stores first line 
    secondLine = lines[1].split(" ") # stores second line 
    thirdLine = lines[2].split(" ") # stores third line
    fourthLine = lines[3].split(" ") # stores fourth line
    fifthLine = lines[4].split(" ") # stores fifth line
    sixthLine = lines[5].split(" ") # stores sixth line
    
    shortestWordFirst = str("") # creates string variable for shortest word in first line
    longestWordFirst = str("") # creates string variable for longest word in first line
    for i in range(1, len(firstLine)): # loops through line
        if len(firstLine[i]) <= len(firstLine[0]): # executes if current word is shorter than or equal to the length of the first word
            if firstLine[i].isalpha(): # executes if the word is made of alphabetical characters
                shortestWordFirst = firstLine[i] # stores current word as shortest word
        if len(firstLine[i]) > len(firstLine[i - 1]): # executes if current word is longer than previous word
            if firstLine[i].isalpha(): # executes if the word is made of alphabetical characters 
                if len(longestWordFirst) < len(firstLine[i]): # executes if previously stored longest word is shorter than the current word
                    longestWordFirst = firstLine[i] # stores current word as longest word
    print("Line 1 - Shortest word:", shortestWordFirst, "|| Longest Word:", longestWordFirst) # returned output

    shortestWordSecond = str("") # creates string variable for shortest word in second line
    longestWordSecond = str("") # creates string variable for longest word in second line
    for i in range(1, len(secondLine)): # loops through line
        if len(secondLine[i]) <= len(secondLine[0]): # executes if current word is shorter than or equal to the length of the first word
            if secondLine[i].isalpha(): # executes if the word is made of alphabetical characters
                shortestWordSecond = secondLine[i] # stores current word as shortest word
        if len(secondLine[i]) > len(secondLine[i - 1]): # executes if current word is longer than the previous word
            if secondLine[i].isalpha(): # executes if the word is made of alphabetical characters
                if len(longestWordSecond) < len(secondLine[i]): # executes if the previously stored longest word is shorter than the current word
                    longestWordSecond = secondLine[i] # stores current word as longest word
    print("Line 2 - Shortest word:", shortestWordSecond, "|| Longest Word:", longestWordSecond) # returned output

    shortestWordThird = str("") # creates string variable for shortest word in third line
    longestWordThird = str("") # creates string variable for longest word in third line
    for i in range(1, len(thirdLine)): # loops through line
        if len(thirdLine[i]) < len(thirdLine[0]): # executes if current word is shorter than the length of the first word
            if thirdLine[i].isalpha(): # executes if the word is made of alphabetical characters
                shortestWordThird = thirdLine[i] # stores current word as shortest word
        if len(thirdLine[i]) > len(thirdLine[i - 1]): # executes if current word is longer than the previous word
            if thirdLine[i].isalpha(): # executes if the word is made of alphabetical characters
                if len(longestWordThird) < len(thirdLine[i]): # executes if the previously stored longest word is shorter than the current word
                    longestWordThird = thirdLine[i] # stores current word as longest word
    print("Line 3 - Shortest word:", shortestWordThird, "|| Longest Word:", longestWordThird) # returned output

    shortestWordFourth = str("") # creates string variable for shortest word in fourth line
    longestWordFourth = str("") # creates string variable for longest word in fourth line
    for i in range(1, len(fourthLine)): # loops through line
        if len(fourthLine[i]) <= len(fourthLine[0]): # executes if current word is shorter than or equal to the length of the first word
            if fourthLine[i].isalpha(): # executes if the word is made of alphabetical characters
                shortestWordFourth = fourthLine[i] # stores current word as shortest word
        if len(fourthLine[i]) > len(fourthLine[i - 1]): # executes if current word is longer than the previous word
            if fourthLine[i].isalpha(): # executes if the word is made of alphabetical characters
                if len(longestWordFourth) < len(fourthLine[i]): # executes if the previously stored longest word is shorter than the current word
                    longestWordFourth = fourthLine[i] # stores current word as longest word
    print("Line 4 - Shortest word:", shortestWordFourth, "|| Longest Word:", longestWordFourth) # returned output
        
    shortestWordFifth = str("") # creates string variable for shortest word in fifth line
    longestWordFifth = str("") # creates string variable for longest word in fifth line
    for i in range(1, len(fifthLine)): # loops through line
        if len(fifthLine[i]) <= len(fifthLine[0]): # executes if current word is shorter than or equal to the length of the first word
            if fifthLine[i].isalpha(): # executes if the word is made of alphabetical characters
                shortestWordFifth = fifthLine[i] # stores current word as shortest word
        if len(fifthLine[i]) > len(fifthLine[i - 1]): # executes if current word is longer than the previous word
            if fifthLine[i].isalpha(): # executes if the word is made of alphabetical characters
                if len(longestWordFifth) < len(fifthLine[i]): # executes if the previously stored longest word is shorter than the current word
                    longestWordFifth = fifthLine[i] # stores current word as longest word
    print("Line 5 - Shortest word:", shortestWordFifth, "|| Longest Word:", longestWordFifth) # returned output

    shortestWordSixth = str("") # creates string variable for shortest word in sixth line
    longestWordSixth = str("") # creates string variable for longest word in sixth line
    for i in range(1, len(sixthLine)): # loops through line
        if len(sixthLine[i]) < len(sixthLine[0]): # executes if current word is shorter than the length of the first word
            if sixthLine[i].isalpha(): # executes if the word is made of alphabetical characters
                if len(sixthLine[i]) == 1: # executes if length of current word is 1 [I couldn't return "I" as the shortest word otherwise]
                    shortestWordSixth = sixthLine[i] # stores current word as shortest word                    
        if len(sixthLine[i]) > len(sixthLine[i - 1]): # executes if current word is longer than the previous word
            if sixthLine[i].isalpha(): # executes if the word is made of alphabetical characters
                if len(longestWordSixth) < len(sixthLine[i]): # executes if the previously stored longest word is shorter than the current word
                    longestWordSixth = sixthLine[i] # stores current word as longest word
    print("Line 6 - Shortest word:", shortestWordSixth, "|| Longest Word:", longestWordSixth) # returned output

print("\n\n")

# Task B
print("Task B")
print("------------------------")
with open("project1.txt", 'r') as file: # runs while file is open and being read 
    lineCount = int(0) # initializes integer value to store number of lines
    wordCount = int(0) # initializes integer value to store number of words
    for line in file: # loops through lines in file
        wordCount = len(line.split(" ")) # splits lines at the spaces, takes the word's length, and then stores that in the word count
        lineCount += 1 # calculates number of lines by incrementing by 1 every iteration
        print("Number of words in Line", lineCount, ":", wordCount)
    print("Total number of lines:", lineCount)



print("\n\n")

# Task C
print("Task C")
print("------------------------")
with open("project1.txt", 'r') as file:  # runs while file is open and being read 
    threeCount = int(0) # initializes integer value to store number of three-letter words
    sixCount = int(0) # initializes integer value to store number of six-letter words

    words = [] # declares list titled "words"
    for line in file: # loops through file
        words.append(line.split(" ")) # lines are split at spaces, then appended to the end of the list
    
    # list values stored in corresponding variables
    lineOne = words[0]
    lineTwo = words[1]
    lineThree = words[2]
    lineFour = words[3]
    lineFive = words[4]
    lineSix = words[5]

    for i in range(0, len(lineOne)): # loops through length of line 1
        if len(lineOne[i]) == 3: # executes if word is of length 3
            threeCount += 1 # increments total of three-letter words by 1
        elif len(lineOne[i]) == 6: # executes if word is of length 6
            sixCount += 1 # increments total of six-letter words by 6
    for i in range(0, len(lineTwo)): # loops through length of line 2
        if len(lineTwo[i]) == 3: # executes if word is of length 3
            threeCount += 1 # increments total of three-letter words by 1
        elif len(lineTwo[i]) == 6: # executes if word is of length 6
            sixCount += 1 # increments total of six-letter words by 6
    for i in range(0, len(lineThree)): # loops through length of line 3
        if len(lineThree[i]) == 3: # executes if word is of length 3
            threeCount += 1 # increments total of three-letter words by 1
        elif len(lineThree[i]) == 6: # executes if word is of length 6
            sixCount += 1 # increments total of six-letter words by 6
    for i in range(0, len(lineFour)): # loops through length of line 4
        if len(lineFour[i]) == 3: # executes if word is of length 3
            threeCount += 1 # increments total of three-letter words by 1
        elif len(lineFour[i]) == 6: # executes if word is of length 6
            sixCount += 1 # increments total of six-letter words by 6
    for i in range(0, len(lineFive)): # loops through length of line 5
        if len(lineFive[i]) == 3: # executes if word is of length 3
            threeCount += 1 # increments total of three-letter words by 1
        elif len(lineFive[i]) == 6: # executes if word is of length 6
            sixCount += 1 # increments total of six-letter words by 6     
    for i in range(0, len(lineSix)): # loops through length of line 6
        if len(lineSix[i]) == 3: # executes if word is of length 3
            threeCount += 1 # increments total of three-letter words by 1
        elif len(lineSix[i]) == 6: # executes if word is of length 6
            sixCount += 1 # increments total of six-letter words by 6

    print("Three Count:", threeCount) # outputs number of three-letter words
    print("Six Count:", sixCount) # outputs number of six-letter words
    

print("\n\n")

# Task D
print("Task D")
print("------------------------")
with open("project1.txt", 'r') as file: # runs while file is opened and being read
    lineList = [] # initializes a new list of lines
    for line in file: # loops through file
        lineList.append(line.rstrip()) # each line is stripped of trailing characters and then stored in the list
    
    temp = str("") # temp variable to hold string value (aka the line)
    for i in range(0, len(lineList)):
        if len(lineList[i]) <= len(lineList[0]): # finds shortest line
            temp = lineList[0]
            lineList[0] = lineList[i]
            lineList[i] = temp
        if len(lineList[i]) <= len(lineList[1]) and len(lineList[i]) > len(lineList[0]): # finds next shortest line; executes if current line is smaller than all other lines and larger than the already smallest line
            temp = lineList[1]
            lineList[1] = lineList[i]
            lineList[i] = temp
        if len(lineList[i]) <= len(lineList[2]) and len(lineList[i]) > len(lineList[1]): # finds third shortest line; executes if current line is smaller than all remaining lines and larger than the other two
            temp = lineList[2]
            lineList[2] = lineList[i]
            lineList[i] = temp
        if len(lineList[i]) <= len(lineList[3]) and len(lineList[i]) > len(lineList[2]): # finds third longest line; executes if current line is smaller than all remaining lines and larger than the other three
            temp = lineList[3]
            lineList[3] = lineList[i]
            lineList[i] = temp
        if len(lineList[i]) <= len(lineList[4]) and len(lineList[i]) > len(lineList[3]): # finds second longest line; executes if current line is smaller than other line and larger than the other four
            temp = lineList[4]
            lineList[4] = lineList[i]
            lineList[i] = temp
        
    
    oFile = open("project1-reordered.txt", 'w') # creates output file for sorted results
    for i in range(0, len(lineList)): # loops through the length of lineList
        oFile.write(lineList[i] + "\n") # prints the sorted list to the file
        print(lineList[i]) # prints sorted list to the screen for the user

print("\n\n")

# Task E
file = open("project1.txt", 'r')
print("Task E")
print("------------------------")
for line in file: # loops through file
    line = line.split("-") # divides line by the hyphen
    print(line[0]) # prints the first index aka the quote
print("\n\n")

# Task F
print("Task F")
print("------------------------")
with open("project1.txt", 'r') as file: # runs while file is open and being read 
    authors = [] # declares list called "authors"
    for line in file: # loops through lines in the file
        line = line.rstrip().split("-") # splits the lines at the hyphen, strips them of any straggling characters, and then replaces the line with these versions
        authors.append(line[1]) # appends each line's first index (the author) to the authors list

    authors.sort() # sorts the authors list
    outputFile = open("project1-authors.txt", 'w') # creates the output file we are writing to
    for i in range(0, len(authors)): # loops through authors list
        print(authors[i]) # prints authors to screen so we can see what's being printed to output file
        outputFile.write((authors[i] + "\n")) # writes each author element to the output file


print("\n\n")
# Task G
print("Task G")
print("------------------------")
with open("project1.txt", 'r') as file: # runs while file is opened and being read
    newLines = [] # initializes a new list of lines
    for line in file: # loops through file
        newLines.append(line.rstrip().split(" ")) # each line is stripped of trailing characters, split at the spaces, and then stored in the list

    swapOne = newLines[0] # first line is stored in container variable
    swapTwo = newLines[1] # second line is stored in container variable
    swapThree = newLines[2] # third line is stored in container variable
    swapFour = newLines[3] # fourth line is stored in container variable
    swapFive = newLines[4] # fifth line is stored in container variable
    swapSix = newLines[5] # sixth line is stored in container variable

    swapOneFirstWord = swapOne[0] # stores first word of line one
    swapOneSecondWord = swapOne[1] # stores second word of line one
    swapOneThirdWord = swapOne[2] # stores third word of line one
    swapTwoFirstWord = swapTwo[0] # stores first word of line two
    swapTwoSecondWord = swapTwo[1] # stores second word of line two
    swapTwoThirdWord = swapTwo[2] # stores third word of line one
    swapThreeFirstWord = swapThree[0] # stores first word of line three
    swapThreeSecondWord = swapThree[1] # stores second word of line three
    swapThreeThirdWord = swapThree[2] # stores third word of line three
    swapFourFirstWord = swapFour[0] # stores first word of line four
    swapFourSecondWord = swapFour[1] # stores second word of line four
    swapFourThirdWord = swapFour[2] # stores third word of line four
    swapFiveFirstWord = swapFive[0] # stores first word of line five
    swapFiveSecondWord = swapFive[1] # stores second word of line five
    swapFiveThirdWord = swapFive[2] # stores third word of line five
    swapSixFirstWord = swapSix[0] # stores first word of line six
    swapSixSecondWord = swapSix[1] # stores second word of line six
    swapSixThirdWord = swapSix[2] # stores third word of line six

    swapOne[0] = swapSixFirstWord # swaps first word of first line
    swapOne[1] = swapSixSecondWord # swaps second word of first line
    swapOne[2] = swapSixThirdWord # swaps third word of first line
    swapTwo[0] = swapOneFirstWord # swaps first word of second line
    swapTwo[1] = swapOneSecondWord # swaps second word of second line
    swapTwo[2] = swapOneThirdWord # swaps third word of second line
    swapThree[0] = swapTwoFirstWord # swaps first word of third line
    swapThree[1] = swapTwoSecondWord # swaps second word of third line
    swapThree[2] = swapTwoThirdWord # swaps third word of third line
    swapFour[0] = swapThreeFirstWord # swaps first word of fourth line
    swapFour[1] = swapThreeSecondWord # swaps second word of fourth line
    swapFour[2] = swapThreeThirdWord # swaps third word of fourth line
    swapFive[0] = swapFourFirstWord # swaps first word of fifth line
    swapFive[1] = swapFourSecondWord # swaps second word of fifth line
    swapFive[2] = swapFourThirdWord # swaps third word of fifth line
    swapSix[0] = swapFiveFirstWord # swaps first word of sixth line
    swapSix[1] = swapFiveSecondWord # swaps second word of sixth line
    swapSix[2] = swapFiveThirdWord # swaps third word of sixth line

    print(swapOne)
    print(swapTwo)
    print(swapThree)
    print(swapFour)
    print(swapFive)
    print(swapSix)

print("\n\n")
    