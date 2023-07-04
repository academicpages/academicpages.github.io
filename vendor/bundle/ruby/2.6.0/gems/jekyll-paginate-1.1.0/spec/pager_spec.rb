require 'spec_helper'

RSpec.describe(Jekyll::Paginate::Pager) do

  it "calculate number of pages" do
    expect(described_class.calculate_pages([], '2')).to eql(0)
    expect(described_class.calculate_pages([1], '2')).to eql(1)
    expect(described_class.calculate_pages([1,2], '2')).to eql(1)
    expect(described_class.calculate_pages([1,2,3], '2')).to eql(2)
    expect(described_class.calculate_pages([1,2,3,4], '2')).to eql(2)
    expect(described_class.calculate_pages([1,2,3,4,5], '2')).to eql(3)
  end

  context "with the default paginate_path" do
    let(:site) { build_site }

    it "determines the correct pagination path for each page" do
      expect(described_class.paginate_path(site, 1)).to eql("/index.html")
      expect(described_class.paginate_path(site, 2)).to eql("/page2")
    end
  end

  context "with paginate_path set to a subdirectory with no index.html" do
    let(:site) { build_site({'paginate_path' => '/blog/page-:num'}) }

    it "determines the correct pagination path for each page" do
      expect(described_class.paginate_path(site, 1)).to eql("/index.html")
      expect(described_class.paginate_path(site, 2)).to eql("/blog/page-2")
    end
  end

  context "with paginate_path set to a subdirectory with no index.html with num pages being in subdirectories" do
    let(:site) { build_site({'paginate_path' => '/blog/page/:num'}) }

    it "determines the correct pagination path for each page" do
      expect(described_class.paginate_path(site, 1)).to eql("/index.html")
      expect(described_class.paginate_path(site, 2)).to eql("/blog/page/2")
    end
  end

  context "with paginate_path set to a subdirectory wherein an index.html exists" do
    let(:site) { build_site({'paginate_path' => '/contacts/page:num'}) }

    it "determines the correct pagination path for each page" do
      expect(described_class.paginate_path(site, 1)).to eql("/contacts/index.html")
      expect(described_class.paginate_path(site, 2)).to eql("/contacts/page2")
    end
  end

  context "with paginate_path set to a subdir wherein an index.html exists with pages in subdirs" do
    let(:site) { build_site({'paginate_path' => '/contacts/page/:num'}) }

    it "determines the correct pagination path for each page" do
      expect(described_class.paginate_path(site, 1)).to eql("/contacts/index.html")
      expect(described_class.paginate_path(site, 2)).to eql("/contacts/page/2")
    end
  end

  context "pagination disabled" do
    let(:site) { build_site('paginate' => nil) }

    it "report that pagination is disabled" do
      expect(described_class.pagination_enabled?(site)).to be_falsey
    end
  end

  context "pagination enabled for 2" do
    let(:site)  { build_site('paginate' => 2) }
    let(:posts) { site.posts }

    it "report that pagination is enabled" do
      expect(described_class.pagination_enabled?(site)).to be_truthy
    end

    context "with 4 posts" do
      let(:posts) { site.posts[1..4] }

      it "create first pager" do
        pager = described_class.new(site, 1, posts)
        expect(pager.posts.size).to eql(2)
        expect(pager.total_pages).to eql(2)
        expect(pager.previous_page).to be_nil
        expect(pager.next_page).to eql(2)
      end

      it "create second pager" do
        pager = described_class.new(site, 2, posts)
        expect(pager.posts.size).to eql(2)
        expect(pager.total_pages).to eql(2)
        expect(pager.previous_page).to eql(1)
        expect(pager.next_page).to be_nil
      end

      it "not create third pager" do
        expect { described_class.new(site, 3, posts) }.to raise_error
      end

    end

    context "with 5 posts" do
      let(:posts) { site.posts[1..5] }

      it "create first pager" do
        pager = described_class.new(site, 1, posts)
        expect(pager.posts.size).to eql(2)
        expect(pager.total_pages).to eql(3)
        expect(pager.previous_page).to be_nil
        expect(pager.next_page).to eql(2)
      end

      it "create second pager" do
        pager = described_class.new(site, 2, posts)
        expect(pager.posts.size).to eql(2)
        expect(pager.total_pages).to eql(3)
        expect(pager.previous_page).to eql(1)
        expect(pager.next_page).to eql(3)
      end

      it "create third pager" do
        pager = described_class.new(site, 3, posts)
        expect(pager.posts.size).to eql(1)
        expect(pager.total_pages).to eql(3)
        expect(pager.previous_page).to eql(2)
        expect(pager.next_page).to be_nil
      end

      it "not create fourth pager" do
        expect { described_class.new(site, 4, posts) }.to raise_error(RuntimeError)
      end

    end
  end

end
