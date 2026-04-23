user = env['res.users'].search([('login', '=', 'zeda5138@gmail.com')])
if user:
    user.write({'password': 'NewPassword123'})
    env.cr.commit()
    print(f"Password successfully changed for: {user.name} ({user.login})")
else:
    print("User not found!")
