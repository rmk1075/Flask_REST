from typing import Dict


# Entity layer
class Room:
    def __init__(self, code: str, size: int, price: int, longitude: float, latitude: float):
        self.code = code
        self.size = size
        self.price = price
        self.latitude = latitude
        self.longitude = longitude

    @classmethod
    def from_dict(cls, adict: Dict):
        return cls(
            code=adict["code"],
            size=adict["size"],
            price=adict["price"],
            latitude=adict["latitude"],
            longitude=adict["longitude"],
        )

    def to_dict(self):
        return {
            "code": self.code,
            "size": self.size,
            "price": self.price,
            "latitude": self.latitude,
            "longitude": self.longitude,
        }

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()