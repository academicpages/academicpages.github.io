require 'helper.rb'

module BibTeX
  class RDFConverterTest < Minitest::Spec
    subject { BibTeX::Entry::RDFConverter.new(entry) }
    let(:entry) { Entry.new }

    before do
      entry.parse_names
      entry.parse_month
    end

    describe '#abstract' do
      let(:entry) { Entry.new(abstract: 'foo') }

      it 'should run successfully' do
        subject.abstract
      end
    end

    describe '#annote' do
      let(:entry) { Entry.new(annote: 'foo') }

      it 'should run successfully' do
        subject.annote
      end
    end

    describe '#author' do
      let(:entry) { Entry.new(author: 'Gustav Gans and Donald Duck') }

      it 'should run successfully' do
        subject.author
      end
    end

    describe '#bdsk_url' do
      let(:entry) { Entry.new('bdsk-url-1': 'http://www.example.com') }

      it 'should run successfully' do
        subject.bdsk_url
      end
    end

    describe '#booktitle' do
      let(:entry) { Entry.new(booktitle: 'Entenhausen brennt!') }

      it 'should run successfully' do
        subject.booktitle
      end
    end

    describe '#chapter' do
      let(:entry) { Entry.new(chapter: '4') }

      it 'should run successfully' do
        subject.chapter
      end
    end

    describe '#children' do
      it 'should run successfully'
    end

    describe '#copyright' do
      let(:entry) { Entry.new(copyright: 'King Kong') }

      it 'should run successfully' do
        subject.copyright
      end
    end

    describe '#date_added' do
      let(:entry) { Entry.new('date-added': '2014-01-20') }

      it 'should run successfully' do
        subject.date_added
      end
    end

    describe '#date_modified' do
      let(:entry) { Entry.new('date-modified': '2014-01-20') }

      it 'should run successfully' do
        subject.date_modified
      end
    end

    describe '#doi' do
      let(:entry) { Entry.new(doi: '10.1000/182') }

      it 'should run successfully' do
        subject.doi
      end
    end

    describe '#edition' do
      let(:entry) { Entry.new(edition: 'fifth edition') }

      it 'should run successfully' do
        subject.edition
      end
    end

    describe '#editor' do
      let(:entry) { Entry.new(editor: 'Dagobert Duck') }

      it 'should run successfully' do
        subject.editor
      end
    end

    describe '#fallback_default' do
      it 'should run successfully' do
        subject.fallback_default
      end
    end

    describe '#howpublished' do
      let(:entry) { Entry.new(howpublished: 'http://www.example.com') }

      it 'should run successfully' do
        subject.howpublished
      end
    end

    describe '#institution' do
      let(:entry) { Entry.new(institution: 'University of Duckberg') }

      it 'should run successfully' do
        subject.institution
      end
    end

    describe '#isbn' do
      let(:entry) { Entry.new(isbn: '978-3-935322-14-0') }

      it 'should run successfully' do
        subject.isbn
      end
    end

    describe '#issn' do
      let(:entry) { Entry.new(issn: '978-3-935322-14-0') }

      it 'should run successfully' do
        subject.issn
      end
    end

    describe '#journal_dc_source' do
      let(:entry) { Entry.new(journal: 'Lustiges Taschenbuch') }

      it 'should run successfully' do
        subject.journal_dc_source
      end
    end

    describe '#journal_dc_part_of' do
      let(:entry) { Entry.new(journal: 'Lustiges Taschenbuch') }

      it 'should run successfully' do
        subject.journal_dc_part_of
      end
    end

    describe '#key' do
      let(:entry) { Entry.new(key: 'pickaxe') }

      it 'should run successfully' do
        subject.key
      end
    end

    describe '#keywords' do
      let(:entry) { Entry.new(keywords: 'Ruby, RDF, Fun') }

      it 'should run successfully' do
        subject.keywords
      end
    end

    describe '#language' do
      let(:entry) { Entry.new(language: 'french') }

      it 'should run successfully' do
        subject.language
      end
    end

    describe '#location' do
      let(:entry) { Entry.new(location: 'Duckberg') }

      it 'should run successfully' do
        subject.location
      end
    end

    describe '#lccn' do
      let(:entry) { Entry.new(lccn: '1234') }

      it 'should run successfully' do
        subject.lccn
      end
    end

    describe '#note' do
      let(:entry) { Entry.new(note: 'Never gonna give you up!') }

      it 'should run successfully' do
        subject.note
      end
    end

    describe '#number' do
      let(:entry) { Entry.new(number: '2') }

      it 'should run successfully' do
        subject.number
      end
    end

    describe '#organization' do
      let(:entry) { Entry.new(organization: 'Azkaban Prison') }

      it 'should run successfully' do
        subject.organization
      end
    end

    describe '#pages' do
      let(:entry) { Entry.new(pages: '1--12') }

      it 'should run successfully' do
        subject.pages
      end
    end

    describe '#pagetotal' do
      let(:entry) { Entry.new(pagetotal: '12') }

      it 'should run successfully' do
        subject.pagetotal
      end
    end

    describe '#parent' do
      it 'should run successfully'
    end

    describe '#publisher' do
      let(:entry) { Entry.new(publisher: 'Neustaedter Zeitung') }

      it 'should run successfully' do
        subject.publisher
      end
    end

    describe '#school' do
      let(:entry) { Entry.new(school: 'Hogwarts School of Witchcraft and Wizardry') }

      it 'should run successfully' do
        subject.school
      end
    end

    describe '#series' do
      let(:entry) { Entry.new(series: 'Harry Potter') }

      it 'should run successfully' do
        subject.series
      end
    end

    describe '#thesis_degree' do
      let(:entry) { Entry.new(type: :thesis) }

      it 'should run successfully' do
        subject.thesis_degree
      end
    end

    describe '#title' do
      let(:entry) { Entry.new(title: 'My Title') }

      it 'should run successfully' do
        subject.title
      end
    end

    describe '#translator' do
      let(:entry) { Entry.new(translator: 'Jon Doe') }

      it 'should run successfully' do
        subject.translator
      end
    end

    describe '#type' do
      let(:entry) { Entry.new(type: :proceedings) }

      it 'should run successfully' do
        subject.type
      end
    end

    describe '#url' do
      let(:entry) { Entry.new(url: 'http://www.example.com') }

      it 'should run successfully' do
        subject.url
      end
    end

    describe '#volume' do
      let(:entry) { Entry.new(volume: '4') }

      it 'should run successfully' do
        subject.volume
      end
    end

    describe '#volumes' do
      let(:entry) { Entry.new(volumes: '7') }

      it 'should run successfully' do
        subject.volumes
      end
    end

    describe '#year' do
      let(:entry) { Entry.new(year: '1977', month: 'jan') }

      it 'should run successfully' do
        subject.year
      end
    end
  end
end
