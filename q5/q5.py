import os
import subprocess

path = "q5/my-python-project"

pythonFileCount = 0
codeLineCount = 0
commentLineCount = 0
functionCount = 0

# walk through folder
for (root, dirs, files) in os.walk(path):
    # Part e
    for dir in dirs:
        dirPath = os.path.join(root, dir)
        print(f"Size of {dirPath}: {os.stat(dirPath).st_size / 1048576} MB")
        # not sure how to limit to 2 level depth
        # iterating through all files using recursive function does not adhere to 2 level depth limit
        
    for filename in files:
        if filename.endswith(".py"):
            # Part a
            pythonFileCount += 1
            
            # open python files
            filePath = os.path.join(root, filename)
            with open(filePath, "r") as f:
                content = f.read().split('\n')
                for line in content:
                    # remove indentations
                    line = line.strip()
                    if line != "":
                        # Part b
                        if line.startswith("#"):
                            commentLineCount += 1
                        else:
                            codeLineCount += 1
                        
                        # Part c
                        if line.startswith("def"):
                            functionCount += 1

print("Number of python files:", pythonFileCount)
print("Number of lines of code:", codeLineCount)
print("Number of comment lines:", commentLineCount)
print("Number of functions defined:", functionCount)

# -----------------------------------------------------------------
# Part d
lineChanges = 0

# run git diff --shortstat HEAD~3 HEAD
result = subprocess.run(["git", "diff", "--shortstat", "HEAD~3", "HEAD"], stdout=subprocess.PIPE).stdout.decode('utf-8')

# find insertions and deletions
if result != "":
    resultList = result.strip().split()
    for i in range(len(resultList)):
        if "insertion" in resultList[i] or "deletion" in resultList[i]:
            # number is 1 index before the word
            lineChanges += int(resultList[i - 1])

print("Number of lines changed:", lineChanges)