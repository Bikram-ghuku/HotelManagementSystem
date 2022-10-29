from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

from sql.manager import insertResturantResrvation


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def makeResturantReservation(parent):
    canvas = Canvas(parent,bg = "#FFFFFF",height = 500,width = 900,bd = 0,highlightthickness = 0,relief = "ridge")

    canvas.place(x = 0, y = 0)

    global entry_image_1
    entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(169.5,242.5,image=entry_image_1)
    entry_1 = Entry(bd=0,bg="#D9D9D9",highlightthickness=0)
    entry_1.place(x=71.0,y=215.0,width=197.0,height=53.0)

    global entry_image_2
    entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(754.5,242.5,image=entry_image_2)
    entry_2 = Entry(bd=0,bg="#D9D9D9",highlightthickness=0)
    entry_2.place(x=656.0,y=215.0,width=197.0,height=53.0)

    global entry_image_3
    entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(448.5,242.5,image=entry_image_3)
    entry_3 = Entry(bd=0,bg="#D9D9D9",highlightthickness=0)
    entry_3.place(x=350.0,y=215.0,width=197.0,height=53.0)

    canvas.create_text(51.0,24.0,anchor="nw",text="Make Resturant Reservation:",fill="#1AA2EC",font=("Saira Condensed Bold", 50 * -1))

    global button_image_1
    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    button_1 = Button(image=button_image_1,borderwidth=0,highlightthickness=0,command=lambda: insertResturantResrvation(entry_1.get(), entry_3.get(), entry_2.get()),relief="flat")
    button_1.place(x=330.0,y=389.0,width=237.0,height=55.0)

    canvas.create_text(82.0,178.0,anchor="nw",text="Name:",fill="#000000",font=("Saira Condensed Bold", 25 * -1))

    canvas.create_text(349.0,179.0,anchor="nw",text="No Of Guests:",fill="#000000",font=("Saira Condensed Bold", 25 * -1))

    canvas.create_text(667.0,180.0,anchor="nw",text="Date:",fill="#000000",font=("Saira Condensed Bold", 25 * -1))

if __name__=="__main__":
    window = Tk()

    window.geometry("900x500")
    window.configure(bg = "#FFFFFF")
    makeResturantReservation(window)
    window.resizable(False, False)
    window.mainloop()
