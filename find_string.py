from hashlib import md5
import random
is_find = False;

def check_validation(s):
    print(s)
    if s[0] != '0' or s[1] != 'e':
        return False

    try:
        float(s[2: len(s)])
    except ValueError:
        return False
        
    return True


while not is_find:
    rand_num = random.randrange(0,100000000000000)
    rand_string = ('0e' + str(rand_num)).encode('utf-8')
    
    md5_string = md5(rand_string).hexdigest()

    if(check_validation(md5_string)):
        is_find = True
        print(rand_string)
    else:
        print(md5_string+' : '+str(rand_string))
    
