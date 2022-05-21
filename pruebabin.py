import re
entrada="12+56/13"

entrada=[int(s) for s in re.findall(r'\b\d+\b', entrada)]
print (entrada)