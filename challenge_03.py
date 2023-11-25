import requests

def validate_passwords(password_list):
    valid_count = 0
    invalid_count = 0
    password_invalid_42 = ''

    for poli_password in password_list:
        policy, password = poli_password.split(':')
        bounds, char = policy.split(' ')
        min_limit, max_limit = map(int, bounds.split('-'))
        char_count = password.count(char)

        if min_limit <= char_count <= max_limit:
            valid_count += 1
        else:
            invalid_count += 1
            if invalid_count == 42:
                password_invalid_42 = password
    
    result = [valid_count, invalid_count, password_invalid_42]
    return result

# Get input
# url = 'https://codember.dev/data/encryption_policies.txt'

url = input('Ingrese la URL: ')
response = requests.get(url)
password_text = response.text
password_list = password_text.split('\n')

validate_pass = validate_passwords(password_list)

print(f'Total valid passwords: {validate_pass[0]}')
print(f'Total invalid passwords; {validate_pass[1]}')
print(f'Password invalid number 42: {validate_pass[2]}')
