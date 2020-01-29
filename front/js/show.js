$(document).ready(function () {
    var current_move = 0;
    var history;
    var piece_types;

    $("#previous-step-button").click(function () {
        $("#game-state").text("Current move: " + current_move);
        current_move = Math.max(current_move-1, 0);
        redraw();
    });
    $("#next-step-button").click(function () {
        $("#game-state").text("Current move: " + current_move);
        current_move = Math.min(current_move+1, history.length-1);
        redraw()
    });

    $.get("/patchwork/front/history.json",
        {},
        function (data) {
            history = data.history;
            piece_tpes = data.piece_types;
            redraw();
        });

    function redraw(){
        removeAll();
        console.log(history);

        loadBoard($("#player1-board")[0], history[current_move].p1board)
        loadBoard($("#player2-board")[0], history[current_move].p2board)
        loadMap($("#map")[0], $("#pieces")[0], history[current_move].map);
    }

    function removeAll() {
        $("#player1-board").empty();
        $("#player2-board").empty();
        $("#pieces").empty();
        $("#map").empty();
    }
    function loadMap(mapDiv, piecesDiv, map) {
        console.log(map);

        for (let i = 0; i < map.length; i++) {
            let clas = 'field-empty';
            if (map.player1_offset === i){
                clas = 'player1';
            }
            if (map.player2_offset === i){
                clas = 'player2';
            }
            $('<div/>', {
                id: mapDiv.id + '-field-' + i,
                class: 'field ' + clas
            }).appendTo(mapDiv);
        }

        let pieces = map.pieces;
        for (let i = 0; i < pieces.length; i++) {
            if (map.pointer_offset === i){
                $('<div/>', {
                    id: piecesDiv.id + '-field-pointer',
                    text: ">",
                    class: 'field pointer'
                }).appendTo(piecesDiv);
            }
            $('<div/>', {
                id: piecesDiv.id + '-field-' + i,
                text: pieces[i].name,
                class: 'field'
            }).appendTo(piecesDiv);
        }
        if (map.pointer_offset === pieces.length){
            $('<div/>', {
                id: piecesDiv.id + '-field-pointer',
                text: ">",
                class: 'field pointer'
            }).appendTo(piecesDiv);
        }
    }

    function loadBoard(div, data){
        let board = data.board;

        for (let i = 0; i < board.length; i++) {
            $('<div/>', {
                id: div.id + '-row-' + i,
                class: 'row'
            }).appendTo(div);

            for (let j = 0; j < board[i].length; j++) {
                let clas = 'field-empty';
                if (board[i][j] === 1){
                    clas = 'field-occupied';
                }
                let field = $('<div/>', {
                    id: div.id + '-field-' + (i * 8 + j),
                    class: 'field ' + clas
                });
                field.appendTo('#' + div.id + '-row-' + i);
            }
        }
    }
})