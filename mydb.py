import json
import os

class Database: 
    
    
    def add_data(self,name,email,password):
        
        # db_file = os.path.join(os.path.dirname(__file__), 'db.json')
        db_file = 'db.json'
        
        # Check file existence and size
        # print(f"Checking file: {db_file}")
        
        # If file doesn't exist or is empty, initialize with empty dict
        if not os.path.exists(db_file) or os.path.getsize(db_file) == 0:
            # print("File doesn't exist or is empty. Initializing empty database.")
            database = {}
        else:
            with open(db_file,'r') as rf:
                try:
                    database = json.load(rf)
                except json.JSONDecodeError:
                    print("Invalid JSON. Reinitializing empty database.")
                    database = {}
                    
        # print(f"Current DB: {database}")
            
        if email in database:
            return 0    # Already exisiting user
        else:
            database[email] = [name,password]
            with open('db.json','w') as wf:
                json.dump(database,wf)
            return 1    # Registration successful
        
    def search(self,email,password):
        
        db_file = 'db.json'
        
        with open(db_file,'r') as rf:
            database = json.load(rf)
            if email in database: 
                if database[email][1] == password:
                    return 1
                else:
                    return 0
            else:
                return 0