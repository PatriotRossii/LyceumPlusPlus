import sys
import json


result = {"request": {}, "response": {}}
lines = [e.strip() for e in sys.stdin.readlines()]
for line in lines:
    parameter, value = line.split(" = ")

    if int(value) > 0:
        result["response"][parameter] = value
    elif int(value) < 0:
        result["request"][parameter] = value

with open('contact.json', 'w') as f:
    json.dump(result, f)
