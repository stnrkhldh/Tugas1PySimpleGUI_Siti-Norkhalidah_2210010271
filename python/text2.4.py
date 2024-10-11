import PySimpleGUI as sg
sg.theme("Brightcolors")
sg.theme_text_color("#007FFF")
window = sg.Window(title="Profile",
                   layout=[[sg.Text ("FTI UNISKA",
                                     font=("heltivitica",24),text_color=("#FFFF00"))],
                           [sg.Text ("FAKULTAS TEKNOLOGI INFORMASI",
                                     font=("courier",18,"italic","bold","underline"))],
                           [sg.Text ("UNISKA MAB BANJARMASIN",text_color="#FFFF00")],
                           ],                
                   size=(430,200),
                    font=("Times",18))
window()
window.close()