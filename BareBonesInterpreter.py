def Main():
    lines = OpenFile()
    global variables
    global variaValues
    global loops
    variables = []
    variaValues = []
    loops = []
    unclosedLoops = []
    totLines = len(lines)
    currentLine = 0
    for line in lines:         #Adding all variables and loops to a list
        if len(line) > 1 and line[1] not in variables:
            variables.append(line[1])
            variaValues.append(0)
        if line[0] == "while":
            unclosedLoops.append(currentLine)
        elif line[0] == "end":
            start = unclosedLoops.pop()
            loops.append([start, currentLine])
        currentLine += 1
    
    currentLine = 0
    while currentLine < totLines:
        currentLine = Execute(lines[currentLine], currentLine)
        currentLine += 1
    
    print("PROGRAM FINISHED")
    print("FINAL VALUES:")
    for i in range(0, len(variables)):    #Prints the final value of each variable
        print(f"{variables[i]}: {variaValues[i]}")
    
def OpenFile():
    f = open("barebonesinput.txt")
    text = f.readlines()
    lines = []
    for line in text:
        line = line.strip()
        line = line[:-1]
        line = line.split(" ")
        lines.append(line)
    return lines

def Execute(line, currentLine):
    if len(line) != 1:
        indx = variables.index(line[1])
    match line[0]:
        case "clear":
            variaValues[indx] = 0
        case "incr":
            variaValues[indx] += 1
        case "decr":
            variaValues[indx] -= 1
        case "end":
            for loop in loops:
                if loop[1] == currentLine:
                    currentLine = loop[0] - 1
                    return currentLine
        case "while":
            value = int(line[3])
            if variaValues[indx] == value:
                for loop in loops:
                    if loop[0] == currentLine:
                        currentLine = loop[1]
                        return currentLine
    return currentLine                


Main()