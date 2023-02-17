function par(n)
    resto = mod(n,2)
    if resto == 0
        println("O numero $n é par")
    else
        println("O numero $n é ímpar")
    end
end