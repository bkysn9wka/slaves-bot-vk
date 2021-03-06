# slaves-bot-vk

[Бот для мини-игры ВКонтакте "Рабы"](https://vk.com/app7794757)
[Тема на Lolzteam](https://lolz.guru/threads/2389937/)

## Какие настройки присутствуют? Настройка в Config.json
![image](https://i.imgur.com/qfENg1P.png)
- Min/Max_delay. Рандомизация времени на выдачу цепей, покупку рабов и выдачу названвания работы
- Job_name. Имя, имена работ
- Min/Max_price. Минимальная и максимальная цена за которую покупать рабов
- Buy_slave, true/false. Покупка рабов
- Buy_fetter, true/false. Покупка оков

## Флуд в консоль ошибками
- Error when buying slave, possibly a cooldown. Возможно флуд-контроль на покупку рабов
- Error when installing the job, possibly cooldown. Возможно флуд-контроль на установку названия работы
- Error when buying fetter, possibly a cooldown. Возможно флуд-контроль на покупку оков
![image](https://i.imgur.com/E0GDfzN.png)

## Как не получить Cooldown (система антифлуда)
- Min_delay в Config.json не должен быть меньше 5 секунд
- Старайте указывать больше работ в Config.json (Job_name)

## Как обойти Cooldown?
Есть не точная информация, но она была проверена на нескольких людях
- Воспользуйтесь VPN, если айпи не статический - перезагрузите роутер. Сделайте, что угодно, но вы должны изменить свой IP на другой

## Запуск скрипта на Windows
- Скачать архив с репозитория
- Установить Python последней версии http://python.org
- Поставить галочку ADD TO PATH
- Установить модули pip install -r requirements.txt
- Запустить скрипт
- Ввести ключ:
![image](https://i.imgur.com/mZODDE7.png)

## Установка на Android
- Устанавливаем Termux с Play Market
- Запускаем Termux
- Пишем pkg install -y git
- Далее git clone https://github.com/vuchaev2015/slaves-bot-vk
- cd slaves-bot-vk
- pkg install -y python
- Как установилось пишем pip install -r requirements.txt
- И наконец, после установки модулей пишем python main.py
![image](https://i.imgur.com/P5dqSNS.png)
- Ключ получить можно по инструкции ниже
Небольшая рофляночка, если хотите получить ключ авторизации нужно попросить друга у которого есть доступ к ПК или самому достать его с ПК :)
P.S Редактировать конфиг можно командой nano config.json
![image](https://i.imgur.com/AnX1Cif.png)

## Как получить ключ?
- Заходим в приложение ["Рабы"](https://vk.com/app7794757)
- Открываем консоль CTRL + SHIFT + I
- Переходим по вкладку NETWORK
- В графе filter пишем start
- Обновляем страницу
- Копируем все из поля authorization
![image](https://i.imgur.com/0WT8GH1.png)

## Планы на будущее
- <del>Добавить рандомизацию при установке работ</del> Добавлено!
- Добавить более удобную и автоматизированную установку на Termux

## Информация о последнем обновлении
- Добавлен конфиг для более удобной работы
- Улучшен кулдаун, т.к он получал ранее только одно значение и использовал его на протяжении всего потока
- Добавили рандомизацию работ, может работать кривовато
