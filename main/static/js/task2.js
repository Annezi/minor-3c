document.addEventListener('DOMContentLoaded', () => {
	const form = document.getElementById('task2-form');
	if (form) {
		form.addEventListener('submit', (event) => {
			event.preventDefault();

			const year = parseInt(document.getElementById('year').value);

			if (isNaN(year)) {
				alert('Ошибка: Год должен быть целым числом.');
				return;
			}

			// Определяем, является ли год високосным
			const isLeapYear = (year % 4 === 0 && (year % 100 !== 0 || year % 400 === 0));
			// Определяем век
			const century = Math.floor((year - 1) / 100) + 1;

			const resultContainer = document.getElementById('task2-result');
			resultContainer.innerHTML = `
                <ul>
                    <li>Год: ${year}</li>
                    <li>Високосный: ${isLeapYear ? 'Да' : 'Нет'}</li>
                    <li>Век: ${century}</li>
                </ul>
            `;
		});
	}
});