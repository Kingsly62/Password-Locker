
import sys
PASSWORD = {'email': 'clinton56@gmail.com', 'Username': 'Kingsly62'}
if len(sys.argv) < 2:
    print('Usage: python3.9 password.py [account]- copy account password')
    sys.exit()
    account = sys.argv[1]
    import pyperclip

    if account in PASSWORD:
        pyperclip.copy(PASSWORD[account])
        print('password for ' + account + ' copied to clipboard')
    else:
        print('There is no account named ' + account)
