import PySimpleGUI as sg
from cost_converter import cost_converter

layout = [[sg.Input(size=(30, 1), do_not_clear=False, key='_IN_', font=("Helvetica", 15))],
          [sg.Text('Total Cost:', font=("Helvetica", 20))],
          [sg.Output(size=(25, 2), font=("Helvetica", 20), key='_OUTPUT_')],
          [sg.Button('Convert', bind_return_key=True), sg.Button('Exit')]]

window = sg.Window('Convert Costs', layout)

while True:  # Event Loop
    event, values = window.Read()
    print(event, values)
    if event is None or event == 'Exit':
        break
    if event == 'Convert':
        print(values['_IN_'])
        converted = cost_converter(values['_IN_'])
        window.Element('_OUTPUT_').Update(value=converted)


window.Close()
