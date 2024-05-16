import re


def can_be_email(email):
    pattern = r'[\w\d]+@{1}[a-z]+\.[a-z]+$(?!.*\.$)'

    return bool(re.match(pattern, email))


assert can_be_email("aaa@bbb.ccc"), 'Test1'
assert not can_be_email("@aaa@bbb.ccc"), 'Test2'
assert not can_be_email("aaa@bbb.ccc."), 'Test3'
assert can_be_email("aaa777@bbb.ccc"), 'Test4'
assert not can_be_email("aaa.bbb@ccc"), 'Test5'
assert not can_be_email('aaabbb.ccc'), 'Test6'
assert not can_be_email('aaa@bbbccc'), 'Test7'
assert not can_be_email('aaabbbccc'), 'Test8'
assert not can_be_email('aaa@bbb.ccc#'), 'Test9'
print('Passed')
