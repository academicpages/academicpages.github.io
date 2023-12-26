module Hawkins
  module Commands
    class Post < Jekyll::Command
      class << self
        COMMAND_OPTIONS = {
          "date" => ["-d", "--date [DATE]", "Date to mark post"],
          "editor" => ["-e", "--editor [EDITOR]", "Editor to open"],
          "source" => ["-s", "--source SOURCE", "Custom source directory"],
          "config" => [
            "--config CONFIG_FILE[,CONFIG_FILE2,...]", Array, "Custom configuration file"
          ],
        }.freeze

        def init_with_program(prog)
          prog.command(:post) do |cmd|
            cmd.syntax("post [options]")
            cmd.description("create a new post")
            COMMAND_OPTIONS.each do |key, val|
              cmd.option(key, *val)
            end

            cmd.action do |args, options|
              Hawkins::Commands::Post.create(args, options)
            end
          end
        end

        def create(args, options)
          options["date"] ||= Time.now.to_s
          options["editor"] ||= ENV['VISUAL'] || ENV['EDITOR'] || 'vi'
          begin
            date = Date.parse(options["date"])
          rescue
            Jekyll.logger.abort_with("Could not convert #{options['date']} into date format.")
          end

          if args.length != 1
            Jekyll.logger.abort_with(
              "Please provide an argument to use as the post title.\n
              Remember to quote multiword strings.")
          else
            title = args[0]
          end

          slug = Jekyll::Utils.slugify(title)

          site_opts = configuration_from_options(options)
          site = Jekyll::Site.new(site_opts)
          posts = site.in_source_dir('_posts')
          filename = File.join(posts, "#{date.strftime('%Y-%m-%d')}-#{slug}.md")

          # TODO incorporate Highline and allow users to elect to create the directory
          # Like Thor does
          unless File.exist?(posts)
            Jekyll.logger.abort_with("#{posts} does not exist.  Please create it.")
          end

          # TODO ask if user wishes to overwrite
          if File.exist?(filename)
            Jekyll.logger.abort_with(
              "#{filename} already exists.  Cowardly refusing to overwrite it.")
          end

          content = <<-CONTENT
            ---
            layout: post
            title: #{title}
            ---
          CONTENT

          File.open(filename, 'w') do |f|
            f.write(Jekyll::Utils.strip_heredoc(content))
          end

          Jekyll.logger.info("Wrote #{filename}")

          case options["editor"]
          when /g?vim/
            editor_args = "+"
          when /x?emacs/
            editor_args = "+#{content.lines.count}"
          else
            editor_args = nil
          end

          exec(*[options["editor"], editor_args, filename].compact)
        end
      end
    end
  end
end
