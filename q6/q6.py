import datetime

# all possible date formats in text file
formats = ('%Y/%m/%d', '%m/%d/%Y', '%d/%m/%Y', '%d %b %Y')

dateCount = 0
content = ""

# assuming text file is named example.txt
with open("example.txt", "r") as f:
    content = f.read()

content = content.split()

# testing formats a, b, and c
for str in content:
    for format in formats[:3]:
        try:
            newStr = datetime.datetime.strptime(str, format)
            dateCount += 1
        except:
            pass

# testing format d
for i in range(len(content) - 2):
    # check 3 words at once
    str = " ".join([content[i], content[i + 1], content[i + 2]])
    
    try:
        newStr = datetime.datetime.strptime(str, formats[-1])
        dateCount += 1
    except:
        pass

print(dateCount)