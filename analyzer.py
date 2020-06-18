import numpy # numpy is handy for using arrays in python
fileName="/Users/addisongould/Desktop/EskerTextAnalyzer/testData.txt"
file = open(fileName, "rt")
lines=0
characters=0

# loop through lines of file to get number of lines and characters per line (for total char count)
for line in file:
    lines += 1
    characters = characters + len(line)
print("File name:", fileName)
print("Number of lines:", lines)

# create array to store counts of words x letters long
letterCounts = numpy.zeros(20, dtype=int)

# open file and split text into list, with list item for each word
file = open(fileName, "rt")
data = file.read()
words = data.split() # words is our list of words
wordCount=len(words)
totalLetterCount=0
figureCount=0
otherCharCount=0
# loop over each word
for curWord in range(wordCount):
    curWordLetterCount=0 # counter for number of letters of current word in loop. Reset for each word
    word=words[curWord]
    # loop over each character in current word and increment count of letters, figures, or other characters accordingly
    for curChar in word:
        # this function gets the ASCII val of the character
        asciiVal = ord(curChar)
        # ASCII values 48-57 represent number figures
        if (asciiVal >= 48) and (asciiVal <= 57):
            figureCount += 1
        # ASCII values 65-90 represent cap. letters, 97-122 represent lowercase letters
        elif ((asciiVal >= 65) and (asciiVal <= 90)) or ((asciiVal >= 97) and (asciiVal <= 122)):
            curWordLetterCount += 1
            totalLetterCount += 1
        else:
            otherCharCount = otherCharCount+1
    # increment count of n-letter words, where n is the letter count in the current word
    letterCounts[curWordLetterCount] = letterCounts[curWordLetterCount] + 1


print("Number of characters (total):", characters) # note this counts newline and whitespace characters as well
print("Number of letters:", totalLetterCount)
print("Number of figures:", figureCount) # interpreting "figures" as "numeric characters"
print("Number of other characters:", otherCharCount)
print("Number of whitespaces and newlines:", characters-totalLetterCount-figureCount-otherCharCount)
print("Number of words:", wordCount) # a word being defined as a sequence of characters separated from other sequences by whitespace
# loop through letter count array and print counts of y-letter words.
# Numeric figures and special characters do not count towards letter count. Ex: "vitamin-b12" has 8 letters
for y in range(0, 20):
    print("Number of", y, "letter words:", letterCounts[y])
