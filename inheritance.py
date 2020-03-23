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
