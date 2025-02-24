import sqlite3
import asyncio
import time, random
from user import BFGuser

from aiogram import Dispatcher, Bot, types

from bot import start


class Database:
    def __init__(self):
        self.conn = sqlite3.connect('modules/temp/Youtube')
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users('
                            user_id INTEGER,
                            balanc INTEGER '0',
                            kanal INTEGER '0',
                            namekan TEXT,
                            subscribe INTEGER DEFAULT '0',
                            likes INTEGER DEFAULT '0', 
                            ')''')
                            self.conn.commit()

    async def reg_user(self, user_id):
        ex = self.cursor.execute('SELECT user_id FROM users WHERE user_id = ?', (user_id,)).fetchone()
        if not ex:
            self.cursor.execute('INSERT INTO users (user_id) VALUES (?)', (user_id,))
            self.conn.commit()

    async def getbalanc(self, user_id):
        await self.reg_user(user_id)
        balance = ('SELECT balanc FROM users WHERE user_id = ?', (user_id,)).fetchone()
        self.conn.commit()



    async def upd_youtube(self, user_id):
        await self.reg_user(user_id)
        self.cursor.execute('UPDATE users SELECT kanal = 1 WHERE user_id', (user_id,)).fetchone()
        self.conn.commit()





async def start(message: types.Message, user: BFGuser):
    balanc = await db.getbalanc(user.user_id)

    if balanc >= 500:
        await message.answer('Вы купить ферма ееее')
    else:
        await message.answer('нет денег нищета')
        return
    if kanal is None or kanal[0] == 1:
        await message.answer('У вас уже есть ферма')




def register_handler(dp: Dispatcher):
    dp.register_message_handler(start, lambda message: message.text.lower() == 'ютуб')



MODULE_DESCRIPTION = {
	'name': '👻 ютуб',
	'description': '''Ивент-модуль ютуб:
- Новое оформление
- Новый ивент "монстры"
- Новая игра
- Новые игровые валюты

* Модуль использует собственную базу данных
* Помощью по модулю введите "хеллоуин"'''
}
