import mysql.connector

def check_logindb(username, password):
    x = False
    #TODO: Check if username and password are in the database and reutrn True or False
    if username=="USERNAME" and password=="password":
        x = True
    return x

def getEmptyRooms():
    #TODO: return number of rooms empty
    n = 10
    return n

def getBookRooms():
    n = 12
    #TODO: return number of rooms empty
    return n

def getAmenitiesBooked() -> int:
    #TODO: return total number of amenities booked 
    n = 14
    return n

def getTablesBooked() -> int:
    #TODO: retun total number of tables booked
    n = 16
    return n

def returnBkRByType():
    #TODO: Return number of room booked by type
    x = {"D": 5, "E": 15}
    return x

def makeRoomReservation(Name, noGuest, rType, cinDate, cOutDate, bDate):
    #TODO: Insert all data into "reservation" after assigning an empty rooms and update the room as books in "rooms"
    print("Name:{} Guests:{} rType: {} cinDate: {} cOutDate: {}, bdate: {}".format(Name, noGuest, rType, cinDate, cOutDate, bDate))
    

def getRoomReservation():
    x = (("A", 3, '2020-12-22', "2021-01-2", "A", "A01"), ("B", 4, '2020-12-22', "2021-01-2", "A", "A02"))
    #TODO: Returns Name, Number of guest, CheckInDate, CheckOutDate, RoomType, RoomNo from "reservation"
    return x

def updateReservation(data, name):
    #TODO: Update reservation and set the data where Name=name in "reservation"
    x = 0

def deleteReservation(name):
    #TODO: delete reservation with the given name
    x = 0

def insertResturantResrvation(name, noGuest, date):
    #TODO: insert reservation into table "resturant"
    print("Name: {}, noGuest: {}, date: {}".format(name, noGuest, date))

def getResturantReservation():
    x = (("A", 4, "2022-12-23"), ("B", 5, "2022-12-24"))
    #TODO: returns name, number of guests and date from "resturant"
    return x

def deleteResturant(name, date):
    #TODO: delete resturant reservation with the given name and date from "resturant"
    print("Delete Resturant Reservation with name {} on {}".format(name, date))
    x = 0

def insertAmenitiesRequest(name, noGuests, date, type):
    #TODO: Insert amenities request into "amenities"
    print("name: {}, noGuest: {}, date: {}, type:{}".format(name, noGuests, date, type))
    x= 0 

def getAmenitiesReservation():
    x = (("A", 4, "2022-12-13", "Gym"), ("B", 2, "2023-11-13", "Swimming"))
    #TODO: returns name, number of guest, date and type from "Amenities"
    return x

def deleteAmenitiesReservation(name, date, type):
    print("Deleted {} request with name:{} on {}".format(type, name, date))

def getDetailedReservation(name):

    y = (("A", 3, '2020-12-22', "2021-01-2", "A", "A01"), ("B", 4, '2020-12-22', "2021-01-2", "A", "A02"))
    for i in y:
        if i[0]==name:
            x = i
    return x

def updateRReservation(name, data):
    print("UPDATED RReservation with name {} set values {}".format(name, data))
