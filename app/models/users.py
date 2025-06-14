import bcrypt
import re

def is_hashed(password):
        return bool(re.match(r'^\$2[aby]\$.{56}$', password))
class User:
    
    
    def __init__(self, uid, email, name,password=None ):
        self.uid = uid
        self.email = email
        if password is not None:
            self.password = self.password = password if is_hashed(password) else self.hash_password(password)
        else:
            self.password = None

        self.name = name

    def hash_password(self, password):
        # Convert to bytes and hash
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    
    def to_dict(self):
        return {
            "uid": self.uid,
            "email": self.email,
            #"password": self.password,
            "name": self.name
        }

    def __str__(self):
        return f"User({self.uid}, {self.email}, {self.name})"