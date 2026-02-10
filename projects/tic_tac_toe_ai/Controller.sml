structure Controller =
struct
    open Player 
    
    val mem = Train.train(100000, Dict.empty, Game.start)

    fun controller (s : Game.state) : unit =
    let
      fun handle_input (s : Game.state) =
        let
          val input = TextIO.inputLine TextIO.stdIn
        in
          case input of
              SOME line =>
                (case Game.parse_move (s, line) of
                   SOME move => Game.make_move (s, move)
                 | NONE => (print "Invalid move. Try again.\n"; handle_input s))
        end

      fun game_loop (s : Game.state) =
        let
          val (board, player) = s
          val status = Game.check_status s
        in
          case status of
              Player.Won p => print (Player.player_to_string p ^ " wins\n")
            | Player.Draw => print "It's a draw!\n"
            | Player.Playing =>
                case player of
                    Player.X => (print "Player X's turn\n"; game_loop (handle_input s))
                  | Player.O => (print "Player O's move\n"; game_loop (Train.best_next_state (mem, s)))
        end
    in
      game_loop s
    end

    fun go() = controller(Game.start)
end

