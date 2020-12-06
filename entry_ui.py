import PySimpleGUI as sg

layout = [[sg.Text("Please enter your login details", key='-OUTPUT-')],
          [sg.Text("Username:")],
          [sg.Input(key='-USERNAME-')],
          [sg.Text("Password:")],
          [sg.Input(key='-PASSWORD-')],
          [sg.Button('Confirm'), sg.Button('Exit')]]

heading = "TheAter Login"


