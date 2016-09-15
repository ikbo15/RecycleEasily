var TelegramBot = require('node-telegram-bot-api');
var fs = require('fs');
var jf = require('jsonfile');
var token = '253784221:AAHx55NjmR68iBSpnYHEVRzwRkaaznkdQXg';
var bot = new TelegramBot(token, {polling: true});

//поиск нужного элемента и его номера в массиве по id(бинарный поиск)
function BinSearch(arr, searchElement, h, l)
			{
				if(l>h){
					return null
				}
				if(l===h)
				{
					if(arr[l].id === searchElement.id)
					{
						return [arr[l], l];
					}
					else
					{
						return null
					}
				}
				else
				{
					if (l+1 === h)
					{
						if(arr[l].id === searchElement.id)
						{
							return [arr[l], l]
						}
						else
						{
							if(arr[h].id === searchElement.id)
							{
								return [arr[h], h]
							}
							else
							{
								return null
							}
						}
					}
					else
					{
						var m = Math.floor((l + h)/2);
						if (arr[m].id === searchElement.id)
						{
							return [arr[m], m]
						}
						else
						{
							if(searchElement.id>arr[m].id)
							{
								return search(arr, searchElement, h, m+1)
							}
							else
							{
								return search(arr, searchElement, m-1, l)
							}
						}
					}
				}
			}

function BinSearch2(arr, searchPoints, h, l, d)
{
	if(l>h){
		return null
	}
	if(l===h)
	{
		if(arr[l].searchPoints - searchPoints <= d)
		{
			return [arr[l], l];
		}
		else
		{
			return null
		}
	}
	else
	{
		if (l+1 === h)
		{
			if(arr[l].searchPoints - searchPoints<=d)
			{
				return [arr[l], l]
			}
			else
			{
				if(arr[h].searchPoints - searchPoints<=d)
				{
					return [arr[h], h]
				}
				else
				{
					return null
				}			
			}
		}
		else
		{
			var m = Math.floor((l + h)/2);
			if (arr[m].searchPoints - searchPoints <= d)
			{
				return [arr[m], m]
			}
			else
			{
				if(searchElement.searchPoints>arr[m].searchPoints)
				{
					return search(arr, searchPoints, h, m+1, d)
				}
				else
				{
					return search(arr, searchPoints, m-1, l, d)
				}
			}
		}
	}
}

//класс робота			
function Robot()
{
	this.hitPoints = 100;
    this.damage = 10;
	this.armor = 5;
	this.level = 1
}			

//класс "ищущего игрока"
function SearchUser(user, location)
{
	this.userId = user.id;
	this.chatId = user.chatId;
	this.searchPoints = user.robot.armor*20 + user.robot.damage*10 + user.robot.hitPoints;
	this.location = location
}

//класс "сражающегося игрока"
function FightUser(user)
{
	this.userId = user.id;
	this.chatId = user.chatId
	this.hitPoints = user.robot.hitPoints;
	this.damade = user.robot.damade;
	this.armor = user.robot.armor;
	
}

function Room(_player1, _player2)
{
	this.id;
	this.player1 = _player1;
	this.player2 = _player2;
	this.turn = 1;
}

//построение магазинного меню(добавление к шаблону цен и баланса)
function GetShopMenu(_user)
{
	var menu = jf.readFileSync('./data/menu/shop_menu.json');
	var armorCost = require('./data/prices/armor_price.json').Cost[_user.armorLevel];
	var weaponCost = require('./data/prices/weapon_price.json').Cost[_user.weaponLevel];
	menu.keyboard[1][1].text += '(' + armorCost + ')';
	menu.keyboard[1][0].text += '(' + weaponCost + ')';
	menu.keyboard[2][0].text += _user.money;
	return menu
}

