require 'spec_helper'

describe(Mercenary::Presenter) do
  let(:supercommand) { Mercenary::Command.new(:script_name) }
  let(:command) { Mercenary::Command.new(:subcommand, supercommand) }
  let(:presenter) { described_class.new(command) }

  before(:each) do
    command.version '1.4.2'
    command.description 'Do all the things.'
    command.option 'one', '-1', '--one', 'The first option'
    command.option 'two', '-2', '--two', 'The second option'
    command.alias :cmd
    supercommand.commands[command.name] = command
  end

  it "knows how to present the command" do
    expect(presenter.command_presentation).to eql("script_name subcommand 1.4.2 -- Do all the things.\n\nUsage:\n\n  script_name subcommand\n\nOptions:\n        -1, --one          The first option\n        -2, --two          The second option")
  end

  it "knows how to present the subcommands, without duplicates for aliases" do
    expect(described_class.new(supercommand).subcommands_presentation).to eql("  subcommand, cmd       Do all the things.")
  end

  it "knows how to present the usage" do
    expect(presenter.usage_presentation).to eql("  script_name subcommand")
  end

  it "knows how to present the options" do
    expect(presenter.options_presentation).to eql("        -1, --one          The first option\n        -2, --two          The second option")
  end

  it "allows you to say print_* instead of *_presentation" do
    expect(presenter.print_usage).to       eql(presenter.usage_presentation)
    expect(presenter.print_subcommands).to eql(presenter.subcommands_presentation)
    expect(presenter.print_options).to     eql(presenter.options_presentation)
    expect(presenter.print_command).to     eql(presenter.command_presentation)
  end
end
