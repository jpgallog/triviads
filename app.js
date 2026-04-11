import { questions } from './questions.js';

const app = document.getElementById('app');

let currentQuestions = [];
let currentQuestionIndex = 0;
let score = 0;
let currentDifficulty = null;
let timerInterval;
const TIME_LIMIT = 15;
let timeLeft = TIME_LIMIT;
let lives = 3;
let streak = 0;
let errorsList = [];

// Audio Context Web API (SFX)
const AudioContext = window.AudioContext || window.webkitAudioContext;
let audioCtx;
function initAudio() { if (!audioCtx) audioCtx = new AudioContext(); }
function playTone(freq, type, duration, vol) {
    if (!audioCtx) return;
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    osc.type = type; gain.gain.setValueAtTime(vol, audioCtx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + duration);
    osc.connect(gain); gain.connect(audioCtx.destination);
    osc.start(); osc.stop(audioCtx.currentTime + duration);
}
function playSuccess() { playTone(600, 'sine', 0.1, 0.1); setTimeout(() => playTone(800, 'sine', 0.15, 0.1), 100); }
function playError() { playTone(300, 'square', 0.2, 0.05); setTimeout(() => playTone(250, 'square', 0.3, 0.05), 150); }
function playTick() { playTone(1000, 'sine', 0.05, 0.02); }
function playGameOver() { playTone(200, 'sawtooth', 0.4, 0.1); setTimeout(() => playTone(150, 'sawtooth', 0.6, 0.1), 300); }

function showFloatingScore(points, x, y) {
    const el = document.createElement('div');
    el.className = 'floating-score'; el.textContent = `+${points}`;
    el.style.left = `${x}px`; el.style.top = `${y}px`;
    document.body.appendChild(el);
    setTimeout(() => el.remove(), 1000);
}

function getHighScore(difficulty) {
    if (!difficulty) return 0;
    return parseInt(localStorage.getItem(`meli_ads_highscore_${difficulty}`) || '0');
}

function saveHighScore(newScore, difficulty) {
    if (!difficulty) return false;
    const currentHigh = getHighScore(difficulty);
    if (newScore > currentHigh) {
        localStorage.setItem(`meli_ads_highscore_${difficulty}`, newScore);
        return true;
    }
    return false;
}

function shuffle(array) {
  const arr = [...array];
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}

function renderStart() {
    const hsFacil = getHighScore('facil');
    const hsIntermedio = getHighScore('intermedio');
    const hsDificil = getHighScore('dificil');

    let highScoresHtml = '';
    if (hsFacil > 0 || hsIntermedio > 0 || hsDificil > 0) {
        highScoresHtml = `
            <div class="highscores-list" style="display:flex; justify-content:center; gap:10px; font-size:0.85rem; margin-bottom: 20px;">
                <div class="score-pill" style="color:#00a650; background:#f7f7f7; padding:4px 10px; border-radius:12px; border:1px solid #e1e1e1;">Fácil: <strong>${hsFacil}</strong></div>
                <div class="score-pill" style="color:#fb8c00; background:#f7f7f7; padding:4px 10px; border-radius:12px; border:1px solid #e1e1e1;">Medio: <strong>${hsIntermedio}</strong></div>
                <div class="score-pill" style="color:#f23d4f; background:#f7f7f7; padding:4px 10px; border-radius:12px; border:1px solid #e1e1e1;">Alto: <strong>${hsDificil}</strong></div>
            </div>
        `;
    }

    app.innerHTML = `
        <div class="card">
            <img src="logo.png" alt="TriviAds Logo" style="width: 120px; height: 120px; margin: 0 auto 15px; display: block; filter: drop-shadow(0 10px 20px rgba(0,0,0,0.15));">
            <h1>TriviAds</h1>
            ${highScoresHtml}
            <p class="subtitle" style="margin-top: -5px;">Elige tu nivel de dificultad para comenzar el reto.<br/>Tienes 15 segundos por pregunta.</p>
            <div class="difficulty-container">
                <button class="diff-btn diff-facil" data-diff="facil">Nivel Fácil</button>
                <button class="diff-btn diff-intermedio" data-diff="intermedio">Nivel Intermedio</button>
                <button class="diff-btn diff-dificil" data-diff="dificil">Nivel Difícil</button>
            </div>
        </div>
    `;

    const diffBtns = document.querySelectorAll('.diff-btn');
    diffBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            initAudio(); // Initialize audio context on first user gesture
            currentDifficulty = e.target.closest('button').dataset.diff;
            const filteredQuestions = questions.filter(q => q.difficulty === currentDifficulty);
            currentQuestions = shuffle(filteredQuestions).slice(0, 10);
            currentQuestionIndex = 0;
            score = 0;
            lives = 3;
            streak = 0;
            errorsList = [];
            renderQuestion();
        });
    });
}

