var previousOperation = '+';
var previousValue = 0;
var currentValue = 0;


function calculate(newValue) {
	var displayEl = document.getElementById("calcDisplay");
	
	if(newValue == '-' || newValue == '+') {
		updateDisplay();
		previousOperation = newValue;
		currentValue = '';
		return;
		}
	
	if(newValue == '×') {
		updateDisplay();
		previousOperation = '*';
		currentValue = '';
		return;
	}
	
	if(newValue == '÷') {
		updateDisplay();
		previousOperation = '/';
		currentValue = '';
		return;
	}

	
	if(newValue == '=') {
		updateDisplay();
		previousValue = 0;
		previousOperation = '+';
		currentValue = '';
		return;
	}
	
	if(currentValue == 0) {
		currentValue = newValue;
	}
	else {
		currentValue = currentValue + newValue;
	}
	displayEl.value = currentValue;
}

function updateDisplay() {
	var displayEl = document.getElementById("calcDisplay");
	switch(previousOperation) {
		case '-':
			previousValue = parseInt(previousValue) - parseInt(currentValue);
			break;
		case '+':
			previousValue = parseInt(previousValue) + parseInt(currentValue);
			break;
		case '*':
			previousValue = parseInt(previousValue) * parseInt(currentValue);
			break;
		case '/':
			if(parseInt(currentValue) == 0) {
				displayEl.value = 'error';
				previousValue = 0;
				previousOperation = '+';
				currentValue = '';
				return;
				break;
			}
			previousValue = parseInt(previousValue) / parseInt(currentValue);
			break;
	}
	if(isNaN(previousValue)) {
		return;
	}
	displayEl.value = previousValue;
}