import string
import pymysql
import telebot
import secrets
import commands
import messages


kord = telebot.TeleBot(secrets.kord_token)  # insert token here
kordMessage = messages.messages(kord)
connection = pymysql.connect(host=secrets.kord_host,
                             user=secrets.kord_user,
                             password=secrets.kord_password,
                             db=secrets.kord_db,
                             charset=secrets.kord_charset,
                             cursorclass=pymysql.cursors.DictCursor)


kordCommands = commands.teleCommands(kord, connection)  # command handler


# COMMAND HANDLERS

#HELP & START
@kord.message_handler(commands=['help', 'start'])
def help(message):
    print('start')
    kordCommands.send_help(message)

# KILL


@kord.message_handler(commands=['kill'])
def kill(message):
    print('kill')
    kordCommands.kill_message(message)

# SELECT POKEMON


@kord.message_handler(commands=['select'])
def select_pokemon(message):
    print('select')
    kordCommands.select(message)

# SELECT BOSS


@kord.message_handler(commands=['select_boss'])
def select_boss(message):
    print('select_boss')
    kordCommands.select_boss(message)


# MESSAGE HANDLER
@kord.message_handler(func=lambda message: True)
def reply(message):
    kordMessage.echo_all(message)


kord.polling()
