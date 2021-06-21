require "spec_helper"

describe(Jekyll::Gist::GistTag) do
  let(:http_output) { "<test>true</test>" }
  let(:doc) { doc_with_content(content) }
  let(:content) { "{% gist #{gist} %}" }
  let(:output) do
    doc.content = content
    doc.output  = Jekyll::Renderer.new(doc.site, doc).run
  end

  before(:each) { ENV["JEKYLL_GITHUB_TOKEN"] = nil }

  context "valid gist" do
    context "with user prefix" do
      before { stub_request(:get, "https://gist.githubusercontent.com/#{gist}/raw").to_return(:body => http_output) }
      let(:gist) { "mattr-/24081a1d93d2898ecf0f" }

      it "produces the correct script tag" do
        expect(output).to match(%r!<script src="https:\/\/gist.github.com\/#{gist}.js">\s<\/script>!)
      end
      it "produces the correct noscript tag" do
        expect(output).to match(%r!<noscript><pre>&lt;test&gt;true&lt;\/test&gt;<\/pre><\/noscript>\n!)
      end
    end

    context "without user prefix" do
      before { stub_request(:get, "https://gist.githubusercontent.com/#{gist}/raw").to_return(:body => http_output) }
      let(:gist) { "28949e1d5ee2273f9fd3" }

      it "produces the correct script tag" do
        expect(output).to match(%r!<script src="https:\/\/gist.github.com\/#{gist}.js">\s<\/script>!)
      end
      it "produces the correct noscript tag" do
        expect(output).to match(%r!<noscript><pre>&lt;test&gt;true&lt;\/test&gt;<\/pre><\/noscript>\n!)
      end
    end

    context "classic Gist id style" do
      before { stub_request(:get, "https://gist.githubusercontent.com/#{gist}/raw").to_return(:body => http_output) }
      let(:gist) { "1234321" }

      it "produces the correct script tag" do
        expect(output).to match(%r!<script src="https:\/\/gist.github.com\/#{gist}.js">\s<\/script>!)
      end
      it "produces the correct noscript tag" do
        expect(output).to match(%r!<noscript><pre>&lt;test&gt;true&lt;\/test&gt;<\/pre><\/noscript>\n!)
      end
    end

    context "with file specified" do
      before { stub_request(:get, "https://gist.githubusercontent.com/#{gist}/raw/#{filename}").to_return(:body => http_output) }
      let(:gist)     { "mattr-/24081a1d93d2898ecf0f" }
      let(:filename) { "myfile.ext" }
      let(:content)  { "{% gist #{gist} #{filename} %}" }

      it "produces the correct script tag" do
        expect(output).to match(%r!<script src="https:\/\/gist.github.com\/#{gist}.js\?file=#{filename}">\s<\/script>!)
      end
      it "produces the correct noscript tag" do
        expect(output).to match(%r!<noscript><pre>&lt;test&gt;true&lt;\/test&gt;<\/pre><\/noscript>\n!)
      end
    end

    context "with variable gist id" do
      before { stub_request(:get, "https://gist.githubusercontent.com/#{gist_id}/raw").to_return(:body => http_output) }
      let(:gist_id)  { "1342013" }
      let(:gist)     { "page.gist_id" }
      let(:output) do
        doc.data["gist_id"] = gist_id
        doc.content = content
        doc.output  = Jekyll::Renderer.new(doc.site, doc).run
      end

      it "produces the correct script tag" do
        expect(output).to match(%r!<script src="https:\/\/gist.github.com\/#{doc.data['gist_id']}.js">\s<\/script>!)
      end
      it "produces the correct noscript tag" do
        expect(output).to match(%r!<noscript><pre>&lt;test&gt;true&lt;\/test&gt;<\/pre><\/noscript>\n!)
      end
    end

    context "with variable gist id and filename" do
      before { stub_request(:get, "https://gist.githubusercontent.com/#{gist_id}/raw/#{gist_filename}").to_return(:body => http_output) }
      let(:gist_id)       { "1342013" }
      let(:gist_filename) { "atom.xml" }
      let(:gist)          { "page.gist_id" }
      let(:filename)      { "page.gist_filename" }
      let(:content)       { "{% gist #{gist} #{filename} %}" }
      let(:output) do
        doc.data["gist_id"] = "1342013"
        doc.data["gist_filename"] = "atom.xml"
        doc.content = content
        doc.output  = Jekyll::Renderer.new(doc.site, doc).run
      end

      it "produces the correct script tag" do
        expect(output).to match(%r!<script src="https:\/\/gist.github.com\/#{doc.data['gist_id']}.js\?file=#{doc.data['gist_filename']}">\s<\/script>!)
      end

      it "produces the correct noscript tag" do
        expect(output).to match(%r!<noscript><pre>&lt;test&gt;true&lt;\/test&gt;<\/pre><\/noscript>\n!)
      end
    end

    context "with valid gist id and invalid filename" do
      before { stub_request(:get, "https://gist.githubusercontent.com/#{gist_id}/raw/#{gist_filename}").to_return(:status => 404) }
      let(:gist_id) { "mattr-/24081a1d93d2898ecf0f" }
      let(:gist_filename) { "myfile.ext" }
      let(:content) { "{% gist #{gist_id} #{gist_filename} %}" }

      it "produces the correct script tag" do
        expect(output).to match(%r!<script src="https:\/\/gist.github.com\/#{gist_id}.js\?file=#{gist_filename}">\s<\/script>!)
      end

      it "does not produce the noscript tag" do
        expect(output).to_not match(%r!<noscript><pre>&lt;test&gt;true&lt;\/test&gt;<\/pre><\/noscript>\n!)
      end
    end

    context "with token" do
      before { ENV["JEKYLL_GITHUB_TOKEN"] = "1234" }
      before do
        stub_request(:get, "https://api.github.com/gists/1342013")
          .to_return(:status => 200, :body => fixture("single-file"), :headers => { "Content-Type" => "application/json" })
      end
      let(:gist_id)  { "1342013" }
      let(:gist)     { "page.gist_id" }
      let(:output) do
        doc.data["gist_id"] = gist_id
        doc.content = content
        doc.output  = Jekyll::Renderer.new(doc.site, doc).run
      end

      it "produces the noscript tag" do
        expect(output).to match(%r!<noscript><pre>contents of gist<\/pre><\/noscript>!)
      end

      context "with a filename" do
        before do
          stub_request(:get, "https://api.github.com/gists/1342013")
            .to_return(:status => 200, :body => fixture("multiple-files"), :headers => { "Content-Type" => "application/json" })
        end
        let(:content) { "{% gist 1342013 hello-world.rb %}" }

        it "produces the noscript tag" do
          expect(output).to match(%r!<noscript><pre>puts &#39;hello world&#39;<\/pre><\/noscript>!)
        end
      end
    end

    context "with noscript disabled" do
      let(:doc) { doc_with_content(content, { "gist" => { "noscript" => false } }) }
      let(:output) do
        doc.content = content
        doc.output  = Jekyll::Renderer.new(doc.site, doc).run
      end
      let(:gist) { "mattr-/24081a1d93d2898ecf0f" }

      it "does not produce the noscript tag" do
        expect(output).to_not match(%r!<noscript>!)
      end
    end
  end

  context "invalid gist" do
    context "no gist id present" do
      let(:gist) { "" }

      it "raises an error" do
        expect(-> { output }).to raise_error
      end
    end
  end
end
