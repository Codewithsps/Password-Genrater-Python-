#Password Genrater to Random in Python Program 
 
import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbol = "@#%!$"
all = lower + symbol  + number   + upper
length = 8
password = "".join(random.sample(all,length))
print( "Print Random Password Genrate: "  + password)