bot.on('message', function (msg) {
	//получаем массив пользователей
	var users = jf.readFileSync('./data/Users.json').users;
	//тут находятся команды не имеющие отношение к бою(тет-а-тет с ботом)
	if(msg.chat.type === "private")
	{
		var chatId = msg.chat.id; //куда будем отсылать ответы
		var user = BinSearch(users, msg.from, users.length-1, 0); // ищем пользователя среди зарегестрированых
		var userN; //номер пользователя в массиве зарегестeрированых пользователей
		var txt = msg.text; //текст сообщения
		//регистрация пользователя
		if (txt === '/registration') {
			if(user === null)
			{
				//добовляем новые поля для нашего пльзователя
				user = msg.from;
				user.robot = new Robot();
				user.state = "main_menu";
				user.money = 100;
				user.armorLevel = 0;
				user.weaponLevel = 0;
				user.room = null;
				user.chatId = chatId;
				//вставляем пользователя в массив так чтобы массив остался отсортированным(пузырьком)
				for(var i = users.length; i>=0; i--)
				{
					if(i>0)
					{
						if(user.id<users[i-1].id)
						{
							users[i] = users[i-1]
						}
						else
						{
							users[i] = user;
							break
						}
					}
					else
					{
						users[0] = user;
					}
				}
				//выводим клавиатуру главного меню
				bot.sendMessage(chatId, 'Вы зарегестрированы', {reply_markup : require('./data/menu/main_menu.json')});
				//переписываем файл с массивом пользователей
				fs.writeFile('./data/Users.json', JSON.stringify({users}, null, 4))
			}
			else
			{
				bot.sendMessage(chatId, 'Вы уже зарегестрированы', {reply_markup : require('./data/menu/main_menu.json')})
			}
		}
		//если пользователь не зарегистрирован до других команд даже не доходим
		if(user === null)
		{
			bot.sendMessage(chatId, 'Зарегистрируйтесь с помощью команды /registration')
			return//прерывание функции
		}
		else
		{
				userN = user[1];
				user = user[0];
		}
		//поиск противника
		if(msg.location != null && user.state === "main_menu")
		{
			console.log(msg.location);
			txt = 'null';
			var srch = new SearchUser(users[userN], msg.location);
			var searchUsersArray = jf.readFileSync('./data/Search.json').searchUsersArray;
			var enemy = BinSearch2(searchUsersArray, srch.searchPoints, searchUsersArray.length-1, 0, 30);
			if(enemy === null)
			{
				for(var i = searchUsersArray.length; i>=0; i--)
				{
					if(i>0)
					{
						if(srch.searchPoints<searchUsersArray[i-1].searchPoints)
						{
							searchUsersArray[i] = searchUsersArray[i-1]
						}
						else
						{
							searchUsersArray[i] = srch;
							break
						}
					}
					else
					{
						searchUsersArray[0] = srch;
					}
				}
				fs.writeFile('./data/Search.json', JSON.stringify({searchUsersArray}, null, 4));
				users[userN].state = "search_menu";
				bot.sendMessage(chatId, 'Поиск соперника...', {reply_markup : require('./data/menu/search_menu.json')});
				fs.writeFile('./data/Users.json', JSON.stringify({users}, null, 4))
			}
			else
			{
				var enemyN = BinSearch(users, {id : enemy[0].userId}, users.length-1, 0)[1];
				var searchN = enemy[1];
				bot.sendMessage(enemy[0].chatId, 'Противник найден', {reply_markup : require('./data/menu/fight_menu.json')});
				bot.sendMessage(chatId, 'Противник найден', {reply_markup : require('./data/menu/fight_menu.json')});
				users[userN].state = 'fight_menu';
				users[enemyN].state = "fight_menu";
				for(var i = searchN; i<searchUsersArray.length; i++)
				{
					if(i < searchUsersArray.length-1)
					{
						searchUsersArray[i] = searchUsersArray[i+1]
					}
					else
					{
						searchUsersArray[i] = null;
					}
				}
				var room = new Room(new FightUser(users[userN]), new FightUser(users[enemyN]));
				var rooms = jf.readFileSync('./data/Rooms.json').rooms;
				rooms[rooms.length] = room;
				fs.writeFile('./data/Users.json', JSON.stringify({users}, null, 4))
				fs.writeFile('./data/Search.json', JSON.stringify({searchUsersArray}, null, 4))
				fs.writeFile('./data/Rooms.json', JSON.stringify({rooms}, null, 4))
			}
		}
		//выводим характеристики робота
		if(txt === 'ХАРАКТЕРИСТИКИ' && (user.state === "main_menu" || user.state === "shop_menu"))
		{
			var answer = 'ХАРАКТЕРИСТИКИ ВАШЕГО РОБОТА\n' + 
					     'Уровень - ' + user.robot.level + '\n' +
						 'Здоровье - ' + user.robot.hitPoints + '\n' +
						 'Урон - ' + user.robot.damage + '\n' + 
						 'Защита - ' + user.robot.armor + '\n';
			bot.sendMessage(chatId, answer)
		}
		//переходим в меню магазина
		if(txt === 'МАГАЗИН' && user.state === "main_menu")
		{
			users[userN].state = 'shop_menu';
			fs.writeFile('./data/Users.json', JSON.stringify({users}, null, 4))
			bot.sendMessage(chatId, 'Выберите улучшение для своего робота', {reply_markup : GetShopMenu(user)})
		}
		//улучшение оружия
		if(txt.search('УЛУЧШИТЬ ОРУЖИЕ') != -1 && user.state === "shop_menu")
		{
			var weaponCost = require('./data/prices/weapon_price.json').Cost[user.weaponLevel];
			if (weaponCost <= user.money)
			{
				if(weaponCost != 'max')
				{
					users[userN].robot.damage += 2;
					users[userN].weaponLevel++;
					users[userN].money -= weaponCost;
					fs.writeFile('./data/Users.json', JSON.stringify({users}, null, 4));
					bot.sendMessage(chatId, 'Оружие улучшено(+2 к урону)', {reply_markup : GetShopMenu(users[userN])})
				}
				else
				{
					bot.sendMessage(chatId, 'Ваше оружие уже не требует улучшений', {reply_markup : GetShopMenu(users[userN])})
				}
			}
			else
			{
				bot.sendMessage(chatId, 'Нехватает кредитов', {reply_markup : GetShopMenu(users[userN])})				
			}
		}
		//улучшение брони
		if(txt.search('УЛУЧШИТЬ БРОНЮ') != -1 && user.state === "shop_menu")
		{
			var armorCost = require('./data/prices/weapon_price.json').Cost[user.armorLevel];
			if (armorCost <= user.money)
			{
				if(armorCost != 'max')
				{
					users[userN].robot.armor += 1;
					users[userN].armorLevel++;
					users[userN].money -= armorCost;
					fs.writeFile('./data/Users.json', JSON.stringify({users}, null, 4));
					bot.sendMessage(chatId, 'Броня улучшена(+1 к защите)', {reply_markup : GetShopMenu(users[userN])})
				}	
				else
				{
					bot.sendMessage(chatId, 'Ваша броня уже не требует улучшений', {reply_markup : GetShopMenu(users[userN])})
				}
			}
			else
			{
				bot.sendMessage(chatId, 'Нехватает кредитов', {reply_markup : GetShopMenu(users[userN])})
			}
		}
		//возвращение в главное меню
		if(txt === "НАЗАД")
		{
			users[userN].state = 'main_menu';
			fs.writeFile('./data/Users.json', JSON.stringify({users}, null, 4))
			bot.sendMessage(chatId, 'Главное меню', {reply_markup : require('./data/menu/main_menu.json')})
		}
	}
});
