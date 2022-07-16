import os
import sys
import winreg


def print_(text='', color='default'):
    if color == 'default':
        print(text)
    elif color == 'black':
        print("\033[0;30;40m" + text + "\033[0m")
    elif color == 'red':
        print("\033[0;31;40m" + text + "\033[0m")
    elif color == 'green':
        print("\033[0;32;40m" + text + "\033[0m")
    elif color == 'yellow':
        print("\033[0;33;40m" + text + "\033[0m")
    elif color == 'blue':
        print("\033[0;34;40m" + text + "\033[0m")
    elif color == 'purple':
        print("\033[0;35;40m" + text + "\033[0m")
    elif color == 'cyan':
        print("\033[0;36;40m" + text + "\033[0m")
    elif color == 'white':
        print("\033[0;37;40m" + text + "\033[0m")

def kill_typora():
    try:
        print_(os.system('taskkill /F /IM typora.exe'))
    except Exception as e:
        print_(e.args, 'red')

def del_typora_files():
    user_profile = os.environ.get('USERPROFILE')
    typora_data_path = user_profile + '\\AppData\\Roaming\\Typora\\'
    fucking_files = ['profile.data', 'typora.log', 'typora-old.log']
    
    for i in range(len(fucking_files)):
        this = typora_data_path + fucking_files[i]
        print_('#### delete \"{}\" ...'.format(this), 'cyan')
        try:
            print_(os.remove(this))
        except Exception as e:
            print_(e.args, 'red')
        # DO NOT USE
        # try:
        #     print_(os.mkdir(this))
        # except Exception as e:
        #     print_(e.args, 'red')

def inf_try_out(date='12/31/9999'):
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\Typora', reserved=0, access=winreg.KEY_WRITE)
    except Exception as e:
        print_(e.args, 'red')
    try:
        print_(winreg.SetValueEx(key, 'IDate', 0, winreg.REG_SZ, date))
    except Exception as e:
        print_(e.args, 'red')

def disable_typora_update():
    print_('Would you like to disable typora update by writing a line in hosts? It will not delete others in your hosts. (RECOMMENDED)\n(y,[n])', 'purple')
    i = input()
    i = i.lower()
    if i == 'y':
        windir = os.environ.get('WINDIR')
        hosts_path = windir + "\\System32\\drivers\\etc\\hosts"
        print_(os.system('echo=>>\"{}\"'.format(hosts_path) + ' && ' + 'echo 0.0.0.0\ttypora.io>>\"{}\"'.format(hosts_path)))
    else:
        print_('skipped.', 'purple')
        return



if __name__ == '__main__':
    if sys.platform != 'win32':
        exit()
    
    argv = sys.argv
    if len(argv) == 1:
        print_('#### Make sure you\'re runnning this script as Administrator, then:', 'purple')
        os.system('pause')

        print_('#### Make sure you\'re runned Typora once at least before run this script, then:', 'purple')
        os.system('pause')

        print_('#### Typora will be killed, make sure your work was saved, then:', 'purple')
        os.system('pause')

        print_('#### kill typora.exe ...', 'cyan')
        kill_typora()

        # del_typora_files()

        print_('#### let try-out period never end ...', 'cyan')
        inf_try_out()

        print_('#### disable typora update ...', 'cyan')
        disable_typora_update()

        print_('#### enjoy :)', 'cyan')
    else:
        if argv[1] == 'reg':
            print_('#### let try-out period never end ...', 'cyan')
            inf_try_out()
        elif argv[1] == 'rm':
            del_typora_files()
        else:
            print("""
fucktypora.py <Operation>

No parameter    run normally

Operation:
reg   modify registry value, try-out forever.
rm    delete files: ['profile.data', 'typora.log', 'typora-old.log']
""")
