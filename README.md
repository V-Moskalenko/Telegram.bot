# Telegram_bot 
Данный бот является помощником/напоминалкой для крупных структурных подразделений. Выводит информацию о днях рождения коллег, а также информацию о погоде - позаранее подготовленным кнопкам. Конечно, каждый сотрудник может занести данную информацию в свой календарь, но как правило, все это сделать забывают, а данный инструмент одним запросом поможет не обидеть коллегу с забытым днём рождения.

### requirements (необходимые библиотеки):
* pyTelegramBotAPI==4.4.0
* requests==2.27.1

### Заготовленные запросы
![Image alt](https://github.com/V-Moskalenko/telegram_bot/blob/main/telegram_bot.png)

### Если нужно изменить город запроса погоды
В функции **start**, поменяйте текст на необходимый город:
```python
    btn1 = types.KeyboardButton("Какая погода в Тамани❓")
    btn2 = types.KeyboardButton("Какая погода в Москве❓")
```
В блоке кода функции **func** измените город на необходимый Вам:
```python
    if (message.text == "Какая погода в Тамани❓"):
        bot.send_message(message.chat.id, f'В Тамани сейчас {what_weather("Тамань")}')
    elif (message.text == "Какая погода в Москве❓"):
        bot.send_message(message.chat.id, f'В Москве сейчас {what_weather("Москва")}')
```
### Если нужно изменить эмодзи (emoji)
Выбрать можете из данного списка: [emoji](https://github.com/GnuriaN/format-README/blob/master/emoji.md)

### Deploy
Данный бот размещён на Heroku. В Telegram бот можно найти по имени: @DepRTandA_Bot
