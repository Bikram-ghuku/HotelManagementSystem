from pathlib import Path
import datetime as dt
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame, Label
#Importing dashboard UI
from gui.main_window.dashboard.gui import dashBoard
#Importing amenities UI
from gui.main_window.amenities.make_reservation.gui import makeAmenitiesRervation
from gui.main_window.amenities.view_reservations.gui import viewAmenitiesReservation
#Importing resturant UI
from gui.main_window.resturant.modify_reservation.gui import modifyResturantReservation
from gui.main_window.resturant.view_reservation.gui import viewResturantReservation
from gui.main_window.resturant.make_reservation.gui import makeResturantReservation

#Importing room resrvation UI
from gui.main_window.room.make_reservation.gui import makeResrvation
from gui.main_window.room.modify_reservation.gui import modifyReservation
from gui.main_window.room.view_reservation.gui import viewReservation


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def handle_btn_clk(target, window, username, cname=None):
    
    for i in window.winfo_children():
        i.destroy()
    mainWindow(window, username)
    global current_window
    if target=="dash":
        current_window = dashBoard(window)
        sidebar_navigator.place(x=1193, y=126)
    elif target=="mkAR":
        current_window = makeAmenitiesRervation(window)
        sidebar_navigator.place(x=1193, y=377)
    elif target=="vAR":
        current_window = viewAmenitiesReservation(window)
        sidebar_navigator.place(x=1193, y=422)
    elif target=="mRR":
        current_window = modifyResturantReservation(window, cname)
    elif target=="vRR":
        current_window = viewResturantReservation(window, username)
        sidebar_navigator.place(x=1193, y=326)
    elif target=="mkRR":
        current_window = makeResturantReservation(window)
        sidebar_navigator.place(x=1193, y=275)
    elif target=="mkR":
        current_window = makeResrvation(window)
        sidebar_navigator.place(x=1193, y=176)
    elif target=="mR":
        current_window = modifyReservation(window, cname)
    elif target=="vR":
        current_window = viewReservation(window, username)
        sidebar_navigator.place(x=1193, y=226)


def mainWindow(parent, username):
    canvas = Canvas(parent,bg = "#FFFFFF",height = 600,width = 1200,bd = 0,highlightthickness = 0,relief = "ridge")
    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(900.0,0.0,1200.0,600.0,fill="#1AA2EC",outline="")

    date = dt.datetime.now()

    canvas.create_text(919.0,18.0,anchor="nw",text="Hotel Management System",fill="#FFFFFF",font=("Saira Condensed Bold", 25 * -1))
    canvas.create_text(50.0,550.0,anchor="nw",text=f"{date:%A, %B %d, %Y}",fill="#1AA2EC",font=("Saira Condensed Bold", 25 * -1))
    canvas.create_text(50.0,520.0,anchor="nw",text=f"Welcome {username} !",fill="#1AA2EC",font=("Saira Condensed Bold", 25 * -1))

    global button_image_1
    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    button_1 = Button(image=button_image_1,borderwidth=0,highlightthickness=0,command=lambda: handle_btn_clk("dash", parent, username),relief="flat")
    button_1.place(x=900.0,y=126.0,width=300.0,height=50.0)

    global button_image_2
    button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
    button_2 = Button(image=button_image_2,borderwidth=0,highlightthickness=0,command=lambda: handle_btn_clk("mkR", parent, username),relief="flat")
    button_2.place(x=900.0,y=176.0,width=300.0,height=50.0)

    global button_image_3
    button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
    button_3 = Button(image=button_image_3,borderwidth=0,highlightthickness=0,command=lambda: handle_btn_clk("vR", parent, username),relief="flat")
    button_3.place(x=900.0,y=226.0,width=300.0,height=50.0)

    global button_image_4
    button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
    button_4 = Button(image=button_image_4,borderwidth=0,highlightthickness=0,command=lambda: handle_btn_clk("mkRR", parent, username),relief="flat")
    button_4.place(x=900.0,y=272.0,width=300.0,height=50.0)

    global button_image_5
    button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
    button_5 = Button(image=button_image_5,borderwidth=0,highlightthickness=0,command=lambda: handle_btn_clk("vRR", parent, username),relief="flat")
    button_5.place(x=900.0,y=322.0,width=300.0,height=50.0)
    
    global button_image_6
    button_image_6 = PhotoImage(file=relative_to_assets("button_6.png"))
    button_6 = Button(image=button_image_6,borderwidth=0,highlightthickness=0,command=lambda: handle_btn_clk("vAR", parent, username),relief="flat")
    button_6.place(x=900.0,y=422.0,width=300.0,height=50.0)

    global button_image_7
    button_image_7 = PhotoImage(file=relative_to_assets("button_7.png"))
    button_7 = Button(image=button_image_7,borderwidth=0,highlightthickness=0,command=lambda: handle_btn_clk("mkAR", parent, username),relief="flat")
    button_7.place(x=900.0,y=372.0,width=300.0,height=50.0)

    global button_image_8
    button_image_8 = PhotoImage(file=relative_to_assets("button_8.png"))
    button_8 = Button(image=button_image_8,borderwidth=0,highlightthickness=0,command=lambda: parent.destroy(),relief="flat")
    button_8.place(x=900.0,y=508.0,width=300.0,height=50.0)

    global sidebar_navigator
    sidebar_navigator = Frame(background="#FFFFFF")
    sidebar_navigator.place(x=1193, y=176, height=47, width=7)

def external_launch(username):
    window = Tk()
    window.title("Hotel Management System")
    window.geometry("1200x600")
    window.configure(bg = "#FFFFFF")
    # handle_btn_clk("vR", window)
    mainWindow(window, username)
    dashBoard(window)

    sidebar_navigator.place(x=1193, y=126)
    window.resizable(False, False)
    window.mainloop()


if __name__=="__main__":
    window = Tk()
    window.title("Hotel Management System")
    window.geometry("1200x600")
    window.configure(bg = "#FFFFFF")
    # handle_btn_clk("vR", window)
    mainWindow(window,"ADMINISTRATOR")
    dashBoard(window)
    sidebar_navigator.place(x=1193, y=126)
    window.resizable(False, False)
    window.mainloop()
