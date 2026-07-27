start=int(input("starting limit of force(inN) = "))
end=int(input("ending limit of force(inN) = "))
area= int(input("area(inmm) : "))
stress_limit=float(input("ending limit of material stress(in N/m^2): "))

if area==0:
   print ("not allowed")
   
else: 
        for force in range(start , end ):
            stress = force / area 
            print ('stress=',stress)       
            if stress>=stress_limit:
              print ("danger")
              break 
    
