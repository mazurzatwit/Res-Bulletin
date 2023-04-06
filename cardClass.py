import mysql.connector

connection = mysql.connector.connect(host='localhost',
                                         database='Res Bulletin',
                                         user='root')
cursor = connection.cursor()



class Card:

    def _init_(self, eventName, date, time, location, caName):
        self.name = eventName
        self.date = date
        self.time = time
        self.location = location
        self.caName = caName
    
    def create(self, eventName, eventDate, eventTime, eventLocation, eventCA): #Need help implementing
        formID = 1
        
        add_event = ("INSERT INTO Test (Event_Name, Event_Date, Event_Time, Event_Location, Event_CA, Form_ID) VALUES ('%s', '%s', '%s','%s','%s','%s')" % 
                     ((eventName), (eventDate), (eventTime), (eventLocation), (eventCA), (formID)))

        data_event = {'Event_Name': eventName, 'Event_Date': eventDate, 'Event_Time': eventTime, 'Event_Location': eventLocation, 'Event_CA': eventCA, 'Form_ID': formID}

        cursor.execute(add_event, data_event)

        connection.commit()

        deleteNull = ("DELETE FROM Test WHERE (Event_Name = '')")

        cursor.execute(deleteNull)

        connection.commit()

        #cursor.close()
        #connection.close()

    #def edit(self, card): #Need help implementing

    #def delete(self, card): #Need help implementing