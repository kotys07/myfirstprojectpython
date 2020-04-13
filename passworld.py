users = {
    'user': "124qwe",
    'user1': "qwe45",
    'user2': "ert5667",
    'user3': "ert567",
    'user4': "sdf456"
}
__chars = set('!@$%^&*()_+.-|\/?,')

user_name = input("Your  userName: ")
password = input("Input your password: ")

try:
    if user_name in users:
        print("Access Granted")
        if not any((c in __chars) for c in password):
            print('Valid password')
        else:
            print('Invalid password')
    else:
        raise KeyError('Invalid')
except KeyError:
    print("Please register")