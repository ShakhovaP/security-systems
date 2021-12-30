import os
import getpass
import datetime
from commands import Commands, commands, execute 
from users import User, users


def logging_in():
    current_user = users['guest']
    while True:
        get_user = 'Login: '
        get_password = 'Password: '

        current_login = input(get_user)
        if current_login in users:
            current_user = users[current_login]
            password = getpass.getpass(get_password)

            if password == current_user['password']:               
                break
            else:
                print('Incorrect password!')
                continue
        else:
            text = 'No such user in userlist! Do you want to create new user? (y/n)'
            ans = input(text)
            if ans == 'y':
                new_login = input('Enter your login: ')
                new_password = input('Enter your password: ')
                new = User(new_login, new_password, 0o666)
                continue
            print('\nYou logged in as guest.')
            current_user = users['guest']
            break   
    
    return current_user


def input_command(help_text):
    param = '../my-filesyst/'
    user_input = input(help_text).split(" ")
    user_command = user_input[0]
    if len(user_input) == 2: param += user_input[1]
    print(param)
    return user_command, param


#############################################################################################
current_user = logging_in()
workdir = r'../my-filesyst/'
os.chmod(workdir, current_user['chmod'])     
read = os.access(workdir, os.R_OK)
write = os.access(workdir, os.W_OK)
exec = os.access(workdir, os.X_OK)
print(f'You now have READ_ACCESS: {read}, WRITE_ACCESS: {write}, EXECUTE_ACCESS: {exec}.')
        
while True:
    help_text = f'\nCommands to execute: {"   ".join(commands)}\n> '
    user_command, arg = input_command(help_text)
    if user_command == 'exit':
        break
    elif user_command == 'log-out':
        current_user = logging_in()
    elif user_command in commands:
        try:
            execute(user_command, arg)

        except PermissionError:
            print('Permission denied!')
            date = datetime.datetime.now()
            report = f'{date}       {current_user["login"]}       {user_command}\n'
            f = open('permission_denied_list.txt', 'a')
            f.write(report)
            f.close()
            continue
    else:
        print('Unknown command!\n')
