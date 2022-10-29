import imp
from sql import manager
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from gui.main_window.gui import external_launch

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

window.geometry("1200x600")
window.configure(bg = "#1AA7EC")

def check_login():
    username = entry_1.get()
    password = entry_2.get()
    if manager.check_logindb(username, password):
        window.destroy()
        external_launch(username)
    else:
        print("Login failed")

canvas = Canvas(window,bg = "#1AA7EC",height = 600,width = 1200,bd = 0,highlightthickness = 0,relief = "ridge")

canvas.place(x = 0, y = 0)
canvas.create_rectangle(736.0,0.0,1137.0,600.0,fill="#FFFFFF",outline="")

canvas.create_text(57.0,80.0,anchor="nw",text="HOTEL",fill="#FFFFFF",font=("Saira Condensed Bold", 50 * -1))

canvas.create_text(183.0,137.0,anchor="nw",text="MANAGEMENT",fill="#FFFFFF",font=("Saira Condensed Bold", 50 * -1))

canvas.create_text(456.0,195.0,anchor="nw",text="SYSTEM",fill="#FFFFFF",font=("Saira Condensed Bold", 50 * -1))

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(999.5,251.5,image=entry_image_1)
entry_1 = Entry(bd=0,bg="#D9D9D9",highlightthickness=0)
entry_1.place(x=901.0,y=224.0,width=197.0,height=53.0)

entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(999.5,367.5,image=entry_image_2)
entry_2 = Entry(bd=0,bg="#D9D9D9",highlightthickness=0,show='*')
entry_2.place(x=901.0,y=340.0,width=197.0,height=53.0)

canvas.create_text(750.0,232.0,anchor="nw",text="Username:",fill="#1AA7EC",font=("Saira Condensed Regular", 25 * -1))

canvas.create_text(883.0,40.0,anchor="nw",text="LOGIN",fill="#1AA7EC",font=("Saira Condensed Bold", 50 * -1))

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(image=button_image_1,borderwidth=0,highlightthickness=0,command=lambda: check_login(),relief="flat")
button_1.place(x=832.0,y=504.0,width=209.0,height=54.0)

canvas.create_text(23.0,356.0,anchor="nw",text="It is a computerised hotel management system for effective",fill="#FFFFFF",font=("Saira Condensed Regular", 25 * -1))

canvas.create_text(750.0,345.0,anchor="nw",text="Password:",fill="#1AA7EC",font=("Saira Condensed Regular", 25 * -1))

canvas.create_text(23.0,402.0,anchor="nw",text="management of rooms, guests and bookings. Login to see",fill="#FFFFFF",font=("Saira Condensed", 25 * -1))

canvas.create_text(23.0,441.0,anchor="nw",text="around",fill="#FFFFFF",font=("Saira Condensed", 25 * -1))
window.title("Hotel Management System Login")
window.resizable(False, False)
window.mainloop()


