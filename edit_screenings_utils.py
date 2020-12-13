import re

def convertToEditForm(input):
    o = input.split(' -')[0]
    input = input.replace(o+" -  ", "")
    o = o.replace("Screen ", "")
    output = input.split(': ')[0]
    t = input.replace(output+":  ", "")
    output = output + "," + o + ","
    output = output + t.replace(" ", ",")
    output = output.removesuffix(",")

    return output

def convertToSaveForm(input):
    o = input.split(' -')[0]
    input = input.replace(o+" -  ", "")
    o = o.replace("Screen ", "")
    output = input.split(': ')[0]
    t = input.replace(output+": ", "")
    output = output + "," + o
    output = output + t.replace(" ", ", ")

    return output

def convertToDisplayForm(input):
    elements = input.split(",")
    count = 0
    output = ""
    t = ""
    for element in elements:
        if count == 0 : 
            t = element + ":  "
        elif count == 1:
            if re.match("[0-9][0-9]|[0-9]", element):
                output = "Screen " + element + " -  " + t
        else:
            if re.match("(2[0-3]:[0-5][0-9]|[0-1][0-9]:[0-5][0-9])", element):
                output += element + " "
        count += 1

    return output

def deleteSelected(delete, values):
    output = []
    for v in values:
        if v != delete:
            output.append(v)

    return output