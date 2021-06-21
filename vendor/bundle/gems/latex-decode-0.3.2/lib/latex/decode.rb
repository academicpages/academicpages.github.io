#--
# LaTeX::Decode
# Copyright (C) 2011-2013 Sylvester Keil <sylvester.keil.or.at>
# Copyright (C) 2010 François Charette
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

require 'latex/decode/version'
require 'latex/decode/compatibility'
require 'latex/decode/base'

require 'latex/decode/accents'
require 'latex/decode/diacritics'
require 'latex/decode/maths'
require 'latex/decode/punctuation'
require 'latex/decode/symbols'
require 'latex/decode/greek'

module LaTeX

  class << self
    def decode(string)
      return string unless string.respond_to?(:to_s)

      string = string.is_a?(String) ? string.dup : string.to_s

      Decode::Base.normalize(string)

      Decode::Maths.decode!(string)

      Decode::Accents.decode!(string)
      Decode::Diacritics.decode!(string)
      Decode::Punctuation.decode!(string)
      Decode::Symbols.decode!(string)
      Decode::Greek.decode!(string)

      Decode::Base.strip_braces(string)

      LaTeX.normalize_C(string)
    end
  end
end
