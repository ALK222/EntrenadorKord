class messages(object):
    def __init__(self, kord):
        self.kord = kord
    
    def echo_all(self, message):
        if(message.text.lower() == 'me cago en'):
            self.kord.reply_to(message, "mi puta vida")  
        message_split = message.text.split()
        if(message_split[0].lower() == 'soy'):
            self.kord.reply_to(message, self.switch_soy(message_split[1].lower()))
        else:
            if("agus" in message.text.lower()):
                self.kord.reply_to(message, "No se llama Agus, se llama ÒwÓ") 
        if(message.text.lower() == 'tiene por culpa como tú'):
            self.kord.reply_to(message, "el mismo contexto sexual?") 
        if(("jaja" in message.text.lower()) | ("abstención" in message.text.lower()) | ("abstencion" in message.text.lower())):
            self.kord.reply_to(message, "Ja ja ja es gracioso porque")
        if(message.from_user.username == "SantaClaus255"):
            if(message.text.lower() == 'lo hacemos?'): 
                self.kord.reply_to(message, "Tan desesperado estás como para hacerlo con un bot?")
        if(message.text.lower() == "kord, di lo tuyo"):
            self.kord.reply_to(message, "Los shinies no molan, son pokemons enfermos")

    def switch_soy(self, message):
        print(message)
        switcher = {
            'gilipollas': "Pero te queremos igualmente",
            'carapolla': 'Hola, Almeida',
            'agus': "Hola, ÒwÓ", 
            }.get(message, 'Hola, ' + message)
        return switcher