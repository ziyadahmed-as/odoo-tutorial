import xmlrpc.client
url = 'http://localhost:8069'
db = 'odoomanage'
username = 'admin'
password = 'admin'
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
views = models.execute_kw(db, uid, password, 'ir.ui.view', 'search_read', [[('model', '=', 'beltech.project')]], {'fields': ['name', 'xml_id', 'arch_db']})
for v in views:
    print(f"--- View: {v['name']} ({v.get('xml_id')}) ---")
    print(v['arch_db'])
