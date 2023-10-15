class CarAccsess:
    def open(self):
        print('Openning door')

    def close(self):
        print('Close the car door!')


# proxy
class SecuritySystem:
    def __init__(self, door):
        self.door = door

    def open(self, password):
        if self.auntificate(password):
            self.door.open()
        else:
            print("Access denied!")


    def auntificate(self, password):
        return password == 'Ilon'

    def close(self):
        self.door.close() 


if __name__ == "__main__":
    door = SecuritySystem(CarAccsess())

    door.open("Jack")
    door.open("Ilon")
    door.close()
