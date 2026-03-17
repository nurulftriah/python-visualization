words = ['cat','window','defenestrate']
for w in words:
    print(w, len(w))

users = {'Hans':'active','Eleonore':'inactive','Kentaro':'active'}

for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

print(active_users)
