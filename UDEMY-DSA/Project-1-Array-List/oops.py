# class star:
#     def __int__(self,value):
#         self.value = value
#
#
#
# new1 = star(10)
# new1.value = 10
# new1.value = 20
# print(new1.value)


class youtube:
    def __init__(self,user,sub):
        self.user = user
        self.sub = sub
        print(f"user = {self.user}, sub = {self.sub}")
        if self.sub>100:
            print('sucess')


user1 = youtube("els",10)
user2 = youtube("els1",102)
user1 = youtube("els2",10)



