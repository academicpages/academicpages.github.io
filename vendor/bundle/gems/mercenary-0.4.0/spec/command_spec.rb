# frozen_string_literal: true

require "spec_helper"

describe(Mercenary::Command) do
  context "a basic command" do
    let(:command) { Mercenary::Command.new(:my_name) }
    let(:parent)  { Mercenary::Command.new(:my_parent) }
    let(:with_sub) do
      c = Mercenary::Command.new(:i_have_subcommand)
      add_sub.call(c)
      c
    end
    let(:command_with_parent) do
      Mercenary::Command.new(
        :i_have_parent,
        parent
      )
    end
    let(:add_sub) do
      proc do |c|
        c.command(:sub_command) { |p| }
      end
    end

    it "can be created with just a name" do
      expect(command.name).to eql(:my_name)
    end

    it "can hold a parent command" do
      expect(command_with_parent.parent).to eql(parent)
    end

    it "can create subcommands" do
      expect(add_sub.call(command)).to be_a(Mercenary::Command)
      expect(add_sub.call(command).parent).to eq(command)
    end

    it "can set its version" do
      version = "1.4.2"
      command.version version
      expect(command.version).to eq(version)
    end

    it "can set its syntax" do
      syntax_string = "my_name [options]"
      cmd = described_class.new(:my_name)
      cmd.syntax syntax_string
      expect(cmd.syntax).to eq(syntax_string)
    end

    it "can set its description" do
      desc = "run all the things"
      command.description desc
      expect(command.description).to eq(desc)
    end

    it "can set its options" do
      name = "show_drafts"
      opts = ["--drafts", "Render posts in the _drafts folder"]
      option = Mercenary::Option.new(name, opts)
      command.option name, *opts
      expect(command.options).to eql([option])
      expect(command.map.values).to include(name)
    end

    it "knows its full name" do
      expect(command_with_parent.full_name).to eql("my_parent i_have_parent")
    end

    it "knows its identity" do
      command_with_parent.version "1.8.7"
      expect(command_with_parent.identity).to eql("my_parent i_have_parent 1.8.7")
    end

    it "raises an ArgumentError if I specify a default_command that isn't there" do
      c = command # some weird NameError with the block below?
      expect { c.default_command(:nope) }.to raise_error(ArgumentError)
    end

    it "sets the default_command" do
      expect(with_sub.default_command(:sub_command).name).to eq(:sub_command)
    end

    context "with an alias" do
      before(:each) do
        command_with_parent.alias(:an_alias)
      end
      it "shows the alias in the summary" do
        expect(command_with_parent.summarize).to eql("  i_have_parent, an_alias  ")
      end

      it "its names_and_aliases method reports both the name and alias" do
        expect(command_with_parent.names_and_aliases).to eql("i_have_parent, an_alias")
      end
    end
  end
end
