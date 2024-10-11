import PySimpleGUI as sg
sg.theme("darkgreen4")
sg.theme_text_color("#FFFF00")
window = sg.Window(title="contoh button",
                   layout=[[sg.Text("contoh button")],
                           [sg.Button("button simpan")],
                           [sg.Button("button keluar")],
                           ],
                    size=(400,200),
                    font=("Times",18))
kejadian,nilai = window.read()
print(kejadian,"=>",nilai)
window.close()