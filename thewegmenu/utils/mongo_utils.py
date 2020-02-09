import pymongo, json, hashlib, os, random, re, sys

DIR = os.path.dirname(__file__) or '.'
dbname = json.loads(open(DIR + "/../secrets.JSON").read())['mongo']

connection = pymongo.MongoClient(dbname)
db = connection.thewegmenu
users = db.users
recipes = db.recipes
calendars = db.calendars

DAYS = {"SUNDAY": [], "MONDAY": [], "TUESDAY": [], "WEDNESDAY": [], "THURSDAY": [], "FRIDAY": [], "SATURDAY": []}

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

def add_recipe(recipe):
    recipes.insert_one(recipe)

def get_recipes_by_food(food, results=20):
    result = list(recipes.find({"label": {"$regex": re.compile(str(food), re.IGNORECASE)}}))
    random.shuffle(result)
    return result[:results]

def add_recipe_to_calendar(recipe_id, day, username):
    day = str(day).upper()
    if day not in DAYS:
        return False
    cal = calendars.find_one({"username": username})
    if cal == None:
        cal = {"username": username, **DAYS}
        cal[day].append(recipe_id)
        calendars.insert_one(cal)
    else:
        calendars.update_one(
            {"username": username},
            {"$push": {day: recipe_id}},
        )
    return True

def remove_recipe_from_calendar(recipe_id, day, username):
    day = str(day).upper()
    cal = calendars.find_one({"username": username})
    if not cal:
        return False
    new_arr = cal[day]
    new_arr.remove(recipe_id)
    calendars.update_one(
        {"username": username},
        {"$set": {day: new_arr}},
    )
    return True


if __name__ == '__main__':
    # print(register("bob", "1234"))
    # print(register("bob", "1234"))
    # print(authenticate("bob", "1234"))
    # print(authenticate("bob", "12345"))
    # print(authenticate("bobo", "12345"))

    # if len(sys.argv) < 2:
    #     print("Please input a food")
    #     exit()


    # print(*[x['label']+"\n" for x in get_recipes_by_food(sys.argv[1])])

    #add_recipe_to_calendar(16, "monday", "bob")
    remove_recipe_from_calendar(12, "sunday", "bob")
