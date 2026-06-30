letter='''Dear <|Name|>,
You are selected!
<|Date|>'''
name=input("Enter name ")
date=input("Enter Date ")

print(letter.replace("<|Name|>",name).replace("<|Date|>",date))
