import PySimpleGUI as sg
sg.theme("bluepurple")
sg.theme_text_color("#00FFFF")
window = sg.Window(title="Profile",
                   layout=[[sg.Text ("SELAMAT DATANG DIKELAS",
                                    font=("Arial",25))],
                           [sg.Text ("Npm : 2210010271")],
                           [sg.Text ("Nama : Siti Norkhalidah")],
                           [sg.Text ("Kelas : 5N Reguler Banjarmasin")]
                           ],                
                   size=(500,200),
                    font=("Times",18))
window()
window.close()