function renderQuestion() {
    clearTimeout(timerInterval);
    timeLeft = TIME_LIMIT;
    const question = currentQuestions[currentQuestionIndex];
    
    const hearts = '❤️'.repeat(lives) + '🖤'.repeat(3 - lives);
    const streakHtml = streak >= 3 ? `<span class="streak">🔥 Racha x${streak}</span>` : '';
    const progressPercent = (currentQuestionIndex / currentQuestions.length) * 100;

    app.innerHTML = `
        <div class="card">
            <div class="top-stats" style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 25px; flex-wrap: wrap; gap: 10px;">
                <div class="lives-and-streak" style="display: flex; align-items: center; gap: 12px;">
                    <div class="lives-container" id="lives-display" style="margin: 0;">
                        ${'<span class="heart">❤️</span>'.repeat(lives)}${'<span class="heart error">💔</span>'.repeat(3 - lives)}
                    </div>
                    ${streakHtml}
                </div>
                <div class="timer-pill" id="timer-display" style="margin: 0; padding: 6px 14px; font-size: 1.05rem;">
                    <svg width="16" height="16" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
                    <span>${timeLeft}s</span>
                </div>
            </div>
            <div class="progress-container">
                <div class="progress-bar" style="width: ${progressPercent}%;"></div>
            </div>
            <div class="top-bar" style="margin-bottom: 15px;">
                <div class="status-bar" style="width: 100%; justify-content: space-between; margin-bottom: 0;">
                    <span>Pregunta ${currentQuestionIndex + 1} de ${currentQuestions.length}</span>
                    <span>Puntos: ${score}</span>
                </div>
            </div>
            
            <h2 class="question-text">${question.question}</h2>
            <div class="options-container" id="options">
                ${question.options.map((opt, index) => `
                    <button class="option-btn" data-index="${index}">${opt}</button>
                `).join('')}
            </div>
            <div id="feedback" style="display:none;">
                <div class="explanation" id="explanation"></div>
                <button class="btn next-btn" id="next-btn">Continuar</button>
            </div>
        </div>
    `;

    const optionBtns = document.querySelectorAll('.option-btn');
    optionBtns.forEach(btn => {
        btn.addEventListener('click', handleAnswer);
    });

    startTimer();
}

function startTimer() {
    const timerDisplay = document.querySelector('#timer-display span');
    const timerPill = document.getElementById('timer-display');
    
    timerInterval = setInterval(() => {
        timeLeft--;
        timerDisplay.textContent = `${timeLeft}s`;
        
        if (timeLeft <= 5 && timeLeft > 0) {
            timerPill.classList.add('warning');
            playTick();
        }

        if (timeLeft <= 0) {
            clearInterval(timerInterval);
            handleTimeout();
        }
    }, 1000);
}

function handleTimeout() {
    const question = currentQuestions[currentQuestionIndex];
    streak = 0;
    lives--;
    playError();
    app.querySelector('.card').classList.add('shake');
    setTimeout(() => app.querySelector('.card').classList.remove('shake'), 400);
    errorsList.push({ q: question.question, correct: question.options[question.correctAnswer] });
    
    const optionBtns = document.querySelectorAll('.option-btn');
    optionBtns.forEach(btn => {
        btn.disabled = true;
        btn.style.opacity = '0.7';
        if (parseInt(btn.dataset.index) === question.correctAnswer) {
            btn.classList.add('correct');
            btn.style.opacity = '1';
        }
    });

    const feedback = document.getElementById('feedback');
    const explanation = document.getElementById('explanation');
    const nextBtn = document.getElementById('next-btn');
    
    explanation.innerHTML = `<strong>¡Se acabó el tiempo! ⏱️</strong><br/> ${question.explanation}`;
    explanation.style.borderLeftColor = 'var(--error)';
    
    feedback.style.display = 'block';

    setTimeout(() => {
        nextBtn.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }, 100);

    nextBtn.addEventListener('click', () => {
        if (lives <= 0) { playGameOver(); renderResult(true); }
        else {
            currentQuestionIndex++;
            if (currentQuestionIndex < currentQuestions.length) { renderQuestion(); }
            else { renderResult(false); }
        }
    });
}

