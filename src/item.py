class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        
    def __str__(self):
        return f"{self.name}, {self.description}"
    
    def on_take(self, i, player):
        print(f"\n*** {player.name} picked up the {i.name}. ***")
        
    def on_drop(self, item, player):
        print(f"\n*** {player.name} dropped the {item.name}. ***")