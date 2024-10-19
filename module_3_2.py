# Задача "Рассылка писем"

domen_com = ".com"
domen_ru = ".ru"
domen_net = ".net"

def send_email(message, recipient,*, sender = 'university.help@gmail.com'):
    global domen_com, domen_ru, domen_net

    if "@" in recipient and "@" in sender:
        if domen_com in recipient or domen_ru in recipient or domen_net in recipient:
            if domen_com in sender or domen_ru in sender or domen_net in sender:
                if recipient == sender:
                    print("НЕЛЬЗЯ ОТПРАВИТЬ ПИСЬМО САМОМУ СЕБЕ!, ваше сообщение не отправлено." )
                    return
                elif sender != 'university.help@gmail.com':
                    print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! URBAN отправил вам письмо с другого адреса (" + sender + "):", message)
                    return
                else:
                    print(message)
                    return
        else:
            print("Невозможно отправить письмо с адреса ", sender, "на адрес ", recipient)
            return

send_email("Вы огурец, то есть молодец, а может молодка", "print.denis@mail.ru")
send_email("Вы задолжали нам кучку денег", "print.denis@mail.ru", sender = 'urban.fan@mail.ru')
send_email("Вы можете ответить на несколько вопросов?", "print.denis@mail.r")
send_email("Здравствуй URBAN - это УРБАН", "university.help@gmail.com")







