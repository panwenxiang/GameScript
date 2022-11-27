import defAll


handle = defAll.get_handle('夜神模拟器')
print('拿到的handle:', handle)

if handle:
    defAll.template_all_search(handle)

