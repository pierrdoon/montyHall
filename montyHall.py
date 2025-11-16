function montyHall() {
    const door = ['0', '0', '1'];
    let choice = Math.floor(Math.random() * 3);
    const availableReveals = [];
    
    // Находим двери, которые можно открыть (не выбранная игроком и с козлом)
    for (let i = 0; i < 3; i++) {
        if (i !== choice && door[i] === '0') {
            availableReveals.push(i);
        }
    }
    
    // Выбираем случайную дверь для открытия
    const reveals = availableReveals[Math.floor(Math.random() * availableReveals.length)];
    const switchChoice = Math.random() < 0.5;
    
    if (switchChoice) {
        // Находим оставшуюся дверь для переключения
        for (let i = 0; i < 3; i++) {
            if (i !== choice && i !== reveals) {
                choice = i;
                break;
            }
        }
    }
    
    return door[choice] === '1';
}

let wins = 0;
const attempts = 10000;

for (let i = 0; i < attempts; i++) {
    if (montyHall()) {
        wins++;
    }
}

const winPercentage = (wins / attempts) * 100;
console.log(`Процент побед после ${attempts} попыток: ${winPercentage}%`);