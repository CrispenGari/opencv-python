import re

string = "The rain in Spain falls mainly in the plain!"
regexp = r'ai{2|1|0}'
print(re.findall(regexp, string))
