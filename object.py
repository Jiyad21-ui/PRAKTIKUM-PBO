class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, nim, nama):
        self.nim = nim  # Instance attribute
        self.nama = nama  # Instance attribute

# Creating an object of the Dog class
dog1 = Dog("230705113", "jiyad")

print(dog1.nim)
print(dog1.nama)
