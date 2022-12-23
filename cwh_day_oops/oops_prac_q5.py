class Train:
    organization = "Indian Railways"

    def __init__(self, trainName, noOfSeats, fare):
        self.train = trainName
        self.noOfSeats = noOfSeats
        self.fare = fare
        print(f"Welcome to {self.train} express !!")

    def getStatus(self):
        print(f"No. of seats remaining in {self.train} express is {self.noOfSeats}")

    def getFare(self):
        print(f"Fare is {self.fare}")

    def bookTicket(self):
        if self.noOfSeats > 0:
            print(f"Your ticket has been booked and Your seat number is {self.noOfSeats}")
            self.noOfSeats = self.noOfSeats - 1
        else :
            print(f"Sorry this train is full, Kindly try in tatkal")

    def cancelTicket(self):
        self.noOfSeats = self.noOfSeats + 1 
        print(f"No. of seats now are {self.noOfSeats}")

kamayani = Train("Kamayani", 2, 720)
kamayani.getFare()
kamayani.getStatus()
kamayani.bookTicket()
kamayani.bookTicket()
kamayani.getStatus()
kamayani.bookTicket()
kamayani.cancelTicket()
kamayani.bookTicket()
kamayani.getStatus()
kamayani.bookTicket()
