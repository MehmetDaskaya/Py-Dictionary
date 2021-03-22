import json

data = json.load(open("data.json"))
def process():
    word = input("Please enter the word that you want to know.\n")
    word = word.lower()

    if word in data:        
        turned = data[word]
        return turned     
    else:
        print("This word does not exist in this dictionary. Please try another word.\n")
        
while True:
    output = process()
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)
    input("\nPress Enter to continue.")