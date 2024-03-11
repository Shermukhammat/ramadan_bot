from aiogram import Dispatcher
from aiogram.dispatcher.middlewares import BaseMiddleware

from loader import dp
from .throttling import ThrottlingMiddleware

if __name__ == 'middlewares':
    dp.middleware.setup(ThrottlingMiddleware())