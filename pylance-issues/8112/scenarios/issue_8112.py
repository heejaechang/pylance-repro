from vec2 import vec2


try:
	import ac	
except ImportError:
	from acDevLibs.acDev import ac as ac

class Button:
    def __init__(self, app, text, pos, size, onClick = None):
        return self.pos.y + self.size.y

    def setSize(self, size):
         ac.setSize(self.button, size.x, size.y)

    def maxX(self):
        return self.pos.x + self.size.x
