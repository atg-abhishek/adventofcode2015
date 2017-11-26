from pprint import pprint 
import hashlib 
secret_key = "iwrupvqb"

num = 1

while True:
    m = hashlib.md5()
    input_string = (secret_key+str(num)).encode('utf-8')
    m.update(input_string)
    hashed = m.hexdigest()
    
    if hashed[:6] == "000000":
        break
    num+=1

pprint(num)