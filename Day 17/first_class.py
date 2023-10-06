#
# class User:
#     # constructor
#     def __init__(self, user_id, user_name):
#         self.id = str(user_id)
#         self.username = user_name
#         self.followers = 0
#         self.following = 0
#
#     def follow(self, user):
#         user.followers += 1
#         self.following += 1
#
#
#
# class Car:
#
#     # constructor
#     def __init__(self, seats, colour):
#         self.seats = seats
#         self.colour = colour
#
#     def enter_race_mode(self):
#         self.seats = 2
#
#
# user_1 = User("001", "Ricardo")
# user_2 = User("002", "Miguel")
# user_1.follow(user_2)