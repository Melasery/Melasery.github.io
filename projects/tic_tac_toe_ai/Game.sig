signature GAME =
sig
    type board
    val show_board : board -> string
    type state = board * Player.player 
    val start : state
    val hash : state -> string
    val check_status : state -> Player.status
    type move
    val parse_move : state * string -> move option
    val show_move : move -> string
    val possible_moves : state -> move Seq.seq
    val make_move : state * move -> state
end
