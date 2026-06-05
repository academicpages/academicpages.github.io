Jekyll::Hooks.register :site, :after_init do |site|
  require 'css_parser'
  require 'digest'
  require 'fileutils'
  require 'nokogiri'
  require 'open-uri'
  require 'uri'

  font_file_types = ['otf', 'ttf', 'woff', 'woff2']
  image_file_types = ['.gif', '.jpg', '.jpeg', '.png', '.webp']

  def download_and_change_rule_set_url(rule_set, rule, dest, dirname, config, file_types)
    # check if the rule has a url
    if rule_set[rule].include?('url(')
      # get the file url
      url = rule_set[rule].split('url(').last.split(')').first

      # remove quotes from the url
      if url.start_with?('"') || url.start_with?("'")
        url = url[1..-2]
      end

      file_name = url.split('/').last.split('?').first

      # verify if the file is of the correct type
      if file_name.end_with?(*file_types)
        # fix the url if it is not an absolute url
        unless url.start_with?('https://')
          url = URI.join(url, url).to_s
        end

        # download the file
        download_file(url, File.join(dest, file_name))

        # change the url to the local file, considering baseurl
        previous_rule = rule_set[rule]
        if config['baseurl']
          # add rest of the src attribute if it exists
          if rule_set[rule].split(' ').length > 1
            rule_set[rule] = "url(#{File.join(config['baseurl'], 'assets', 'libs', dirname, file_name)}) #{rule_set[rule].split(' ').last}"
          else
            rule_set[rule] = "url(#{File.join(config['baseurl'], 'assets', 'libs', dirname, file_name)})"
          end
        else
          # add rest of the src attribute if it exists
          if rule_set[rule].split(' ').length > 1
            rule_set[rule] = "url(#{File.join('/assets', 'libs', dirname, file_name)}) #{rule_set[rule].split(' ').last}"
          else
            rule_set[rule] = "url(#{File.join('/assets', 'libs', dirname, file_name)})"
          end
        end
        puts "Changed #{previous_rule} to #{rule_set[rule]}"
      end
    end
  end

  def download_file(url, dest)
    # only try to download the file if url doesn't start with | for security reasons
    if url.start_with?('|')
      return
    end

    # create the directory if it doesn't exist
    dir = File.dirname(dest)
    unless File.directory?(dir)
      FileUtils.mkdir_p(dir)
    end

    # download the file if it doesn't exist
    unless File.file?(dest)
      puts "Downloading #{url} to #{dest}"
      File.open(dest, "wb") do |saved_file|
        URI.open(url, "rb") do |read_file|
          saved_file.write(read_file.read)
        end
      end

      # check if the file was downloaded successfully
      unless File.file?(dest)
        raise "Failed to download #{url} to #{dest}"
      end
    end
  end

  def download_fonts(url, dest, file_types)
    # only try to download the file if url doesn't start with | for security reasons
    if url.start_with?('|')
      return
    end

    # only download fonts if the directory doesn't exist or is empty
    unless File.directory?(dest) && !Dir.empty?(dest)
      puts "Downloading fonts from #{url} to #{dest}"
      # get available fonts from the url
      doc = Nokogiri::HTML(URI.open(url, "User-Agent" => "Ruby/#{RUBY_VERSION}"))
      doc.css('a').each do |link|
        # get the file name from the url
        file_name = link['href'].split('/').last.split('?').first

        # verify if the file is a font file
        if file_name.end_with?(*file_types)
          # download the file and change the url to the local file
          download_file(URI.join(url, link['href']).to_s, File.join(dest, file_name))
        end
      end
    end
  end

  def download_images(url, dest, file_types)
    # only try to download the file if url doesn't start with | for security reasons
    if url.start_with?('|')
      return
    end

    # only download images if the directory doesn't exist or is empty
    unless File.directory?(dest) && !Dir.empty?(dest)
      puts "Downloading images from #{url} to #{dest}"
      # get available fonts from the url
      doc = Nokogiri::HTML(URI.open(url, "User-Agent" => "Ruby/#{RUBY_VERSION}"))
      doc.xpath('/html/body/div/div[3]/table/tbody/tr/td[1]/a').each do |link|
        # get the file name from the url
        file_name = link['href'].split('/').last.split('?').first

        # verify if the file is a font file
        if file_name.end_with?(*file_types)
          # download the file and change the url to the local file
          download_file(URI.join(url, link['href']).to_s, File.join(dest, file_name))
        end
      end
    end
  end

  def download_fonts_from_css(config, url, dest, lib_name, file_types)
    # only try to download the file if url doesn't start with | for security reasons
    if url.start_with?('|')
      return
    end

    # get the file name from the url
    file_name = url.split('/').last.split('?').first

    if file_name == 'css'
      file_name = 'google-fonts.css'
    end

    # only download the css file if it doesn't exist
    unless File.file?(File.join(dest, file_name))
      puts "Downloading fonts from #{url} to #{dest}"
      # download the css file with a fake user agent to force downloading woff2 fonts instead of ttf
      # user agent from https://www.whatismybrowser.com/guides/the-latest-user-agent/chrome
      doc = Nokogiri::HTML(URI.open(url, "User-Agent" => "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"))
      css = CssParser::Parser.new
      css.load_string! doc.document.text

      # get the font-face rules
      css.each_rule_set do |rule_set|
        # check if the rule set has a url
        download_and_change_rule_set_url(rule_set, 'src', File.join(dest, 'fonts'), File.join(lib_name, 'fonts'), config, file_types)
      end

      # save the modified css file
      puts "Saving modified css file to #{File.join(dest, file_name)}"
      File.write(File.join(dest, file_name), css.to_s)
    end

    return file_name
  end

  # replace {{version}} with the version number in all 3rd party libraries urls
  site.config['third_party_libraries'].each do |key, value|
    if key != 'download'
      value['url'].each do |type, url|
        # check if url is a dictionary
        if url.is_a?(Hash)
          url.each do |type2, url2|
            # replace {{version}} with the version number if it exists
            if url2.include?('{{version}}')
              site.config['third_party_libraries'][key]['url'][type][type2] = url2.gsub('{{version}}', site.config['third_party_libraries'][key]['version'])
            end
          end
        else
          # replace {{version}} with the version number if it exists
          if url.include?('{{version}}')
            site.config['third_party_libraries'][key]['url'][type] = url.gsub('{{version}}', site.config['third_party_libraries'][key]['version'])
          end
        end
      end
    end
  end

  # download 3rd party libraries if required
  if site.config['third_party_libraries']['download']
    site.config['third_party_libraries'].each do |key, value|
      if key != 'download'
        value['url'].each do |type, url|
          # check if url is a dictionary
          if url.is_a?(Hash)
            url.each do |type2, url2|
              # get the file name from the url
              file_name = url2.split('/').last.split('?').first
              # download the file and change the url to the local file
              dest = File.join(site.source, 'assets', 'libs', key, file_name)
              download_file(url2, dest)
              # change the url to the local file, considering baseurl
              if site.config['baseurl']
                site.config['third_party_libraries'][key]['url'][type][type2] = File.join(site.config['baseurl'], 'assets', 'libs', key, file_name)
              else
                site.config['third_party_libraries'][key]['url'][type][type2] = File.join('/assets', 'libs', key, file_name)
              end
            end

          else
            if type == 'fonts'
              # get the file name from the url
              file_name = url.split('/').last.split('?').first

              if file_name.end_with?('css')
                # if the file is a css file, download the css file, the fonts from it, and change information on the css file
                file_name = download_fonts_from_css(site.config, url, File.join(site.source, 'assets', 'libs', key), key, font_file_types)
                # change the url to the local file, considering baseurl
                if site.config['baseurl']
                  site.config['third_party_libraries'][key]['url'][type] = File.join(site.config['baseurl'], 'assets', 'libs', key, file_name)
                else
                  site.config['third_party_libraries'][key]['url'][type] = File.join('/assets', 'libs', key, file_name)
                end
              else
                # download the font files and change the url to the local file
                download_fonts(url, File.join(site.source, 'assets', 'libs', key, site.config['third_party_libraries'][key]['local'][type]), font_file_types)
              end

            elsif type == 'images'
              # download the font files and change the url to the local file
              download_images(url, File.join(site.source, 'assets', 'libs', key, site.config['third_party_libraries'][key]['local'][type]), image_file_types)

            else
              # get the file name from the url
              file_name = url.split('/').last.split('?').first
              # download the file and change the url to the local file
              dest = File.join(site.source, 'assets', 'libs', key, file_name)
              download_file(url, dest)
              # change the url to the local file, considering baseurl
              if site.config['baseurl']
                site.config['third_party_libraries'][key]['url'][type] = File.join(site.config['baseurl'], 'assets', 'libs', key, file_name)
              else
                site.config['third_party_libraries'][key]['url'][type] = File.join('/assets', 'libs', key, file_name)
              end
            end
          end
        end
      end
    end
  end
end
