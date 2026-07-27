 # input type kinetic energy and potential 
import numpy as np

print ("=" * 60)
m=(np.array([(int(input("Enter mass: ")))]))
h=np.array([int(input("Enter height: "))])
v=np.array ([int( input("Enter velocity:"))])
diameter =np.array([int(input("Enter diameter:"))])
force =np.array([int(input("Enter force: "))])
PE=9.8*m*h
KE=0.5*m*v**2
area=np.pi*(diameter /2)**2
stress =force/area
print ('KE=',KE,'kgm**2')
print ('PE=',PE,'kgm**2sec**2' )
print ('stress=',stress,'kgm**-1sec**2')
print ("=" * 60)
)
