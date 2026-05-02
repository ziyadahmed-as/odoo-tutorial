# -*- coding: utf-8 -*-
# Create Books
books_data = [
    {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'isbn': '9780743273565', 'genre': 'fiction'},
    {'title': '1984', 'author': 'George Orwell', 'isbn': '9780451524935', 'genre': 'fiction'},
    {'title': 'The Hobbit', 'author': 'J.R.R. Tolkien', 'isbn': '9780547928227', 'genre': 'fiction'},
    {'title': 'Clean Code', 'author': 'Robert C. Martin', 'isbn': '9780132350884', 'genre': 'other'},
]

created_books = []
for data in books_data:
    # Avoid duplicates
    existing = env['library.book'].search([('isbn', '=', data['isbn'])])
    if not existing:
        book = env['library.book'].create(data)
        created_books.append(book)
        print(f"Created Book: {book.title}")
    else:
        created_books.append(existing[0])
        print(f"Book already exists: {existing.title}")

# Find a partner (user)
partner = env['res.partner'].search([('name', 'ilike', 'Ziyad')], limit=1) or env.user.partner_id
print(f"Assigning loan to: {partner.name}")

# Create a Loan if no active loan exists for the first book
if created_books:
    existing_loan = env['library.loan'].search([('book_id', '=', created_books[0].id), ('state', '=', 'active')])
    if not existing_loan:
        loan = env['library.loan'].create({
            'book_id': created_books[0].id,
            'partner_id': partner.id,
            'loan_date': '2026-05-01',
            'return_date': '2026-05-15',
        })
        print(f"Created Loan for: {loan.book_id.title}")
    else:
        print(f"Loan already exists for: {created_books[0].title}")

env.cr.commit()
print("Demo data successfully processed.")
