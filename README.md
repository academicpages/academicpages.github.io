The webpage for the Gravel Lab at Mcgill University

# Instructions for Lab Members

To make edits to this page, ie. adding a biography or publications, follow these instructions:
1. From this repository, click Fork in the top right corner.
1. Clone your fork to your local machine using the command 'git clone'
1. Make your desired changes.
1. Optionally, run your site locally to view your changes.
1. Commit your changes with 'git commit', then push your changes with 'git push'.
1. If you did not run your site locally, run it from github and view your changes there.
1. From this repository, click on 'Pull Requests', then 'New Pull Request'.
1. Click 'compare across forks', then choose your repository as the head repository. Then click 'Create pull request'.

## Running the site locally

1. Install ruby-dev (), ruby-gem (), and nodejs ()
1. Open a terminal in your repository's location, and run 'bundle install' and 'bundle exec jekyll serve'.
1. Open 'localhost:4000' in your browser.

### Known issues
If you get "Error:  No source of timezone data could be found.", add a line "gem 'tzinfo-data'" to the Gemfile.<br>
If you get "cannot load such file -- webrick (LoadError)", add a line "gem 'webrick'" to the Gemfile.<br>
Make sure to run 'bundle install' again after editing the Gemfile.

## Running the site from your github fork

1. Rename your fork to "[your GitHub username].github.io"
1. Go to "[your GitHub username].github" in your browser
