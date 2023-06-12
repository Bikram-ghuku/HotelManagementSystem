import mysql.connector


conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotelmanagementsystem")
curs = conn.cursor()

def check_logindb(username, password):
    quer = "SELECT * FROM login WHERE USERNAME='{}' AND PASSWORD='{}'".format(str(username), str(password))
    curs.execute(quer)
    result = curs.fetchall()
    x = result!=[]
    return x

def getEmptyRooms():
    quer = "SELECT * FROM roomsavail WHERE booked=False"
    curs.execute(quer)
    result = curs.fetchall()
    n = len(result)
    return n

def getBookRooms():
    quer = "SELECT * FROM roomsavail WHERE booked=True"
    curs.execute(quer)
    result = curs.fetchall()
    n = len(result)
    return n

def getAmenitiesBooked() -> int:
    n = len(getAmenitiesReservation())
    return n

def getTablesBooked() -> int:
    n = len(getResturantReservation())
    return n

def returnBkRByType():
    quer = "SELECT Type, count(Type) FROM roomsavail WHERE Booked=1 Group By Type"
    curs.execute(quer)
    result = curs.fetchall()
    x={}
    for i in result:
        x[i[0]] = i[1]
    return x

def makeRoomReservation(Name, noGuest, rType, cinDate, cOutDate, bDate):
    d = "SELECT Number FROM roomsavail WHERE Booked=0 AND Type='{}'".format(rType)
    curs.execute(d)
    result = curs.fetchall()
    quer = "INSERT INTO rooms VALUES {}".format(((Name, noGuest, rType, result[0][0], cinDate, cOutDate, bDate)))
    quer2 = f"UPDATE roomsavail SET Booked = 1 WHERE Number='{result[0][0]}'"
    curs.execute(quer)
    conn.commit() 
    curs.execute(quer2)
    conn.commit() 

def getRoomReservation():
    quer = "SELECT Name, guests, cindate, cout, rType, rnumber FROM rooms";
    curs.execute(quer)
    result = curs.fetchall()
    return result

def updateReservation(data, name):
    quer = f"UPDATE rooms SET guests={data[1]}, cindate='{data[2]}', cout='{data[3]}', rType='{data[4]}', rnumber='{data[5]}' WHERE name='{name}'"
    curs.execute(quer)
    conn.commit()

def deleteReservation(data):
    quer = f"DELETE FROM rooms WHERE name='{data[0]}' AND guests={data[1]} AND cindate='{data[2]}' AND cout='{data[3]}' AND rType='{data[4]}' AND rnumber='{data[5]}'"
    curs.execute(quer)
    quer2 = f"UPDATE roomsavail SET Booked =0 WHERE Number='{data[5]}'"
    curs.execute(quer2)
    conn.commit()

def insertResturantResrvation(name, noGuest, date):
    quer = "INSERT INTO resturant VALUES {}".format((name, noGuest, date))
    curs.execute(quer)
    conn.commit()

def getResturantReservation():
    quer = "SELECT * FROM resturant"
    curs.execute(quer)
    x = curs.fetchall()
    return x

def deleteResturant(name, date):
    quer = "DELETE FROM resturant WHERE name='{}' AND date='{}'".format(name, date)
    curs.execute(quer)
    conn.commit()

def insertAmenitiesRequest(name, noGuests, date, type):
    quer = "INSERT INTO amenities VALUES {}".format((name, noGuests, date, type))
    curs.execute(quer) 

def getAmenitiesReservation():
    quer = "SELECT * FROM amenities"
    curs.execute(quer)
    x = curs.fetchall()
    return x

def deleteAmenitiesReservation(name, date, type):
    quer = f"DELETE from amenities WHERE name='{name}' and date='{date}' and type='{type}'"
    curs.execute(quer)

def getDetailedReservation(name):
    x = tuple()
    y = getRoomReservation()
    for i in y:
        if i[0] == name:
            x = i

    return x

def updateRReservation(name, data):
    quer = f"UPDATE resturant set noGuest={data[1]}, date='{data[2]}' WHERE name = '{name}'"
    curs.execute(quer)
    conn.commit()
