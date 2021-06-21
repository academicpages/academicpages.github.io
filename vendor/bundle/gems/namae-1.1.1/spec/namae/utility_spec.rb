describe 'Namae' do

  describe '.parse' do
    it 'returns an empty list by default' do
      expect(Namae.parse('')).to be_empty
    end
  end

  describe '.parse!' do
    it 'returns an empty list by default' do
      expect(Namae.parse!('')).to be_empty
    end
  end
    
  describe '.options' do
    it 'returns the parse options' do
      expect(Namae.options).to equal(Namae::Parser.instance.options)
    end
  end

end