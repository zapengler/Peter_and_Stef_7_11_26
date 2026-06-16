html_content = r'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Stefanie & Peter</title>
    <link href="https://fonts.googleapis.com/css2?family=Libre+Baskerville:wght@400;700&display=swap" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            background: #ffffff;
            font-family: circular, helvetica, sans-serif;
            color: #21201f;
            line-height: 1.5;
        }

        /* --- Screens --- */
        .screen { display: none; width: 100%; max-width: 500px; padding: 30px 20px; text-align: center; }
        .screen.active { display: flex; flex-direction: column; align-items: center; }

        /* --- Typography --- */
        h1 { font-family: 'Libre Baskerville', serif; color: #667D5D; font-size: 32px; margin-bottom: 5px; }
        h2 { font-family: 'Libre Baskerville', serif; color: #667D5D; font-size: 24px; margin-bottom: 10px; }
        .subtitle { color: #888; font-size: 16px; margin-bottom: 25px; font-family: 'Libre Baskerville', serif; }
        .welcome { color: #555; font-size: 15px; margin-bottom: 30px; line-height: 1.6; }

        /* --- Buttons --- */
        .btn {
            display: inline-block; padding: 14px 30px; font-size: 15px;
            background: #667D5D; color: #ffffff; border: none; border-radius: 6px;
            cursor: pointer; margin: 6px; transition: background 0.2s;
            font-family: 'Libre Baskerville', serif; min-width: 220px;
        }
        .btn:hover { background: #576e4f; }
        .btn.disabled {
            background: #c5c5c5; cursor: not-allowed; color: #888;
        }
        .btn.disabled:hover { background: #c5c5c5; }
        .btn.unlocked { background: #667D5D; cursor: pointer; color: #fff; }
        .btn.unlocked:hover { background: #576e4f; }
        .btn-small {
            padding: 10px 20px; font-size: 13px; min-width: 140px;
        }
        .back-btn {
            align-self: flex-start; background: none; border: none; cursor: pointer;
            color: #667D5D; font-size: 20px; margin-bottom: 10px; padding: 5px 10px;
            font-family: 'Libre Baskerville', serif;
        }
        .back-btn:hover { color: #576e4f; }

        /* --- Game info --- */
        .game-info { margin-bottom: 15px; font-size: 16px; color: #666; }

        /* --- Sliding Puzzle --- */
        #puzzle-grid {
            display: grid; grid-template-columns: repeat(4, 72px); grid-template-rows: repeat(4, 72px);
            gap: 4px; background: #e8ece6; padding: 8px; border-radius: 10px;
        }
        .tile {
            display: flex; align-items: center; justify-content: center;
            font-size: 22px; font-weight: bold; border-radius: 6px;
            cursor: pointer; transition: all 0.15s ease;
        }
        .tile.number { background: #667D5D; color: #ffffff; }
        .tile.number:hover { background: #576e4f; }
        .tile.empty { background: transparent; cursor: default; }

        /* --- Memory Match --- */
        #memory-grid {
            display: grid; grid-template-columns: repeat(4, 72px); grid-template-rows: repeat(4, 72px);
            gap: 6px; margin-bottom: 10px;
        }
        .card {
            width: 72px; height: 72px; border-radius: 8px; cursor: pointer;
            display: flex; align-items: center; justify-content: center;
            font-size: 28px; transition: transform 0.3s; position: relative;
            background: #667D5D; color: #667D5D; border: 2px solid #e8ece6;
            user-select: none;
        }
        .card.flipped, .card.matched { background: #ffffff; color: #21201f; border: 2px solid #667D5D; }
        .card.matched { cursor: default; }

        /* --- Word Scramble --- */
        #scramble-display {
            font-family: 'Libre Baskerville', serif; font-size: 32px;
            letter-spacing: 6px; color: #667D5D; margin: 20px 0;
            font-weight: 700;
        }
        #guess-input {
            padding: 12px 20px; font-size: 18px; border: 2px solid #e8ece6;
            border-radius: 6px; text-align: center; width: 250px;
            font-family: circular, helvetica, sans-serif; color: #21201f;
            outline: none;
        }
        #guess-input:focus { border-color: #667D5D; }
        .hint { color: #888; font-size: 14px; margin: 10px 0 15px; }
        .scramble-feedback { color: #c0392b; font-size: 14px; min-height: 20px; margin-top: 8px; }

        /* --- Seating Chart --- */
        .seating-table {
            width: 100%; border-collapse: collapse; margin: 15px 0;
            font-size: 14px;
        }
        .seating-table th {
            background: #667D5D; color: #fff; padding: 10px 15px;
            font-family: 'Libre Baskerville', serif; font-weight: 400;
        }
        .seating-table td {
            padding: 10px 15px; border-bottom: 1px solid #e8ece6;
        }
        .seating-table tr:hover td { background: #f5f7f4; }

        /* --- Win Overlay --- */
        .overlay {
            display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0,0,0,0.5); z-index: 1000;
            justify-content: center; align-items: center;
        }
        .overlay.active { display: flex; }
        .overlay-box {
            background: #fff; border-radius: 12px; padding: 40px 30px;
            text-align: center; max-width: 360px; width: 90%;
        }
        .overlay-box h2 { margin-bottom: 8px; }
        .overlay-box p { color: #666; margin-bottom: 20px; font-size: 15px; }

        /* --- Lock icon --- */
        .lock-label { display: block; font-size: 12px; color: #aaa; margin-top: 4px; }
    </style>
</head>
<body>

<!-- ==================== HOME SCREEN ==================== -->
<div id="home" class="screen active">
    <h1>Stefanie & Peter</h1>
    <div class="subtitle">July 11, 2026 &middot; Mount Airy, NC</div>
    <div class="welcome">Welcome! Play a game to unlock the seating chart. Choose any game below — you only need to win once.</div>
    <button class="btn" onclick="showScreen('puzzle')">&#129513; Sliding Puzzle</button>
    <button class="btn" onclick="showScreen('memory')">&#127183; Memory Match</button>
    <button class="btn" onclick="showScreen('scramble')">&#128221; Word Scramble</button>
    <div style="margin-top: 15px;">
        <button id="seating-btn" class="btn disabled" onclick="goSeating()" disabled>
            &#128274; View Seating Chart
            <span id="lock-label" class="lock-label">Win any game to unlock!</span>
        </button>
    </div>
</div>

<!-- ==================== SLIDING PUZZLE ==================== -->
<div id="puzzle" class="screen">
    <button class="back-btn" onclick="showScreen('home')">&larr; Home</button>
    <h2>Sliding Puzzle</h2>
    <div id="puzzle-moves" class="game-info">Moves: 0</div>
    <div id="puzzle-grid"></div>
    <button class="btn btn-small" style="margin-top:15px;" onclick="shufflePuzzle()">Shuffle</button>
</div>

<!-- ==================== MEMORY MATCH ==================== -->
<div id="memory" class="screen">
    <button class="back-btn" onclick="showScreen('home')">&larr; Home</button>
    <h2>Memory Match</h2>
    <div id="memory-moves" class="game-info">Moves: 0</div>
    <div id="memory-grid"></div>
    <button class="btn btn-small" style="margin-top:10px;" onclick="initMemory()">Reset</button>
</div>

<!-- ==================== WORD SCRAMBLE ==================== -->
<div id="scramble" class="screen">
    <button class="back-btn" onclick="showScreen('home')">&larr; Home</button>
    <h2>Word Scramble</h2>
    <div id="scramble-display"></div>
    <div class="hint" id="scramble-hint"></div>
    <input type="text" id="guess-input" placeholder="Your guess..." autocomplete="off">
    <div class="scramble-feedback" id="scramble-feedback"></div>
    <div style="margin-top:12px;">
        <button class="btn btn-small" onclick="checkGuess()">Submit</button>
        <button class="btn btn-small" onclick="newWord()">New Word</button>
    </div>
</div>

<!-- ==================== SEATING CHART ==================== -->
<div id="seating" class="screen">
    <button class="back-btn" onclick="showScreen('home')">&larr; Home</button>
    <h2>Seating Chart</h2>
    <p style="color:#666; margin-bottom:15px;">Find your table below!</p>
    <table class="seating-table">
        <thead>
            <tr><th>Table</th><th>Guests</th></tr>
        </thead>
        <tbody>
            <tr><td>1</td><td>Mom & Dad Kraack, Grandma Kraack, Uncle Jim & Aunt Sue</td></tr>
            <tr><td>2</td><td>Mom & Dad Engler, Grandma Engler, Cousin Mike</td></tr>
            <tr><td>3</td><td>Sarah & Josh, Emily & Dave, Katie & Ryan</td></tr>
            <tr><td>4</td><td>College Crew: Alex, Jordan, Taylor, Morgan</td></tr>
            <tr><td>5</td><td>Work Friends: Pat, Brian, Nolan, Monte</td></tr>
            <tr><td>6</td><td>High School Gang: Chris, Sam, Drew, Jamie</td></tr>
        </tbody>
    </table>
</div>

<!-- ==================== WIN OVERLAY ==================== -->
<div id="win-overlay" class="overlay">
    <div class="overlay-box">
        <h2>&#127881; You Won!</h2>
        <p>Congratulations! The seating chart is now unlocked.</p>
        <button class="btn btn-small" id="overlay-replay" onclick="replayGame()">Play Again</button>
        <button class="btn btn-small" onclick="showScreen('home'); closeOverlay();">Home</button>
        <button class="btn btn-small" onclick="showScreen('seating'); closeOverlay();">View Seating Chart</button>
    </div>
</div>

<script>
    // ========== SCREEN NAVIGATION ==========
    let currentGame = null;

    function showScreen(id) {
        document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
        document.getElementById(id).classList.add('active');
        updateSeatingBtn();
        if (id === 'puzzle') { currentGame = 'puzzle'; shufflePuzzle(); }
        if (id === 'memory') { currentGame = 'memory'; initMemory(); }
        if (id === 'scramble') { currentGame = 'scramble'; newWord(); }
    }

    function updateSeatingBtn() {
        const btn = document.getElementById('seating-btn');
        const label = document.getElementById('lock-label');
        if (sessionStorage.getItem('puzzleWon') === 'true') {
            btn.classList.remove('disabled');
            btn.classList.add('unlocked');
            btn.disabled = false;
            btn.innerHTML = '&#128275; View Seating Chart';
        } else {
            btn.classList.add('disabled');
            btn.classList.remove('unlocked');
            btn.disabled = true;
            btn.innerHTML = '&#128274; View Seating Chart<span class="lock-label">Win any game to unlock!</span>';
        }
    }

    function goSeating() {
        if (sessionStorage.getItem('puzzleWon') === 'true') showScreen('seating');
    }

    function triggerWin() {
        sessionStorage.setItem('puzzleWon', 'true');
        document.getElementById('win-overlay').classList.add('active');
    }

    function closeOverlay() {
        document.getElementById('win-overlay').classList.remove('active');
    }

    function replayGame() {
        closeOverlay();
        if (currentGame === 'puzzle') shufflePuzzle();
        if (currentGame === 'memory') initMemory();
        if (currentGame === 'scramble') newWord();
    }

    // ========== SLIDING PUZZLE ==========
    let tiles = [], puzzleMoves = 0;

    function renderPuzzle() {
        const grid = document.getElementById('puzzle-grid');
        grid.innerHTML = '';
        tiles.forEach((val, idx) => {
            const div = document.createElement('div');
            div.classList.add('tile');
            if (val === 0) { div.classList.add('empty'); }
            else {
                div.classList.add('number');
                div.textContent = val;
                div.addEventListener('click', () => clickTile(idx));
            }
            grid.appendChild(div);
        });
    }

    function clickTile(idx) {
        const emptyIdx = tiles.indexOf(0);
        const row = Math.floor(idx / 4), col = idx % 4;
        const eRow = Math.floor(emptyIdx / 4), eCol = emptyIdx % 4;
        const adj = (row === eRow && Math.abs(col - eCol) === 1) || (col === eCol && Math.abs(row - eRow) === 1);
        if (adj) {
            tiles[emptyIdx] = tiles[idx]; tiles[idx] = 0;
            puzzleMoves++;
            document.getElementById('puzzle-moves').textContent = 'Moves: ' + puzzleMoves;
            renderPuzzle();
            if (tiles.slice(0,15).every((v,i) => v === i+1)) triggerWin();
        }
    }

    function shufflePuzzle() {
        tiles = []; for (let i=1;i<=15;i++) tiles.push(i); tiles.push(0);
        for (let i=0;i<200;i++) {
            const ei = tiles.indexOf(0), r = Math.floor(ei/4), c = ei%4, nb=[];
            if(r>0) nb.push(ei-4); if(r<3) nb.push(ei+4);
            if(c>0) nb.push(ei-1); if(c<3) nb.push(ei+1);
            const pick = nb[Math.floor(Math.random()*nb.length)];
            tiles[ei]=tiles[pick]; tiles[pick]=0;
        }
        puzzleMoves = 0;
        document.getElementById('puzzle-moves').textContent = 'Moves: 0';
        renderPuzzle();
    }

    // ========== MEMORY MATCH ==========
    const emojis = ['\uD83D\uDC8D','\uD83D\uDC92','\uD83D\uDC70','\uD83E\uDD35','\uD83C\uDF82','\uD83E\uDD42','\uD83C\uDF38','\uD83D\uDC90'];
    let memCards=[], memFlipped=[], memMatched=0, memMoves=0, memLocked=false;

    function initMemory() {
        const deck = [...emojis, ...emojis];
        for (let i = deck.length-1; i>0; i--) { const j=Math.floor(Math.random()*(i+1)); [deck[i],deck[j]]=[deck[j],deck[i]]; }
        memCards = deck; memFlipped = []; memMatched = 0; memMoves = 0; memLocked = false;
        document.getElementById('memory-moves').textContent = 'Moves: 0';
        renderMemory();
    }

    function renderMemory() {
        const grid = document.getElementById('memory-grid');
        grid.innerHTML = '';
        memCards.forEach((emoji, idx) => {
            const card = document.createElement('div');
            card.classList.add('card');
            card.dataset.idx = idx;
            card.textContent = emoji;
            if (memFlipped.includes(idx)) card.classList.add('flipped');
            if (card.classList.contains('matched')) {}
            card.addEventListener('click', () => flipCard(idx));
            grid.appendChild(card);
        });
        // re-apply matched
        document.querySelectorAll('.card').forEach(c => {
            const i = parseInt(c.dataset.idx);
            if (memFlipped.includes(i) && document.querySelectorAll('.card.matched').length >= 0) {
                // check matched pairs from memFlipped permanent
            }
        });
    }

    let memPermanent = new Set();

    function flipCard(idx) {
        if (memLocked) return;
        if (memPermanent.has(idx)) return;
        if (memFlipped.includes(idx)) return;
        memFlipped.push(idx);
        const cards = document.querySelectorAll('.card');
        cards[idx].classList.add('flipped');

        if (memFlipped.length === 2) {
            memMoves++;
            document.getElementById('memory-moves').textContent = 'Moves: ' + memMoves;
            const [a, b] = memFlipped;
            if (memCards[a] === memCards[b]) {
                memPermanent.add(a); memPermanent.add(b);
                cards[a].classList.add('matched'); cards[b].classList.add('matched');
                memMatched += 2;
                memFlipped = [];
                if (memMatched === memCards.length) setTimeout(triggerWin, 400);
            } else {
                memLocked = true;
                setTimeout(() => {
                    cards[a].classList.remove('flipped');
                    cards[b].classList.remove('flipped');
                    memFlipped = [];
                    memLocked = false;
                }, 800);
            }
        }
    }

    // ========== WORD SCRAMBLE ==========
    const words = ['BOUQUET','WEDDING','FOREVER','DANCING','ROMANCE','FLOWERS','MARRIED','CHERISH','DEVOTED','PROMISE'];
    let currentWord = '';

    function newWord() {
        currentWord = words[Math.floor(Math.random() * words.length)];
        let scrambled = currentWord.split('');
        // keep shuffling until different from original
        do { for(let i=scrambled.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[scrambled[i],scrambled[j]]=[scrambled[j],scrambled[i]];} }
        while (scrambled.join('') === currentWord);
        document.getElementById('scramble-display').textContent = scrambled.join('');
        document.getElementById('scramble-hint').textContent = currentWord.length + ' letters \u2022 wedding related';
        document.getElementById('guess-input').value = '';
        document.getElementById('scramble-feedback').textContent = '';
    }

    function checkGuess() {
        const guess = document.getElementById('guess-input').value.trim().toUpperCase();
        if (guess === currentWord) { triggerWin(); }
        else { document.getElementById('scramble-feedback').textContent = 'Not quite \u2014 try again!'; }
    }

    // Enter key support
    document.addEventListener('keydown', e => {
        if (e.key === 'Enter' && document.getElementById('scramble').classList.contains('active')) checkGuess();
    });

    // ========== INIT ==========
    updateSeatingBtn();
</script>
</body>
</html>'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print('index.html generated successfully!')
