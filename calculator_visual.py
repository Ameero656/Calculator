import PySimpleGUI as sg

output =0

layout = [ 
    [sg.Button("2N Basic Calc")],
    [sg.Text('Output:', output)]
    ]

# Create the window
window = sg.Window("Calculator", layout)

# Create an event loop
while True:
    event, values = window.read()
    print(event)
    if event == '2NBasic Calc':
        pass
    
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()