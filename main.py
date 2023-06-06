import os
import qrcode
import PySimpleGUI as sg

sg.theme('DarkGrey4')

leftLayout=[
    [
        sg.Text("Enter the content of the QR Code"),
        sg.Input(key="qrLink")
    ],
    [
        sg.Text("Name of QR Code"),
        sg.Input(key="qrName")
    ],
    [
        sg.Text("Where to save the QR Code (optional)"),
        sg.In(size=(25,1),enable_events=True, key="saveFolder"),
        sg.FolderBrowse()
    ],
    [sg.Button("Generate")]
]

rightLayout=[
    [sg.Text("Your QrCode image")],
    [sg.Image(key="qrImage")],
]

layout = [
    [
        sg.Column(leftLayout),
        sg.VSeparator(),
        sg.Column(rightLayout),
    ]
]

window = sg.Window("QrCode Generator", layout, margins=(50, 50))
folderLocation=""

while True:
    event, values = window.read()
    if event=="saveFolder":
        folderLocation = values["saveFolder"]
    if event == "Generate":
        qrLink = values["qrLink"]
        qrName = values["qrName"]
        if(qrLink!="" and qrName!=""):
            imgQr = qrcode.make(qrLink)

            if folderLocation=="":
                imgQr.save("tempQr.png")
                window["qrImage"].update(filename="tempQr.png")
                os.remove("tempQr.png")
            else:
                imgQr.save(folderLocation + "/" +  qrName + ".png")
                window["qrImage"].update(filename=(folderLocation + "/" + qrName + ".png"))

    if event==sg.WINDOW_CLOSED:
        break
window.close()