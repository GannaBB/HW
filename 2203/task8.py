#  Създайте програма, която определя и показва броя на уникалните символи в
# низ, въведен от потребителя. Например, “Здравей, Свят!” има 13 уникални знака, докато
# “zzz” има само един уникален символ. Използвайте речник за решаването на този
# проблем.


try:
    txt = input('Enter your text: ')
except:
    print('Oops, something is wrong')

test = {}
for a in txt:
    test[a] = 1

res = len(test)

print('Your text has ', res, 'unique characters')

