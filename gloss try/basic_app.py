import gloss as g
import random
class Test(g.GlossGame):
    def draw(self):
        print g.Gloss.running_slowly
        for count in range(150):
            g.Gloss.draw_box(position = (count,count), width = random.randint(0,128), height = random.randint(0,128), rotation = random.randint(0,360), origin = (0, 0), scale = 1, color = g.Color.WHITE)
    def load_content(self):
        self.bck=g.Texture("content/background.jpg")
app=Test("Testing boss..")
g.Gloss.screen_resolution = 640,480
#g.Gloss.full_screen = True
app.run()