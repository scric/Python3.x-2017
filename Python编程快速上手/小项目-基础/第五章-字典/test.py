dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
staff = {}
for i in dragonLoot:
    staff.setdefault(i, 0)
    staff[i] += 1
print(staff)
