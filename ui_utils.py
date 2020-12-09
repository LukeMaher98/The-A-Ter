import listings
import list_objects

def get_view_list(type, filename):
        listData = open(filename, "r")
        lineData = listData
        list_data = []
        movieListing = 0
        for line in lineData:
            index = 0
            length = len(line)
            current_entry = ["","",[]]
            while index < length:
                if line[index] == ",":
                    index += 1
                    break
                else:
                    current_entry[0] +=line[index]
                index += 1
            while index < length:
                if line[index] == ",":
                    index += 1
                    break
                else:
                    current_entry[1] +=line[index]
                index += 1
            hold = ""
            if type == "movies" :
                while index < length:
                    if line[index] == ",":
                        index += 1
                        current_entry[2].append(hold)
                        hold = ""
                    else:
                        hold +=line[index]
                    index += 1
                hold = hold[:-1]
                current_entry[2].append(hold)
                movieListing = list_objects.Movie(current_entry)
            if type == "concessions":
                movieListing = list_objects.Concession(current_entry)
            if type == "concession sale":
                movieListing = list_objects.ConcessionSales(current_entry)
            if type == "ticket sale":
                movieListing = list_objects.TicketSales(current_entry)
            list_data.append(movieListing)
        
        return list_data

def save_to_file(filename, content):
    f = open(filename, "w")  
    for c in content:
        n = c.split(':  ')[0]
        t = c.replace(n+":", "")
        n = n + "," + t.replace("  ", "")
        if n.endswith("\n") != True:
            n = n + "\n"
        f.write(n)