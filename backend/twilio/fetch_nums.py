import requests
import send_text

response = requests.get('https://randomuser.me/api')

print(response.status_code)
print(response.json())

print()
gender = response.json()['results'][0]['gender']
first_name = response.json()['results'][0]['name']['first']
last_name = response.json()['results'][0]['name']['last']
title = response.json()['results'][0]['name']['title']
age = response.json()['results'][0]['dob']['age']


print(gender)
print(first_name)
print(last_name)
print(title)
print(f'{first_name} {last_name}')
print(age)
# SKY SCOUT

# phone_nums = [3475268228,2674296833,6017918060,4243558411]
phone_nums = [3475268228,2674296833,6017918060,4243558411]

post_mgs = " WORKING BEES "

for num in phone_nums:
    send_text.send_text_msg(num,f"Testing 1: {post_mgs}")
