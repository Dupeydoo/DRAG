import DRAG.datacontext as dc

def constructinput(cleaned_data):
    input = []
    input.append(cleaned_data["beatone"])
    input.append(cleaned_data["beattwo"])
    input.append(cleaned_data["beatthree"])
    input.append(cleaned_data["beatfour"])
    input.append(cleaned_data["beatfive"])
    input.append(cleaned_data["beatsix"])
    input.append(cleaned_data["beatseven"])
    input.append(cleaned_data["beateight"])
    return input

def getpreset(index):
    return dc.context["presets"][index]