import PySimpleGUI as sg
sg.theme("Brightcolors")
sg.theme_text_color("#007FFF")
window = sg.Window(title="Profile",
                   layout=[[sg.Text ("FTI UNISKA")],
                           [sg.Text ("FAKULTAS TEKNOLOGI INFORMASI")],
                           [sg.Text ("UNISKA MAB BANJARMASIN")],
                           ],                
                   size=(430,200),
                    font=("Times",18))
window()
window.close()