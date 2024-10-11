import PySimpleGUI as sg
susunan=[[sg.VPush()],
           [sg.Text("UNISKA MAAB",font=("helvetica",24))],
           [sg.Text("BANJARMASIN",font=("courier",18))],
           [sg.VPush()]]
window = sg.Window(title="elemen text",
                   layout=susunan,
                   element_justification = " Center ",
                   size=(430,200))
window.read()
window.close()
            