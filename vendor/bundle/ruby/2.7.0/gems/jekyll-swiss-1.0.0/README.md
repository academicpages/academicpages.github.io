# Swiss Jekyll Theme

Swiss is a bold Jekyll theme inspired by Swiss design and the works of Massimo Vignelli. This theme lends itself well to sites heavy on written content.

### Features:
* Mobile-first design ensures this theme performs fastest on mobile while scaling elegantly to desktop-size screens.
* Designed for blogs and sites heavy on written content, with bold typography styles, homepage summaries, and previous/next snippets.
* Supports a wide range of HTML elements and markdown.
* Flexible styles that can be reused for customization without adding additional CSS.
* Dynamically generated navigation links. See docs for adding pages with specific post category for-loops.

## Installation

Add this line to your Jekyll site's Gemfile:

```ruby
gem "github-pages", group: :jekyll_plugins
```

And add this line to your Jekyll site:

```yaml
remote_theme: broccolini/swiss
```

And then execute:

    $ bundle

## Usage

This theme comes in eight different color variations. The default is set to the black theme, to change to a different theme edit the config under `theme_color: black` to one of the following colors:

|                                                                                                                                          |                                                                                                                                          |
|:-----------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------|
| `theme_color: black`                                                                                                                     | `theme_color: red`                                                                                                                       |
| <img width="330" alt="black" src="https://cloud.githubusercontent.com/assets/334891/18476835/8d70b330-7999-11e6-8c84-a558906d636e.png">  | <img width="330" alt="red" src="https://cloud.githubusercontent.com/assets/334891/18477185/c53af09a-799a-11e6-9354-b9bf1a7f1826.png">    |
| `theme_color: white`                                                                                                                     | `theme_color: gray`                                                                                                                      |
| <img width="330" alt="white" src="https://cloud.githubusercontent.com/assets/334891/18477206/d9dc55fc-799a-11e6-89f2-b4ae150caa80.png">  | <img width="330" alt="gray" src="https://cloud.githubusercontent.com/assets/334891/18477058/4e61700c-799a-11e6-80a0-805e57f2563e.png">   |
| `theme_color: blue`                                                                                                                      | `theme_color: magenta`                                                                                                                      |
| <img width="330" alt="blue" src="https://cloud.githubusercontent.com/assets/334891/18477240/f03646d2-799a-11e6-8895-25b37d3a1438.png">   | <img width="330" alt="magenta" src="https://cloud.githubusercontent.com/assets/334891/18477252/fb2f5128-799a-11e6-8c8f-e79d9c1884b7.png">   |
| `theme_color: orange`                                                                                                                    | `theme_color: yellow`                                                                                                                    |
| <img width="330" alt="orange" src="https://cloud.githubusercontent.com/assets/334891/18477265/06e302bc-799b-11e6-970e-6461b2a89c57.png"> | <img width="330" alt="yellow" src="https://cloud.githubusercontent.com/assets/334891/18477278/117347aa-799b-11e6-83a8-f82341c143e0.png"> |

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/broccolini/swiss. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](http://contributor-covenant.org) code of conduct.

## Development

To set up your environment to develop this theme, run `bundle install`.

Your theme is setup just like a normal Jekyll site! To test your theme, run `bundle exec jekyll serve` and open your browser at `http://localhost:4000`. This starts a Jekyll server using your theme. Add pages, documents, data, etc. like normal to test your theme's contents. As you make modifications to your theme and to your content, your site will regenerate and you should see the changes in the browser after a refresh, just like normal.

When your theme is released, only the files in `_layouts`, `_includes`, and `_sass` tracked with Git will be released.

## License

The theme is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).
