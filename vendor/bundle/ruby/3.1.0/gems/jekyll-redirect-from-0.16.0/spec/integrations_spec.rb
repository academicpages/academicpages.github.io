# frozen_string_literal: true

RSpec.describe "JekyllRedirectFrom integration tests" do
  before { site.process }
  let(:relative_path) { "" }
  let(:path) { dest_dir(relative_path) }
  let(:contents) { File.read(path) }

  context "pages" do
    context "single redirect from" do
      let(:relative_path) { "some/other/path.html" }

      it "exists in the built site" do
        expect(path).to exist
        expect(contents).to match("http://jekyllrb.com/one_redirect_from.html")
      end
    end

    context "multiple redirect froms" do
      %w(help contact let-there/be/light-he-said geepers/mccreepin).each do |redirect|
        context "the #{redirect} redirect" do
          let(:relative_path) { "#{redirect}.html" }

          it "exists in the built site" do
            expect(path).to exist
            expect(contents).to match("http://jekyllrb.com/multiple_redirect_froms.html")
          end
        end
      end
    end

    context "a redirect to URL" do
      let(:relative_path) { "one_redirect_to_url.html" }

      it "exists in the built site" do
        expect(path).to exist
        expect(contents).to match("https://www.github.com")
      end
    end

    context "a redirect to path" do
      let(:relative_path) { "one_redirect_to_path.html" }

      it "exists in the built site" do
        expect(path).to exist
        expect(contents).to match("http://jekyllrb.com/foo")
      end
    end
  end

  context "documents" do
    context "a single redirect from" do
      let(:relative_path) { "articles/23128432159832/mary-had-a-little-lamb.html" }

      it "exists in the built site" do
        expect(path).to exist
        expect(contents).to match("http://jekyllrb.com/articles/redirect-me-plz.html")
      end
    end

    context "redirect to" do
      let(:relative_path) { "articles/redirect-somewhere-else-plz.html" }

      it "exists in the built site" do
        expect(path).to exist
        expect(contents).to match("http://www.zombo.com")
      end
    end

    context "with a permalink" do
      let(:relative_path) { "tags/our projects/index.html" }

      it "exists in the built site" do
        expect(path).to exist
        expect(contents).to match("http://jekyllrb.com/tags/our-projects/")
      end
    end
  end

  context "sitemap" do
    let(:relative_path) { "sitemap.xml" }

    it "doesn't contain redirects" do
      expect(contents).to_not be_nil
      expect(contents).to_not match("redirect_to")
    end
  end
end
