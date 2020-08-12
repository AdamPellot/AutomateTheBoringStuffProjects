#! python3
# commaCode.py - Takes a list value as an argument and returns a string
#                with all the items separated by a comma and a space,
#                with and inserted before the last item.
# Adam Pellot


# Separates each list value with a comma and space.
def commaCode(listyList):
    finalString = ''
    for item in listyList:
        if item != listyList[len(listyList)-1]:
            finalString = finalString + item + ', '
        else:
            finalString = finalString + 'and ' + item
    return finalString

spam = ['apples', 'bananas', 'tofu', 'cats']
print(commaCode(spam))
