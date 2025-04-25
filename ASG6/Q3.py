def default(length,unit):
    if(unit == 'inches'):
        return length*0.08333333
    elif(unit == 'yards'):
        return length*3
    elif(unit == 'miles'):
        return length*5280
    elif(unit == 'kilometers'):
        return length*3280.84
    elif(unit == 'meters'):
        return length*3.28084
    elif(unit == 'centimeters'):
        return length*0.0328084
    return length*0.00328084

class Converter:
    def __init__(self,length,unit):
        self.length = length
        self.unit = unit
        if(self.unit != 'feet'):
            self.length = default(self.length,self.unit)

    def inches(self):
        return format(self.length*12,".2f")
    def feet(self):
        return format(self.length,".2f")
    def yards(self):
        return format(self.length*0.333333,".2f")
    def miles(self):
        return format(self.length*0.000189394,".6f")
    def kilometers(self):
        return format(self.length*0.0003048,".6f")
    def meters(self):
        return format(self.length*0.3048,".3f")
    def centimeters(self):
        return format(self.length*30.48,".2f")
    def millimeters(self):
        return format(self.length*304.8,".2f")
    
c = Converter(9,'meters')
print(c.inches())
print(c.feet())
print(c.yards())
print(c.miles())
print(c.kilometers())
print(c.meters())
print(c.centimeters())
print(c.millimeters())