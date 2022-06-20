def get_mail():
    user_mail = input('wpisz maila')

    return user_mail


def get_list():
    with open('maile.txt') as f:
        content = f.readlines()
        mail_list = []

        for mail in content:
            mail = mail.strip('\n')
            mail_list.append(mail)

    return mail_list


def search_mail(user, mail_list):
    if user in  mail_list:
        print(f'mail {user} jest na liście')
        return True
    else:
        print('Podane maila nie ma na liście')
        return False


def main():
    user = get_mail()
    mail_list = get_list() #['adam@onet.pl', 'tomek@onet.pl', 'basia@onet.pl', 'ola@onet.pl', 'henio@onet.pl']

    result = search_mail(user, mail_list)
    print(result)

main()

