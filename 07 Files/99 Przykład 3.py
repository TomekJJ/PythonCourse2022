sweets_list = ['chocolate', 'lollipop','cookie', 'candy']


# # z writelines (wymaga dodania \n po każdym elemencie listy)
# with open('save.txt', 'w') as f:
#     f.writelines(sweets_list)

# # z forem
# with open('save.txt', 'w') as f:
#     for i in sweets_list:
#         f.write(i + '\n')

# # z joinem
with open('save.txt', 'w') as f:
    f.write('\n'.join(sweets_list))