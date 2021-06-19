# -*- encoding: utf-8 -*-

require 'helper'

module BibTeX

  class BibliographyTest < Minitest::Spec

    describe 'when newly created' do
      it 'should not be nil' do
        assert Bibliography.new
      end
      it 'should be empty' do
        assert Bibliography.new.empty?
      end
    end

    describe '.open' do
      it 'accepts a block and save the file after execution' do
        tmp = Tempfile.new('bibtex')
        tmp.close
        b = BibTeX.open(Test.fixtures(:bibdesk)).save_to(tmp.path)

        BibTeX.open(tmp.path) do |bib|
          bib.delete(:rails)
        end

        assert_equal b.length - 1, BibTeX.open(tmp.path).length
      end

    end

    describe '.parse' do
      it 'accepts filters' do
        Bibliography.parse("@misc{k, title = {\\''u}}", :filter => 'latex')[0].title.must_be :==, 'ü'
      end

      it 'accepts filters in an array' do
        Bibliography.parse("@misc{k, title = {\\''u}}", :filter => ['latex'])[0].title.must_be :==, 'ü'
      end
    end

    describe 'given a populated biliography' do
      before do
        @bib = BibTeX.parse <<-END
        @book{rails,
          address = {Raleigh, North Carolina},
          author = {Ruby, Sam, and Thomas, Dave, and Hansson Heinemeier, David},
          booktitle = {Agile Web Development with Rails},
          edition = {third},
          keywords = {ruby, rails},
          publisher = {The Pragmatic Bookshelf},
          series = {The Facets of Ruby},
          title = {Agile Web Development with Rails},
          year = {2009}
        }
        @book{flanagan2008,
          title={{The ruby programming language}},
          author={Flanagan, D. and Matsumoto, Y.},
          keywords = {ruby},
          year={2008},
          publisher={O'Reilly}
        }
        @article{segaran2007,
          title={{Programming collective intelligence}},
          author={Segaran, T.},
          year={2007},
          publisher={O'Reilly},
          type={interview}
        }
        @string{ foo = "foobar" }
        @misc{flanagan-1,
          title={{Foo Bar}},
          author={Flanagan, Dav and Thomas Segaran}
        }
        @misc{flanagan-2,
          title={{Foo Bar}},
          author={Flanagan, David and Matsumoto, Yukihiro}
        }
        END
      end

      describe '#entries_at' do
        it 'returns a list of all entries identified by the passed-in keys' do
          assert_equal [@bib['segaran2007'], @bib['rails']], @bib.entries_at('segaran2007', :rails)
        end
      end

      describe '#extend_initials' do
        it 'extends the initials in matching names' do
          @bib.names.map(&:to_s).wont_include 'Flanagan, Dave'
          @bib.extend_initials(['Dave', 'Flanagan'])
          @bib.names.map(&:to_s).must_include 'Flanagan, Dave'
        end
      end

      describe '#extend_initials!' do
        it 'extends the initials of all names to the longest prototype' do
          assert_equal "Ruby, Sam Thomas, Dave Hansson Heinemeier, David Flanagan, David Matsumoto, Yukihiro Segaran, Thomas",
            @bib.extend_initials!.names.map(&:sort_order).uniq.join(' ')
        end
      end

      describe '#unify' do
        it 'sets all fields matching the given pattern to the passed-in value' do
          @bib.unify :publisher, /reilly/i, 'OReilly'
          assert_equal 'OReilly', @bib['segaran2007'].publisher
          assert_equal 'OReilly', @bib['flanagan2008'].publisher
        end

        it 'does not change the value of fields that do not match' do
          @bib.unify :publisher, /reilly/i, 'OReilly'
          assert_equal 'The Pragmatic Bookshelf', @bib['rails'].publisher
        end

        it 'passes each entry with matching fields to the block if given' do
          years = []
          @bib.unify(:publisher, /reilly/i) { |e| years << e.year.to_s }
          assert_equal ['2007','2008'], years.sort
        end

        it 'returns the bibliography' do
          assert_equal @bib, @bib.unify(:publisher, /reilly/i, 'OReilly')
        end
      end

      describe '#group_by' do
        it 'returns an empy hash by default' do
          assert_equal({}, Bibliography.new.group_by)
          assert_equal({}, Bibliography.new.group_by(:a, :b))
        end

        it 'returns a hash with all the entries mapped to their default digest' do
          assert_equal @bib.entries.length, @bib.group_by.length
        end

        it 'uses the given block to determine the key' do
          assert_equal @bib.entries.length, (@bib.group_by { 'x' })['x'].length
        end
      end

      it 'supports access by index' do
        assert_equal 'ruby', @bib[1].keywords
      end

      it 'supports access by range' do
        assert_equal %w{2008 2007}, @bib[1..2].map(&:year)
      end

      it 'supports access by index and offset' do
        assert_equal %w{2008 2007}, @bib[1,2].map(&:year)
      end

      it 'supports queries by symbol key' do
        refute_nil @bib[:rails]
        assert_nil @bib[:ruby]
      end

      it 'supports queries by symbol key and selector' do
        assert_equal 1, @bib.q(:all, :rails).length
        refute_nil @bib.q(:first, :rails)
        assert_nil @bib.q(:first, :railss)
      end

      it 'supports queries by string key' do
        refute_nil @bib['rails']
        assert_nil @bib['ruby']
      end

      it 'supports queries by type string' do
        assert_equal 2, @bib['@book'].length
        assert_equal 1, @bib['@article'].length
        assert_equal 0, @bib['@collection'].length
        assert_equal 1, @bib['@string'].length
      end

      it 'supports queries by negated type string' do
        assert_equal 4, @bib['!@book'].length
        assert_equal 5, @bib['!@article'].length
        assert_equal 6, @bib['!@collection'].length
        assert_equal 1, @bib['!@*'].length
        assert_equal 4, @bib['!@misc'].length
        assert_equal 5, @bib['!@string'].length
      end

      it 'supports queries by type string and selector' do
        assert_equal 2, @bib.q(:all, '@book').length
        refute_nil @bib.q(:first, '@book')
        assert_equal 1, @bib.q(:all, '@article').length
        refute_nil @bib.q(:first, '@article')
        assert_equal 0, @bib.q(:all, '@collection').length
        assert_nil @bib.q(:first, '@collection')
      end


      it 'supports queries by pattern' do
        assert_equal 0, @bib[/reilly/].length
        assert_equal 2, @bib[/reilly/i].length
      end

      it 'supports queries by type string and conditions' do
        assert_equal 1, @bib['@book[keywords=ruby]'].length
        assert_equal 1, @bib['@book[keywords = ruby]'].length
        assert_equal 1, @bib['@book[ keywords = ruby]'].length
        assert_equal 1, @bib['@book[keywords=ruby ]'].length
        assert_equal 1, @bib['@*[type=interview]'].length
      end

      it 'supports queries with negative conditions' do
        assert_equal 4, @bib['@*[keywords!=ruby]'].length
      end

      it 'supports queries with pattern conditions' do
        assert_equal 1, @bib['@*[keywords~=rails]'].length
      end

      it 'supports queries with attribute conditions' do
        assert_equal 2, @bib['@*[keywords]'].length
        assert_equal 0, @bib['@*[foobar]'].length
      end

      it 'supports queries with start-pattern conditions' do
        assert_equal 2, @bib['@*[keywords^=ruby]'].length
      end

      it 'supports queries with numeric conditions' do
        assert_equal 3, @bib['@*[year<=2010]'].length
        assert_equal 3, @bib['@*[year<=2009]'].length
        assert_equal 2, @bib['@*[year>=2008]'].length
        assert_equal 0, @bib['@*[year>=2010]'].length
      end


      it 'supports queries by bibtex element' do
        entry = Entry.parse(<<-END).first
        @article{segaran2007,
          title = {{Programming collective intelligence}},
          author = {Segaran, T.},
          year = {2007},
          publisher = {O'Reilly},
          type={interview}
        }
        END
        assert_equal 1, @bib[entry].length
        entry.year = '2006'
        assert_equal 0, @bib[entry].length
      end

      it 'supports query and additional block' do
        assert_equal 1, @bib.q('@book') { |e| e.keywords.split(/,/).length > 1 }.length
      end

      it 'supports saving the bibliography to a file' do
        tmp = Tempfile.new('bibtex')
        tmp.close
        @bib.save_to(tmp.path)
        assert_equal @bib.length, BibTeX.open(tmp.path).length
      end

      describe '#query' do

        it 'returns all elements when passed no arguments' do
          @bib.query.length.must_be :==, 6
        end

        it 'returns all elements when passed :all and an empty condition' do
          @bib.query(:all, '').length.must_be :==, 6
        end

        it 'returns all entries when passed a * wildcard' do
          @bib.query('@*').length.must_be :==, 5
        end

      end

      describe 'duplicates' do

        it 'understands select_duplicates_by' do
          assert_equal 1, @bib.select_duplicates_by.length
        end

        it 'understands duplicates?' do
          assert @bib.duplicates?
        end

      end

      describe '#uniq!' do
        before do
          @a = BibTeX.parse <<-END
            @book{b1,
              title = {FOO},
              year = {2013},
              author = {Doe, John},
              pages = {1-2}}
            @book{b2,
              title = {BAR},
              year = {2013},
              author = {Doe, John},
              pages = {1-3},
              }
          END
          @b = BibTeX.parse <<-END
            @book{b3,
              title = {FOO},
              year = {2013},
              author = {Doe, John},
              pages = {1-2}}
          END
        end

        it 'returns the bibliography unchanged if there are no duplicates' do
          assert @a.length == @a.uniq!.length
          assert @b.length == @b.uniq!.length
        end

        it 'removes duplicate entries and returns the bibliography' do
          assert @a.length > @a.uniq!(:author).length
        end

        describe 'with block' do
          it 'removes duplicate entries and returns the bibliography' do
            assert @a.length > @a.uniq!(:author){|d,e| d+'|'+e.pages_from}.length
          end
        end
      end

      describe 'given a filter' do
        before do
          @filter = Object.new
          def @filter.apply (value); value.is_a?(::String) ? value.upcase : value; end
        end

        it 'supports arbitrary conversions' do
          @bib.convert(@filter)
          assert_equal 'RUBY, RAILS', @bib[:rails].keywords
        end

        it 'supports conditional arbitrary conversions' do
          @bib.convert(@filter) { |e| e.key != 'rails' }
          assert_equal 'ruby, rails', @bib[:rails].keywords
          assert_equal 'RUBY', @bib[:flanagan2008].keywords
        end

      end

      describe 'sorting' do

        before do
          @small_bib = BibTeX.parse <<-END
        @book{flanagan2008,
          title={{The ruby programming language}},
          author={Flanagan, D. and Matsumoto, Y.},
          keywords = {ruby},
          year={2008},
          publisher={O'Reilly}
        }
        @book{rails,
          address = {Raleigh, North Carolina},
          author = {Ruby, Sam, and Thomas, Dave, and Hansson Heinemeier, David},
          booktitle = {Agile Web Development with Rails},
          edition = {third},
          keywords = {ruby, rails},
          publisher = {The Pragmatic Bookshelf},
          series = {The Facets of Ruby},
          title = {Agile Web Development with Rails},
          year = {2009}
        }
        @article{segaran2007,
          title={{Programming collective intelligence}},
          author={Segaran, T.},
          year={2007},
          publisher={O'Reilly}
        }
        END
      end

        it 'can be sorted destructively' do
          @small_bib.sort!
          @small_bib.map(&:key).must_equal [ 'segaran2007', 'flanagan2008', 'rails']
        end

        it 'can be sorted by field destructively' do
          @small_bib.sort_by! { |e| -e[:year].to_i }
          @small_bib.map(&:key).must_equal [  'rails', 'flanagan2008', 'segaran2007' ]
        end

        it 'can be sorted non-destructively' do
          sorted_entries = @small_bib.sort
          sorted_entries.map(&:key).must_equal [ 'segaran2007', 'flanagan2008', 'rails']
          @small_bib.map(&:key).must_equal [  'flanagan2008', 'rails', 'segaran2007']
        end

        it 'can be sorted by field non-destructively' do
          sorted_entries = @small_bib.sort_by { |e| -e[:year].to_i }
          sorted_entries.map(&:key).must_equal [  'rails', 'flanagan2008', 'segaran2007' ]
          @small_bib.map(&:key).must_equal [  'flanagan2008', 'rails', 'segaran2007']
        end
      end

      describe 'LaTeX filter' do
        before do
          @bib['rails'].keywords = 'r\\"uby'
        end

        it 'converts LaTeX umlauts' do
          @bib.convert(:latex)['rails'].keywords.must_be :==, 'rüby'
        end

      end

      describe 'BibTeXML export' do
        before { @bibtexml = Tempfile.new('bibtexml') }
        after  { @bibtexml.unlink }

        it 'supports exporting to BibTeXML' do
          @bib.to_xml.write(@bibtexml, 2)
          @bibtexml.rewind
          xml = REXML::Document.new(@bibtexml)
          xml.root.namespace.must_be :==, 'http://bibtexml.sf.net/'
          xml.root.get_elements('//bibtex:entry').wont_be_empty
        end

        it 'supports exporting to extended BibTeXML' do
          @bib.to_xml(:extended => true).write(@bibtexml, 2)
          @bibtexml.rewind
          xml = REXML::Document.new(@bibtexml)
          xml.root.namespace.must_be :==, 'http://bibtexml.sf.net/'
          xml.root.get_elements('//bibtex:person').wont_be_empty
        end

      end
    end

    describe '#add' do
      before do
        @bib = Bibliography.new(allow_missing_keys: true)
      end

      it 'should respect options provided to initializer' do
        assert_equal(@bib.add('@article{, title = test}'), @bib)
        assert(! @bib.entries.keys.any?(&:empty?))
      end
    end
  end
end
