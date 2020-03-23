class Device:
    def __init__(self,name,connectedby):
        self.name=name 
        self.connectedby=connectedby
        self.connected=True 
    def __str__(self):
        return f"Device {self.name}! connected by: {self.connectedby}"
    def disconnect(self):
        self.connected=False
        print(f"Device: {self.name} disconnected")
    
    def connect(self):
        self.connected=True
        print(f"Device: {self.name} connected")
class Printer(Device):
    def __init__(self,name,connectedby,capacity):
        super().__init__(name,connectedby)
        self.capacity=capacity
        self.remaining_pages=capacity
    def __str__(self):
        return f"{super().__str__()}{self.remaining_pages} pages remaining" 
    def print(self,pages):
        if not self.connected:
           print("OOps, printer is not connected ")
        else:
            print(f"printing {pages} pages")



d1=Printer("HP","USB",30)
d1.disconnect()
d1.print(20)
d1.connect()
d1.print(20)
