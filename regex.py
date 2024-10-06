import re


text: str = 'hello! i am me ?'


print(re.findall(r'[^.?]+', text))


