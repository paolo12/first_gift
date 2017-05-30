def golf(password):
    pword = str(password)
    a = b = c =0
    for i in pword:
            if 'a' <= i <= 'z':
                a += 1
            elif 'A' <= i <= 'Z':
                b += 1
            elif '0' <= i <= '9':
                c += 1
    if a != 0 and b != 0 and c != 0 and len(pword) >= 10:
        return True
    else:
        return False


# if __name__ == '__main__':
#     # These "asserts" using only for self-checking and not necessary for auto-testing
#     golf('A1213pokl') == False
#     golf('bAse730onE') == True
#     golf('asasasasasasasaas') == False
#     golf('QWERTYqwerty') == False
#     golf('123456123456') == False
#     golf('QwErTy911poqqqq') == True
#     print("Use 'Check' to earn sweet rewards!")

print(golf('asasasasasasasaas'))
