import os

class EditMovies:
    cwd = os.getcwd()
    file = cwd+r"\Data\Movies.txt"
    movies = [] 
    movies = ReadFile(file)


    def ReadFile(self, file):
        f = open(file, "r")
        m = []
        for x in f:
            m.append(x)

        f.close()
        return m

    def WriteFile(self, cwd, movies):
        f = open(cwd+r"\Data\Movies.txt", "w")  
        for m in movies:
            f.write(m+"/n")

        f.close()  

