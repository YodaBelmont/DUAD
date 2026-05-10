user_logged_in = True


def requires_login(func):
    def wrapper(user):
        if user_logged_in == False:
            print(f"USER MUST BE LOGGED IN TO PROCEED")
            return
        func(user)

    return wrapper


@requires_login
def show_profile(user):
    print(f"Showing {user} profile...")


show_profile("Esteban")
