day_names = {
	0: "Понедельник",
	1: "Вторник",
	2: "Среда",
	3: "Четверг",
	4: "Пятница",
	5: "Суббота",
}

numb_to_lat = {
	0: "I",
	1: "II",
	2: "III",
	3: "IV",
	4: "V",
}

function openModalForm(data, day, numb) {
	for (var i=0;i<=2;i++) {
		document.getElementById('body'+ i).value = ''
		document.getElementById('teacher'+ i).value = ''
		document.getElementById('room'+ i).value = ''
		document.getElementById('frequency'+ i).value = ''
		document.getElementById('enable'+ i).checked = false
	}	

	document.getElementById('mformStatus').innerHTML = day_names[day] 
		+ ", " 
		+ numb_to_lat[numb]
		+ " пара."
	for (var key in data[day][numb]) {
		document.getElementById('body'+ key).value = data[day][numb][key]['body']
		document.getElementById('teacher'+ key).value = data[day][numb][key]['teacher']
		document.getElementById('room'+ key).value = data[day][numb][key]['room']
		document.getElementById('frequency'+ key).value = data[day][numb][key]['frequency']
		document.getElementById('enable'+ key).checked = true
		
	}
	location.href='#modalForm'
}
