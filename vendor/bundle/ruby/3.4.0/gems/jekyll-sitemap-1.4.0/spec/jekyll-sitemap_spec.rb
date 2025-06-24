# frozen_string_literal: true

require "spec_helper"

describe(Jekyll::JekyllSitemap) do
  let(:overrides) do
    {
      "source"      => source_dir,
      "destination" => dest_dir,
      "url"         => "http://example.org",
      "collections" => {
        "my_collection" => { "output" => true },
        "other_things"  => { "output" => false },
      },
    }
  end
  let(:config) do
    Jekyll.configuration(overrides)
  end
  let(:site)     { Jekyll::Site.new(config) }
  let(:contents) { File.read(dest_dir("sitemap.xml")) }
  before(:each) do
    site.process
  end

  it "has no layout" do
    expect(contents).not_to match(%r!\ATHIS IS MY LAYOUT!)
  end

  it "creates a sitemap.xml file" do
    expect(File.exist?(dest_dir("sitemap.xml"))).to be_truthy
  end

  it "doesn't have multiple new lines or trailing whitespace" do
    expect(contents).to_not match %r!\s+\n!
    expect(contents).to_not match %r!\n{2,}!
  end

  it "puts all the pages in the sitemap.xml file" do
    expect(contents).to match %r!<loc>http://example\.org/</loc>!
    expect(contents).to match %r!<loc>http://example\.org/some-subfolder/this-is-a-subpage\.html</loc>!
  end

  it "only strips 'index.html' from end of permalink" do
    expect(contents).to match %r!<loc>http://example\.org/some-subfolder/test_index\.html</loc>!
  end

  it "puts all the posts in the sitemap.xml file" do
    expect(contents).to match %r!<loc>http://example\.org/2014/03/04/march-the-fourth\.html</loc>!
    expect(contents).to match %r!<loc>http://example\.org/2014/03/02/march-the-second\.html</loc>!
    expect(contents).to match %r!<loc>http://example\.org/2013/12/12/dec-the-second\.html</loc>!
  end

  describe "collections" do
    it "puts all the `output:true` into sitemap.xml" do
      expect(contents).to match %r!<loc>http://example\.org/my_collection/test\.html</loc>!
    end

    it "doesn't put all the `output:false` into sitemap.xml" do
      expect(contents).to_not match %r!<loc>http://example\.org/other_things/test2\.html</loc>!
    end

    it "remove 'index.html' for directory custom permalinks" do
      expect(contents).to match %r!<loc>http://example\.org/permalink/</loc>!
    end

    it "doesn't remove filename for non-directory custom permalinks" do
      expect(contents).to match %r!<loc>http://example\.org/permalink/unique_name\.html</loc>!
    end

    it "performs URI encoding of site paths" do
      expect(contents).to match %r!<loc>http://example\.org/this%20url%20has%20an%20%C3%BCmlaut</loc>!
    end
  end

  it "generates the correct date for each of the posts" do
    expect(contents).to match %r!<lastmod>2014-03-04T00:00:00(-|\+)\d+:\d+</lastmod>!
    expect(contents).to match %r!<lastmod>2014-03-02T00:00:00(-|\+)\d+:\d+</lastmod>!
    expect(contents).to match %r!<lastmod>2013-12-12T00:00:00(-|\+)\d+:\d+</lastmod>!
  end

  it "puts all the static HTML files in the sitemap.xml file" do
    expect(contents).to match %r!<loc>http://example\.org/some-subfolder/this-is-a-subfile\.html</loc>!
  end

  it "does not include assets or any static files that aren't .html" do
    expect(contents).not_to match %r!<loc>http://example\.org/images/hubot\.png</loc>!
    expect(contents).not_to match %r!<loc>http://example\.org/feeds/atom\.xml</loc>!
  end

  it "converts static index.html files to permalink version" do
    expect(contents).to match %r!<loc>http://example\.org/some-subfolder/</loc>!
  end

  it "does include assets or any static files with .xhtml and .htm extensions" do
    expect(contents).to match %r!/some-subfolder/xhtml\.xhtml!
    expect(contents).to match %r!/some-subfolder/htm\.htm!
  end

  it "does include assets or any static files with .pdf extension" do
    expect(contents).to match %r!/static_files/test.pdf!
  end

  it "does not include any static files named 404.html" do
    expect(contents).not_to match %r!/static_files/404.html!
  end

  if Gem::Version.new(Jekyll::VERSION) >= Gem::Version.new("3.4.2")
    it "does not include any static files that have set 'sitemap: false'" do
      expect(contents).not_to match %r!/static_files/excluded\.pdf!
    end

    it "does not include any static files that have set 'sitemap: false'" do
      expect(contents).not_to match %r!/static_files/html_file\.html!
    end
  end

  it "does not include posts that have set 'sitemap: false'" do
    expect(contents).not_to match %r!/exclude-this-post\.html</loc>!
  end

  it "does not include pages that have set 'sitemap: false'" do
    expect(contents).not_to match %r!/exclude-this-page\.html</loc>!
  end

  it "does not include the 404 page" do
    expect(contents).not_to match %r!/404\.html</loc>!
  end

  it "correctly formats timestamps of static files" do
    expect(contents).to match %r!/this-is-a-subfile\.html</loc>\s+<lastmod>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(-|\+)\d{2}:\d{2}</lastmod>!
  end

  it "includes the correct number of items" do
    # static_files/excluded.pdf is excluded on Jekyll 3.4.2 and above
    if Gem::Version.new(Jekyll::VERSION) >= Gem::Version.new("3.4.2")
      expect(contents.scan(%r!(?=<url>)!).count).to eql 20
    else
      expect(contents.scan(%r!(?=<url>)!).count).to eql 21
    end
  end

  context "with a baseurl" do
    let(:config) do
      Jekyll.configuration(Jekyll::Utils.deep_merge_hashes(overrides, "baseurl" => "/bass"))
    end

    it "correctly adds the baseurl to the static files" do
      expect(contents).to match %r!<loc>http://example\.org/bass/some-subfolder/this-is-a-subfile\.html</loc>!
    end

    it "correctly adds the baseurl to the collections" do
      expect(contents).to match %r!<loc>http://example\.org/bass/my_collection/test\.html</loc>!
    end

    it "correctly adds the baseurl to the pages" do
      expect(contents).to match %r!<loc>http://example\.org/bass/</loc>!
      expect(contents).to match %r!<loc>http://example\.org/bass/some-subfolder/this-is-a-subpage\.html</loc>!
    end

    it "correctly adds the baseurl to the posts" do
      expect(contents).to match %r!<loc>http://example\.org/bass/2014/03/04/march-the-fourth\.html</loc>!
      expect(contents).to match %r!<loc>http://example\.org/bass/2014/03/02/march-the-second\.html</loc>!
      expect(contents).to match %r!<loc>http://example\.org/bass/2013/12/12/dec-the-second\.html</loc>!
    end

    it "adds baseurl to robots.txt" do
      content = File.read(dest_dir("robots.txt"))
      expect(content).to match("Sitemap: http://example.org/bass/sitemap.xml")
    end
  end

  context "with urls that needs URI encoding" do
    let(:config) do
      Jekyll.configuration(Jekyll::Utils.deep_merge_hashes(overrides, "url" => "http://ümlaut.example.org"))
    end

    it "performs URI encoding of site url" do
      expect(contents).to match %r!<loc>http://xn--mlaut-jva.example.org/</loc>!
      expect(contents).to match %r!<loc>http://xn--mlaut-jva.example.org/some-subfolder/this-is-a-subpage.html</loc>!
      expect(contents).to match %r!<loc>http://xn--mlaut-jva.example.org/2014/03/04/march-the-fourth.html</loc>!
      expect(contents).to match %r!<loc>http://xn--mlaut-jva.example.org/2016/04/01/%E9%94%99%E8%AF%AF.html</loc>!
      expect(contents).to match %r!<loc>http://xn--mlaut-jva.example.org/2016/04/02/%E9%94%99%E8%AF%AF.html</loc>!
      expect(contents).to match %r!<loc>http://xn--mlaut-jva.example.org/2016/04/03/%E9%94%99%E8%AF%AF.html</loc>!
    end

    it "does not double-escape urls" do
      expect(contents).to_not match %r!%25!
    end

    context "readme" do
      let(:contents) { File.read(dest_dir("robots.txt")) }

      it "has no layout" do
        expect(contents).not_to match(%r!\ATHIS IS MY LAYOUT!)
      end

      it "creates a robots.txt file" do
        expect(File.exist?(dest_dir("robots.txt"))).to be_truthy
      end

      it "renders liquid" do
        expect(contents).to match("Sitemap: http://xn--mlaut-jva.example.org/sitemap.xml")
      end
    end
  end

  context "with user-defined robots.txt" do
    let(:fixture) { "/" }
    let(:fixture_source) { robot_fixtures(fixture) }
    let(:fixture_dest) { robot_fixtures(fixture, "_site") }
    let(:robot_contents) { File.read(robot_fixtures(fixture, "_site", "robots.txt")).strip }
    let(:overrides) do
      {
        "source"      => fixture_source,
        "destination" => fixture_dest,
        "url"         => "http://example.org",
      }
    end

    before(:each) { setup_fixture(fixture) }
    after(:each) { cleanup_fixture(fixture) }

    context "as a static-file at source-root" do
      let(:fixture) { "static-at-source-root" }

      it "doesn't override the robots file" do
        expect(robot_contents).to eql("Allow: /")
      end
    end

    context "as a static-file in a subdir" do
      let(:fixture) { "static-in-subdir" }

      it "generates a valid robot.txt" do
        expect(robot_contents).to eql("Sitemap: http://example.org/sitemap.xml")
      end
    end

    context "as a page at root" do
      let(:fixture) { "page-at-root" }

      it "doesn't override the robots file" do
        expect(robot_contents).to eql("Allow: http://example.org")
      end
    end

    context "as a page with permalink in a subdir" do
      let(:fixture) { "permalinked-page-in-subdir" }

      it "doesn't override the robots file" do
        expect(robot_contents).to eql("Allow: http://example.org")
      end
    end
  end
end
