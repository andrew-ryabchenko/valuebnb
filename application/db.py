import psycopg2
import hashlib

# Checks if user exists in the database returns `email_hash` if user exists and `False` if one doesn't exist
# Returns 101 if there was a database problem
def exists(uname, passwd):
    try:
        conn = psycopg2.connect("postgres://oqovqoyz:lKFHnpOHJBoVNVH-DNd81C4I-z2jK2PE@otto.db.elephantsql.com:5432/oqovqoyz")
        cursor = conn.cursor()
        query = f"SELECT email_hash FROM users WHERE uname = '{uname}' AND password = '{passwd}';"
        cursor.execute(query)
        result = cursor.fetchall()
        if (len(result)==0):
            return False
        result = result[0][0]
        conn.close()
        return result

    except psycopg2.OperationalError as err:
        # Could not connect to database or other databse issue
        print(err)
        if (conn):
            conn.close()
        return 101

# Returns email_has of newly created user
# Returns `False` if user exists in the database
# Returns 101 if there was a database problem 
def create_user(uname, passwd):
    try:
        conn = psycopg2.connect("postgres://oqovqoyz:lKFHnpOHJBoVNVH-DNd81C4I-z2jK2PE@otto.db.elephantsql.com:5432/oqovqoyz")
        cursor = conn.cursor()
        result = exists(uname, passwd)
        if (result!=101): #Checks if there is database error on exists() call.
            # Response returned by database
            if (not exists(uname, passwd)):
                # User doesn't exist in the database and can be added
                email_hash = hashlib.sha256()
                email_hash.update(bytes(uname, "ascii"))
                email_hash = email_hash.hexdigest()
                query = f"""INSERT INTO users(uname, password, email_hash)
                            VALUES ('{uname}', '{passwd}', '{email_hash}')"""
                cursor.execute(query)
                conn.commit()
                conn.close()
                return email_hash
                
            else:
                # User exists in database and can't be added
                conn.close()
                return False
        else:
            # Could not connect to database on exists() call.
            return 101
    
    except psycopg2.OperationalError as err:
        # Could not connect to database
        if (conn):
            conn.close()
        print(err)
        return 101
