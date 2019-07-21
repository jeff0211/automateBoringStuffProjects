inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'silver coin']

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(k,v)
        item_total += v
    print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):
    for each in addedItems:
        if each in inventory:
            inventory[each] = inventory[each] + 1
        else:
            inventory[each] = 1
    return inventory

inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
