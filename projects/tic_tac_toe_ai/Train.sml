structure Train :> TRAIN =
struct
    open Player

    local
        val r = Random.rand (05052023, 33409756234)
    in
        fun randRange (low : int, hi : int) : int =
            if low = hi then low else Random.randRange(low, hi) r 
    end

    type memory = (string, real) Dict.dict

    val update_rate = 0.3
        
    fun best_next_state (mem : memory, (board, who) : Game.state) : Game.state * real =
    let
        val moves = Game.possible_moves (board, who)

        fun get_score move =
            let
                val next_s = Game.make_move ((board, who), move)
                val s_hash = Game.hash next_s
            in
                case Dict.lookup (String.compare, mem, s_hash) of
                    SOME score => score
                  | NONE => 0.0
            end

        val move_scores = Seq.zip (moves, Seq.map get_score moves)
        val best_move = Seq.nth (randRange(0, Seq.length move_scores - 1), move_scores)
        val best_next_s = Game.make_move ((board, who), best_move)
    in
        (best_next_s, get_score best_move)
    end
end

