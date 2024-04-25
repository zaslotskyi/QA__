import string

email = "aaa@bbb.ccc"

found = False

if (email.index("@") < email.index(".")
        and email[0] != "@"
        and email[-1] != "."
        and email.count("@") == 1
        and email.count(".") == 1):
    for char in email:
        if char not in string.ascii_letters + string.digits + "@.":
            found = True
            break
    if not found:
        print(True)
    else:
        print(False)
else:
    print(False)



