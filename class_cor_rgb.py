
class CorRGB:
    def __init__(self, red, green, blue):
        self.red   = max(min(red,1.0),0.0)
        self.green = max(min(green,1.0),0.0)
        self.blue  = max(min(blue,1.0),0.0)

    def __repr__(self):
        STRred = str(int(255*self.red))
        STRgreen = str(int(255*self.green))
        STRblue = str(int(255*self.blue))
        return STRred+" "+STRgreen+" "+STRblue    
