class User:
    """
    This class for users
    """
    def __init__(self, user_id = "0", user_name = "None", user_followers = 0, user_following = 0):
        self.id = user_id
        self.name = user_name
        self.followers = user_followers
        self.following = user_following


user_1 = User ("001", "Ahmed", "1000", "10")

print (user_1.id)
print (user_1.name)
print (user_1.followers)
print (user_1.following)
