from pathlib import Path
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

#Import sql controler
from sql import manager


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)



def dashBoard(parent):
    canvas = Canvas(parent,bg = "#FFFFFF",height = 500,width = 900,bd = 0,highlightthickness = 0,relief = "ridge")

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(0.0,0.0,900.0,500.0,fill="#FFFFFF",outline="")

    canvas.create_text(56.0,19.0,anchor="nw",text="Dashboard:",fill="#1AA2EC",font=("Saira Condensed Bold", 40 * -1))

    global entry_image_1
    entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(128.5,153.5,image=entry_image_1)
    entry_1 = Entry(bd=0,bg="#D9D9D9",highlightthickness=0, font=("Saira Condensed Bold", 40 * -1))
    entry_1.place(x=73.0,y=103.0,width=111.0,height=99.0)
    entry_1.insert(0, manager.getBookRooms())
    entry_1.config(state="disabled",disabledbackground="#D9D9D9")

    global entry_image_2
    entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(195.5,369.5,image=entry_image_2)
    entry_2 = Text(bd=0,bg="#D9D9D9",highlightthickness=0, state="disabled")
    entry_2.place(x=74.0,y=265.0,width=243.0,height=207.0)

    global entry_image_3
    entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(450.0,227.5,image=entry_image_3)
    entry_3 = Text(bd=0,bg="#D9D9D9",highlightthickness=0, state="disabled")
    entry_3.place(x=34.5,y=223.0,width=831.0,height=7.0)

    global entry_image_4
    entry_image_4 = PhotoImage(file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(548.5,369.5,image=entry_image_4)
    entry_4 = Text(bd=0,bg="#D9D9D9",highlightthickness=0, state="disabled")
    entry_4.place(x=427.0,y=265.0,width=243.0,height=207.0)

    global entry_image_5
    entry_image_5 = PhotoImage(file=relative_to_assets("entry_5.png"))
    entry_bg_5 = canvas.create_image(335.5,153.5,image=entry_image_5)
    entry_5 = Entry(bd=0,bg="#D9D9D9",highlightthickness=0, font=("Saira Condensed Bold", 40 * -1))
    entry_5.place(x=280.0,y=103.0,width=111.0,height=99.0)
    entry_5.insert(0, manager.getEmptyRooms())
    entry_5.config(state="disabled",disabledbackground="#D9D9D9")

    global entry_image_6
    entry_image_6 = PhotoImage(file=relative_to_assets("entry_6.png"))
    entry_bg_6 = canvas.create_image(542.5,153.5,image=entry_image_6)
    entry_6 = Entry(bd=0,bg="#D9D9D9",highlightthickness=0, font=("Saira Condensed Bold", 40 * -1))
    entry_6.place(x=487.0,y=103.0,width=111.0,height=99.0)
    entry_6.insert(0, manager.getAmenitiesBooked())
    entry_6.config(state="disabled",disabledbackground="#D9D9D9")

    global entry_image_7
    entry_image_7 = PhotoImage(file=relative_to_assets("entry_7.png"))
    entry_bg_7 = canvas.create_image(749.5,153.5,image=entry_image_7)
    entry_7 = Entry(bd=0,bg="#D9D9D9",highlightthickness=0, font=("Saira Condensed Bold", 40 * -1))
    entry_7.place(x=694.0,y=103.0,width=111.0,height=99.0)
    entry_7.insert(0, manager.getTablesBooked())
    entry_7.config(state="disabled",disabledbackground="#D9D9D9")

    canvas.create_text(70.0,84.0,anchor="nw",text="ROOMS BOOKED",fill="#1AA2EC",font=("Saira Condensed Bold", 15 * -1))

    canvas.create_text(81.0,246.0,anchor="nw",text="ROOMS STATUS",fill="#1AA2EC",font=("Saira Condensed Bold", 15 * -1))

    canvas.create_text(431.0,246.0,anchor="nw",text="ROOMS STATUS BY TYPE",fill="#1AA2EC",font=("Saira Condensed Bold", 15 * -1))

    canvas.create_text(277.0,82.0,anchor="nw",text="ROOMS EMPTY",fill="#1AA2EC",font=("Saira Condensed Bold", 15 * -1))

    canvas.create_text(691.0,80.0,anchor="nw",text="AMENITIES BOOKED",fill="#1AA2EC",font=("Saira Condensed Bold", 15 * -1))

    canvas.create_text(484.0,82.0,anchor="nw",text="TABLES BOOKED",fill="#1AA2EC",font=("Saira Condensed Bold", 15 * -1))

    #Rooms booked pie graph
    fig_rbk = Figure(figsize=(2.4, 1.6), dpi=100)
    fig_rbk.set_facecolor("#D9D9D9")
    plt_rbk = fig_rbk.add_subplot(111)
    plt_rbk.pie([manager.getEmptyRooms(), manager.getBookRooms()],
        [0.05, 0.05],
        startangle=-30,
        colors=("#1AA2EC", "#8a8a8a")
    )
    plt_rbk.legend(["unbooked", "booked"], loc="upper left", fontsize = "7")
    canva_rbk = FigureCanvasTkAgg(fig_rbk, parent)
    canva_rbk.draw()
    canva_rbk.get_tk_widget().place(x = 70, y=285)

    colors = ["#1AA2EC", "#8a8a8a", "#797EF6", "#a4a4a4"]
    # Rooms booked by type graph
    fig_rbt = Figure(figsize=(2.4, 1.6), dpi=100)
    fig_rbt.set_facecolor("#D9D9D9")
    plt_rbt = fig_rbt.add_subplot(111)
    x_data = list(manager.returnBkRByType().values())
    x = [(i+1)*0.05 for i in range(len(x_data))]
    plt_rbt.pie(x_data,
        explode=x,
        startangle=-30,
        colors=colors[:len(x_data)]
    )
    plt_rbt.legend(list(manager.returnBkRByType().keys()), loc="upper left", fontsize = "7")
    canva_rbt = FigureCanvasTkAgg(fig_rbt, parent)
    canva_rbt.draw()
    canva_rbt.get_tk_widget().place(x = 420, y=285)

    

if __name__=="__main__":
    window = Tk()

    window.geometry("900x500")
    window.configure(bg = "#FFFFFF")
    dashBoard(window)
    window.resizable(False, False)
    window.mainloop()
