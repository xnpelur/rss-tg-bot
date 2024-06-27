class Messages:
    WELCOME = "Приветствую! Нажмите кнопку, чтобы получить случайную статью"
    SOURCES_MANAGEMENT = "Нажмите одну из кнопок ниже, чтобы добавить или удалить источник"
    UNKNOWN = "Сообщение не распознано"
    ERROR = "Что-то пошло не так, пожалуйста повторите попытку"
    URLS_EMPTY = "Список источников статей пуст"
    ADDING_SOURCE = "Для добавления нового источника нажмите одну из кнопок ниже или введите ссылку на RSS рассылку в сообщение"
    ADDING_SOURCE_SUCCESS = "Новый источник добавлен"


class Buttons:
    GET_ARTICLE = "Получить статью"
    MANAGE_SOURCES = "Управление источниками"
    ADD_SOURCE = "Добавить источник"
    REMOVE_SOURCE = "Удалить источник"
    BACK = "Назад"


SOURCES = {
    "Хабр": "https://habr.com/ru/rss/articles/?fl=ru",
    "vc.ru": "https://vc.ru/rss",
    "РБК": "https://rssexport.rbc.ru/rbcnews/news/20/full.rss",
}