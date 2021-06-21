module Namae
  describe 'Name' do

    describe '.new' do

      it 'returns an empty name by default' do
        expect(Name.new).to be_empty
      end

      it 'sets all passed-in attributes' do
        expect(Name.new(:given => 'Foo').given).to eq('Foo')
      end

      it 'ignores unknown attributes' do
        expect(Name.new(:foo => 'bar')).to be_empty
      end

    end

    describe '.parse' do
      it 'returns an empty name for an empty string' do
        expect(Name.parse('')).to be_empty
        expect(Name.parse('')).to be_a(Name)
      end

      it 'returns a single name object if there is more than one name' do
        expect(Name.parse('Plato and Sokrates').given).to eq('Plato')
      end
    end

    describe '#values_at' do
      it 'returns an array with the given values' do
        expect(Name.new(:family => 'foo').values_at(:family)).to eq(['foo'])
      end

      it 'returns an array with the given values' do
        expect(Name.new(:family => 'foo').values_at(:family)).to eq(['foo'])
      end
    end

    describe '#initials' do
      it "returns the name's initials" do
        expect(Name.new(:family => 'Poe', :given => 'Edgar A.').initials).to eq('E.A.P.')
      end

      it "returns the name's initials but leaves the family name expanded" do
        expect(Name.new(:family => 'Poe', :given => 'Edgar A.').initials(:expand => true)).to eq('E.A. Poe')
      end
    end

    describe '#normalize_initials' do
      it "adds dots to existing initials" do
        expect(Name.new(:given => 'Edgar A').normalize_initials.given).to eq('Edgar A.')
        expect(Name.new(:given => 'A').normalize_initials.given).to eq('A.')
        expect(Name.new(:given => 'E A').normalize_initials.given).to eq('E.A.')
        expect(Name.new(:given => 'EA').normalize_initials.given).to eq('E.A.')
        expect(Name.new(:given => 'JFK').normalize_initials.given).to eq('J.F.K.')
        expect(Name.new(:given => 'E-A').normalize_initials.given).to eq('E.-A.')
      end
    end

    describe '#merge' do
      it 'merges the attributes in the given hash into the name' do
        expect(Name.new.merge(:family => 'foo').family).to eq('foo')
      end

      it 'merges the attributes in the given name into the name' do
        expect(Name.new.merge(Name.new(:family => 'foo')).family).to eq('foo')
      end

      it 'ignores unknown attributes' do
        expect(Name.new.merge(:foo => 'bar')).to be_empty
      end

      it 'ignores nil values' do
        expect(Name.new(:family => 'foo').merge(:family => nil).family).to eq('foo')
      end
    end

    describe '#inspect' do
      it 'returns the name as a string' do
        expect(Name.new(:given => 'Ichiro').inspect).to eq('#<Name given="Ichiro">')
      end
    end

    describe '#sort_order' do
      it 'returns an empty string by default' do
        expect(Name.new.sort_order).to eq('')
      end

      it 'returns the name in sort order' do
        expect(Name.new(:given => 'Ichiro', :family => 'Suzuki').sort_order).to eq('Suzuki, Ichiro')
      end

      it 'returns only the given if there is no family name' do
        expect(Name.new(:given => 'Ichiro').sort_order).to eq('Ichiro')
      end

      it 'returns only the family if there is no given name' do
        expect(Name.new(:family => 'Suzuki').sort_order).to eq('Suzuki')
      end

      it 'includes the suffix' do
        expect(Name.new(:family => 'Griffey', :suffix => 'Jr.').sort_order).to eq('Griffey, Jr.')
        expect(Name.new(:family => 'Griffey', :given => 'Ken', :suffix => 'Jr.').sort_order).to eq('Griffey, Jr., Ken')
      end
    end

    describe '#display_order' do
      it 'returns an empty string by default' do
        expect(Name.new.display_order).to eq('')
      end

      it 'returns the name in display order' do
        expect(Name.new(:given => 'Ichiro', :family => 'Suzuki').display_order).to eq('Ichiro Suzuki')
      end

      it 'returns only the given if there is no family name' do
        expect(Name.new(:given => 'Ichiro').display_order).to eq('Ichiro')
      end

      it 'returns only the family if there is no given name' do
        expect(Name.new(:family => 'Suzuki').display_order).to eq('Suzuki')
      end

      it 'includes the suffix' do
        expect(Name.new(:family => 'Griffey', :suffix => 'Jr.').display_order).to eq('Griffey Jr.')
        expect(Name.new(:family => 'Griffey', :given => 'Ken', :suffix => 'Jr.').display_order).to eq('Ken Griffey Jr.')
      end
    end

  end
end
