# if mwe want to reuse the variable, we can initialise

class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "alvin")
user_2 = User("002", "Jack")

print(user_1.id)
print(user_1.followers)  # 0, all objects created using this class have followers attribute set up as 0

user_1.follow(user_2)
print(user_1.followers)  # Should still be 0
print(user_1.following)  # Should be 1
print(user_2.followers)  # Should be 1
print(user_2.following)  # Should be 0


# # If we want to create a class without anything in it, we can use pass
# class User:
#     pass
#
#
# user_1 = User()
#
# # Attribute is a vaiable that is associated with the object
# user_1.id = "001"
# user_1.username = "alvin"
#
# print(user_1.username)

"""
In relation to setting up attributes, we can also add method. 

The attributes are the things that the object has and 
the method are the things that the object does

a function that is tied to an object is a method

A method always need to have a self parameter as the first parameter,
this means that when this method is called, it knows the object that called it

in addition to the self parameter, we're goign to pass in the user that we've decided to follow
"""





