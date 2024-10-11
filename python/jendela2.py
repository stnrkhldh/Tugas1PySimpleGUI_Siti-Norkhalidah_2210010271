import PySimpleGUI as sg
sg.theme("DarkGreen")
sg.theme_text_color("#FFFF00")
window = sg.Window(title="Profile",
                   layout=[[sg.Text ("Npm : 2210010271")],
                           [sg.Text ("Nama : Siti Norkhalidah")],
                           [sg.Text ("Kelas : 5N Reguler Pagi Banjarmasin")],
                           [sg.Text ("Matkul : Pemrograman Visual 3")]
                           ],                
                   size=(400,200),
                    font=("Times",18))
window()
window.close()