import logic_controller
import ui_controller
import os

def eventLoop(window, event, values):
    cwd = os.getcwd()
    file = cwd+r"\Data\Movies.txt"
    movies = ReadFile(file)

    window['-MOVIES-'].update(movies)
    if event == 'Exit':
        logic_controller.logic.exit()
    if event == 'Save':
        movies = values['-Movies-']
        WriteFile(cwd, movies)

def ReadFile(file):
        f = open(file, "r")
        m = f.readlines()
        f.close()
        return m

def WriteFile(cwd, movies):
    f = open(cwd+r"\Data\Movies.txt", "w")  
    for m in movies:
        f.write(m+"/n")

    f.close()