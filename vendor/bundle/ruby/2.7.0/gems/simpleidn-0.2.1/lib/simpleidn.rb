require 'simpleidn/version'
require 'simpleidn/uts46mapping'
require 'unf'

module SimpleIDN
  # The ConversionError is raised when an error occurs during a
  # Punycode <-> Unicode conversion.
  class ConversionError < RangeError
  end

  module Punycode
    INITIAL_N = 0x80
    INITIAL_BIAS = 72
    DELIMITER = 0x2D
    BASE = 36
    DAMP = 700
    TMIN = 1
    TMAX = 26
    SKEW = 38
    MAXINT = 0x7FFFFFFF
    ASCII_MAX = 0x7F

    EMPTY = ''.encode(Encoding::UTF_8).freeze

    module_function

    # decode_digit(cp) returns the numeric value of a basic code
    # point (for use in representing integers) in the range 0 to
    # base-1, or base if cp is does not represent a value.
    def decode_digit(cp)
      cp - 48 < 10 ? cp - 22 : cp - 65 < 26 ? cp - 65 : cp - 97 < 26 ? cp - 97 : BASE
    end

    # encode_digit(d) returns the basic code point whose value
    # (when used for representing integers) is d, which needs to be in
    # the range 0 to base-1.
    def encode_digit(d)
      d + 22 + 75 * (d < 26 ? 1 : 0)
      #  0..25 map to ASCII a..z
      # 26..35 map to ASCII 0..9
    end

    # Bias adaptation function
    def adapt(delta, numpoints, firsttime)
      delta = firsttime ? (delta / DAMP) : (delta >> 1)
      delta += (delta / numpoints)

      k = 0
      while delta > (((BASE - TMIN) * TMAX) / 2)
        delta /= BASE - TMIN
        k += BASE
      end
      k + (BASE - TMIN + 1) * delta / (delta + SKEW)
    end

    # Main decode
    def decode(input)
      input_encoding = input.encoding
      input = input.encode(Encoding::UTF_8).codepoints.to_a
      output = []

      # Initialize the state:
      n = INITIAL_N
      i = 0
      bias = INITIAL_BIAS

      # Handle the basic code points: Let basic be the number of input code
      # points before the last delimiter, or 0 if there is none, then
      # copy the first basic code points to the output.
      basic = input.rindex(DELIMITER) || 0

      input[0, basic].each do |char|
        raise(ConversionError, "Illegal input >= 0x80") if char > ASCII_MAX
        output << char
      end

      # Main decoding loop: Start just after the last delimiter if any
      # basic code points were copied; start at the beginning otherwise.

      ic = basic > 0 ? basic + 1 : 0
      while ic < input.length
        # ic is the index of the next character to be consumed,

        # Decode a generalized variable-length integer into delta,
        # which gets added to i. The overflow checking is easier
        # if we increase i as we go, then subtract off its starting
        # value at the end to obtain delta.
        oldi = i
        w = 1
        k = BASE
        loop do
          raise(ConversionError, "punycode_bad_input(1)") if ic >= input.length

          digit = decode_digit(input[ic])
          ic += 1

          raise(ConversionError, "punycode_bad_input(2)") if digit >= BASE

          raise(ConversionError, "punycode_overflow(1)") if digit > (MAXINT - i) / w

          i += digit * w
          t = k <= bias ? TMIN : k >= bias + TMAX ? TMAX : k - bias
          break if digit < t
          raise(ConversionError, "punycode_overflow(2)") if w > MAXINT / (BASE - t)

          w *= BASE - t
          k += BASE
        end

        out = output.length + 1
        bias = adapt(i - oldi, out, oldi == 0)

        # i was supposed to wrap around from out to 0,
        # incrementing n each time, so we'll fix that now:
        raise(ConversionError, "punycode_overflow(3)") if (i / out) > MAXINT - n

        n += (i / out)
        i %= out

        # Insert n at position i of the output:
        output.insert(i, n)
        i += 1
      end

      output.collect {|c| c.chr(Encoding::UTF_8)}.join(EMPTY).encode(input_encoding)
    end

    # Main encode function
    def encode(input)
      input_encoding = input.encoding
      input = input.encode(Encoding::UTF_8).codepoints.to_a
      output = []

      # Initialize the state:
      n = INITIAL_N
      delta = 0
      bias = INITIAL_BIAS

      # Handle the basic code points:
      output = input.select { |char| char <= ASCII_MAX }

      h = b = output.length

      # h is the number of code points that have been handled, b is the
      # number of basic code points

      output << DELIMITER if b > 0

      # Main encoding loop:
      while h < input.length
        # All non-basic code points < n have been
        # handled already. Find the next larger one:

        m = MAXINT

        input.each do |char|
          m = char if char >= n && char < m
        end

        # Increase delta enough to advance the decoder's
        # <n,i> state to <m,0>, but guard against overflow:

        raise(ConversionError, "punycode_overflow (1)") if m - n > ((MAXINT - delta) / (h + 1)).floor

        delta += (m - n) * (h + 1)
        n = m

        input.each_with_index do |char, _|
          if char < n
            delta += 1
            raise(ConversionError, "punycode_overflow(2)") if delta > MAXINT
          end

          next unless char == n

          # Represent delta as a generalized variable-length integer:
          q = delta
          k = BASE
          loop do
            t = k <= bias ? TMIN : k >= bias + TMAX ? TMAX : k - bias
            break if q < t
            output << encode_digit(t + (q - t) % (BASE - t))
            q = ((q - t) / (BASE - t)).floor
            k += BASE
          end
          output << encode_digit(q)
          bias = adapt(delta, h + 1, h == b)
          delta = 0
          h += 1
        end

        delta += 1
        n += 1
      end
      output.collect {|c| c.chr(Encoding::UTF_8)}.join(EMPTY).encode(input_encoding)
    end
  end

  ACE_PREFIX = 'xn--'.encode(Encoding::UTF_8).freeze
  ASCII_MAX = 0x7F
  DOT = 0x2E.chr(Encoding::UTF_8).freeze
  EMPTY = ''.encode(Encoding::UTF_8).freeze
  LABEL_SEPERATOR_RE = /[\u002e\uff0e\u3002\uff61]/

  unless defined?(UTS64MAPPING)
    # Define a basic uppercase to lowercase mapping for ASCII a..z
    UTS64MAPPING = Hash[(65..90).map { |n| [n, n + 32] }].freeze
  end

  # See UTS46 Table 1
  TRANSITIONAL = {
    0x00DF => [0x0073, 0x0073],
    0x03C2 => 0x03C3,
    0x200C => [],
    0x200D => []
  }.freeze

  module_function

  # Applies UTS46 mapping to a Unicode string
  # Returns a UTF-8 string in Normalization Form C (NFC)
  def uts46map(str, transitional = false)
    mapped = str.codepoints.map { |cp| UTS64MAPPING.fetch(cp, cp) }
    mapped = mapped.map { |cp| TRANSITIONAL.fetch(cp, cp) } if transitional
    mapped = mapped.flatten.map { |cp| cp.chr(Encoding::UTF_8) }.join(EMPTY)
    mapped.to_nfc
  end

  # Converts a UTF-8 unicode string to a punycode ACE string.
  # == Example
  #   SimpleIDN.to_ascii("møllerriis.com")
  #    => "xn--mllerriis-l8a.com"
  def to_ascii(domain, transitional = false)
    return nil if domain.nil?
    mapped_domain = uts46map(domain.encode(Encoding::UTF_8), transitional)
    domain_array = mapped_domain.split(LABEL_SEPERATOR_RE, -1) rescue []
    out = []
    content = false
    domain_array.each do |s|
      # Skip leading empty labels
      next if s.empty? && !content
      content = true

      out << (s.codepoints.any? { |cp| cp > ASCII_MAX } ? ACE_PREFIX + Punycode.encode(s) : s)
    end

    # If all we had were dots; return "."
    out = [DOT] if out.empty? && !mapped_domain.empty?

    out.join(DOT).encode(domain.encoding)
  end

  # Converts a punycode ACE string to a UTF-8 unicode string.
  # == Example
  #   SimpleIDN.to_unicode("xn--mllerriis-l8a.com")
  #    => "møllerriis.com"
  def to_unicode(domain, transitional = false)
    return nil if domain.nil?
    mapped_domain = uts46map(domain.encode(Encoding::UTF_8), transitional)
    domain_array = mapped_domain.split(LABEL_SEPERATOR_RE, -1) rescue []
    out = []
    content = false
    domain_array.each do |s|
      # Skip leading empty labels
      next if s.empty? && !content
      content = true

      out << (s.start_with?(ACE_PREFIX) ? Punycode.decode(s[ACE_PREFIX.length..-1]) : s)
    end

    # If all we had were dots; return "."
    out = [DOT] if out.empty? && !mapped_domain.empty?

    out = out.join(DOT)
    # Try to convert to the input encoding, but don't error on failure
    # Given that the input is plain 7-bit ASCII only, converting back
    # frequently fails.  We will try to allow UTF-16 and Unicode encodings
    begin
      out.encode!(domain.encoding)
    rescue Encoding::UndefinedConversionError
    end
    out
  end
end
