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
                    output += "  "+ element +","
                count +=1
            output = output[0:len(output)-1]
            list_data.append(output)
        return list_data

# true for ui format, false for database format
def title_times_split(string, ui):
    title = string[:string.index(":")]
    showTimes = []

    string = string[string.index(":")+1:]
    if ui:
        while True:
            if ":" in string:
                showTimes.append(title + ": " + string[string.index(":")-2:string.index(":")+3])
                string = string[string.index(":")+1:]
            else:
                break
    else: 
        while True:
            if ":" in string:
                showTimes.append(string[string.index(":")-2:string.index(":")+3])
                string = string[string.index(":")+1:]
            else:
                break

    return title, showTimes

def read_bookings(user):
    bookings = []
    with open("databases/bookings_db.txt", "r") as db:
        for line in db:
            string = line.split(",")
            if user == string[0]:
                bookings.append(string[1] + ": " + string[2])
    
    return bookings

def read_bookings_review():
    dict = {}
    bookings = []
    with open("databases/bookings_db.txt", "r") as db:
        for line in db:
            movie = line.split(",")[1]
            if movie not in dict:
                dict[movie] = 1
            else:
                dict[movie] = dict[movie] + 1
    
    return dict.items()
def save_to_file(filename, content):
    f = open(filename, "w")  
    for c in content:
        n = c.split(':\t')[0]
        t = c.replace(n+":", "")
        n = n + "," + t.replace("\t", "")
        if n.endswith("\n") != True:
            n = n + "\n"
        f.write(n)

def save_to_file(filename, content):
    f = open(filename, "w")  
    for c in content:
        n = c.split(':  ')[0]
        t = c.replace(n+":", "")
        n = n + "," + t.replace("  ", "")
        if n.endswith("\n") != True:
            n = n + "\n"
        f.write(n)
