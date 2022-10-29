from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

from sql.manager import getDetailedReservation, updateReservation


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def handleUpdate(x:tuple):
    updateReservation(x, x[0])

def modifyReservation(parent, name=None):

    x = getDetailedReservation(name)
    canvas = Canvas(parent,bg = "#FFFFFF",height = 500,width = 900,bd = 0,highlightthickness = 0,relief = "ridge")

    canvas.place(x = 0, y = 0)
    global entry_image_1
    entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(169.5,181.5,image=entry_image_1)
    entry_1 = Entry(bd=0,bg="#D9D9D9",highlightthickness=0)
    entry_1.place(x=71.0,y=154.0,width=197.0,height=53.0)
    entry_1.insert(0, x[0])
    entry_1.config(state = "disabled", disabledbackground="#D9D9D9")

    global entry_image_2
    entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(169.5,331.5,image=entry_image_2)
    entry_2 = Entry(bd=0,bg="#D9D9D9",highlightthickness=0)
    entry_2.place(x=71.0,y=304.0,width=197.0,height=53.0)
    entry_2.insert(0, x[2])

    global entry_image_3
    entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(448.5,331.5,image=entry_image_3)
    entry_3 = Entry(bd=0,bg="#D9D9D9",highlightthickness=0)
    entry_3.place(x=350.0,y=304.0,width=197.0,height=53.0)
    entry_3.insert(0, x[3])

    global entry_image_4
    entry_image_4 = PhotoImage(file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(727.5,331.5,image=entry_image_4)
    entry_4 = Entry(bd=0,bg="#D9D9D9",highlightthickness=0)
    entry_4.place(x=629.0,y=304.0,width=197.0,height=53.0)
    entry_4.insert(0, x[5])

    global entry_image_5
    entry_image_5 = PhotoImage(file=relative_to_assets("entry_5.png"))
    entry_bg_5 = canvas.create_image(727.5,181.5,image=entry_image_5)
    entry_5 = Entry(bd=0,bg="#D9D9D9",highlightthickness=0)
    entry_5.place(x=629.0,y=154.0,width=197.0,height=53.0)
    entry_5.insert(0, x[4])

    global entry_image_6
    entry_image_6 = PhotoImage(file=relative_to_assets("entry_6.png"))
    entry_bg_6 = canvas.create_image(448.5,181.5,image=entry_image_6)
    entry_6 = Entry(bd=0,bg="#D9D9D9",highlightthickness=0)
    entry_6.place(x=350.0,y=154.0,width=197.0,height=53.0)
    entry_6.insert(0, x[1])

    canvas.create_text(51.0,24.0,anchor="nw",text="Modify Room Reservation:",fill="#1AA2EC",font=("Saira Condensed Bold", 50 * -1))

    global button_image_1
    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    button_1 = Button(image=button_image_1,borderwidth=0,highlightthickness=0,command=lambda: handleUpdate((entry_1.get(),entry_6.get(), entry_2.get(), entry_3.get(), entry_5.get(), entry_4.get())),relief="flat")
    button_1.place(x=330.0,y=389.0,width=237.0,height=55.0)

    canvas.create_text(82.0,117.0,anchor="nw",text="Name:",fill="#000000",font=("Saira Condensed Bold", 25 * -1))

    canvas.create_text(349.0,118.0,anchor="nw",text="No Of Guests:",fill="#000000",font=("Saira Condensed Bold", 25 * -1))

    canvas.create_text(616.0,119.0,anchor="nw",text="Room Type:",fill="#000000",font=("Saira Condensed Bold", 25 * -1))

    canvas.create_text(349.0,263.0,anchor="nw",text="Check-Out Date:",fill="#000000",font=("Saira Condensed Bold", 25 * -1))

    canvas.create_text(616.0,264.0,anchor="nw",text="Room No:",fill="#000000",font=("Saira Condensed Bold", 25 * -1))

    canvas.create_text(82.0,262.0,anchor="nw",text="Check-In Date:",fill="#000000",font=("Saira Condensed Bold", 25 * -1))

if __name__=="__main__":
    window = Tk()

    window.geometry("1200x600")
    window.configure(bg = "#FFFFFF")
    modifyReservation(window)
    window.resizable(False, False)
    window.mainloop()
