# -*- coding: utf-8 -*-
# Get module
module = env['ir.module.module'].search([('name', '=', 'library_management')])
if module.state != 'installed':
    print("Installing library_management module...")
    module.button_immediate_install()
    env.cr.commit()

# Create Books
books_data = [
    {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'isbn': '9780743273565', 'genre': 'fiction'},
    {'title': '1984', 'author': 'George Orwell', 'isbn': '9780451524935', 'genre': 'fiction'},
    {'title': 'The Hobbit', 'author': 'J.R.R. Tolkien', 'isbn': '9780547928227', 'genre': 'fiction'},
    {'title': 'Clean Code', 'author': 'Robert C. Martin', 'isbn': '9780132350884', 'genre': 'other'},
]

created_books = []
for data in books_data:
    book = env['library.book'].create(data)
    created_books.append(book)
    print(f"Created Book: {book.title}")

# Find a partner (user)
partner = env['res.partner'].search([('name', 'ilike', 'Ziyad')], limit=1) or env.user.partner_id
print(f"Assigning loan to: {partner.name}")

# Create a Loan
loan = env['library.loan'].create({
    'book_id': created_books[0].id,
    'partner_id': partner.id,
    'loan_date': '2026-05-01',
    'return_date': '2026-05-15',
})
print(f"Created Loan for: {loan.book_id.title}")

env.cr.commit()
print("Demo data successfully loaded.")
