class User:
    """
    This class for users
    """
    def __init__(self, user_id = "0", user_name = "None", user_followers = 0, user_following = 0):
        self.id = user_id
        self.name = user_name
        self.followers = user_followers
        self.following = user_following

    def follow (self, user):
        user.followers += 1
        self.following += 1

    def print_user (self):
        print (f"User name: {self.name}")
        print (f"User ID: {self.id}")
        print (f"Followers: {self.followers}")
        print (f"Following: {self.following}")

user_1 = User ("001", "Ahmed", 1000, 10)
user_2 = User ("002", "Basam", 2000, 20)

user_1.print_user ()
print ("----------------------")
user_2.print_user ()

print ("=======================================================")
user_1.follow (user_2)

user_1.print_user ()
print ("----------------------")
user_2.print_user ()