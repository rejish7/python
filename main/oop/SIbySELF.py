class SimpleInterest:
  
    def values(self):
         P=int(input("Enter the principal amount:"))
         T=int(input("Enter the time:"))
         R=int(input("Enter thr Rate of intrest:"))
         return(P,T,R)
    
    def calc(self):
       P,T,R =self.values()
       SI = (P*T*R) /100
       return SI
    
    def display(self):
        SI=self.calc()
        print(f"The simple interst of a number is :{SI}")

odj=SimpleInterest()
odj.display()


         