while True:
    import telebot
    TOKEN ="6501385261:AAFyi77xZls45acuBn2VRcAPuq0L0xt5O-I"
    bot = telebot.TeleBot(token=TOKEN)
    @bot.message_handler(commands=["start"])
    def send_welcome(message):
        username = (
        message.from_user.username
    )  
        xabar = f"Assalom alaykum, {username} factorialni hisoblivchi bot xush kelibsiz!"
        xabar += "\nSonni yuboring."
        bot.reply_to(message, xabar)
    @bot.message_handler(func=lambda msg: msg is not None)
    def translit(message) -> int:
        msg=message.text
        s=int(input("1-sonni kiriting: "))
        s2=int(input("2-sonni kiriting: "))
        javob=s+s2 
        bot.reply_to(message,javob)
    bot.polling()