Client-server application
===========

## Функциональные возможности

:hibiscus: Вход пользователя в приложение с помощью логина и пароля
:hibiscus: Вывод таблицы из Базы данных на экран пользователя
:hibiscus: Вставка новой записи пользователм

## Инструкция по использованию

При запуске приложения появляется окно входа в приложения. Там пользователь вводит свой логин и пароль. 

![Внешний вид окна входа](https://github.com/kristrof/Client-server-application/blob/master/Image/log.png)

После того, как пользователь верно ввел свой логин и пароль открывается главное окно, где представлен основной функционал приложения. 

![Внешний вид главного окна](https://github.com/kristrof/Client-server-application/blob/master/Image/main.png)

Пользователь, например, может вывести интересующую его таблицу.

![Вывод таблицы на экран](https://github.com/kristrof/Client-server-application/blob/master/Image/show_table.png)

После чего клиент может добавить новую запись в таблицу, для этого он должен выполнить следующие действия:
1. В начале пользователь должен нажать на кнопку :heavy_plus_sign:, находящуюся над полем вывода таблице. В поле появится новая пустая строка.

![Добавление новой строки](https://github.com/kristrof/Client-server-application/blob/master/Image/new_row.png)

2. После заполнить данными пустую строку и нажать кнопку :heavy_check_mark: для отправки изменений на сервер.

![Заполненная стркоа](https://github.com/kristrof/Client-server-application/blob/master/Image/row.png)

Теперь можно убедиться, что введенная пользователем строка сохранилась в БД на сервере.

![Проверка действий](https://github.com/kristrof/Client-server-application/blob/master/Image/test.png)

## Техническая часть

### Серверная часть

Серверная часть состоит из трех файлов:
+ [Файл с кодом для соединения Сервера и клиента через сокет](https://github.com/kristrof/Client-server-application/blob/master/Server/conn.py)
+ [Файл с кодом функции, выполняющих вывод таблицы на экран, вставку строки в таблицу и так далее](https://github.com/kristrof/Client-server-application/blob/master/Server/server.py)
+ [Файл объединяющий два предыдущих для коректной работы сервера](https://github.com/kristrof/Client-server-application/blob/master/Server/main.py)

### Клиентаская часть

Клиентская часть состоит из 4-х файлов:
+ [Дизайн окна входа](https://github.com/kristrof/Client-server-application/blob/master/Client/design/login.py)
+ [Дизайн главного окна](https://github.com/kristrof/Client-server-application/blob/master/Client/design/main_window.py)
+ [Файл с кодом соединения клиента и сервера через сокет](https://github.com/kristrof/Client-server-application/blob/master/Client/Connect.py)
+ [Файл, объединяющий все выше перечисленное в одно](https://github.com/kristrof/Client-server-application/blob/master/Client/Interface_test.py)