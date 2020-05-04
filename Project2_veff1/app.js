var mBoard = document.getElementById("MinesweeperBoard");
var gameboard;
var gamerow;
var gamecol;
var gamemines;
var defaultBoard = {
    minePositions: [[1,4],[3,0],[4,2],[4,5],[4,7],[6,9],[7,7],[8,9],[9,3],[9,9]]
}


function requestBoard() {
    document.getElementById("MinesweeperBoard").innerHTML = '';
    document.getElementById("resultMsg").style="display: none";
    var rows = document.getElementById("rows").value;
    var col = document.getElementById("cols").value;
    var mines = document.getElementById("mines").value;
    if (rows == "") {
        rows = 10;
    }
    if (col == "") {
        col = 10;
    }
    if (mines == "") {
        mines = 10;
    }

    if (rows > 40 || rows <= 0 || col > 40 || col <= 0 || mines <= 0)
    {
        document.getElementById("resultMsg").style="display: block;";
        document.getElementById("resultMsg").className="alert alert-danger";
        document.getElementById("resultMsg").textContent = "Cannot be less than 1 rows and/or columns and no more than 40 rows and/or columns.";
    }
    else if (rows*col<mines)
    {
        document.getElementById("resultMsg").style="display: block;";
        document.getElementById("resultMsg").className="alert alert-danger";
        document.getElementById("resultMsg").textContent = "Cannot be more mines than squares on the board.";
        
    }
    else 
    {
        getBoard(rows, col, mines, function (board) {
            if (board == null) {
                board = defaultBoard;
                board.rows = 10
                board.cols = 10
                board.mines = 10
            }
            generateBoard(board);
        });
    }
}


function getBoard(rows, col, mines, callback) {
    var url = 'https://veff213-minesweeper.herokuapp.com/api/v1/minesweeper';

    axios.post(url, {rows: rows, cols: col, mines: mines})
        .then(function (response){
            callback(response.data.board);
        })
        .catch(function (error) {
            callback(null);
        })
        .then(function () {
            // This code is always executed, independent of whether the request succeeds or fails.   
        });
}

function generateBoard(board) {
    gameboard = board
    gamecol = board.cols
    gamerow = board.rows
    gamemines = board.mines
    for (var i=0; i < board.cols; i++) {
        var col = document.createElement('div');
        col.id = "col"+i
        mBoard.appendChild(col)
        for (var j=0; j < board.rows; j++) {
            var but = document.createElement('button');
            but.classList.add('btn', 'btn-secondary');
            but.id = "but" + i + j;
            but.addEventListener('click', function() {
                clicker(this.id,event);
            })
            but.addEventListener('contextmenu', function(e) {
                e.preventDefault()
                rightclicker(this.id,event);
            })
            col.appendChild(but);
        };
    }
    
    getMines(board);
}

function clicker(butid){
    var but = document.getElementById(butid);
    if (!but.classList.contains("flag")) {
        if (but.classList.contains("sprengja")) {
            var mines = gameboard.minePositions
            for (var i=0; i < gameboard.cols; i++) {
                for (var j=0; j < gameboard.rows; j++) {
                    document.getElementById("but"+i+j).disabled = true;
                }
            }
            for (i=0; i < mines.length;i++) {
                var but = document.getElementById("but"+mines[i][0]+mines[i][1]);
                but.classList.add('bomb');
                but.style = "background-color: red";
            }
            document.getElementById("resultMsg").style="display: block;";
            document.getElementById("resultMsg").className="alert alert-danger";
            document.getElementById("resultMsg").textContent = "GAME OVER";
            }
        else {
            check_neighbours(butid)
            checkVictory();
        }
    }
}

function check_neighbours(butid, old_nei=0) {
    if (old_nei != 0) {
        old_nei = old_nei.substring(3,5)
    }
    var row = parseInt(butid.substring(3,4));
    var col = parseInt(butid.substring(4));
    var neighbors = [];
    var finalneighbors = [];
	neighbors.push( (row - 1) + "," + (col - 1) );
	neighbors.push( (row - 1) + "," + col );
	neighbors.push( (row - 1) + "," + (col + 1) );
	neighbors.push( row + "," + (col - 1) );
	neighbors.push( row + "," + (col + 1) );
	neighbors.push( (row + 1) + "," + (col - 1) );
	neighbors.push( (row + 1) + "," + col );
	neighbors.push( (row + 1) + "," + (col + 1) );
    for( var i = 0; i < neighbors.length; i++)
	{ 
        var a = neighbors[i].split(",")[0];
        var b = neighbors[i].split(",")[1];
        if ( a >= gamerow || a < 0 || b >= gamecol || b < 0 || a == old_nei[0] && b == old_nei[1]) 
        {      /*pass*/
        } 
        else {
            if (document.getElementById("but"+a+b).style.backgroundColor == "lightgrey") {
            }
            else {
                finalneighbors.push(neighbors[i].replace(",", ""));
            }
        }
    }
    return getNeighbours(finalneighbors,butid)
}

function getNeighbours(neighbors,butid) {
    var but = document.getElementById(butid);
    but.style.backgroundColor = "lightgrey";
    var bombcount = 0;
    for (i=0; i < neighbors.length; i++)
        if (document.getElementById("but"+neighbors[i]).classList.contains("sprengja"))
            {
                bombcount++;
            }
    but.innerHTML = bombcount;
    but.style.fontWeight = '900';
    if (bombcount == 0) {
        but.innerHTML = '';
        var i;
        if (neighbors.length == 0) {
        }
        else {
            for (i=0; i < neighbors.length; i++) {
                var butt = ("but"+neighbors[i]);
                check_neighbours(butt,butid);
        }
    }
    }
    else if (bombcount == 1) {
        but.style.color = "blue"
        return
    }
    else if(bombcount==2) {
        but.style.color = "green";
        return
    }
    else if(bombcount>=3) {
        but.style.color = "red";
        return
    }
}


function rightclicker(butid){
    var but = document.getElementById(butid);
    if (but.style.backgroundColor != "lightgrey") {
        but.classList.toggle("flag");
        checkVictory();
    }

}

function checkVictory() {
    var mines = gameboard.minePositions 
    var counter = 0;
    var victorycounter = 0;
    var victory = false;
    for (i=0; i < gamemines; i++) {
        var but = document.getElementById("but"+mines[i][0]+mines[i][1]);
        if (but.classList.contains("flag")) {
            counter++;
        }
    }
    if (counter == gamemines) {
        for (var i=0; i < gameboard.cols; i++) {
            for (var j=0; j < gameboard.rows; j++) {
                if (document.getElementById("but"+i+j).classList.contains("sprengja")) {
                }
                else {
                    if (document.getElementById("but"+i+j).style.backgroundColor == "lightgrey") {
                        victorycounter++;
                    }
                }

            }
        }
        if ((gamerow*gamecol)-gamemines == victorycounter) {
            for (var i=0; i < gameboard.cols; i++) {
                for (var j=0; j < gameboard.rows; j++) {
                    document.getElementById("but"+i+j).disabled = true;
                    document.getElementById("resultMsg").style="display: block;";
                    document.getElementById("resultMsg").className="alert alert-success";
                    document.getElementById("resultMsg").textContent = "VICTORY! YOU WIN";
                }
            }
        }   
    }
}
function getMines(board) {
    var mines = board.minePositions
    for (i=0; i < mines.length;i++) {
        var but = document.getElementById("but"+mines[i][0]+mines[i][1]);
        but.className += " sprengja";
    }
}
