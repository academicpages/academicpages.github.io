function newton(xk,ϵ,maxiter)
    iter = 0

    en = NaN
    enm1 = NaN
    enm2 = NaN

    while true
        en = abs(xk - ξ)
        p = (log(en) - log(enm1)) / (log(enm1) - log(enm2))

        #println("$iter   $xk   $(f(xk)) $p  $en")
        @printf("%5d   %20.15e   %20.15e   %20.15e   %20.15e\n",iter,xk,f(xk),p,en)
        if abs(f(xk)) < ϵ
            println("Oba!!! Achei a solução!!!!!")
            return xk
        end
        iter = iter + 1
        if iter > maxiter
            println("Eita! A solução não foi encontrada!!!")
            return nothing
        end
        xk = ϕ(xk)
        enm2 = enm1 
        enm1 = en
    end

end

function ϕ(x)

    return x - f(x) / df(x)

end