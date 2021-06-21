require_relative './spec_helper'

module Hawkins
  RSpec.describe "Hawkins" do
    context "when creating a post" do
      let(:date) do
        Time.now.strftime('%Y-%m-%d')
      end

      before(:each) do
        site = instance_double(Jekyll::Site)
        allow(Jekyll::Site).to receive(:new).and_return(site)
        allow(site).to receive(:in_source_dir).with("_posts").and_return("/no/thing/_posts")

        allow(Jekyll).to receive(:configuration).and_return({})
      end

      def build_expected_path(date, title)
        "_posts/#{date}-#{Jekyll::Utils.slugify(title)}.md"
      end

      it 'fails on a bad post date' do
        expect do
          Commands::Post.create(["title"], 'date' => 'BAD_DATE')
        end.to raise_error(SystemExit).and output(/Could not convert BAD_DATE/).to_stderr
      end

      it 'fails on a missing title' do
        expect do
          Commands::Post.create([], {})
        end.to raise_error(SystemExit).and output(/Please provide an argument/).to_stderr
      end

      # TODO There is a lot of redundancy here.  There's got to be a better way.
      # Look at http://betterspecs.org for ideas.
      it 'uses a provided date' do
        title = "1999"
        expected_body = <<-BODY.gsub(/^\s*/, '')
        ---
        layout: post
        title: #{title}
        ---
        BODY
        expected_file = build_expected_path("1999-12-31", title)

        allow(File).to receive(:exist?).with(/_posts$/).and_return(true)
        allow(File).to receive(:exist?).with(/.md$/).and_return(false)

        file = double('file')
        allow(File).to receive(:open).with(/#{expected_file}/, 'w').and_yield(file)
        expect(file).to receive(:write).with(/#{expected_body}/)

        allow(Commands::Post).to receive(:exec).and_return(nil)

        expect do
          Commands::Post.create([title], "date" => "1999-12-31")
        end.to output(/Wrote/).to_stdout
      end

      it 'uses today as the default date' do
        title = "Raspberry Beret"
        expected_body = <<-BODY.gsub(/^\s*/, '')
        ---
        layout: post
        title: #{title}
        ---
        BODY
        expected_file = build_expected_path(date, title)

        allow(File).to receive(:exist?).with(/_posts$/).and_return(true)
        allow(File).to receive(:exist?).with(/.md$/).and_return(false)

        file = double('file')
        allow(File).to receive(:open).with(/#{expected_file}/, 'w').and_yield(file)
        expect(file).to receive(:write).with(/#{expected_body}/)

        allow(Commands::Post).to receive(:exec).and_return(nil)

        expect do
          Commands::Post.create([title], "date" => date)
        end.to output(/Wrote/).to_stdout
      end

      it 'uses a provided editor' do
        title = "Little Red Corvette"
        expected_file = build_expected_path(date, title)

        allow(File).to receive(:exist?).with(/_posts$/).and_return(true)
        allow(File).to receive(:exist?).with(/.md$/).and_return(false)

        file = double('file')
        allow(File).to receive(:open).with(/#{expected_file}/, 'w').and_yield(file)
        expect(file).to receive(:write)

        allow(Commands::Post).to receive(:exec).with("foo", /#{expected_file}/).and_return(nil)

        expect do
          Commands::Post.create([title], "editor" => "foo")
        end.to output(/Wrote/).to_stdout
      end

      it 'uses the editor from the environment' do
        title = "Let's Go Crazy"
        expected_file = build_expected_path(date, title)

        stub_const("ENV", ENV.to_h.tap { |h| h['VISUAL'] = 'default' })

        allow(File).to receive(:exist?).with(/_posts$/).and_return(true)
        allow(File).to receive(:exist?).with(/.md$/).and_return(false)

        file = double('file')
        allow(File).to receive(:open).with(/#{expected_file}/, 'w').and_yield(file)
        expect(file).to receive(:write)

        allow(Commands::Post).to receive(:exec).with('default', /#{expected_file}/).and_return(nil)

        expect do
          Commands::Post.create([title], {})
        end.to output(/Wrote/).to_stdout
      end

      it 'sets correct vim options' do
        title = "When Doves Cry"
        expected_file = build_expected_path(date, title)

        allow(File).to receive(:exist?).with(/_posts$/).and_return(true)
        allow(File).to receive(:exist?).with(/.md$/).and_return(false)

        file = double('file')
        allow(File).to receive(:open).with(/#{expected_file}/, 'w').and_yield(file)
        expect(file).to receive(:write).twice

        %w(gvim vim).each do |editor|
          allow(Commands::Post).to receive(:exec)
            .with(editor, '+', /#{expected_file}/)
            .and_return(nil)
          stub_const("ENV", ENV.to_h.tap { |h| h['VISUAL'] = editor })
          expect do
            Commands::Post.create([title], {})
          end.to output(/Wrote/).to_stdout
        end
      end

      it 'sets correct emacs options' do
        title = "Purple Rain"
        expected_file = build_expected_path(date, title)

        allow(File).to receive(:exist?).with(/_posts$/).and_return(true)
        allow(File).to receive(:exist?).with(/.md$/).and_return(false)

        file = double('file')
        allow(File).to receive(:open).with(/#{expected_file}/, 'w').and_yield(file)
        expect(file).to receive(:write).twice

        %w(xemacs emacs).each do |editor|
          allow(Commands::Post).to receive(:exec)
            .with(editor, '+4', /#{expected_file}/)
            .and_return(nil)
          stub_const("ENV", ENV.to_h.tap { |h| h['VISUAL'] = editor })
          expect do
            Commands::Post.create([title], {})
          end.to output(/Wrote/).to_stdout
        end
      end

      xit 'handles a missing _posts directory' do
      end

      xit 'handles a file name conflict' do
      end
    end
  end
end
