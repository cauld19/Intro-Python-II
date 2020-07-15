# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, location, finish=True):
        self.name = name
        self.location = location
        self.finish = finish
        
    def __str__(self):
        return f"name: {self.name}, Location: {self.location}"
