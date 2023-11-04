import requests

def word_count(message):
    words = message.lower().split()
    count = {}
    result = ''
    
    for word in words:
        # Remove any punctuation marks or special characters
        word = ''.join(e for e in word if e.isalnum())
        
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    
    # Create the text string with the required formatting
    for word in words:
        word = ''.join(e for e in word if e.isalnum())

        if word in count:
            result += word + str(count[word])
            del count[word]
    
    return result

# Get the message
# Url: https://codember.dev/data/message_01.txt

url = input('Ingrese la URL: ')
response = requests.get(url)

if response.status_code == 200:
    message_r1 = response.text
    result = word_count(message_r1)
    print(result)
else:
    print(f'No se pudo obneter el mensaje. Código del estado: {response.status_code}')