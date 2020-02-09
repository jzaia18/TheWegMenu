import pymongo, json, hashlib, os

DIR = os.path.dirname(__file__) or '.'
dbname = json.loads(open(DIR + "/../secrets.JSON").read())['mongo']

connection = pymongo.MongoClient(dbname)
db = connection.thewegmenu
users = db.users

def get_hashed_password(user, passw):
    return hashlib.sha256((passw + user).encode('utf-8')).hexdigest()

def register( user, passw ):
    if user_exists(user):
        return False
    hashed = get_hashed_password(user, passw)
    users.insert_one({'user': user, 'hashed': hashed })
    return True

def authenticate(user, passw):
    hashed = get_hashed_password(user, passw)
    info = users.find_one({'user': user})
    if info and info['hashed'] == hashed:
        return True
    else:
        return False

def user_exists(user):
    if users.find_one({'user': user}):
        return True
    return False


if __name__ == '__main__':
    print(register("bob", "1234"))
    print(register("bob", "1234"))
    print(authenticate("bob", "1234"))
    print(authenticate("bob", "12345"))
    print(authenticate("bobo", "12345"))
