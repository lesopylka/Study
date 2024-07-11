uni_objects = set()
for obj in objects:
    uni_objects.add(id(obj))

ans = len(uni_objects)
print(ans)