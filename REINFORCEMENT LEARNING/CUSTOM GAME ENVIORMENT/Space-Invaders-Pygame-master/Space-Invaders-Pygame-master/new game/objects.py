import pymunk
from random import randint

class Ball():
    
    def __init__(self,body=pymunk.Body(body_type=pymunk.Body.DYNAMIC),radius=10,color=(255,0,0,100)):
        self.body = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
        self.radius = radius
        self.color = color

        
    def create_ball(self,space,mass=100,elst=1,fric=0):
        self.body.position=(randint(100,700),(randint(100,700)))
        self.shape=pymunk.Circle(self.body,radius=self.radius)
        self.shape.mass=mass
        self.shape.elasticity=elst
        self.shape.friction=fric
        body=pymunk.Body()
        body.position=(randint(100,700),(randint(100,700)))
        space.add(self.body,self.shape)
        return self.shape
 


     
class meteotite(Ball):
    
        def create_ball(self,space,mass=100,elst=1,fric=0):
            self.body.position=(randint(100,700),(randint(100,700)))
            self.shape=pymunk.Poly(  self.body, vertices=[(0,0),(50,50),(25,25),(0,0)], radius=3)
            self.shape.mass=mass
            self.shape.elasticity=elst
            self.shape.friction=fric
            body=pymunk.Body()
            body.position=(randint(100,700),(randint(100,700)))
            space.add(self.body,self.shape)
            return self.shape
         


class spaceship():
    def __init__(self,body=pymunk.Body(body_type=pymunk.Body.DYNAMIC),color=(255,0,0,100)):
        
        self.body = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
        self.body.position=(400,400)
        self.color = color

    
    
    
        
    def create_ball(self,space,mass=100,elst=1,fric=0):
       
        self.shape=pymunk.Poly( self.body, vertices=[(0,0),(50,50),(25,25),(0,0)], radius=3)
        
        self.shape.mass=mass
        self.shape.elasticity=elst
        self.shape.friction=fric
        body=pymunk.Body()
        body.position=(randint(100,700),(randint(100,700)))
        space.add(self.body,self.shape)
        return self.shape
    





















