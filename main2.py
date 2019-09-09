import easyimap
import os
import telebot
import time
login = ''
password = ''

token = ""
CHANNEL_NAME = '@p3114'
bot = telebot.TeleBot(token)

def attachmentSend(docpath):
    global bot
    global CHANNEL_NAME
    doc = open(docpath, 'rb')
    bot.send_document(CHANNEL_NAME, doc)
def textSend(text):
    global bot
    global CHANNEL_NAME
    bot.send_message(CHANNEL_NAME, text)

imapper = easyimap.connect('imap.mail.ru', login, password)
lastdate = None
while True:
    mail = imapper.listup(1)[0]
    print(mail)
    if lastdate != mail.date:
        print(mail.title)
        textSend(mail.title + ' - ' + mail.body)
        for attachment in mail.attachments:
            if not os.path.exists("attachments/"+mail.date[5:15].replace(' ','')+'/'):
                os.makedirs("attachments/"+mail.date[5:15].replace(' ','')+'/')
            f = open("attachments/"+mail.date[5:15].replace(' ','')+'/' + attachment[0], "wb+")
            f.write(attachment[1])
            f.close()
            attachmentSend("attachments/"+mail.date[5:15].replace(' ','')+'/')
        lastdate = mail.date
    time.sleep(30)