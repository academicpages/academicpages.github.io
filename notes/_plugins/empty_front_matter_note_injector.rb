# frozen_string_literal: true

EMPTY_FRONT_MATTER = <<~JEKYLL
  ---
  ---

JEKYLL

# Inject empty front matter in notes that don't have any
Jekyll::Hooks.register :site, :after_init do |site|
  Dir.glob(site.collections['notes'].relative_directory + '/**/*.md').each do |filename|
    raw_note_content = File.read(filename)
    unless raw_note_content.start_with?('---')
      raw_note_content.prepend(EMPTY_FRONT_MATTER)
      File.write(filename, raw_note_content)
    end
  end
end
