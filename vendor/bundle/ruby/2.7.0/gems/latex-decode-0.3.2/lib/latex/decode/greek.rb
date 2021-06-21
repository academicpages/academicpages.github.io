# -*- coding: utf-8 -*-

module LaTeX
  module Decode

    class Greek < Decoder
      @map = Hash[*%w{
        alpha      α
        beta       β
        gamma      γ
        delta      δ
        epsilon    ε
        zeta       ζ
        eta        η
        theta      θ
        iota       ι
        kappa      κ
        lambda     λ
        mu         μ
        nu         ν
        xi         ξ
        rho        ρ
        sigma      σ
        tau        τ
        upsilon    υ
        phi        φ
        chi        χ
        psi        ψ
        omega      ω
        Alpha      Α
        Beta       Β
        Gamma      Γ
        Delta      Δ
        Epsilon    Ε
        Zeta       Ζ
        Eta        Η
        Theta      Θ
        Iota       Ι
        Kappa      Κ
        Lambda     Λ
        Mu         Μ
        Nu         Ν
        Xi         Ξ
        Rho        Ρ
        Sigma      Σ
        Tau        Τ
        Upsilon    Υ
        Phi        Φ
        Chi        Χ
        Psi        Ψ
        Omega      Ω
      }].freeze

      @patterns = [
        /\\(#{ map.keys.map { |k| Regexp.escape(k) }.join('|') })(?:\{\}|\s+|\b)/ou
      ].freeze

    end

  end
end
