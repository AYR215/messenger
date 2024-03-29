Комментарии по интерфейсу и реализации:

1) Редактирование личной информации пользователя (имя и аватар): ссылки на регистрацию, логин/разлогин и личный кабинет
пользователя находятся в шапке стартовой и др. страниц.
После регистрации и логина аватар/имя пользователя можно установить/сменить через личный кабинет (PERSONAL).
ВАЖНО: для корректного отображения картинок, хранящихся на локальном сервере, требуется установить в виртуальное
окружение библиотеку pillow (https://pillow.readthedocs.io/en/stable/).

2) Просмотр списка других пользователей:
На стартовой странице расположены ссылки на приватные (один на один) и публичные (групповые чаты), PRIVATE CHATS и
PUBLIC CHATS соответственно. При переходе в раздел private chats по нажатию на кнопку SHOW ALL USERS будет открыт
список всех зарегистрированных пользователей. При нажатии на имя пользователя откроется чат с ним.

3) Отправка и получение сообщений (приватный чат, публичный чат):
Поле ввода сообщений находится под текстовым полем чата. Сообщения отправляются по клику на кнопку SEND.
Имя отправителя сообщения будет указано слева от сообщения.

4) REST-функционал групповых чатов:
При выборе на стартовой странице PUBLIC CHATS, открывается страница, на которой по клику на кнопку SHOW ALL CHATS
доступен весь список чатов. Их можно удалять (кнопка DELETE), создавать новые чаты (поле для ввода названия чата и
кнопка CREATE под списком), а также изменять (см. ниже) при помощи REST API.
В частности, при клике на название чата откроется сам чат (об отправке сообщений - см. п.3), а также появится поле и
кнопка для смены названия чата.

ВАЖНО: На данном этапе задание не предполагало автоматического обновления страницы при изменениях в базе данных. Поэтому
для того, чтобы увидеть изменение в списке чатов (создание/удаление/смену названия), пока что страницы нужно
перезагружать вручную. Это также может быть изменено при дальнейшей разработке проекта.

5) WebSocket-функционал групповых чатов: сделан на основе "идеологии комнат", как и предполагалось.
ВАЖНО: для корректного функционирования websockets необходимо установить библиотеку channels (https://channels.readthedocs.io/en/stable/)
