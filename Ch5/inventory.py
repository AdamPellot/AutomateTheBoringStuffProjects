#! python3
#  inventory.py - Solution to Fantasy Game Inventory and List to
#                 Dictionary Function for Fantasy Game Inventory
#                 from Automate the Boring Stuff.
# Adam Pellot


# Displays the current inventory of a passed inventory dictionary.
def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        item_total = item_total + inventory.get(k)
        print(str(inventory.get(k)) + ' ' + k)
    print("Total number of items: " + str(item_total))


# Takes an inventory dictionary an added items list and adds those items
# to the dictionary.
def addToInventory(inventory, addedItems):
    for item in addedItems:
        if item in inventory.keys():
            inventory.update({item: inventory.get(item) + 1})
        else:
            inventory[item] = 1
    return inventory


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
