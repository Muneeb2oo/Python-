post=input("Enter post about which you want to find ")
name=input("Enter Nmae to find post is related or not ")
if(name.lower() in post.lower()):
     print("This Post Is About ",name)
else:
     print("this is not about ",name)