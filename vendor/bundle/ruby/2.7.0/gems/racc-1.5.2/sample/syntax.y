#
#
# Racc syntax checker.  This grammer file generates
# invalid ruby program, you cannot run this parser.

class P
  token A B C

  convert
    A '5'
  end

  prechigh
    left B
  preclow

  options omit_action_call

  start target
rule
  target: A B C
            {
              print 'abc'
            }
        | B C A
        | C B A
            {
              print 'cba'
            }
        | cont
  
  cont  : A c2 B c2 C

  c2    : C C C C C
end

---- inner

    junk code  !!!!

kjaljlajrlaolanbla  /// %%%  (*((( token rule
akiurtlajluealjflaj    @@@@   end end end end __END__
  laieu2o879urkq96ga(Q#*&%Q#
 #&lkji  END

         q395q?///  liutjqlkr7
