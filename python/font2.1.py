import PySimpleGUI as sg
sg.theme("DarkGreen4")
sg.theme_text_color("#C1CDCD")
window = sg.Window(title="Profile",
                   layout=[[sg.Text ("FTI UNISKA",
                                     font=("Helvitica",24))],
                           [sg.Text ("FAKULTAS TEKNOLOGI INFORMASI")],
                           [sg.Text ("UNISKA MAB BANJARMASIN")],
                           ],                
                   size=(430,200),
                    font=("Times",18))
window()
window.close()