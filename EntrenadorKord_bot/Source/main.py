import string
import pymysql
import telebot
from commands import teleCommands
from messages import messages

kord = telebot.TeleBot("")#insert token here
kordMessage = messages(kord)
connection = pymysql.connect(host='localhost',
                             user='Kord',
                             password='NoMeSaleElShiny',
                             db='pokemongobot',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


kordCommands = teleCommands(kord, connection)#command handler



#COMMAND HANDLERS

#HELP & START
@kord.message_handler(commands=['help', 'start'])
def help(message):
    print('start')
    kordCommands.send_help(message)

#KILL
@kord.message_handler(commands=['kill'])
def kill(message):
    print('kill')
    kordCommands.kill_message(message)

#SELECT POKEMON
@kord.message_handler(commands=['select'])
def select_pokemon(message):
    print('select')
    kordCommands.select(message)

#SELECT BOSS
@kord.message_handler(commands=['select_boss'])
def select_boss(message):
    print('select_boss')
    kordCommands.select_boss(message)


#MESSAGE HANDLER
@kord.message_handler(func=lambda message: True)
def reply(message):
    kordMessage.echo_all(message)


kord.polling()