function handleAnswer(e) {
    if(timeLeft <= 0) return;
    clearInterval(timerInterval);
    
    const selectedBtn = e.target;
    if(selectedBtn.disabled) return;
    
    const selectedIndex = parseInt(selectedBtn.dataset.index);
    const question = currentQuestions[currentQuestionIndex];
    const isCorrect = selectedIndex === question.correctAnswer;

    const optionBtns = document.querySelectorAll('.option-btn');
    optionBtns.forEach(btn => {
        btn.disabled = true;
        btn.style.opacity = '0.7';
        if (parseInt(btn.dataset.index) === question.correctAnswer) {
            btn.classList.add('correct');
            btn.style.opacity = '1';
        }
    });

    if (isCorrect) {
        streak++;
        let pointsEarned = 100;
        if (streak >= 3) pointsEarned *= 2;
        score += pointsEarned;
        playSuccess();
        triggerConfetti(e.clientX, e.clientY);
        showFloatingScore(pointsEarned, e.clientX, e.clientY);
    } else {
        streak = 0;
        lives--;
        playError();
        app.querySelector('.card').classList.add('shake');
        setTimeout(() => app.querySelector('.card').classList.remove('shake'), 400);
        errorsList.push({ q: question.question, correct: question.options[question.correctAnswer] });
        
        selectedBtn.classList.add('wrong');
        selectedBtn.style.opacity = '1';
    }

    document.querySelector('.status-bar').innerHTML = `
        <span>Pregunta ${currentQuestionIndex + 1} de ${currentQuestions.length}</span>
        <span>Puntos: ${score}</span>
    `;

    const feedback = document.getElementById('feedback');
    const explanation = document.getElementById('explanation');
    const nextBtn = document.getElementById('next-btn');
    
    explanation.innerHTML = `<strong>${isCorrect ? '¡Correcto!' : '¡Oops!'}</strong><br/> ${question.explanation}`;
    explanation.style.borderLeftColor = isCorrect ? 'var(--success)' : 'var(--error)';
    feedback.style.display = 'block';

    setTimeout(() => {
        nextBtn.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }, 100);

    nextBtn.addEventListener('click', () => {
        if (lives <= 0) { playGameOver(); renderResult(true); }
        else {
            currentQuestionIndex++;
            if (currentQuestionIndex < currentQuestions.length) { renderQuestion(); }
            else { renderResult(false); }
        }
    });
}

function renderResult(isGameOver = false) {
    const isNewHigh = saveHighScore(score, currentDifficulty);
    
    let message = "";
    if (isGameOver) {
        message = "¡Te quedaste sin vidas! 💔 Repasa e inténtalo de nuevo.";
    } else if (score >= 1000) {
        message = "¡Impresionante! Has dominado el juego nivel Black. 🚀";
        triggerMassiveConfetti();
    } else {
        message = "¡Muy buen esfuerzo! Completaste el desafío. 💡";
        triggerMassiveConfetti();
    }

    const newRecordHtml = isNewHigh && score > 0 ? `<div class="high-score-badge" style="background:#fff159; border-color:#d4c74a;">🎉 ¡Nuevo Récord Personal!</div>` : '';

    let errorSummaryHtml = '';
    if (errorsList.length > 0) {
        errorSummaryHtml = `
            <div class="error-summary">
                <h3 style="font-size:1.05rem; color:#444; margin-bottom:12px;">📚 Preguntas para repasar:</h3>
                ${errorsList.map(e => `
                    <div class="error-item">
                        <p><strong>P:</strong> ${e.q}</p>
                        <p><strong>R:</strong> <span class="correct-ans">${e.correct}</span></p>
                    </div>
                `).join('')}
            </div>
        `;
    }

    app.innerHTML = `
        <div class="card">
            <h1>Evaluación Final</h1>
            ${newRecordHtml}
            <div class="score-display" style="font-size:3.5rem;">${score} <span style="font-size: 1.2rem; color:#888;">pts</span></div>
            <p class="score-message">${message}</p>
            ${errorSummaryHtml}
            <button class="btn" id="restart-btn" style="margin-top: 20px;">Jugar de Nuevo</button>
        </div>
    `;

    document.getElementById('restart-btn').addEventListener('click', renderStart);
}

// Visual Effects
function triggerConfetti(x, y) {
    if (window.confetti) {
        try {
            const xPos = x / window.innerWidth;
            const yPos = y / window.innerHeight;
            confetti({
                particleCount: 50,
                spread: 70,
                origin: { x: xPos, y: yPos },
                colors: ['#FFF159', '#3483FA', '#00a650'],
                zIndex: 1000
            });
        } catch(e) {}
    }
}

function triggerMassiveConfetti() {
    if (window.confetti) {
        var duration = 3 * 1000;
        var animationEnd = Date.now() + duration;
        var defaults = { startVelocity: 30, spread: 360, ticks: 60, zIndex: 1000 };

        var interval = setInterval(function() {
            var timeLeft = animationEnd - Date.now();
            if (timeLeft <= 0) return clearInterval(interval);
            var particleCount = 50 * (timeLeft / duration);
            confetti(Object.assign({}, defaults, { particleCount, origin: { x: randomInRange(0.1, 0.3), y: Math.random() - 0.2 }, colors: ['#FFF159', '#3483FA', '#00a650'] }));
            confetti(Object.assign({}, defaults, { particleCount, origin: { x: randomInRange(0.7, 0.9), y: Math.random() - 0.2 }, colors: ['#FFF159', '#3483FA', '#00a650'] }));
        }, 250);
    }
}

function randomInRange(min, max) {
    return Math.random() * (max - min) + min;
}

// Initial Render
renderStart();
