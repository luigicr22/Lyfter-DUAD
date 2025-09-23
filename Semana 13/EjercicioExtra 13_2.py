class User:

    def __init__(self, user_name, password):
        self._user_name = user_name
        self._password = password
        self._user_logged_in = False
        print("Usuario creado")
    
    def autentication(self,user,password):
        if self._user_name == user and self._password == password:
            print ("Usuario autenticado")
            self._user_logged_in = True
        else:
            print("Usuario o contraseña incorrectas")

    def requires_login(func):
        def wrapper (self):
            if self._user_logged_in:
                func(self)
            else:
                print("Usuario no autenticado")
        return wrapper

    @requires_login
    def view_profile(self):
        print("\nPerfil del usuario:")
        print (f"Nombre del usuario: {self._user_name}")
        print (f"Contraseña del usuario: {self._password}")

user1 = User("Luis", "1234")
user1.view_profile()
user1.autentication("Luis", "1234")
user1.view_profile()