class View_Controller:

    def get_view_list(self, filename):
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
                    output += "  "+ element +"   "
                count +=1
            list_data.append(output)
        
        return list_data

view = View_Controller()
