module Namae
  describe 'Parser' do
    describe '.instance' do
      let(:parser) { Parser.instance }

      it 'returns the parser' do
        expect(parser).to be_a(Parser)
      end

      describe '#next_token' do
				before(:each) do
					Parser.instance.reset
				end

        describe 'when the input is empty' do
          it 'returns nil' do
            expect(parser.send(:next_token)).to be_nil
          end
        end

        describe 'when the next input is " and "' do
          before { parser.send(:input).string = ' and ' }
          it 'returns an AND token' do
            expect(parser.send(:next_token)).to eq([:AND, :AND])
          end
        end

        describe 'when the next input is " & "' do
          before { parser.send(:input).string = ' & ' }
          it 'returns an AND token' do
            expect(parser.send(:next_token)).to eq([:AND, :AND])
          end
        end

        describe 'when the next input is " , "' do
          before { parser.send(:input).string = ' , ' }
          it 'returns a COMMA token' do
            expect(parser.send(:next_token)).to eq([:COMMA, :COMMA])
          end
        end

        describe 'when the next input is ", "' do
          before { parser.send(:input).string = ', ' }
          it 'returns a COMMA token' do
            expect(parser.send(:next_token)).to eq([:COMMA, :COMMA])
          end
        end

        describe 'when the next input is "; "' do
          before { parser.send(:input).string = '; ' }
          it 'returns an AND token' do
            expect(parser.send(:next_token)).to eq([:AND, :AND])
          end
        end

        describe 'when the next input is "foo;"' do
          before { parser.send(:input).string = 'foo;' }
          it 'returns an LWORD token "foo"' do
            expect(parser.send(:next_token)).to eq([:LWORD, 'foo'])
          end
        end

        describe 'when the next input is " \'foo bar\' "' do
          before { parser.send(:input).string = " 'foo bar' " }
          it 'returns a NICK token' do
            expect(parser.send(:next_token)).to eq([:NICK, 'foo bar'])
          end
        end

        %w{Mr. Mr Mrs. Ms Herr Frau Miss}.each do |appellation|
          describe "the next token is #{appellation.inspect}" do
            before { parser.reset.send(:input).string = appellation }
            it 'returns an APPELLATION token' do
              expect(parser.send(:next_token)).to eq([:APPELLATION, appellation])
            end
          end
        end

        %w{Jr. Jr Sr. Sr II II. VII IX}.each do |suffix|
          describe "the next token is #{suffix.inspect}" do
            before { parser.send(:input).string = suffix }
            it 'returns an SUFFIX token' do
              expect(parser.send(:next_token)).to eq([:SUFFIX, suffix])
            end

            it 'the input matches the suffix pattern' do
              expect(parser.suffix).to match(suffix)
            end
          end
        end

        %w{Ph.D. PhD PHD Dr. Dr Prof.}.each do |title|
          describe "the next token is #{title.inspect}" do
            before { parser.send(:input).string = title }
            it 'returns a TITLE token' do
              expect(parser.send(:next_token)).to eq([:TITLE, title])
            end

            it 'the input matches the suffix pattern' do
              expect(parser.title).to match(title)
            end
          end
        end

        %w{Gen. Adm Col. Maj Capt. Cmdr. Lt. Sgt. Cpl Pvt.}.each do |title|
          describe "the next token is #{title.inspect}" do
            before { parser.send(:input).string = title }
            it 'returns a TITLE token' do
              expect(parser.send(:next_token)).to eq([:TITLE, title])
            end

            it 'the input matches the suffix pattern' do
              expect(parser.title).to match(title)
            end
          end
        end

        %w{Pastor Pr. Reverend Rev. Elder Deacon Deaconess Father Fr. Vicar Rabbi Cantor}.each do |title|
          describe "the next token is #{title.inspect}" do
            before { parser.send(:input).string = title }
            it 'returns a TITLE token' do
              expect(parser.send(:next_token)).to eq([:TITLE, title])
            end

            it 'the input matches the suffix pattern' do
              expect(parser.title).to match(title)
            end
          end
        end
      end

      describe '#parse!' do
        it 'returns an empty list by default' do
          expect(parser.parse!('')).to be_empty
        end

        it 'returns a list of names' do
          expect(parser.parse!('foo')[0]).to be_a(Name)
        end

        describe 'when parsing a single name' do

          it 'treats "Ichiro" as a given name' do
            expect(parser.parse!('Ichiro')[0].given).to eq('Ichiro')
          end

          it 'treats "Lord Byron" as a title and family name' do
            expect(parser.parse!('Lord Byron')[0].values_at(:family, :title)).to eq(['Byron', 'Lord'])
          end

          it 'parses given and family part name in "Ichiro Suzuki"' do
            expect(parser.parse!('Ichiro Suzuki')[0].values_at(:given, :family)).to eq(%w{Ichiro Suzuki})
          end

          it 'parses given, nick and family part name in "Yukihiro \'Matz\' Matsumoto"' do
            expect(parser.parse!("Yukihiro 'Matz' Matsumoto")[0].values_at(:given, :family, :nick)).to eq(%w{Yukihiro Matsumoto Matz})
          end

          it 'parses given, nick and family part name in \'Yukihiro "Matz" Matsumoto\'' do
            expect(parser.parse!('Yukihiro "Matz" Matsumoto')[0].values_at(:given, :family, :nick)).to eq(%w{Yukihiro Matsumoto Matz})
          end

          it 'parses appellation and nick in \'Mr. Yukihiro "Matz" Matsumoto\'' do
            expect(parser.parse!('Mr. Yukihiro "Matz" Matsumoto')[0].values_at(:appellation, :nick)).to eq(%w{Mr. Matz})
          end

          it 'parses suffix and nick in \'Yukihiro "Matz" Matsumoto Jr.\'' do
            expect(parser.parse!('Yukihiro "Matz" Matsumoto Jr.')[0].values_at(:suffix, :nick)).to eq(%w{Jr. Matz})
          end

          it 'parses given and family name in "Poe, Edgar A."' do
            expect(parser.parse!('Poe, Edgar A.')[0].values_at(:given, :family)).to eq(['Edgar A.', 'Poe'])
          end

          %w{Mr. Mr Mrs. Ms Herr Frau Miss}.each do |appellation|
            it "recognizes #{appellation.inspect} as an appellation" do
              expect(parser.parse!([appellation, 'Edgar A. Poe'].join(' '))[0].appellation).to eq(appellation)
            end
          end

          it 'parses common Jr. as a suffix in sort order' do
            expect(parser.parse!('Griffey, Jr., Ken')[0].values_at(:given, :family, :suffix)).to eq(['Ken', 'Griffey', 'Jr.'])
            expect(parser.parse!('Griffey, Ken, Jr.')[0].values_at(:given, :family, :suffix)).to eq(['Ken', 'Griffey', 'Jr.'])
          end

          it 'parses common Jr. as a suffix in display order' do
            expect(parser.parse!('Ken Griffey Jr.')[0].values_at(:given, :family, :suffix)).to eq(['Ken', 'Griffey', 'Jr.'])
          end

          it 'parses Ph.D. title suffix in display order' do
            expect(parser.parse!('Bernado Franecki Ph.D.')[0].values_at(:given, :family, :title)).to eq(['Bernado', 'Franecki', 'Ph.D.'])
            #expect(parser.parse!('Bernado Franecki, Ph.D.')[0].values_at(:given, :family, :title)).to eq(['Bernado', 'Franecki', 'Ph.D.'])
          end

          it 'parses consecutive titles in display order' do
            expect(parser.parse!('Lt. Col. Bernado Franecki')[0].values_at(:given, :family, :title)).to eq(['Bernado', 'Franecki', 'Lt. Col.'])
          end

          context 'when include_particle_in_family is false' do
            let(:parser) { Parser.new(include_particle_in_family: false) }

            it 'parses common capitalized particles as the family name in display order' do
              expect(parser.parse!('Carlos De Silva')[0].values_at(:given, :family, :particle)).to eq(['Carlos', 'Silva', 'De'])
            end

            it 'parses common capitalized particles with punctuation as the family name in display order' do
              expect(parser.parse!('Matt St. Hilaire')[0].values_at(:given, :family, :particle)).to eq(['Matt', 'Hilaire', 'St.'])
            end

            it 'parses multiple common capitalized particles as the family name in display order' do
              expect(parser.parse!('Tom Van De Weghe')[0].values_at(:given, :family, :particle)).to eq(['Tom', 'Weghe', 'Van De'])
            end

            it 'parses common lowercase particles as a particle, not family name in display order' do
              expect(parser.parse!('Carlos de Silva')[0].values_at(:given, :family, :particle)).to eq(['Carlos', 'Silva', 'de'])
            end

            it 'parses common capitalized particles as the family name in sort order' do
              expect(parser.parse!('De Silva, Carlos')[0].values_at(:given, :family, :particle)).to eq(['Carlos', 'Silva', 'De'])
            end

            it 'parses common lowercase particles as a particle, not family name in sort order' do
              expect(parser.parse!('de Silva, Carlos')[0].values_at(:given, :family, :particle)).to eq(['Carlos', 'Silva', 'de'])
            end

            it 'parses common capitalized particles with punctuation as the family name in display order' do
              expect(parser.parse!('St. Hilaire, Matt')[0].values_at(:given, :family, :particle)).to eq(['Matt', 'Hilaire', 'St.'])
            end
          end

          context 'when include_particle_in_family is true' do
            let(:parser) { Parser.new(include_particle_in_family: true) }

            it 'parses common capitalized particles as the family name in display order' do
              expect(parser.parse!('Carlos De Silva')[0].values_at(:given, :family, :particle)).to eq(['Carlos', 'De Silva', nil])
            end

            it 'parses common capitalized particles with punctuation as the family name in display order' do
              expect(parser.parse!('Matt St. Hilaire')[0].values_at(:given, :family, :particle)).to eq(['Matt', 'St. Hilaire', nil])
            end

            it 'parses common lowercase particles as family name in display order' do
              expect(parser.parse!('Carlos de Silva')[0].values_at(:given, :family, :particle)).to eq(['Carlos', 'de Silva', nil])
            end

            it 'parses common capitalized particles as the family name in sort order' do
              expect(parser.parse!('De Silva, Carlos')[0].values_at(:given, :family, :particle)).to eq(['Carlos', 'De Silva', nil])
            end

            it 'parses common lowercase particles as family name in sort order' do
              expect(parser.parse!('de Silva, Carlos')[0].values_at(:given, :family, :particle)).to eq(['Carlos', 'de Silva', nil])
            end

            it 'parses common capitalized particles with punctuation as the family name in display order' do
              expect(parser.parse!('St. Hilaire, Matt')[0].values_at(:given, :family, :particle)).to eq(['Matt', 'St. Hilaire', nil])
            end
          end
        end
      end

    end
  end
end
