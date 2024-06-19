Name = input (" Enter your UserName :")
Email = input("Enter your Email Address :")
handle = open ("python/data.txt","a")
handle.write(Name)
handle.write(Email)
handle.write("\n")


