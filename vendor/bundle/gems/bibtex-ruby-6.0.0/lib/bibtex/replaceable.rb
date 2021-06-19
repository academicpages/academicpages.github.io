#--
# BibTeX-Ruby
# Copyright (C) 2010  Sylvester Keil <sylvester.keil.or.at>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#++

module BibTeX
  #
  # The Replaceable module provides methods that expose a Value attribute
  # and the ability to join or replace the contained BibTeX symbols.
  #
  module Replaceable
    extend Forwardable

    attr_reader :value

    def value=(value)
      @value = Value.new(value)
    end

    def replace(*arguments)
      @value.replace(*arguments)
      self
    end

    def join
      @value.join
      self
    end

    def <<(value)
      @value << value
      self
    end

    alias v value
  end
end
