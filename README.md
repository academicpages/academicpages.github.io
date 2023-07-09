
### Note: if you are using this repo and now get a notification about a security vulnerability, delete the Gemfile.lock file. 

# About me

I am an associate professor in the school of computer and mathematical sciences and the leader of the Information warfare and advanced cyber theme within the Defence trailblazer, the University of Adelaide.

I'm leading a research group on Cyber-AI, applying new advances in AI to solve problems in network fragility and security. Our research evolves around developing autonomous and provable cyber defensive solutions. This means building and configuring systems that are secure by design and training trustworthy AI agents to help defend networked systems. By employing tools from graph theory, game theory and AI/ML we are able to develop practical solutions that help human operators deal with the complexity, fast-paced and deceptive nature of the cyber environments.

Prospective students (2022-11-11): We are offering generous research scholarships (PhDs and Masters) and summer research scholarships (undergraduates) on applying Artificial Intelligence/Machine Learning and Game Theory to solve problems in network (anti)fragility and security.

Please contact me directly with your CV if interested.

Short Bio: A/Prof Hung Nguyen is the Cyber lead for the Defence trailblazer (the University of Adelaide and UNSW). He has an excellent track record in working with Industry and in developing academia-industry collaborations. Over the last 15 years, he has been leading more than 15 successful projects delivering solutions in network security, modelling and simulation of networked systems for Defence and Industry. Outside of academia, he has worked both in start-ups (Telari); consulting to leading telecom and solution providers such as Telstra, CSL, AT&T and CISCO; and providing security and modelling solutions for the Australian Defence Force and Cybersecurity SMEs. He has published more than 80 publications on these topics at prestigious international journals and conferences.

## To run locally (not on GitHub Pages, to serve on your own computer)

1. Clone the repository and made updates as detailed above
1. Make sure you have ruby-dev, bundler, and nodejs installed: `sudo apt install ruby-dev ruby-bundler nodejs`
1. Run `bundle clean` to clean up the directory (no need to run `--force`)
1. Run `bundle install` to install ruby dependencies. If you get errors, delete Gemfile.lock and try again.
1. Run `bundle exec jekyll liveserve` to generate the HTML and serve it from `localhost:4000` the local server will automatically rebuild and refresh the pages on change.

# Changelog -- bugfixes and enhancements

There is one logistical issue with a ready-to-fork template theme like academic pages that makes it a little tricky to get bug fixes and updates to the core theme. If you fork this repository, customize it, then pull again, you'll probably get merge conflicts. If you want to save your various .yml configuration files and markdown files, you can delete the repository and fork it again. Or you can manually patch. 

To support this, all changes to the underlying code appear as a closed issue with the tag 'code change' -- get the list [here](https://github.com/academicpages/academicpages.github.io/issues?q=is%3Aclosed%20is%3Aissue%20label%3A%22code%20change%22%20). Each issue thread includes a comment linking to the single commit or a diff across multiple commits, so those with forked repositories can easily identify what they need to patch.
