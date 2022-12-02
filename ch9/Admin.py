from dog import User

#A simple attempt at Exercise 9-7
class Admin(User):
    """An attempt to describe the privileges of an Admin."""
    def __init__(self, first_name, last_name, *other_info):
        """Initializing the attributes of the parent class."""
        super().__init__(first_name, last_name, *other_info)
        self.privileges = []

    def show_privileges(self):
        """A list of administrator's set of privileges."""
        print("\nThe administrator has the following privileges:")
        for privileges in self.privileges:
            print(f"-{privileges}")

my_admin = Admin("ebuka", "ihekwereme", "location:Lagos")
my_admin.privileges = ("can add post", "can delete post", "can ban user")

my_admin.show_privileges()