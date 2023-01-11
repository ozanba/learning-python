
def house():
    num = input("Kaç katlı olsun: ")
    roof()
   
    m=float(num)
    while m>0: 
        base()
        m=m-1
        
    road()
    

def roof():
    print("Hello this is a house")
    print("     /\\")
    print("    /  \\")
    print("   /    \\")
    print("  /      \\")
    print(" /        \\")
    print("------------")
def base():
    print("|          |")
    print("|          |")
    print("|          |")
    print("|          |")
    print("|          |")
    print("------------")
def road():
    print("  \\    \\")
    print("   \\    \\")
    print("    \\    \\")
    print("     \\    \\")
    
    
    
house()