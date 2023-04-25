class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

operation1 = Operation(12, 3)

print("Le nombre 1 est", operation1.nombre1) # Output: "Le nombre 1 est 12"
print("Le nombre 2 est", operation1.nombre2) # Output: "Le nombre 2 est 3"