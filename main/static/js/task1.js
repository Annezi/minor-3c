document.addEventListener('DOMContentLoaded', () => {
	const form = document.getElementById('task1-form');
	if (form) {
		form.addEventListener('submit', (event) => {
			event.preventDefault();

			const countriesInput = document.getElementById('countries').value.trim().split(/\s+/);
			const gdpInput = document.getElementById('gdp_per_capita').value.trim().split(/\s+/);
			const threshold = parseFloat(document.getElementById('threshold').value);

			if (countriesInput.length !== gdpInput.length || isNaN(threshold)) {
				alert('Ошибка: Проверьте введенные данные.');
				return;
			}

			// Фильтруем страны
			const result = [];
			for (let i = 0; i < countriesInput.length; i++) {
				const gdp = parseFloat(gdpInput[i]);
				if (!isNaN(gdp) && gdp >= threshold) {
					result.push(countriesInput[i]);
				}
			}

			const resultContainer = document.getElementById('task1-result');
			if (result.length > 0) {
				resultContainer.innerHTML = `<ul>${result.map(country => `<li>${country}</li>`).join('')}</ul>`;
			} else {
				resultContainer.innerHTML = '<p>Нет стран, удовлетворяющих условию.</p>';
			}
		});
	}
});