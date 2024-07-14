n = int(input())
namespaces = {'global':{'parents':None,'vars':set()}}

def create(namespace,parent):
    namespaces[namespace][parent] = {'parents': parent, 'vars':set()}

def add(namespace,var):
    namespaces[namespace][var].add(var)

def get(namespace,var):
    if var in namespaces[namespace]['vars']:
        return namespaces
    elif namespaces[namespace]['parents'] is None:
        return None
    else:
        return get(namespaces[namespace]['parent'],get)

for _ in range(n):
    command = input().split()
    if command[0] == 'create':
        _, namespace, parent = command
        create(parent, namespace)
    if command[0] == 'add':
        _, namespace, var = command
        add(namespace, var)
    if command[0] == 'get':    
        _, namespace, var = command
        print(get(namespace, var))




    