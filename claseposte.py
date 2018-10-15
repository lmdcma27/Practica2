
class poste():
    def __init__(self):
        self.items = []

    def condicion_poste(self):
        return self.items == []

    def recibir(self, item):
        self.items.append(item)

    def entregar(self):
        self.items.pop()

    def longitud(self):
        return len(self.items)

    def e_superior(self):
        return self.items[len(self.items) - 1]

    def get_items(self):
        return self.items

   
   




