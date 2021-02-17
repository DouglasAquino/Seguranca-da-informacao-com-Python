import phonenumbers

from phonenumbers import geocoder

phone = input('Digite o Telefone: ')

phone_numbers = phonenumbers.parse(phone)

print(geocoder.description_for_number(phone_number, 'pt'))