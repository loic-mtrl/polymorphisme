class phone:
    def __init__(self, name, battery):
        self.battery = battery
        self. name = name
    def showOS():
        pass

class apple(phone):
    def showOS(self):
        return "IOS"

class samsung(phone):
    def showOS(self):
        return "android"

class xiaomi(phone):
    def showOS(self):
        return "android"

iphone = apple("Iphone 16", 42)
samsungPhone = samsung("samsung s24", 99)
xiaomiPhone = xiaomi("xiaomi 14", 17)

for phone in (iphone, samsungPhone, xiaomiPhone):
    print("----------------------------------")
    print(phone.name)    
    print(f'Battery level : {phone.battery}')
    os = phone.showOS()
    print(f'Phone os : {os}')
    print("----------------------------------")
