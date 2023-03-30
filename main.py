from api.bot_loader import start_bot, bot
from telebot.types import (
  CallbackQuery,
  Message
)
from commands import (
  help,
  lowprice,
  highprice,
  bestdeal,
  history,
  start
)

'''
Основной модуль Телеграмм бота
  - Обработчик нажатия кнопок основного меню
  - Обработчик команд
  - Обработчик нового пользователя
  - Обработчик текстового сообщения со словом 'Привет'
'''


@bot.message_handler(commands=['hello-world'])
def goto_help(message: Message) -> None:
  """Вывод в бот слово "Привет" в ответ на команду "/hello-world"
  Args:
     message (Message): Сообщение пользователя Боту
  """
  msg = bot.send_message(message.chat.id, text='Привет', parse_mode="HTML")


@bot.message_handler(content_types=["new_chat_members"])
def handler_new_member(message: Message) -> None:
  """Функция обработчик нового пользователя Бота
  запускает обработчик команды '/star'
  Args:
      message (Message):  Сообщение пользователя Боту
  """
  send_text = f'''<b>Привет {message.from_user.first_name}!</b>
  Я молодое и перспективное турагентство <b>Too Easy Travel.</b>

  Я могу следующее:


      '''
  msg = bot.send_message(message.chat.id, text=send_text, parse_mode="HTML")
  start.get_start(message)


@bot.callback_query_handler(func=lambda c: c.data == '/lowprice')
def goto_lowprice(callback_query: CallbackQuery) -> None:
  """Функция обработчик нажатия кнопки 'Топ самых дешевых отелей' основного Меню
  запускает обработчик команды '/lowprice'
  Args:
      callback_query (CallbackQuery):  Объект сгененрированый на нажатие кнопки Меню
  """
  get_lowprice(callback_query.message)


@bot.message_handler(commands=['lowprice'])
def get_lowprice(message: Message) -> None:
  """Функция обработчик команды '/lowprice'
  запускает функцию 'start_choose' модуля 'commands/highprice.py'
  Args:
      message (Message):  Сообщение пользователя Боту
  """
  lowprice.start_choose(message)


@bot.callback_query_handler(func=lambda c: c.data == '/highprice')
def goto_highprice(callback_query: CallbackQuery):
  """Функция обработчик нажатия кнопки 'Топ самых дорогих отелей' основного Меню
  запускает обработчик команды '/highprice'
  Args:
      callback_query (CallbackQuery):  Объект сгененрированый на нажатие кнопки Меню
  """
  get_highprice(callback_query.message)


@bot.message_handler(commands=['highprice'])
def get_highprice(message: Message) -> None:
  """Функция обработчик команды '/highprice'
  запускает функцию 'start_choose' модуля 'commands/highprice.py'
  Args:
      message (Message):  Сообщение пользователя Боту
  """
  highprice.start_choose(message)


@bot.callback_query_handler(func=lambda c: c.data == '/bestdeal')
def goto_bestdeal(callback_query: CallbackQuery):
  """Функция обработчик нажатия кнопки 'Топ самых дорогих отелей' основного Меню
  запускает обработчик команды '/bestdeal'
  Args:
      callback_query (CallbackQuery):  Объект сгененрированый на нажатие кнопки Меню
  """
  get_bestdeal(callback_query.message)


@bot.message_handler(commands=['bestdeal'])
def get_bestdeal(message: Message) -> None:
  """Функция обработчик команды '/bestdeal'
  запускает функцию 'start_choose' модуля 'commands/bestdeal.py'
  Args:
      message (Message):  Сообщение пользователя Боту
  """
  bestdeal.start_choose(message)


@bot.callback_query_handler(func=lambda c: c.data == '/history')
def goto_history(callback_query: CallbackQuery):
  """Функция обработчик нажатия кнопки 'История поиска отелей' основного Меню
  запускает обработчик команды '/history'
  Args:
      callback_query (CallbackQuery):  Объект сгененрированый на нажатие кнопки Меню
  """
  get_history(callback_query.message)


@bot.message_handler(commands=['history'])
def get_history(message: Message) -> None:
  """Функция обработчик команды '/history'
  запускает функцию 'get_history' модуля 'commands/history.py'
  Args:
      message (Message):  Сообщение пользователя Боту
  """
  history.get_history(message)


@bot.callback_query_handler(func=lambda c: c.data == '/help')
def goto_help(callback_query: CallbackQuery):
  """Функция обработчик нажатия кнопки 'История поиска отелей' основного Меню
  запускает обработчик команды '/help'
  Args:
      callback_query (CallbackQuery):  Объект сгененрированый на нажатие кнопки Меню
  """
  get_help(callback_query.message)


@bot.message_handler(commands=['help'])
def get_help(message):
  """Функция обработчик команды '/help'
  запускает функцию 'get_help' модуля 'commands/help.py'
  Args:
      message (Message):  Сообщение пользователя Боту
  """
  msg_text = help.get_help()
  bot.send_message(chat_id=message.chat.id, text=msg_text)


@bot.message_handler(content_types=['text'])
def text_control(message: Message) -> None:
  """Принимает любое текстовое сообщение от пользователя
Если это слово 'Привет' то запускает функцию 'handler_new_member',
 которая приветсвует нового пользователя
  Args:
      message (Message): Сообщение пользователя Боту
  """
  if message.text.lower() == 'привет':
    handler_new_member(message)


def __main() -> None:
  """Запускает Бота из модуля 'api\bot_loader.py'
  """
  start_bot()


if __name__ == "__main__":
  """Защищает запуск модуля из сторонних модулей
  """
  __main()
