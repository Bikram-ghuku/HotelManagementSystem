from pathlib import Path
from tkinter import END, VERTICAL, Scrollbar, Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter.ttk import Treeview
import gui.main_window.gui as mwg
from sql.manager import deleteReservation, getRoomReservation

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def item_selected(event):
    global item
    id_item = tree.selection()[0]
    item = tree.item(id_item, "values")
    button_1["state"] = "normal"
    button_2["state"] = "normal"
    button_3["state"] = "normal"
    
def handle_checkOut():
    deleteReservation(item[0])

def handle_delete():
    deleteReservation(item)

def handle_modify(parent, username):
    
    mwg.handle_btn_clk("mR", parent, username, item[0])


def viewReservation(parent, username):
    canvas = Canvas(parent,bg = "#FFFFFF",height = 500,width = 900,bd = 0,highlightthickness = 0,relief = "ridge")

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(0.0, 0.0,900.0,500.0,fill="#FFFFFF",outline="")

    canvas.create_text(56.0,19.0,anchor="nw",text="View Room Reservations:",fill="#1AA2EC",font=("Saira Condensed Bold", 50 * -1))

    canvas.create_rectangle(46.0,93.0,854.0,390.0,fill="#D9D9D9",outline="")

    canvas.create_text(46.0,393.0,anchor="nw",text="Actions:",fill="#1AA2EC",font=("Saira Condensed Bold", 50 * -1))

    global button_image_1
    global button_1
    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    button_1 = Button(image=button_image_1,borderwidth=0,highlightthickness=0,command=lambda: handle_delete(),relief="flat")
    button_1.place(x=573.0,y=418.0,width=140.0,height=45.0)
    button_1["state"] = "disabled"

    global button_image_2
    global button_2
    button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
    button_2 = Button(image=button_image_2,borderwidth=0,highlightthickness=0,command=lambda: handle_checkOut(),relief="flat")
    button_2.place(x=427.0,y=418.0,width=140.0,height=45.0)
    button_2["state"] = "disabled"

    global button_image_3
    global button_3
    button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
    button_3 = Button(image=button_image_3,borderwidth=0,highlightthickness=0,command=lambda: handle_modify(parent, username),relief="flat")
    button_3.place(x=719.0,y=418.0,width=140.0,height=45.0)
    button_3["state"] = "disabled"

    columns=("Name", "Number of guests", "CheckIn Date", "CheckOut Date", "Room Type","Room Number")
    global tree
    tree = Treeview(parent, columns=columns, height=14)
    for i in columns:
        tree.heading(i, text=i)
        tree.column(i, width=101)

    for i in getRoomReservation():
        tree.insert('', END, values=i)
    sBar = Scrollbar(parent, orient=VERTICAL, command=tree.yview)
    tree.configure(yscroll=sBar.set)
    sBar.grid(row=0, column=1, sticky='ns')
    tree.place(x=46, y=93)

    tree.bind("<<TreeviewSelect>>", item_selected)

if __name__=="__main__":
    window = Tk()
    window.geometry("1200x600")
    viewReservation(window)
    window.resizable(False, False)
    window.mainloop()
