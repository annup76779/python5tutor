

def client_function():
    registry_dict = {
        "name": "Anurag",
        "country": "India",
        "email": "anurag@gmail.com",
        "mob_num":"+91 8726771497",
        "password": "password",
    }

    check = server_function(registry_dict) # submitting the form to the server_function
    if check:
        print("Form submitted. ")
    else:
        print("Form not submitted")

def server_function(form_data: dict) -> bool:
    """
        This function will take form data and checks the client input and verify it.
    """

    name = form_data["name"]
    country = form_data["country"]

    # trying to make mob_num optional
    mob_num = form_data.get("mob_num", None)
    email = form_data["email"]
    password = form_data["password"]

    if (name is not None) and (country is not None) and (email is not None) and (password is not None):
        if mob_num is not None:
            print("we Get the mob_num")
        else:
            print("we don't get the mob_num.")

        return True
    else:
        return False


client_function()