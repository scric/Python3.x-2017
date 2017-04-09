# 物品清单
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


# 建立一个 displayInventory() 函数 , 它可以接受任何可能的物品清单, 并显示 .
def displayInventory(inventory):
    print("Inventory: ")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print("Total number of items: " + str(item_total))

# displayInventory(stuff)

# 好了, 现在我们杀死了一条巨龙, 获得了它的战利品, 列表如下
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'ruby']

# 我们要写一个名为 addToInventory(inventory, addedItems) 的函数, 表示更新过后的物品清单

# def addToInventory(inventory, addedItems):
#     # 我们应该先把 addedItems 这个列表转化为字典
#     things = {}
#     for i in addedItems:
#         things.setdefault(i, 0)
#         things[i] += 1
#     # 转化完后, 应该将 things 字典中的值添加到 inventory 中去
#     for k in things:
#         inventory.setdefault(k, 0)
#         inventory[k] += 1
#     return inventory
# 应该使用两个字典合并的 方法来修改.


def addToInventory2(inventory, addedItems):
    # 错误版本.
    # for item in dragonLoot:  # 循环列表里的项目
    #     if item not in inventory.keys():  # 如果 item 不在 inventory 的键里面, 则将 item 作为 inventory 字典中的一个键, 并给定键值, 键值为 addedItems 列表中 item 表项相同值的总数
    #         inventory.setdefault(item, addedItems.count(item))  # 错误就在这里, 如果列表中存在两个不存在的相同的表项 , 第一个表项被添加进去为新的键, 键值为 2 , 第二个相同的表项执行 else 语句, 自增 1, 所以键值变成了 3 . 故错误
    #     else:
    #         inventory[item] += 1
    # return inventory

    # for items in addedItems:
    #     if items not in inventory.keys():
    #         inventory.setdefault(items, 0)
    #         inventory[items] +=1
    #     else:
    #         inventory[items] += 1
    # return inventory
    # 修改一下, 不用判断

    for items in addedItems:
        inventory.setdefault(items, 0)
        inventory[items] += 1
    return inventory

inv = {'gold coin': 42, 'rope': 1}
inv = addToInventory2(inv, dragonLoot)
displayInventory(inv)
