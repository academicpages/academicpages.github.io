module Jekyll
  class Scholar

    class Details < Page
      include Scholar::Utilities

      def initialize(site, base, dir, entry)
        @site, @base, @dir, @entry = site, base, dir, entry

        @config = Scholar.defaults.merge(site.config['scholar'] || {})

        # Specify a temporary filename for now based upon the citation key. Jekyll
        # will modify this according to the URL template below
        @name = entry.key.to_s.gsub(/[:\s]+/, '_')
        @name << '.html'

        process(@name)
        read_yaml(File.join(base, '_layouts'), config['details_layout'])

        data.merge!(reference_data(entry))
        data['title'] = data['entry']['title'] if data['entry'].has_key?('title')
      end

      def url
        # Reuse the logic in the utilities module for deciding URLs
        details_link_for(@entry)
      end
    end

    class DetailsGenerator < Generator
      include Scholar::Utilities

      safe true
      priority :high

      attr_reader :config

      def generate(site)
        @site, @config = site, Scholar.defaults.merge(site.config['scholar'] || {})

        if generate_details?
          entries.each do |entry|
            details = Details.new(site, site.source, File.join('', details_path), entry)
            details.render(site.layouts, site.site_payload)
            details.write(site.dest)

            site.pages << details

            site.regenerator.add_dependency(
              site.in_source_dir(details.path),
              bibtex_path
            )
          end

        end
      end

    end


  end
end
