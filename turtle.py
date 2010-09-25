from Tkinter import *
from math import *

class TurtleClass(object):
	"the turtle class "	
	def __init__(self,c):
		self.c = c
		self.angle = 0.000001 
		self.x,self.y = 0,0
		self.l1,self.l2,self.l3 = 0,0,0
		self.x1,self.x2,self.x3,self.y1,self.y2,self.y3 = 0,0,0,0,0,0
	def dr_tur(self,x=300,y=300):
		"draws the turtle"
		self.del_tur()
		self.x,self.y=x,y
		self.x1,self.y1=self.x+30,self.y
		self.x2,self.y2=self.x,self.y-15
		self.x3,self.y3=self.x,self.y+15
		self.l1 = self.c.create_line(self.x1,self.y1,self.x2,self.y2)	
		self.l2 = self.c.create_line(self.x1,self.y1,self.x3,self.y3)	
		self.l3 = self.c.create_line(self.x3,self.y3,self.x2,self.y2)
	def del_tur(self):
		"deletes the turtle"
		self.c.delete(self.l1)	
		self.c.delete(self.l2)	
		self.c.delete(self.l3)
	def mv_fwd(self,d):
		"forward move"
		self.del_tur()
		a = cos(self.angle*pi/180)*d
		b = sin(self.angle*pi/180)*d
		self.l4 = self.c.create_line(self.x,self.y,self.x+a,self.y-b) 
		self.x = self.x + a
		self.y = self.y - b
		self.rt_lt(0)
		
	def rt_lt(self,angle):
		"rotate left"
		self.angle =self.angle + angle
		self.del_tur()
		a = sin(self.angle*pi/180)*30  
		b = a/tan(self.angle*pi/180)
		self.x1 = self.x + b
		self.y1 = self.y - a
		c = cos(self.angle*pi/180)*15
		d = sin(self.angle*pi/180)*15
		self.x2 = self.x - d
		self.y2 = self.y - c
		e = cos(self.angle*pi/180)*15
		f = sin(self.angle*pi/180)*15
		self.x3 = self.x + f
		self.y3 = self.y + e
		self.l1 = self.c.create_line(self.x1,self.y1,self.x2,self.y2)
                self.l2 = self.c.create_line(self.x1,self.y1,self.x3,self.y3)
                self.l3 = self.c.create_line(self.x3,self.y3,self.x2,self.y2)
	def rt_rt(self,angle):
		"rotate right"
		self.rt_lt(angle*-1)
  

r=Tk()
c=Canvas(width=600,height=600)
c.pack()

