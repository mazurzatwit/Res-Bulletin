import mysql.connector

connection = mysql.connector.connect(host='localhost',
                                         database='Res Bulletin',
                                         user='root')
cursor = connection.cursor()



class Card:

    def _init_(self, eventName, date, time, location, caName, yes, no, maybe, tags):
        self.name = eventName
        self.date = date
        self.time = time
        self.location = location
        self.caName = caName
        self.yes = yes
        self.no = no
        self.maybe = maybe
        self.tags = tags #class attributes instead?? cause they be shared by all cards???
    
    #def create(self, card): #Need help implementing

    #def edit(self, card): #Need help implementing

    #def delete(self, card): #Need help implementing