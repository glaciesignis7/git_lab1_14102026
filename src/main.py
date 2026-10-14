print("Hello, World") 
from datetime import datetime 
print(datetime.now()) 
date = str(datetime.now()) 
print(sum([int(i) for i in date if i in "0123456789"])) 
