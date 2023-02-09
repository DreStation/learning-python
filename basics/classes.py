# Parent class
class Gun():
    def shoot(self, magazine):
        self.magazine = magazine

        while (self.magazine > 0):
            self.magazine -= 1
            print("💥🔫 Bam!")

# Child class
class Kalashnikov(Gun):
    # def init means you must use these args on object creation
    def __init__(self, name, type):
        # self. allows you to access these vars
        self.name = name
        self.type = type

        if type == "assault rifle":
            self.magazine = 30
        if type == "machine gun":
            self.magazine = 75

    # Add new shooting functionality
    def shoot(self):
        capacity = self.magazine

        # Run parent method
        super().shoot(self.magazine)

        print("Fired all " + str(capacity) + " bullets")

ak47 = Kalashnikov("AK-47", "assault rifle")
rpk = Kalashnikov("RPK", "machine gun")
print("Name: " + ak47.name)
print("Name: " + rpk.name)

ak47.shoot() # Shoots 30 bullets
rpk.shoot() # Shoots 75 bullets