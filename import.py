# from calcu import add
#
# print(add(4,6))
# print(dir()) #user defined  modules


# import os
# a=(dir(os))
# print(a)
#os,math,random ,sys ,platform,json
# import json
# c=(dir(json))
# print(c)
import json
x={"name":"sajin","age":12}
y=json.dumps(x)
print(y)     #python to json use dumps
print(type(y))

import json
x='{"name":"sajin","age":12}'
y=json.dump(x)
print(y)
print(type(y))