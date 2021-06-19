# -*- coding: utf-8 -*- #
# frozen_string_literal: true

module Rouge
  module Lexers
    class Coq < RegexLexer
      title "Coq"
      desc 'Coq (coq.inria.fr)'
      tag 'coq'
      mimetypes 'text/x-coq'

      def self.gallina
        @gallina ||= Set.new %w(
          as fun if in let match then else return end Type Set Prop
          forall
        )
      end

      def self.coq
        @coq ||= Set.new %w(
          Definition Theorem Lemma Remark Example Fixpoint CoFixpoint
          Record Inductive CoInductive Corollary Goal Proof
          Ltac Require Import Export Module Section End Variable
          Context Polymorphic Monomorphic Universe Universes
          Variables Class Instance Global Local Include
          Printing Notation Infix Arguments Hint Rewrite Immediate
          Qed Defined Opaque Transparent Existing
          Compute Eval Print SearchAbout Search About Check
        )
      end

      def self.ltac
        @ltac ||= Set.new %w(
          apply eapply auto eauto rewrite setoid_rewrite
          with in as at destruct split inversion injection
          intro intros unfold fold cbv cbn lazy subst
          clear symmetry transitivity etransitivity erewrite
          edestruct constructor econstructor eexists exists
          f_equal refine instantiate revert simpl
          specialize generalize dependent red induction
          beta iota zeta delta exfalso autorewrite setoid_rewrite
          compute vm_compute native_compute
        )
      end

      def self.tacticals
        @tacticals ||= Set.new %w(
          repeat first try
        )
      end

      def self.terminators
        @terminators ||= Set.new %w(
          omega solve congruence reflexivity exact
          assumption eassumption
        )
      end

      def self.keyopts
        @keyopts ||= Set.new %w(
          := => -> /\\ \\/ _ ; :> : ⇒ → ↔ ⇔ ≔ ≡ ∀ ∃ ∧ ∨ ¬ ⊤ ⊥ ⊢ ⊨ ∈
        )
      end

      def self.end_sentence
        @end_sentence ||= Punctuation::Indicator
      end

      def self.classify(x)
        if self.coq.include? x
          return Keyword
        elsif self.gallina.include? x
          return Keyword::Reserved
        elsif self.ltac.include? x
          return Keyword::Pseudo
        elsif self.terminators.include? x
          return Name::Exception
        elsif self.tacticals.include? x
          return Keyword::Pseudo
        else
          return Name::Constant
        end
      end

      operator = %r([\[\];,{}_()!$%&*+./:<=>?@^|~#-]+)
      id = /(?:[a-z][\w']*)|(?:[_a-z][\w']+)/i
      dot_id = /\.((?:[a-z][\w']*)|(?:[_a-z][\w']+))/i
      dot_space = /\.(\s+)/
      module_type = /Module(\s+)Type(\s+)/
      set_options = /(Set|Unset)(\s+)(Universe|Printing|Implicit|Strict)(\s+)(Polymorphism|All|Notations|Arguments|Universes|Implicit)(\s*)\./m

      state :root do
        rule %r/[(][*](?![)])/, Comment, :comment
        rule %r/\s+/m, Text::Whitespace
        rule module_type do |m|
          token Keyword , 'Module'
          token Text::Whitespace , m[1]
          token Keyword , 'Type'
          token Text::Whitespace , m[2]
        end
        rule set_options do |m|
          token Keyword , m[1]
          i = 2
          while m[i] != ''
            token Text::Whitespace , m[i]
            token Keyword , m[i+1]
            i += 2
          end
          token self.class.end_sentence , '.'
        end
        rule id do |m|
          @name = m[0]
          @continue = false
          push :continue_id
        end
        rule %r(/\\), Operator
        rule %r/\\\//, Operator

        rule %r/-?\d[\d_]*(.[\d_]*)?(e[+-]?\d[\d_]*)/i, Num::Float
        rule %r/\d[\d_]*/, Num::Integer

        rule %r/'(?:(\\[\\"'ntbr ])|(\\[0-9]{3})|(\\x\h{2}))'/, Str::Char
        rule %r/'/, Keyword
        rule %r/"/, Str::Double, :string
        rule %r/[~?]#{id}/, Name::Variable

        rule %r/./ do |m|
          match = m[0]
          if self.class.keyopts.include? match
            token Punctuation
          elsif match =~ operator
            token Operator
          else
            token Error
          end
        end
      end

      state :comment do
        rule %r/[^(*)]+/, Comment
        rule(/[(][*]/) { token Comment; push }
        rule %r/[*][)]/, Comment, :pop!
        rule %r/[(*)]/, Comment
      end

      state :string do
        rule %r/(?:\\")+|[^"]/, Str::Double
        mixin :escape_sequence
        rule %r/\\\n/, Str::Double
        rule %r/"/, Str::Double, :pop!
      end

      state :escape_sequence do
        rule %r/\\[\\"'ntbr]/, Str::Escape
      end

      state :continue_id do
        # the stream starts with an id (stored in @name) and continues here
        rule dot_id do |m|
          token Name::Namespace , @name
          token Punctuation , '.'
          @continue = true
          @name = m[1]
        end
        rule dot_space do |m|
          if @continue
            token Name::Constant , @name
          else
            token self.class.classify(@name) , @name
          end
          token self.class.end_sentence , '.'
          token Text::Whitespace , m[1]
          @name = false
          @continue = false
          pop!
        end
        rule %r// do
          if @continue
            token Name::Constant , @name
          else
            token self.class.classify(@name) , @name
          end
          @name = false
          @continue = false
          pop!
        end
      end

    end
  end
end
