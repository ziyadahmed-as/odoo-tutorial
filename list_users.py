users = env['res.users'].search([])
print("\n=== ALL ODOO USERS ===")
for user in users:
    print(f"Name: {user.name} | Login: {user.login} | Active: {user.active}")

print("\n=== ADMIN/MANAGER USERS ===")
admin_group = env.ref('base.group_erp_manager')
admins = env['res.users'].search([('groups_id', 'in', admin_group.id)])
for user in admins:
    print(f"Admin: {user.name} | Login: {user.login}")
