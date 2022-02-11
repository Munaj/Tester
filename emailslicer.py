#get user email
email = input("Enter your email:").strip()

#slice out user name
user_name = email[:email.index("@")]
#slice out domain name
domain_name = email[email.index("@")+1:]
#format message
output = f"Your user name is: {user_name} and  your domain name is: {domain_name}"
#display output message
print(output)
