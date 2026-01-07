structure Dict =
struct
    type ('k, 'v) dict = ('k * 'v) list
    fun empty : ('k, 'v) dict = []
    fun lookup (cmp, d, k) =
        case d of
            [] => NONE
          | (key, value) :: rest => if cmp(key, k) = EQUAL then SOME value else lookup (cmp, rest, k)
    fun insert (cmp, d, (k, v)) =
        case d of
            [] => [(k, v)]
          | (key, value) :: rest => if cmp(key, k) = EQUAL then (k, v) :: rest else (key, value) :: insert (cmp, rest, (k, v))
end
