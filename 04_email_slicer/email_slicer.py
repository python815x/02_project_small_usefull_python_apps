def main():
    print("Welcome to the email slicer", end="\n")

    email = input("Enter email:")
    username = ''
    domain = ''
    extension = ''

    (username, domain) = email.split('@')
    (domain, extension) = domain.split('.')

    print("User: ", username)
    print("Domain: ", domain)
    print("Extension: ", extension, end="\n")


while True:
    main()
