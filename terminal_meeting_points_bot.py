#библиотеки, которые загружаем из вне
import telebot
import config
import random

from telebot import types

f = open('/content/kef_facts.txt', 'r', encoding='UTF-8')
kef_facts = f.read().split('\n')
f.close()

f = open('/content/auh_facts.txt', 'r', encoding='UTF-8')
auh_facts = f.read().split('\n')
f.close()

f = open('/content/led_facts.txt', 'r', encoding='UTF-8')
led_facts = f.read().split('\n')
f.close()

f = open('/content/alc_facts.txt', 'r', encoding='UTF-8')
alc_facts = f.read().split('\n')
f.close()

f = open('/content/fra_facts.txt', 'r', encoding='UTF-8')
fra_facts = f.read().split('\n')
f.close()

f = open('/content/hnd_facts.txt', 'r', encoding='UTF-8')
hnd_facts = f.read().split('\n')
f.close()

f = open('/content/msq_facts.txt', 'r', encoding='UTF-8')
msq_facts = f.read().split('\n')
f.close()

f = open('/content/dub_facts.txt', 'r', encoding='UTF-8')
dub_facts = f.read().split('\n')
f.close()

f = open('/content/lpb_facts.txt', 'r', encoding='UTF-8')
lpb_facts = f.read().split('\n')
f.close()

f = open('/content/hel_facts.txt', 'r', encoding='UTF-8')
hel_facts = f.read().split('\n')
f.close()

f = open('/content/lhr_facts.txt', 'r', encoding='UTF-8')
lhr_facts = f.read().split('\n')
f.close()

f = open('/content/anr_facts.txt', 'r', encoding='UTF-8')
anr_facts = f.read().split('\n')
f.close()

f = open('/content/sxm_facts.txt', 'r', encoding='UTF-8')
sxm_facts = f.read().split('\n')
f.close()

bot = telebot.TeleBot('5523725569:AAEICUQ6xRLx7Ckh4joFfm5OwTJoOJFzSn0')

