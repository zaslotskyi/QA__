import string


def can_be_email(email):
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
            return True
        else:
            return False
    else:
        return False



assert can_be_email("aaa@bbb.ccc") == True, 'Test1'
assert can_be_email("@aaa@bbb.ccc") == False, 'Test2'
assert can_be_email("aaa@bbb.ccc.") == False, 'Test3'
assert can_be_email("aaa777@bbb.ccc") == True, 'Test4'
assert can_be_email("aaa.bbb@ccc") == False, 'Test5'
print('Passed')





