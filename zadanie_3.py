class Property:
    def __init__(self, area: float, rooms: int, price: int, address:str):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address


class House(Property):
    def __init__(self, area: float, rooms: int, price: int, address: str, plot:int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return (f"House | Area: {self.area} m2, Rooms: {self.rooms}, "
                f"Plot: {self.plot} m2, Price: {self.price}, "
                f"Address: {self.address}")


class Flat(Property):
    def __init__(self, area: float, rooms: int, price: int, address: str, floor: int):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return (f"Flat | Area: {self.area} m2, Rooms: {self.rooms}, "
                f"Floor: {self.floor}, Price: {self.price}, "
                f"Address: {self.address}")

house=House(120, 5, 850000, "Policyjna 62/6", 500)
flat=Flat(65, 3, 20000000, "Brynowska 26", 4)

print(house)
print(flat)
