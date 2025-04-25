length=float(input("Enter a length in feet : "))
a=int(input('''Press
      1 for inches
      2 for yards
      3 for miles
      4 for millimeters
      5 for centimeters
      6 for meters
      7 for kilometers\n'''))

lst=[]
lst.append(length*12)
lst.append(length*0.333333)
lst.append(length*0.000189394)
lst.append(length*304.8)
lst.append(length*30.48)
lst.append(length*0.3048)
lst.append(length*0.0003048)

print(lst[a-1])