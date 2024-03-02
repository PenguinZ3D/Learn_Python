#Create the class
class Solider:
    #the argument 'self' is always passed. It is used to identity the class itself.
    #the function __init__() is used to initalize the class
    def __init__(self, name, health, armor):
        self.name = name
        self.health = health
        self.armor_type = armor

solider = Solider(None, None, None)

def create_solider():
    global solider
    name = input("Enter the name of your Solider: ")
    health = input("Enter the health of your Solider: ")
    armor = input("Enter the armor type of your Solider: ")
    solider = Solider(name, health, armor)

create_solider()

print(solider.name)
print(solider.health)
print(solider.armor)