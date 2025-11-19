

def robot_uprising():
    print("BEEP BOOP")

#a class is a blueprint

class Robot:
    consistency = "metal"

    def __init__(self, name, battery_life, processing_power, *args, **kargs):
        print("BEEP BOOP MAKING A NEW ROBOT")
        self.name = name
        self.battery_life = battery_life
        self.processing_power = processing_power
        for key in kargs:
            setattr(self, key, kargs[key])

    def __repr__(self):
        return f"Robot( name={self.name} battery_life={self.battery_life} processing_power={self.processing_power})"
    
    def __str__(self):
        return f"HELLO I AM A ROBOT NAMED {self.name}"

    def beep(self):
        return 'BEEP'
    
    def bend(self):
        return 'Bending'
    
    def move(self):
        return f"I AM MOVING : I AM {self}"
    
    def analyze_info(self, info):
        return f"BEEP BOOP ANALYZING {info}"
    