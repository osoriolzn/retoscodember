import requests

def mini_compiler(input_str):
    num_result = 0
    output_str = ''

    for symbol in input_str:
        if symbol == '#':
            num_result += 1
        elif symbol == '@':
            num_result -= 1
        elif symbol == '*':
            num_result *= num_result
        elif symbol == '&':
            output_str += str(num_result)
    
    return output_str

# Get input
# Url: https://codember.dev/data/message_02.txt

url = input('Ingrese la URL: ')
response = requests.get(url)

if response.status_code == 200:
    input_1 = response.text
    result = mini_compiler(input_1)
    print(result)
else:
    print(f'No se pudo obneter el input. Código del estado: {response.status_code}')