@bot.message_handler(commands=['start'])
def welcome(message):
	map1 = open('/content/main_map.jpg', 'rb')
	bot.send_photo(message.chat.id, map1)

	#клавиатура
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("🇦🇪 AUH")
	item2 = types.KeyboardButton("🇮🇸 KEF")
	item3 = types.KeyboardButton("🇳🇱 SXM")
	item4 = types.KeyboardButton("🇧🇪 ANR")
	item5 = types.KeyboardButton("🇬🇧 LHR")
	item6 = types.KeyboardButton("🇫🇮 HEL")
	item7 = types.KeyboardButton("🇧🇴 LPB")
	item8 = types.KeyboardButton("🇮🇪 DUB")
	item9 = types.KeyboardButton("🇧🇾 MSQ")
	item10 = types.KeyboardButton("🇯🇵 HND")
	item11 = types.KeyboardButton("🇩🇪 FRA")
	item12 = types.KeyboardButton("🇪🇸 ALC")
	item13 = types.KeyboardButton("🇷🇺 LED")
	item14 = types.KeyboardButton("🗺 Карта")


	markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, item14)

	bot.send_message(message.chat.id, "Привет, {0.first_name}! Отправил тебе карту с расположением переговорок — её можно открыть и увеличить. Выбери нужную переговорку из списка ниже, и я пришлю тебе ссылку на Гугл-календарь, где можно посмотреть, в какое время она свободна".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

#назначаем действие для клавиатуры
@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == '🇦🇪 AUH':
			bot.send_message(message.chat.id, 'У меня проблема: Lambo или Ferra?')			
			auh_photo = open('/content/auh_view.jpg', 'rb')
			bot.send_photo(message.chat.id, auh_photo)
			bot.send_message(message.chat.id, 'Перейди по ссылке, чтобы посмотреть свободные слоты в календаре Google https://calendar.google.com/calendar/u/0/r?cid=MWdrOWd2ZzdqbWdjYmxxb3BzZXJ2dm8xMmtAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ')			
			bot.send_message(message.chat.id, 'А вот карта, чтобы быстро найти переговорку')
			auh_where = open('/content/auh_where.png', 'rb')
			bot.send_photo(message.chat.id, auh_where)
			bot.send_message(message.chat.id, 'Если хочешь узнать ещё об ОАЭ, нажми на /auh_facts.')
		elif message.text == '/auh_facts':
			answer = random.choice(auh_facts)
			bot.send_message(message.chat.id, answer)
			bot.send_message(message.chat.id, 'Если хочешь узнать ещё об ОАЭ, нажми на /auh_facts.')
		elif message.text == '🇮🇸 KEF':
			bot.send_message(message.chat.id, 'Мемные вулканы, гейзеры и потрясающая северная природа')
			kef_photo = open('/content/kef_view.jpg', 'rb')
			bot.send_photo(message.chat.id, kef_photo)
			bot.send_message(message.chat.id, 'Перейди по ссылке, чтобы посмотреть свободные слоты в календаре Google https://calendar.google.com/calendar/u/0/r?cid=cGZ1YWg5aWptanA3ZTQybGRyN25xZmo5YjhAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ')			
			bot.send_message(message.chat.id, 'А вот карта, чтобы быстро найти переговорку')			
			kef_where = open('/content/kef_where.png', 'rb')
			bot.send_photo(message.chat.id, kef_where)
			bot.send_message(message.chat.id, 'Если хочешь узнать ещё об Исландии, нажми на /kef_facts.')
		elif message.text == '/kef_facts':
			answer = random.choice(kef_facts)
			bot.send_message(message.chat.id, answer)
			bot.send_message(message.chat.id, 'Если хочешь узнать ещё об Исландии, нажми на /kef_facts.')
		elif message.text == '🇳🇱 SXM':
			bot.send_message(message.chat.id, 'Сен-Мартен? А вы, смотрю, споттер? Самолетики любите фотографировать?')			
			sxm_photo = open('/content/sxm_view.jpg', 'rb')
			bot.send_photo(message.chat.id, sxm_photo)
			bot.send_message(message.chat.id, 'Перейди по ссылке, чтобы посмотреть свободные слоты в календаре Google https://calendar.google.com/calendar/u/0/r?cid=bmk3dG83cGs2a2E5MDgwdmFwcGNyb3UxazhAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ')			
			bot.send_message(message.chat.id, 'А вот карта, чтобы быстро найти переговорку')					
			sxm_where = open('/content/sxm_where.png', 'rb')
			bot.send_photo(message.chat.id, sxm_where)
			bot.send_message(message.chat.id, 'Если хочешь узнать ещё о Сен-Мартене, нажми на /sxm_facts.')
		elif message.text == '/sxm_facts':
			answer = random.choice(sxm_facts)
			bot.send_message(message.chat.id, answer)
			bot.send_message(message.chat.id, 'Если хочешь узнать ещё об Сен-Мартене, нажми на /sxm_facts.')
		elif message.text == '🇧🇪 ANR':
			bot.send_message(message.chat.id, 'Прихватить вафель, шоколада, 3 Fonteinen Oude Geuze и залечь на дно в Брюгге')
			anr_photo = open('/content/anr_view.jpg', 'rb')
			bot.send_photo(message.chat.id, anr_photo)
			bot.send_message(message.chat.id, 'Перейди по ссылке, чтобы посмотреть свободные слоты в календаре Google https://calendar.google.com/calendar/u/0/r?cid=YThzNmhycml1NG1uMXRsOWxtOTYxYmZrcTBAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ')			
			bot.send_message(message.chat.id, 'А вот карта, чтобы быстро найти переговорку')				
			anr_where = open('/content/anr_where.png', 'rb')
			bot.send_photo(message.chat.id, anr_where)			
			bot.send_message(message.chat.id, 'Если хочешь узнать ещё о Бельгии, нажми на /anr_facts.')
		elif message.text == '/anr_facts':
			answer = random.choice(anr_facts)
			bot.send_message(message.chat.id, answer)
			bot.send_message(message.chat.id, 'Если хочешь узнать ещё о Бельгии, нажми на /anr_facts.')
		elif message.text == '🇬🇧 LHR':
			bot.send_message(message.chat.id, 'Да, в Лондоне! Ну это там, где рыба, чипсы, дрянная еда, отвратная погода, Мэри «Мать её» Поппинс!')
			lhr_photo = open('/content/lhr_view.jpg', 'rb')
			bot.send_photo(message.chat.id, lhr_photo)
			bot.send_message(message.chat.id, 'Перейди по ссылке, чтобы посмотреть свободные слоты в календаре Google https://calendar.google.com/calendar/u/0/r?cid=cjZkOG85OW85NzcxOGM4ZGttMDdqbmJxdW9AZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ')			
			bot.send_message(message.chat.id, 'А вот карта, чтобы быстро найти переговорку')			
			lhr_where = open('/content/lhr_where.png', 'rb')
			bot.send_photo(message.chat.id, lhr_where)						
			bot.send_message(message.chat.id, 'Если хочешь узнать ещё о Великобритании, нажми на /lhr_facts.')
		elif message.text == '/lhr_facts':
			answer = random.choice(lhr_facts)
			bot.send_message(message.chat.id, answer)
			bot.send_message(message.chat.id, 'Если хочешь узнать ещё о Великобритании, нажми на /lhr_facts.')
		elif message.text == '🇫🇮 HEL':
			bot.send_message(message.chat.id, 'Шенген пробить да в Disas финской ухи навернуть — красота.')
			hel_photo = open('/content/hel_view.jpg', 'rb')
			bot.send_photo(message.chat.id, hel_photo)
			bot.send_message(message.chat.id, 'Перейди по ссылке, чтобы посмотреть свободные слоты в календаре Google https://calendar.google.com/calendar/u/0/r?cid=Z3VoMGFkOGVxMmk1Y3A5MHUzOXJyaTliczRAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ')			
			bot.send_message(message.chat.id, 'А вот карта, чтобы быстро найти переговорку')					
			hel_where = open('/content/hel_where.png', 'rb')
			bot.send_photo(message.chat.id, hel_where)				
			bot.send_message(message.chat.id, 'Если хочешь узнать ещё о Финляндии, нажми на /hel_facts.')
		elif message.text == '/hel_facts':
			answer = random.choice(hel_facts)
			bot.send_message(message.chat.id, answer)
			bot.send_message(message.chat.id, 'Если хочешь узнать ещё о Финляндии, нажми на /hel_facts.')
		elif message.text == '🇧🇴 LPB':
			bot.send_message(message.chat.id, 'Приехать в Боливию, увидеть Тиуанако и умереть')
			lpb_photo = open('/content/lpb_view.jpg', 'rb')
			bot.send_photo(message.chat.id, lpb_photo)
			bot.send_message(message.chat.id, 'Перейди по ссылке, чтобы посмотреть свободные слоты в календаре Google https://calendar.google.com/calendar/u/0/r?cid=M25wbmlmMjIxdmpmYTdsOTNxMjJlYW4xMWNAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ')			
			bot.send_message(message.chat.id, 'А вот карта, чтобы быстро найти переговорку')			
			lpb_where = open('/content/lpb_where.png', 'rb')
			bot.send_photo(message.chat.id, lpb_where)			
			bot.send_message(message.chat.id, 'Если хочешь узнать ещё о Боливии, нажми на /lpb_facts.')
		elif message.text == '/lpb_facts':
			answer = random.choice(lpb_facts)
			bot.send_message(message.chat.id, answer)
			bot.send_message(message.chat.id, 'Если хочешь узнать ещё о Боливии, нажми на /lpb_facts.')
		elif message.text == '🇮🇪 DUB':
			bot.send_message(message.chat.id, 'Чем отличаются ирландские похороны от ирландской свадьбы? На похоронах пьет и танцует на одного человека меньше.')
			dub_photo = open('/content/dub_view.jpg', 'rb')
			bot.send_photo(message.chat.id, dub_photo)
			bot.send_message(message.chat.id, 'Перейди по ссылке, чтобы посмотреть свободные слоты в календаре Google https://calendar.google.com/calendar/u/0/r?cid=Nm1hYjMxM2N2cTdyZms4c3VoOWk1azZ0c2NAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ')			
			bot.send_message(message.chat.id, 'А вот карта, чтобы быстро найти переговорку')	
			dub_where = open('/content/dub_where.png', 'rb')
			bot.send_photo(message.chat.id, dub_where)			
			bot.send_message(message.chat.id, 'Если хочешь узнать ещё об Ирландии, нажми на /dub_facts.')
		elif message.text == '/dub_facts':
			answer = random.choice(dub_facts)
			bot.send_message(message.chat.id, answer)
			bot.send_message(message.chat.id, 'Если хочешь узнать ещё об Ирландии, нажми на /dub_facts.')
		elif message.text == '🇧🇾 MSQ':
			bot.send_message(message.chat.id, 'Шчучыншчына')
			msq_photo = open('/content/msq_view.jpg', 'rb')
			bot.send_photo(message.chat.id, msq_photo)
			bot.send_message(message.chat.id, 'Перейди по ссылке, чтобы посмотреть свободные слоты в календаре Google https://calendar.google.com/calendar/u/0/r?cid=b2FyaDhpMXFhdWJmdXZmb2tubTFpMjg5bDhAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ')			
			bot.send_message(message.chat.id, 'А вот карта, чтобы быстро найти переговорку')				
			msq_where = open('/content/msq_where.png', 'rb')
			bot.send_photo(message.chat.id, msq_where)			
			bot.send_message(message.chat.id, 'Если хочешь узнать ещё о Беларуси, нажми на /msq_facts.')
		elif message.text == '/msq_facts':
			answer = random.choice(msq_facts)
			bot.send_message(message.chat.id, answer)
			bot.send_message(message.chat.id, 'Если хочешь узнать ещё о Беларуси, нажми на /msq_facts.')
		elif message.text == '🇯🇵 HND':
			bot.send_message(message.chat.id, 'В Токио уже темно и запели цикады')
			hnd_photo = open('/content/hnd_view.jpg', 'rb')
			bot.send_photo(message.chat.id, hnd_photo)
			bot.send_message(message.chat.id, 'Перейди по ссылке, чтобы посмотреть свободные слоты в календаре Google https://calendar.google.com/calendar/u/0/r?cid=cTR0NmF0MW9xZWptbGw2cXU3M3Vic3N2bjRAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ')			
			bot.send_message(message.chat.id, 'А вот карта, чтобы быстро найти переговорку')				
			hnd_where = open('/content/hnd_where.png', 'rb')
			bot.send_photo(message.chat.id, hnd_where)			
			bot.send_message(message.chat.id, 'Если хочешь узнать ещё о Японии, нажми на /hnd_facts.')
		elif message.text == '/hnd_facts':
			answer = random.choice(hnd_facts)
			bot.send_message(message.chat.id, answer)
			bot.send_message(message.chat.id, 'Если хочешь узнать ещё о Японии, нажми на /hnd_facts.')
		elif message.text == '🇩🇪 FRA':
			bot.send_message(message.chat.id, 'Где лучшее пшеничное пиво и один чемпион в футболе уже 10 лет? Правильно')
			fra_photo = open('/content/fra_view.jpg', 'rb')
			bot.send_photo(message.chat.id, fra_photo)
			bot.send_message(message.chat.id, 'Перейди по ссылке, чтобы посмотреть свободные слоты в календаре Google https://calendar.google.com/calendar/u/0?cid=cnB1a2hsdmlhMWVyYzdjdmEwNmEyYnZkMmNAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ')			
			bot.send_message(message.chat.id, 'А вот карта, чтобы быстро найти переговорку')			
			fra_where = open('/content/fra_where.png', 'rb')
			bot.send_photo(message.chat.id, fra_where)							
			bot.send_message(message.chat.id, 'Если хочешь узнать ещё о Германии, нажми на /fra_facts.')
		elif message.text == '/fra_facts':
			answer = random.choice(fra_facts)
			bot.send_message(message.chat.id, answer)
			bot.send_message(message.chat.id, 'Если хочешь узнать ещё о Германии, нажми на /fra_facts.')
		elif message.text == '🇪🇸 ALC':
			bot.send_message(message.chat.id, 'Паэлья, Саграда Фамилия и Эль-Классико')
			alc_photo = open('/content/alc_view.jpg', 'rb')
			bot.send_photo(message.chat.id, alc_photo)
			bot.send_message(message.chat.id, 'Перейди по ссылке, чтобы посмотреть свободные слоты в календаре Google https://calendar.google.com/calendar/u/0/r?cid=ODdjcDlxaWwzZ2hhcmlqOGllYmRrbHUyMG9AZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ')			
			bot.send_message(message.chat.id, 'А вот карта, чтобы быстро найти переговорку')					
			alc_where = open('/content/alc_where.png', 'rb')
			bot.send_photo(message.chat.id, alc_where)			
			bot.send_message(message.chat.id, 'Если хочешь узнать ещё об Испании, нажми на /alc_facts.')
		elif message.text == '/alc_facts':
			answer = random.choice(alc_facts)
			bot.send_message(message.chat.id, answer)
			bot.send_message(message.chat.id, 'Если хочешь узнать ещё об Испании, нажми на /alc_facts.')
		elif message.text == '🇷🇺 LED':
			bot.send_message(message.chat.id, 'Sweet Home Saint Pi ')
			led_photo = open('/content/led_view.jpg', 'rb')
			bot.send_photo(message.chat.id, led_photo)
			bot.send_message(message.chat.id, 'Перейди по ссылке, чтобы посмотреть свободные слоты в календаре Google https://calendar.google.com/calendar/u/0/r?cid=dWM5bGUwazduNzYxM2pvOGo1dXNzZzU1bm9AZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ')			
			bot.send_message(message.chat.id, 'А вот карта, чтобы быстро найти переговорку')				
			led_where = open('/content/led_where.png', 'rb')
			bot.send_photo(message.chat.id, led_where)				
			bot.send_message(message.chat.id, 'Если хочешь узнать ещё о России, нажми на /led_facts.')
		elif message.text == '/led_facts':
			answer = random.choice(led_facts)
			bot.send_message(message.chat.id, answer)
			bot.send_message(message.chat.id, 'Если хочешь узнать ещё о России, нажми на /led_facts.')
		elif message.text == '🗺 Карта':
			map2 = open('/content/main_map.jpg', 'rb')
			bot.send_photo(message.chat.id, map2)
		elif message.text == '😎 Автор бота':
			bot.send_message(message.chat.id, '@valiamat')    
		else:
			bot.send_message(message.chat.id, 'Не знаю, что ответить😢')


bot.polling(none_stop=True)









#https://core.telegram.org/bots/api#available-methods