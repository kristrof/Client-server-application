# Client-server application
____
## Функциональные возможности
__
:one: Вход пользователя в приложение с помощью логина и пароля
:two: Вывод таблицы из Базы данных на экран пользователя
:three: Вставка новой записи пользователм

## Инструкция по использованию
__

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