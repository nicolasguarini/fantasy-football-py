class Player:
    def __init__(self, name, surname, price, role, strength):
        self.name = name
        self.surname = surname
        self.price = price
        self.role = role
        self.strength = strength
    
    def print_player(self):
        print("---\nName: %s Surname: %s \nRole: %s Price: %d \nStrength: %d\n--\n" % (self.name, self.surname, self.role, self.price, self.strength))
        

class Roles:
    striker = 'striker'
    defender = 'defender'
    midfielder = 'midfielder'
    goalkeeper = 'goalkeeper'
