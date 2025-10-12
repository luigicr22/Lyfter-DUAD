from abc import ABC, abstractmethod
    
class User (ABC):
    
    @abstractmethod
    def __init__(self, user):
        pass

    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def has_permission(self, permission):
        pass


class AdminUser(User):

    def __init__(self,user):
        self.user = user
        self.role = 'Admin'
        self.user_permission = 'full control'
    
    def get_role(self):
        return self.role
    
    def has_permission(self,permission):
        return True
        
class RegularUser(User):
    
    def __init__(self,user,permission):
        self.user = user
        self.role = 'Regular User'
        self.user_permission = permission
    
    def get_role(self):
        return self.role
    
    def has_permission(self,permission):
        if self.user_permission == permission:
            return True
        else:
            return False

user1 = AdminUser("Carlos")
user2 = RegularUser("Andrea",'write')

print(f"Usuario: {user1.user}\nRol: {user1.get_role()}")
print(f"Permiso para modificar: {user1.has_permission('modify')}")
print(f"Permiso para escribir: {user1.has_permission('write')}")
print(f"Permiso para leer: {user1.has_permission('read')}\n")

print(f"Usuario: {user2.user}\nRol: {user2.get_role()}")
print(f"Permiso para modificar: {user2.has_permission('modify')}")
print(f"Permiso para escribir: {user2.has_permission('write')}")
print(f"Permiso para leer: {user2.has_permission('read')}")