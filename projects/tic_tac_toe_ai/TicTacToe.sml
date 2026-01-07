structure TicTacToe :> GAME =
struct
    open Player

    datatype cell = X | O | EMPTY
    type board = cell Seq.seq Seq.seq
    type move = int * int
    type state = board * player

    val N = 3  (* Board size: 3x3 *)

    (* Create an empty board *)
    fun empty_board () =
        let val empty_row = Seq.repeat (N, EMPTY)
        in Seq.repeat (N, empty_row)
        end

    val start = (empty_board (), Player.X)

    (* Convert a cell to a string representation *)
    fun show_cell c =
        case c of
            X => "X"
          | O => "O"
          | EMPTY => "."

    fun show_board b =
        let
            fun show_row row i =
                if i < N then show_cell (Seq.nth(i, row)) ^ " " ^ show_row row (i+1)
                else ""
            fun show_board_rows i =
                if i < N then show_row (Seq.nth(i, b)) 0 ^ "\n" ^ show_board_rows (i+1)
                else ""
        in show_board_rows 0
        end

    fun hash ((b, p) : state) = show_board b ^ player_to_string p

    (* Win condition checks (rows, columns, diagonals) *)
    fun check_status ((b, _) : state) : status =
        let
            fun has_empty_cells i =
                if i < N then
                    let
                        val row = Seq.nth(i, b)
                        fun row_has_empty j =
                            if j < N then Seq.nth(j, row) = EMPTY orelse row_has_empty (j + 1)
                            else false
                    in row_has_empty 0 orelse has_empty_cells (i + 1)
                    end
                else false
        in
            case check_rows 0 of
                SOME Player.X => Won Player.X
              | SOME Player.O => Won Player.O
              | NONE => if has_empty_cells 0 then Playing else Draw
        end

    (* Generate possible moves *)
    fun possible_moves ((b, _) : state) =
        let
            fun gather_moves i row =
                let
                    fun find_empty j =
                        if j < N then
                           if Seq.nth(j, row) = EMPTY then Seq.cons ((i, j), find_empty (j + 1))
                            else find_empty (j + 1)
                        else
                            Seq.empty ()
                in find_empty 0
                end
            fun gather_all_moves i =
                if i < N then
                    Seq.append (gather_moves i (Seq.nth(i, b)), gather_all_moves (i + 1))
                else
                    Seq.empty ()
        in gather_all_moves 0
        end

    fun make_move (((b, p) : state), (i, j)) =
        let
            fun update_row row =
                Seq.tabulate (fn l => if l = j then p else Seq.nth(l, row), N)
            val new_row = update_row (Seq.nth(i, b))
            val new_board = Seq.tabulate (fn k => if k = i then new_row else Seq.nth(k, b), N)
        in
            (new_board, next p)
        end
end
