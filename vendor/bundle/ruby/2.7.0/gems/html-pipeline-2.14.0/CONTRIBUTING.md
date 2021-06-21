# Contributing

Thanks for using and improving `HTML::Pipeline`!

- [Submitting a New Issue](#submitting-a-new-issue)
- [Sending a Pull Request](#sending-a-pull-request)

## Submitting a New Issue

If there's an idea you'd like to propose, or a design change, feel free to file a new issue. 

If you have an implementation question or believe you've found a bug, please provide as many details as possible:

- Input document
- Output HTML document
- the exact `HTML::Pipeline` code you are using
- output of the following from your project

```
ruby -v
bundle exec nokogiri -v
```

## Sending a Pull Request

[Pull requests][pr] are always welcome!

Check out [the project's issues list][issues] for ideas on what could be improved.

Before sending, please add tests and ensure the test suite passes.

### Running the Tests

To run the full suite:

  `bundle exec rake`

To run a specific test file:

  `bundle exec ruby -Itest test/html/pipeline_test.rb`

To run a specific test:

  `bundle exec ruby -Itest test/html/pipeline/markdown_filter_test.rb -n test_disabling_gfm`  

To run the full suite with all [supported rubies][travisyaml] in bash:

```bash
rubies=(ree-1.8.7-2011.03 1.9.2-p290 1.9.3-p429 2.0.0-p247)
for r in ${rubies[*]} 
do 
  rbenv local $r # switch to your version manager of choice
  bundle install 
  bundle exec rake 
done
```

[issues]: https://github.com/jch/html-pipeline/issues
[pr]: https://help.github.com/articles/using-pull-requests
[travisyaml]: https://github.com/jch/html-pipeline/blob/master/.travis.yml
