# frozen_string_literal: true
class TweetEmbedGenerator < Jekyll::Generator
  def generate(site)
    return if !site.config["embed_tweets"]

    all_notes = site.collections['notes'].docs
    all_pages = site.pages
    all_docs = all_notes + all_pages

    all_docs.each do |current_note|
      current_note.content.gsub!(
        /^https?:\/\/twitter\.com\/(?:#!\/)?(\w+)\/status(es)?\/(\d+)$/i,
        <<~HTML
          <blockquote class="twitter-tweet">
           This tweet could not be embedded. <a href="#{'\0'}">View it on Twitter instead.</a>
          </blockquote>
          <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
        HTML
      )
    end
  end
end
