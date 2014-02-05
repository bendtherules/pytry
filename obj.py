import pyglet as p
list_class=[]
class meta_obj(type):
    def __new__(cls,name,base,clsdict):
        temp_class=type.__new__(cls,name,base,clsdict)
        list_class.append(temp_class)
        cls.priority_order=cls.depth=len(list_class) #by default, priority_order and depth depends on "when class was defined"
        return temp_class

class obj(p.sprite.Sprite):
    __metaclass__=meta_obj
    list_instance=[]
    def __init__(self, *args, **kwargs):
        super(PhysicalObject, self).__init__(*args, **kwargs)
        list_instance.append(self)
        self.velocity_x, self.velocity_y = 0.0, 0.0 # Velocity
        self.list_update=[]

    def update(self, dt):
        """This method should be called every frame."""

        # Update position according to velocity and time
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt

        for update_func in self.list_update:
            update_func(dt)

    def remove_update(self,update_func):
        self.list_update.remove(update_func)