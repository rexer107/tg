import telebot
import random



bot = telebot.TeleBot("5426230278:AAHcQWu9CJZlhZI_7CPAJpDq0imEPOcQH7A")
@bot.message_handler(commands=['start'])
def start(message):
    
    bot.send_message(message.chat.id, text="Привет, {0.first_name}!  Я могу ответить только да, либо нет".format(message.from_user), )
    bot.send_message(message.chat.id, text="Задай мне вопрос, я отвечу на него да, либо нет.(Обязательно поставьте знак вопроса и составьте предложение как минимум из двух слов. Либо поставьте пробел)") #Перезадавать вопросы НЕЛЬЗЯ. ")
    
@bot.message_handler(content_types=['text']) 

def func(message):
    rand_randlist = random.randint(1,6)
    
    if ("?" in message.text):
        if (" " in message.text):
            if(rand_randlist == 1) :
                bot.send_message(message.chat.id, text="Да")
            elif( rand_randlist == 2):
                bot.send_message(message.chat.id, text ="Нет")
            if(rand_randlist == 3) :
                bot.send_message(message.chat.id, text="Возможно")
            elif( rand_randlist == 4):
                bot.send_message(message.chat.id, text ="Я думаю нет")
            if(rand_randlist == 5) :
                bot.send_message(message.chat.id, text="Сто процентов")
            elif( rand_randlist == 6):
                bot.send_message(message.chat.id, text ="Точно нет")
            # sti = open ("sti01.webp","rb")
            # bot.send_sticker(message.chat.id,sti)
        else:
            bot.send_message(message.chat.id,text="Введите вопрос со знаком вопроса или сделайте предложение как минимум из двух слов.")    
    else:
        bot.send_message(message.chat.id,text="Введите вопрос со знаком вопроса или сделайте предложение как минимум из двух слов.")
  

bot.polling(none_stop=True)
