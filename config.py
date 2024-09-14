import tomli

def loadConfig(filePath):
    with open(filePath, 'rb') as file:
        return tomli.load(file)