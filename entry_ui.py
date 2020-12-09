import PySimpleGUI as sg

loginLayout = [[sg.Text("Please enter your login details", key='-OUTPUT-')],
          [sg.Text("Username:")],
          [sg.Input(key='-USERNAME-')],
          [sg.Text("Password:")],
          [sg.Input(key='-PASSWORD-')],
          [sg.Button('Confirm'), sg.Button('Signup'), sg.Button('Exit')]]

loginHeading = "TheAter Login"

signupLayout = [[sg.Text("Please enter your login details", key='-OUTPUT-')],
          [sg.Text("Username:")],
          [sg.Input(key='-USERNAME-')],
          [sg.Text("Password:")],
          [sg.Input(key='-PASSWORD-')],
          [sg.Text("Confirm Password:")],
          [sg.Input(key='-CONFIRM-')],
          [sg.Button('Submit'), sg.Button('Login'), sg.Button('Exit')]]

signupHeading = "TheAter Signup"


