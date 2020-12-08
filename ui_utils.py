def get_view_list(filename):
        listData = open(filename, "r")
        lineData = listData
        list_data = []

        for line in lineData:
            elements = line.split(",")
            count = 0
            output = ""
            for element in elements:
                if count == 0 :
                    output += element + ":"
                else :
                    output += "\t"+ element +","
                count +=1
            output = output.removesuffix(',')
            list_data.append(output)
        return list_data

def save_to_file(filename, content):
    f = open(filename, "w")  
    for c in content:
        n = c.split(':\t')[0]
        t = c.replace(n+":", "")
        n = n + "," + t.replace("\t", "")
        if n.endswith("\n") != True:
            n = n + "\n"
        f.write(n)