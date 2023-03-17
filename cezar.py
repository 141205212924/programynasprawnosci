import string

alphabets = string.ascii_lowercase + string.ascii_lowercase

sentence = list(input('wpisz twój tekst: \n').lower())

what_to_do = input(
    'napisz szyfruj aby zaszyfrować, odszyfruj aby zdekodować, wyjscie aby wyjść z programu \n').lower()

shift_number = int(input('wpisz liczbę liter do przesunięcia od 1 do 25: \n'))

end_program = False

while not end_program:
    if what_to_do == 'szyfruj':
        for i in range(len(sentence)):
            if sentence[i] == ' ':
                sentence[i] = ' '
            else:
                new_letter = alphabets.index(sentence[i]) + shift_number
                sentence[i] = alphabets[new_letter]
        print(''.join(map(str, sentence)))
        end_program = True
    elif what_to_do == 'odszyfruj':
        for i in range(len(sentence)):
            if sentence[i] == ' ':
                sentence[i] = ' '
            else:
                new_letter = alphabets.index(sentence[i]) - shift_number
                sentence[i] = alphabets[new_letter]
        print(''.join(map(str, sentence)))
        end_program = True
    else:
        decide = input(
            'złe hasło, spróbuj ponownie T dla TAK, N dla NIE: \n').lower()
        if decide == 't'
            sentence = list(input('wpisz twój tekst: \n').lower())
            what_to_do = input(
                'napisz szyfruj aby zaszyfrować, odszyfruj aby zdekodować, wyjscie aby wyjść z programu \n').lower()
            shift_number = int(input('wpisz liczbę liter do przesunięcia od 1 do 25: \n'))
        else: 
            end_program = True
