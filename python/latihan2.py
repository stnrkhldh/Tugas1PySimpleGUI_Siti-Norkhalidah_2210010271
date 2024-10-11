import PySimpleGUI as sg
sg.theme("darkgreen4")
sg.theme_text_color("#FFFF00")
window = sg.Window(title="profile",
                   layout=[[sg.Text("SELAMAT DATANG DI KELAS",
                                    font=("arial",25,"italic","bold","underline"))],
                            [sg.Text("Npm       : 2210010271")],
                            [sg.Text("Nama      : Siti Norkhalidah")],
                            [sg.Text("Kelas     : 5N Reguler Banjarmasin")]
                            ],

                    size=(510,200),
                    font=("times",18))
window()
window.close()