from feature import persistence
from interfeces import mainInterface


def main ():
    account = persistence.load_account()
    account = mainInterface.main_interface(account)
    persistence.save_account(account)

if __name__ == "__main__":
    main()