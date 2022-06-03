import json
import random
import urllib.request

HOST = 'localhost'
PORT = 8069
DB = "newprodb"
USER = 'admin'
PASS = 'admin'

def json_rpc(url, method, params):
    data = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params,
        "id": random.randint(0, 1000000000),
    }
    req = urllib.request.Request(url=url, data=json.dumps(data).encode(), headers={
        "Content-Type":"application/json",
    })
    reply = json.loads(urllib.request.urlopen(req).read().decode('UTF-8'))
    if reply.get("error"):
        raise Exception(reply["error"])
    return reply["result"]

def call(url, service, method, *args):
    return json_rpc(url, "call", {"service": service, "method": method, "args": args})

# log in the given database
url = "http://%s:%s/jsonrpc" % (HOST, PORT)
print("URL...........",url)
uid = call(url, "common", "login", DB, USER, PASS)
print("uid...........",uid)

# create a new note
# args = {
#     'memo': 'This is another note',
# }
# note_id = call(url, "object", "execute", DB, uid, PASS, 'note.note', 'create', args)
# print("Created note...",note_id)

# create new customer
# args = {
#     'customer_name': 'Test note for json customer',
# }
# customer_id = call(url, "object", "execute", DB, uid, PASS, 'customer.details', 'create', args)
# print("Created note...",customer_id)

# read operation

# read_data = call(url, "object", "execute", DB, uid, PASS, 'customer.details', 'read', [1])
# print("read data for customer...",read_data)

# write/update operation
# vals = {
#     'customer_name': 'Devyani....update',
# }
# update_data = call(url, "object", "execute", DB, uid, PASS, 'customer.details', 'write', [10], vals)
# print("update data for customer...",update_data)

#delete operation
# delete_data = call(url, "object", "execute", DB, uid, PASS, 'customer.details', 'unlink', [13])