function primo(n)
    K = trunc(sqrt(n))
    j = 2
    while j <= K
        if mod(n,j) == 0
            println("$n não é primo! Pois $j divide $n !!")
            return nothing
        else
            j = j + 1
        end
    end
    println("$n é primo!")
end




