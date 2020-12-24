import re 

def validate_email(email):
    
    regex = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$'
    search_obj = re.search(regex, email)
    if (search_obj):
        if (search_obj.group(0) == email):
            return True
        else: 
            return False
    else: 
        return False

def validate_password(passwd): 
      
    SpecialSym =['$', '@', '#', '%', '!'] 
      
    if len(passwd) < 6: 
        return 'Password length should be at least 6'    
          
    if not any(char.isdigit() for char in passwd): 
        return 'Password should have at least one numeral'
        
          
    if not any(char.isupper() for char in passwd): 
        return 'Password should have at least one uppercase letter'
        
          
    if not any(char.islower() for char in passwd): 
        return 'Password should have at least one lowercase letter'
        
          
    if not any(char in SpecialSym for char in passwd): 
        return 'Password should have at least one of the symbols $ @ # !'
    
    return 'valid'