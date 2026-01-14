#<...3rd program...>

#<... Email Validator Program...>

print("----<<< Email Validator Program >>>----")
def validate_email(email):
    
    if email.count("@") != 1:              # Checking for exactly one '@'
        return False

    username, domain = email.split("@")

    if username == "" or domain == "":      # Username and domain not be empty
        return False

    if "." not in domain:                    # Domain should contain at least one dot
        return False

    if domain.startswith(".") or domain.endswith("."):
        return False

    return True


email_input = input("Enter an email address: ")

if validate_email(email_input):
    print("Valid Email Address")
else:
    print("Invalid Email Address")
