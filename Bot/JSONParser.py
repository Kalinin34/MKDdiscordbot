import json

jsF = open('init.json', 'r')
jsD = jsF.read()
obj = json.loads(jsD)


def getTOKEN() -> str:
    return obj["TOKEN"]


def getDefaultRole() -> str:
    return str(obj["DefaultRole"])
