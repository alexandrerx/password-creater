 password = input("Enter a password that contains numbers, lowercase and uppercase Latin letters, at least 6 characters long: ")
if len(password) < 6:
        print("Password must be at least 6 characters long.")

    elif re.search('[0-9]', password) is None:
        print("Password must contain at least one digit.")
