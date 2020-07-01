import telebot
import os
import variables

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hola "+str(message.chat.first_name)+", que necesitas")
    bot.reply_to(message,str(message.chat.id))
    	
@bot.message_handler(commands=['disco'])
def estado_disco(message):
	disco = os.popen('df /dev/sda5 -h ').read()
	bot.send_message(message.chat.id,disco)

def listener(messages):
	for m in messages:
		if m.content_type == 'text':
		    # print the sent message to the console
		    print str(m.chat.first_name) + " [" + str(m.chat.id) + "]: " + m.text
		    bot.reply_to(m,str(m.chat.id))
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)



bot.polling()
