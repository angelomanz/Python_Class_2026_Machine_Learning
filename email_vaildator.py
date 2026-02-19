email1 = 'user@company.com'
email2 = 'invaild.email'
email3 = 'USER@EMAIL.COM'
for email in [email1, email2, email3]:
    email = email.strip()
    email = email.lower()
    if '@' in email and ',' in email:
        print(email + ' -Valid')
    else:
        print(email + ' -Invaild')
        