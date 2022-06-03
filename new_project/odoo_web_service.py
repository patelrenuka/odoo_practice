url = "http://localhost:8069"
db = "newprodb"
username = 'admin'
password = 'admin'

import xmlrpc.client as xmlrpclib

# common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
# versions=common.version()
# print("Details",versions)
# ORRR


import xmlrpc.client
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
versions=common.version()
print("details",versions)

uid = common.authenticate(db, username, password, {})
print('UID',uid)

models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))
customer_ids=models.execute_kw(db, uid, password,'customer.details', 'search',[[]], {'offset': 2, 'limit': 5})
print("Customers...",customer_ids)

customer_count=models.execute_kw(db, uid, password,'customer.details', 'search_count',[[]])
print("Customers...",customer_count)

customer_record = models.execute_kw(db, uid, password,'customer.details', 'read', [customer_ids],{'fields': ['id','customer_name']})
print("customer_rec...")

for record in customer_record:
    print(record)

search_read_rec=models.execute_kw(db, uid, password,'customer.details', 'search_read',[[]],{'fields': ['id','customer_name'], 'limit': 5})
print("Search_read_record",search_read_rec)
for records in search_read_rec:
    print(records)

# created_new_record = models.execute_kw(db, uid, password, 'customer.details', 'create', [{'customer_name': "Divya",'customer_email':'divya@gmail.com'}])
# print("new Customer",created_new_record)

models.execute_kw(db, uid, password, 'customer.details', 'write', [[4], {'customer_name': "Giri"}])

models.execute_kw(db, uid, password, 'customer.details', 'unlink', [[11]])