import json

# json to dict loads
# # some JSON:
# x =  '{ "name":"John", "age":30, "city":"New York"}'
# print(type(x))
# y = json.loads(x)
# print(type(y))
# print(y)

# # dict to json dumps
# import json
#
# # a Python object (dict):
# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }
# print(type(x))
# # convert into JSON:
# y = json.dumps(x)
# print(type(y))
#
# # the result is a JSON string:
# print(y)


# import json
#
# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# print(json.dumps(x))
# print(json.dumps(x, indent=4))
# print(json.dumps(x, indent=4, separators=(". ", " = ")))
print(json.dumps(x, indent=4, sort_keys=True))
