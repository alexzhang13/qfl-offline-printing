# img_viewer.py

import PySimpleGUI as sg
import os.path
import label

# Initial setup
data_path = "qfldata.csv"
label_folder = "labels/"
font = ("Arial", 20)
INITAL_NAMES = [
    f
    for f in os.listdir(label_folder)
    if os.path.isfile(os.path.join(label_folder, f)) and f.lower().endswith((".label"))
]


# First the window layout in 2 columns
file_list_column = [
    [
        sg.Text(f"Registrant Label Folder: {os.path.abspath(label_folder)}", font=font),
    ],
    [
        sg.Listbox(
            values=INITAL_NAMES,
            enable_events=True,
            size=(40, 20),
            key="filelist",
            font=font,
        )
    ],
]

# For now will only show the name of the file that was chosen
id_submit_column = [
    [sg.Text(f"Current data path: {os.path.abspath(data_path)}")],
    [sg.Text("Enter a registration ID:", font=font, text_color="orange")],
    [sg.Text("Current R-ID: NaN", key="RID_TEXT", font=font)],
    [
        sg.In(size=(40, 2), enable_events=True, key="NEWID", font=font),
    ],
    [sg.Submit(button_text="Generate Labels", font=font)],
]

# ----- Full layout -----
layout = [
    [
        sg.Column(file_list_column),
        sg.VSeperator(),
        sg.Column(id_submit_column),
    ]
]

window = sg.Window("QFL Registration Printer", layout)

labels = label.Label(
    csv_path=data_path,
    save_folder=label_folder,
)

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

    if event == "Generate Labels":
        RID = values["NEWID"]
        window["RID_TEXT"].update(f"Current R-ID: {RID}")

        labels.generate(RID)

        # Update folder list on left
        fnames = [
            f
            for f in os.listdir(label_folder)
            if os.path.isfile(os.path.join(label_folder, f))
            and f.lower().endswith((".label"))
        ]
        window["filelist"].update(fnames)

window.close()
