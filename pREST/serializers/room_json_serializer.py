import json


# Room object -> json encoding
class RoomJsonEncoder(json.JSONEncoder):
    def default(self, o: object):
        try:
            to_serialize = {
                "code": str(o.code),
                "size": o.size,
                "price": o.price,
                "latitude": o.latitude,
                "longitude": o.longitude,
            }
            return to_serialize
        except AttributeError:
            return super().default(o)
