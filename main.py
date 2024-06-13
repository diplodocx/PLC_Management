import telebot
from telebot import types
import socket

bot = telebot.TeleBot("YOUR TOKEN")
HOST = "10.0.174.51"
PORT = 4444


def send_tcp_request(text: str):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(bytes(text, 'utf-8'))
        data = s.recv(1024)
        return str(data, 'utf-8')


def act(message, text):
    res = send_tcp_request(text)
    bot.send_message(message.chat.id, res)


@bot.message_handler(commands=['on'])
def light_on(message):
    bot.send_message(message.chat.id, 'light_on ...')
    act(message, 'M03')

@bot.message_handler(commands=['off'])
def light_off(message):
    bot.send_message(message.chat.id, 'light_off ...')
    act(message, 'M05')

bot.infinity_polling()