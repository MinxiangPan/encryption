import ntpath

def stringxor(s1, s2):
    returnResult = ''
    for x in range(s1.__len__()):
        returnResult += chr(ord(s1[x]) ^ ord(s2[x % s2.__len__()]))
    return returnResult

def encrytion(var, source, destination):
    source_path = source.get()
    destination_path = destination.get()
    password = var.get()
    file = open( source_path, "r")
    result = ""
    while True:
        words = file.readline()
        if words.find('\n') < 1: words += '\n'
        if words != '\n':
            result += stringxor(words, password)
        else:
            break
    file.close()
    writeFile = open(destination_path + "/" + ntpath.basename(source_path)[:ntpath.basename(source_path).__len__()-4] + "-encrytion.txt", "w+")
    writeFile.write(result)
    writeFile.close()

def decrytion(var, source, destination):
    source_path = source.get()
    destination_path = destination.get()
    password = var.get()
    file = open(source_path, "r")
    input = file.read()
    file.close()
    result = ""
    index = 0
    temp = stringxor(input, password)
    while temp.find('\n') > 0:
        temp = stringxor(input[index:], password)
        length = temp.find('\n') + 1
        index += length
        result += temp[: length]
    writeFile = open(destination_path + '/' + ntpath.basename(source_path)[:ntpath.basename(source_path).__len__()-4] + "-decrytion.txt", "w+")
    writeFile.write(result)
    writeFile.close()
