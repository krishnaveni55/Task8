#1.create a python class circle with construtor which will take list as arguments.
#The list is [10,501,22,37,100,999,87,351]
class Circle:
 def __init__(self,a):
   self.a=a
 def number(self):
    print(self.a)
p= Circle("10,501,22,37,100,999,87,351")
p.number()

#2.create a proper member variable inside the task if required and use them when necessary.
#this task create a class private variable pi=3.141
class myClass:
    a = 3.141
    def __privMeth(self):
      print("Im inside class myClass")
    def hello(self):
       print("Private Variable value: ",myClass.a)
f = myClass()
f.hello()
f.a

#3.from thge given list create two class method area and parameter which will be going
#to calculate area of perimeter
class Circle():

 def __init__(self, r):
    self.radius = r
 def area(self):
   return self.radius**3.141
 def perimeter(self):
  return 2*self.radius*3.141
NewCircle = Circle(7)
print(NewCircle.area())
print(NewCircle.perimeter())
#4.url convert uml diagram into python class and its method.
class Tv:
    def __init__ (self,brand,price,inch,on_off,vol = 50,ch = 1):
        self.brand = brand
        self.price = price
        self.inch = inch
        self.on_off = on_off
        self.vol = vol
        self.ch = ch

    def vol_up(self):
        if self.vol < 100:
            self.vol += 1
        else:
            return "Max Volume"
    
    def vol_down(self):
        if self.vol > 0:
            self.vol -= 1
        else:
            return "Min Volume"       
            
    def ch_up(self):
        if self.ch < 50:
            self.ch += 1
        else:
            return "Max Channel"
    
    def ch_down(self):
        if self.ch > 0:
            self.ch -= 1
        else:
            return "Min Channel"   

    def ch_set(self,s_ch):
        if s_ch < 50 and s_ch > 1:
            self.ch = s_ch
            return self.ch
    
    def reset(self):
        self.ch = 1
        self.vol = 50
    
    def status(self):
        return "{} is at channel {} and volume {}".format(self.brand,self.ch,self.vol)

class Led_Plasma(Tv):
    def __init__(self,Screen_Thickness,Energy_Usage,Life_Span,Refresh_Rate,View_Angle,Back_Light):
        self.Screen_Thickness = Screen_Thickness
        self.Energy_Usage = Energy_Usage
        self.Life_Span = Life_Span
        self.Refresh_Rate = Refresh_Rate
        self.View_Angle = View_Angle
        self.Back_Light = Back_Light


obj = Tv("panasonic",50000,55,"on")
#chup_func = obj.ch_up()
#chdown_func = obj.ch_down()
#volup_func = obj.vol_up()
#voldown_func = obj.vol_down()
#ch_set_func = obj.ch_set()
reset_func = obj.reset()
status_func = obj.status()
print(status_func)  