class Device:
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model

    def info(self) -> str:
        return f"{self.brand} {self.model}"


class Laptop(Device):
    def __init__(self, brand: str, model: str, os: str, ram_gb: int):
        super().__init__(brand, model)
        self.os = os
        self.ram_gb = ram_gb

    def info(self) -> str:
        return f"Laptop: {super().info()}, OS: {self.os}, RAM: {self.ram_gb}GB"


class Smartphone(Device):
    def __init__(self, brand: str, model: str, storage_gb: int):
        super().__init__(brand, model)
        self.storage_gb = storage_gb

    def info(self) -> str:
        return f"Smartphone: {super().info()}, Storage:{self.storage_gb}GB"



if __name__ == "__main__":
    laptop= Laptop("Lenovo", "lap18882","Windows 11", 16)
    phone =Smartphone("Samsung","Galaxy S23", 256)

print(laptop.info())
print(phone.info())