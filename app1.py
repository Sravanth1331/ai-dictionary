import difflib
from difflib import get_close_matches
import json

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    
    elif w.title() in data:
        return data[w.title()]
    
    elif w.upper() in data:
        return data[w.upper()]
        
    elif len(get_close_matches(w,data.keys(),cutoff = 0.5)) > 0:
        yn = input("Did you mean %s instead? enter Y if yes or N if no " %get_close_matches(w,data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w,data.keys())[0]]
        else:
            return "Please enter the correct word"
    
    else:
        return "Please double check the word"

word = input("enter a word: ")

output = (translate(word))

if type(output) == list:
    for item in output:
        print(item)

else:
    print(output)
