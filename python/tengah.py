import PySimpleGUI as sg
susunan=[[sg.Text("UNISKA MAAB",font=("helvetica",24))],
         [sg.Text("BANJARMASIN", font=("courier",18))]]
window = sg.Window(title="elemen text",
                   layout=susunan,
                   element_justification = "center",
                   size=(430,200))
window.read()
window.close()