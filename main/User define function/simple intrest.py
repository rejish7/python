def take_values():
    P=int(input("Enter the prin"))
    T=int(input("Enter the time"))
    R=int(input("Enter thr Rate"))
    return[P,T,R]
def calculate():
    P,T,R = take_values()
    return P*T*R / 100

def display():
    print("The simple interst is  :", calculate())
display()  