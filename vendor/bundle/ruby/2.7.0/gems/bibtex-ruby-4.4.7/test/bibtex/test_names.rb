# coding: utf-8

require 'helper'

module BibTeX
  class NamesTest < Minitest::Spec

    before do
      @poe = Name.new(:first => 'Edgar Allen', :last => 'Poe')
    end

    describe 'string behaviour' do
      before do
        @name = Name.new(:first => 'Charles Louis Xavier Joseph', :prefix => 'de la', :last => 'Vallee Poussin', :suffix => 'Jr.')
      end
      it 'should implement upcase!' do
        assert_equal 'DE LA VALLEE POUSSIN, JR., CHARLES LOUIS XAVIER JOSEPH', @name.upcase!.to_s
      end
      it 'should implement downcase!' do
        assert_equal 'de la vallee poussin, jr., charles louis xavier joseph', @name.downcase!.to_s
      end
      it 'should implement gsub!' do
        assert_equal 'dX la VallXX PoussXn, Jr., CharlXs LouXs XavXXr JosXph', @name.gsub!(/[ei]/, 'X').to_s
      end
    end

    describe '#display_order' do
      it 'returns the name as "first last"' do
        @poe.display_order.must_be :==, 'Edgar Allen Poe'
      end

      it 'accepts the :initials option' do
        @poe.display_order(:initials => true).must_be :==, 'E.A. Poe'
      end
    end

    describe '#sort_order' do
      it 'returns the name as "last, first"' do
        @poe.sort_order.must_be :==, 'Poe, Edgar Allen'
      end

      it 'accepts the :initials option' do
        @poe.sort_order(:initials => true).must_be :==, 'Poe, E.A.'
      end
    end

    describe '#initials?' do
      it 'returns true if the name contains a solely initials as a first name' do
        @poe.initials?.must_equal false

        @poe.first = 'Edgar A.'
        @poe.initials?.must_equal false

        @poe.first = 'E.A.'
        @poe.initials?.must_equal true

        @poe.first = ''
        @poe.initials?.must_equal false

        @poe.first = nil
        @poe.initials?.must_equal false
      end
    end

    describe '#rename_if' do
      it 'renames the name to the given attributes if no condition is given' do
        @poe.rename_if({ :first => 'E.A.' }).first.must_equal 'E.A.'
      end

      it 'renames the name to the given attributes if all conditions match' do
        @poe.rename_if({ :first => 'E.A.' }, { :last => @poe.last }).first.must_equal 'E.A.'
        @poe.rename_if({ :first => 'E.A.' }, { :last => @poe.last, :first => @poe.first }).first.must_equal 'E.A.'
      end

      it 'renames the name to the given attributes if the block returns true' do
        @poe.rename_if({ :first => 'E.A.' }) {|n| true}.first.must_equal 'E.A.'
      end

      it 'does not rename the name to the given attributes if at least one condition does not match' do
        @poe.rename_if({ :first => 'E.A.' }, { :last => 'foo' }).first.wont_equal 'E.A.'
        @poe.rename_if({ :first => 'E.A.' }, { :last => 'foo', :first => @poe.first }).first.wont_equal 'E.A.'
        @poe.rename_if({ :first => 'E.A.' }, { :last => @poe.last, :first => 'foo' }).first.wont_equal 'E.A.'
      end

      it 'does not rename the name to the given attributes if the block returns false' do
        @poe.rename_if({ :first => 'E.A.' }) {|n| false}.first.wont_equal 'E.A.'
      end
    end

    describe '#merge!' do
      it 'does not merge duplicates' do
        n1 = Names.new(@poe)
        n2 = Names.new(@poe)
        assert_equal @poe.to_s, n1.merge!(n2).to_s
      end

      it 'merges different names' do
        n1 = Names.new(@poe)
        n2 = Names.new(Name.new(:last => 'Plato'))
        assert_equal "#{@poe.to_s} and Plato", n1.merge!(n2).to_s
      end
    end

    describe '#normalize_initials' do
      it 'returns normalized initials of existing initials only' do
        Name.new(:first => 'Edgar A.', :last => 'Poe').normalize_initials.must_equal 'Edgar A.'
        Name.new(:first => 'E.A.', :last => 'Poe').normalize_initials.must_equal 'E.A.'
        Name.new(:first => 'E. A.', :last => 'Poe').normalize_initials.must_equal 'E.A.'
        Name.new(:first => 'E. A', :last => 'Poe').normalize_initials.must_equal 'E.A.'
        Name.new(:first => 'E A', :last => 'Poe').normalize_initials.must_equal 'E.A.'
        Name.new(:first => 'Edgar A P', :last => 'Poe').normalize_initials.must_equal 'Edgar A.P.'
      end
    end

    describe '#extend_initials' do
      it 'extends the first name if the last name and initials match' do
        Name.new(:first => 'E.A.', :last => 'Poe').extend_initials('Edgar Allen', 'Poe').first.must_equal 'Edgar Allen'
        Name.new(:first => 'Edgar A.', :last => 'Poe').extend_initials('Edgar Allen', 'Poe').first.must_equal 'Edgar Allen'
        Name.new(:first => 'E. A.', :last => 'Poe').extend_initials('Edgar Allen', 'Poe').first.must_equal 'Edgar Allen'
        Name.new(:first => 'E. A', :last => 'Poe').extend_initials('Edgar Allen', 'Poe').first.must_equal 'Edgar Allen'
        Name.new(:first => 'E A', :last => 'Poe').extend_initials('Edgar Allen', 'Poe').first.must_equal 'Edgar Allen'
        Name.new(:first => 'E. Allen', :last => 'Poe').extend_initials('Edgar Allen', 'Poe').first.must_equal 'Edgar Allen'
        Name.new(:first => 'E.A.', :last => 'Poe').extend_initials('Edgar A.', 'Poe').first.must_equal 'Edgar A.'

        Name.new(:first => 'Edgar-A.', :last => 'Poe').extend_initials('Edgar-Allen', 'Poe').first.must_equal 'Edgar-Allen'
        Name.new(:first => 'E.-Allen', :last => 'Poe').extend_initials('Edgar-Allen', 'Poe').first.must_equal 'Edgar-Allen'
        Name.new(:first => 'E.-A.', :last => 'Poe').extend_initials('Edgar-Allen', 'Poe').first.must_equal 'Edgar-Allen'
        Name.new(:first => 'E.-A', :last => 'Poe').extend_initials('Edgar-Allen', 'Poe').first.must_equal 'Edgar-Allen'
        Name.new(:first => 'E-A', :last => 'Poe').extend_initials('Edgar-Allen', 'Poe').first.must_equal 'Edgar-Allen'
      end

      it 'extends the first name if the last name and initials name match with extra middle names' do
        Name.new(:first => 'E.', :last => 'Poe').extend_initials('Edgar Allen', 'Poe').first.must_equal 'Edgar Allen'
        Name.new(:first => 'E', :last => 'Poe').extend_initials('Edgar Allen', 'Poe').first.must_equal 'Edgar Allen'
        Name.new(:first => 'Edgar', :last => 'Poe').extend_initials('Edgar Allen', 'Poe').first.must_equal 'Edgar Allen'

        Name.new(:first => 'E.A.', :last => 'Poe').extend_initials('Edgar', 'Poe').first.must_equal 'E.A.'
        Name.new(:first => 'A.', :last => 'Poe').extend_initials('Edgar', 'Poe').first.must_equal 'A.'
      end

      it 'does not extend the first name if the last name or initials do not match' do
        Name.new(:first => 'E.A.', :last => 'Poe').extend_initials('Edgar Allen', 'Poser').first.wont_equal 'Edgar Allen'
        Name.new(:first => 'E.A.', :last => 'Poe').extend_initials('Edgar Ellen', 'Poe').first.wont_equal 'Edgar Ellen'
        Name.new(:first => 'E.R.', :last => 'Poe').extend_initials('Edgar Allen', 'Poe').first.wont_equal 'Edgar Allen'
      end
    end

		describe "conversions" do
      class UpcaseAll < BibTeX::Filter
        def apply (value)
          value.upcase
        end
      end

      describe "#convert" do
        it "converts the value when given a filter instance" do
					Names.parse('Poe and Hawthorne').convert(UpcaseAll.instance).to_s.must_be :==, 'POE and HAWTHORNE'
        end

				it "converts LaTeX umlauts" do
					Names.parse("S{\\o}ren Kirkegaard and Emmanuel L\\'evinas").convert(:latex).to_s.must_be :==, 'Kirkegaard, Søren and Lévinas, Emmanuel'
				end
			end
		end

  end

end
