html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sliding Puzzle</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            background: #1a1a2e;
            font-family: Arial, sans-serif;
            color: #fff;
        }
        h1 { margin-bottom: 10px; font-size: 28px; }
        #moves { margin-bottom: 15px; font-size: 18px; color: #aaa; }
        #grid {
            display: grid;
            grid-template-columns: repeat(4, 80px);
            grid-template-rows: repeat(4, 80px);
            gap: 4px;
            background: #16213e;
            padding: 8px;
            border-radius: 10px;
        }
        .tile {
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
            font-weight: bold;
            border-radius: 6px;
            cursor: pointer;
            transition: all 0.15s ease;
        }
        .tile.number {
            background: #0f3460;
            color: #e94560;
        }
        .tile.number:hover { background: #1a4a7a; }
        .tile.empty {
            background: transparent;
            cursor: default;
        }
        #shuffle {
            margin-top: 20px;
            padding: 12px 30px;
            font-size: 16px;
            background: #e94560;
            color: #fff;
            border: none;
            border-radius: 6px;
            cursor: pointer;
        }
        #shuffle:hover { background: #c73652; }
        #win-msg {
            margin-top: 10px;
            font-size: 20px;
            color: #4ecca3;
            min-height: 28px;
        }
    </style>
</head>
<body>
    <h1>Sliding Puzzle</h1>
    <div id="moves">Moves: 0</div>
    <div id="grid"></div>
    <button id="shuffle">Shuffle</button>
    <div id="win-msg"></div>

    <script>
        let tiles = [];
        let moves = 0;

        function init() {
            // Create solved state: 1-15, 0 = empty
            tiles = [];
            for (let i = 1; i <= 15; i++) tiles.push(i);
            tiles.push(0);
            moves = 0;
            updateMoves();
            document.getElementById("win-msg").textContent = "";
            render();
        }

        function render() {
            const grid = document.getElementById("grid");
            grid.innerHTML = "";
            tiles.forEach((val, idx) => {
                const div = document.createElement("div");
                div.classList.add("tile");
                if (val === 0) {
                    div.classList.add("empty");
                } else {
                    div.classList.add("number");
                    div.textContent = val;
                    div.addEventListener("click", () => handleClick(idx));
                }
                grid.appendChild(div);
            });
        }

        function handleClick(idx) {
            const emptyIdx = tiles.indexOf(0);
            const row = Math.floor(idx / 4);
            const col = idx % 4;
            const emptyRow = Math.floor(emptyIdx / 4);
            const emptyCol = emptyIdx % 4;

            // Check if adjacent (up, down, left, right)
            const adjacent =
                (row === emptyRow && Math.abs(col - emptyCol) === 1) ||
                (col === emptyCol && Math.abs(row - emptyRow) === 1);

            if (adjacent) {
                tiles[emptyIdx] = tiles[idx];
                tiles[idx] = 0;
                moves++;
                updateMoves();
                render();
                checkWin();
            }
        }

        function updateMoves() {
            document.getElementById("moves").textContent = "Moves: " + moves;
        }

        function checkWin() {
            for (let i = 0; i < 15; i++) {
                if (tiles[i] !== i + 1) return;
            }
            document.getElementById("win-msg").textContent = "You win!";
        }

        function shuffle() {
            // Perform 200 random valid moves from solved state
            init();
            for (let i = 0; i < 200; i++) {
                const emptyIdx = tiles.indexOf(0);
                const row = Math.floor(emptyIdx / 4);
                const col = emptyIdx % 4;
                const neighbors = [];
                if (row > 0) neighbors.push(emptyIdx - 4);
                if (row < 3) neighbors.push(emptyIdx + 4);
                if (col > 0) neighbors.push(emptyIdx - 1);
                if (col < 3) neighbors.push(emptyIdx + 1);
                const pick = neighbors[Math.floor(Math.random() * neighbors.length)];
                tiles[emptyIdx] = tiles[pick];
                tiles[pick] = 0;
            }
            moves = 0;
            updateMoves();
            document.getElementById("win-msg").textContent = "";
            render();
        }

        document.getElementById("shuffle").addEventListener("click", shuffle);
        shuffle();
    </script>
</body>
</html>"""

with open("index.html", "w") as f:
    f.write(html_content)

print("index.html generated successfully!")
