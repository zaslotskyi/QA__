import string

def can_be_email(email):
    if (
        email.count("@") == 1
        and email.count(".") == 1
        and email[0] != "@"
        and email[-1] != "."
        and email.index("@") < email.index(".")
        and "@." not in email
    ):
        for char in email:
            if char not in string.ascii_letters + string.digits + "@.":
                return False
        return True
    else:
        return False

assert can_be_email("aaa@bbb.ccc"), 'Test1'
assert not can_be_email("@aaa@bbb.ccc"), 'Test2'
assert not can_be_email("aaa@bbb.ccc."), 'Test3'
assert can_be_email("aaa777@bbb.ccc"), 'Test4'
assert not can_be_email("aaa.bbb@ccc"), 'Test5'
assert not can_be_email('"aaabbb.ccc"'), 'Test6'
assert not can_be_email('"aaa@bbbccc"'), 'Test7'
assert not can_be_email('"aaabbbccc"'), 'Test8'
print('Passed')
