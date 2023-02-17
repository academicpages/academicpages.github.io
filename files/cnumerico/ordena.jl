function ordena(v)
    n = size(v,2)  # Determina o tamanho do vetor
    troca = 1
    while troca == 1
        troca = 0
        for k in 1 : n-1
            if v[k] > v[k+1]
                troca = 1; 
                salva = v[k]
                v[k] = v[k+1]
                v[k+1] = salva
            end
        end
    end   
    return(v)
end