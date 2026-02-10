structure Player =
struct
    datatype player = X | O

    fun player_to_string (p : player) : string =
        case p of
            X => "X"
          | O => "O"

    fun next (p : player) : player =
        case p of
            X => O
          | O => X

    datatype status = Playing | Won of player | Draw 
end
