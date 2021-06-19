module Namae
  describe 'Parser using threads' do
    let(:name_1_str) { "Foo Bar" }
    let(:name_2_str) { "Baz" }
    let(:name_1) { Namae.parse(name_1_str).first }
    let(:name_2) { Namae.parse(name_2_str).first }

    def compare(string, expectation)
      name = Namae.parse(string).first
      given_name_match = expectation.given == name.given
      family_name_match = expectation.family == name.family
      raise unless given_name_match && family_name_match
    end

    it 'has no conflicts' do
      [[name_1_str, name_1], [name_2_str, name_2]].map do |string, expectation|
        Thread.new do
          1000.times do
            compare(string, expectation)
          end
        end
      end.each(&:join)
    end
  end
end
