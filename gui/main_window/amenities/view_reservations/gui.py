from pathlib import Path
from tkinter import END, VERTICAL, Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter.ttk import Treeview, Scrollbar
from sql.manager import getAmenitiesReservation, deleteAmenitiesReservation
import gui.main_window.gui as mwg

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def item_selected(callback):
    global item
    item_id = tree.selection()[0]
    item = tree.item(item_id, "values")
    button_1["state"] = "normal"

def viewAmenitiesReservation(parent):
    canvas = Canvas(parent,bg = "#FFFFFF",height = 500,width = 900,bd = 0,highlightthickness = 0,relief = "ridge")

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(0.0,0.0,900.0,500.0,fill="#FFFFFF",outline="")

    canvas.create_text(56.0,19.0,anchor="nw",text="View Amenities Reservations:",fill="#1AA2EC",font=("Saira Condensed Bold", 50 * -1))

    canvas.create_rectangle(46.0,93.0,854.0,390.0,fill="#D9D9D9",outline="")

    canvas.create_text(46.0,393.0,anchor="nw",text="Actions:",fill="#1AA2EC",font=("Saira Condensed Bold", 50 * -1))

    global button_image_1
    global button_1
    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    button_1 = Button(image=button_image_1,borderwidth=0,highlightthickness=0,command=lambda: deleteAmenitiesReservation(item[0], item[2], item[3]),relief="flat")
    button_1.place(x=719.0,y=418.0,width=140.0,height=45.0)
    button_1["state"] = "disabled"

    columns=("Name", "Number of guests", "Date", "Type")
    global tree
    tree = Treeview(parent, columns=columns, height=14)
    for i in columns:
        tree.heading(i, text=i)
        tree.column(i, width=151)

    for i in getAmenitiesReservation():
        tree.insert('', END, values=i)
    sBar = Scrollbar(parent, orient=VERTICAL, command=tree.yview)
    tree.configure(yscroll=sBar.set)
    sBar.grid(row=0, column=1, sticky='ns')
    tree.place(x=46, y=93)

    tree.bind("<<TreeviewSelect>>", item_selected)

if __name__=="__main__":
    window = Tk()
    window.geometry("1200x600")
    window.configure(bg = "#FFFFFF")
    viewAmenitiesReservation(window)
    window.resizable(False, False)
    window.mainloop()
