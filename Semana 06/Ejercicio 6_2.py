global_var = "Variable global"

def get_local_var():
    local_var = "Variable local"
    return local_var


def get_global_var():
    global global_var
    global_var = "Variable global modificada"


print (f"Accediendo a la: {get_local_var()}")
get_global_var()
print (f"Accediendo a la: {global_var}")

