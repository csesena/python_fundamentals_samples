import re

def validateUID(uid) -> str:
    # 1. Exactly 10 chars
    if len(uid) != 10:
        valid = False
    
    # 2. Alphanumeric only
    elif not uid.isalnum():
        valid = False
    
    # 3. 1+ uppercase  
    elif uid.islower() or not any(c.isupper() for c in uid):
        valid = False
    
    # 4. 2+ digits
    elif sum(c.isdigit() for c in uid) < 2:
        valid = False
    
    # 5. No repeats
    elif len(set(uid)) != 10:
        valid = False
        
    return("Valid" if valid else "Invalid")


print (validateUID("YD780V5355"))