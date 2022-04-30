$:.unshift File.dirname(__FILE__)

module Colorator
  module_function
  VERSION = "1.1.0"

  # --------------------------------------------------------------------------

  ANSI_MATCHR = /\x1b.*?[jkmsuABGKH]/
  ANSI_COLORS = {
    :black   => 30,
    :red     => 31,
    :green   => 32,
    :yellow  => 33,
    :blue    => 34,
    :magenta => 35,
    :cyan    => 36,
    :white   => 37,
    :bold    => 1
  }

  # --------------------------------------------------------------------------
  # Allows you to check if a string currently has ansi.
  # --------------------------------------------------------------------------

  def has_ansi?(str)
    str.match(ANSI_MATCHR).is_a?(
      MatchData
    )
  end

  # --------------------------------------------------------------------------
  # Jump the cursor, moving it up and then back down to it's spot, allowing
  # you to do fancy things like multiple output (downloads) the way that Docker
  # does them in an async way without breaking term.
  # --------------------------------------------------------------------------

  def ansi_jump(str, num)
    "\x1b[#{num}A#{clear_line(str)}\x1b[#{
      num
    }B"
  end

  # --------------------------------------------------------------------------

  def reset_ansi(str = "")
    "\x1b[0m#{
      str
    }"
  end

  # --------------------------------------------------------------------------

  def clear_line(str = "")
    "\x1b[2K\r#{
      str
    }"
  end

  # --------------------------------------------------------------------------
  # Strip ANSI from the current string, making it just a normal string.
  # --------------------------------------------------------------------------

  def strip_ansi(str)
    str.gsub(
      ANSI_MATCHR, ""
    )
  end

  # --------------------------------------------------------------------------
  # Clear the screen's current view, so the user gets a clean output.
  # --------------------------------------------------------------------------

  def clear_screen(str = "")
    "\x1b[H\x1b[2J#{
      str
    }"
  end

  # --------------------------------------------------------------------------

  def colorize(str = "", color)
    "\x1b[#{color}m#{str}\x1b[0m"
  end

  # --------------------------------------------------------------------------

  Colorator::ANSI_COLORS.each do |color, code|
    define_singleton_method color do |str|
      colorize(
        str, code
      )
    end
  end

  # --------------------------------------------------------------------------

  class << self
    alias reset_color reset_ansi
    alias strip_color strip_ansi
    alias has_color? has_ansi?
  end

  # --------------------------------------------------------------------------

  CORE_METHODS = (
    public_methods - Object.methods
  )
end

require "colorator/core_ext"
