from users import Users
from privileges_and_admin import Admin
from privileges_and_admin import Privileges

admin1 = Admin('James', 'Wagner')

admin1.describe_user()
admin1.privileges.show_privileges()