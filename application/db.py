import psycopg2

try:
    conn = psycopg2.connect("postgres://oqovqoyz:lKFHnpOHJBoVNVH-DNd81C4I-z2jK2PE@otto.db.elephantsql.com:5432/oqovqoyz")
    cursor = conn.cursor()

except psycopg2.OperationalError as err:
    print(err)

# Checks if user exists in the database
def exists(uname, passwd):
    query = f"SELECT EXISTS (SELECT * FROM users WHERE uname = '{uname}' AND password = '{passwd}')"
    cursor.execute(query)
    result = cursor.fetchall()[0][0]
    return result

# Adds new user to the database
# Returns status code. 100 - Created, 101 - User already exists
def create_user(uname, passwd):
    if (not exists(uname, passwd)):
        query = f"""INSERT INTO users(uname, password)
                    VALUES ('{uname}', '{passwd}')"""
        cursor.execute(query)
        conn.commit()
        return 100
        
    else:
        return 101        