module TZInfo
  # Use send as a workaround for erroneous 'wrong number of arguments' errors
  # with JRuby 9.0.5.0 when calling methods with Java implementations. See #114.
  send(:using, RubyCoreSupport::UntaintExt) if RubyCoreSupport.const_defined?(:UntaintExt)

  # An InvalidZoneinfoFile exception is raised if an attempt is made to load an
  # invalid zoneinfo file.
  class InvalidZoneinfoFile < StandardError
  end

  # Represents a timezone defined by a compiled zoneinfo TZif (\0, 2 or 3) file.
  #
  # @private
  class ZoneinfoTimezoneInfo < TransitionDataTimezoneInfo #:nodoc:
    # The year to generate transitions up to.
    #
    # @private
    GENERATE_UP_TO = RubyCoreSupport.time_supports_64bit ? Time.now.utc.year + 100 : 2037

    # Minimum supported timestamp (inclusive).
    #
    # Time.utc(1700, 1, 1).to_i
    MIN_TIMESTAMP = -8520336000

    # Maximum supported timestamp (exclusive).
    #
    # Time.utc(2500, 1, 1).to_i
    MAX_TIMESTAMP = 16725225600

    # Constructs the new ZoneinfoTimezoneInfo with an identifier, path
    # to the file and parser to use to parse the POSIX-like TZ string.
    def initialize(identifier, file_path, posix_tz_parser)
      super(identifier)
      
      File.open(file_path, 'rb') do |file|
        parse(file, posix_tz_parser)
      end
    end
    
    private
      # Unpack will return unsigned 32-bit integers. Translate to 
      # signed 32-bit.
      def make_signed_int32(long)
        long >= 0x80000000 ? long - 0x100000000 : long
      end
      
      # Unpack will return a 64-bit integer as two unsigned 32-bit integers
      # (most significant first). Translate to signed 64-bit
      def make_signed_int64(high, low)
        unsigned = (high << 32) | low
        unsigned >= 0x8000000000000000 ? unsigned - 0x10000000000000000 : unsigned
      end
      
      # Read bytes from file and check that the correct number of bytes could
      # be read. Raises InvalidZoneinfoFile if the number of bytes didn't match
      # the number requested.
      def check_read(file, bytes)
        result = file.read(bytes)
        
        unless result && result.length == bytes
          raise InvalidZoneinfoFile, "Expected #{bytes} bytes reading '#{file.path}', but got #{result ? result.length : 0} bytes"
        end
        
        result
      end

      # Zoneinfo files don't include the offset from standard time (std_offset)
      # for DST periods. Derive the base offset (utc_offset) where DST is
      # observed from either the previous or next non-DST period.
      #
      # Returns the index of the offset to be used prior to the first
      # transition.
      def derive_offsets(transitions, offsets)
        # The first non-DST offset (if there is one) is the offset observed
        # before the first transition. Fallback to the first DST offset if there
        # are no non-DST offsets.
        first_non_dst_offset_index = offsets.index {|o| !o[:is_dst] }
        first_offset_index = first_non_dst_offset_index || 0
        return first_offset_index if transitions.empty?

        # Determine the utc_offset of the next non-dst offset at each transition.
        utc_offset_from_next = nil

        transitions.reverse_each do |transition|
          offset = offsets[transition[:offset]]
          if offset[:is_dst]
            transition[:utc_offset_from_next] = utc_offset_from_next if utc_offset_from_next
          else
            utc_offset_from_next = offset[:utc_total_offset]
          end
        end

        utc_offset_from_previous = first_non_dst_offset_index ? offsets[first_non_dst_offset_index][:utc_total_offset] : nil
        defined_offsets = {}

        transitions.each do |transition|
          offset_index = transition[:offset]
          offset = offsets[offset_index]
          utc_total_offset = offset[:utc_total_offset]

          if offset[:is_dst]
            utc_offset_from_next = transition[:utc_offset_from_next]

            difference_to_previous = (utc_total_offset - (utc_offset_from_previous || utc_total_offset)).abs
            difference_to_next = (utc_total_offset - (utc_offset_from_next || utc_total_offset)).abs

            utc_offset = if difference_to_previous == 3600
              utc_offset_from_previous
            elsif difference_to_next == 3600
              utc_offset_from_next
            elsif difference_to_previous > 0 && difference_to_next > 0
              difference_to_previous < difference_to_next ? utc_offset_from_previous : utc_offset_from_next
            elsif difference_to_previous > 0
              utc_offset_from_previous
            elsif difference_to_next > 0
              utc_offset_from_next
            else
              # No difference, assume a 1 hour offset from standard time.
              utc_total_offset - 3600
            end

            if !offset[:utc_offset]
              offset[:utc_offset] = utc_offset
              defined_offsets[offset] = offset_index
            elsif offset[:utc_offset] != utc_offset
              # An earlier transition has already derived a different
              # utc_offset. Define a new offset or reuse an existing identically
              # defined offset.
              new_offset = offset.dup
              new_offset[:utc_offset] = utc_offset

              offset_index = defined_offsets[new_offset]

              unless offset_index
                offsets << new_offset
                offset_index = offsets.length - 1
                defined_offsets[new_offset] = offset_index
              end

              transition[:offset] = offset_index
            end
          else
            utc_offset_from_previous = utc_total_offset
          end
        end

        first_offset_index
      end

      # Remove transitions before a minimum supported value. If there is not a
      # transition exactly on the minimum supported value move the latest from
      # before up to the minimum supported value.
      def remove_unsupported_negative_transitions(transitions, min_supported)
        result = transitions.drop_while {|t| t[:at] < min_supported }
        if result.empty? || (result[0][:at] > min_supported && result.length < transitions.length)
          last_before = transitions[-1 - result.length]
          last_before[:at] = min_supported
          [last_before] + result
        else
          result
        end
      end

      # Determines if the offset from a transition matches the offset from a
      # rule. This is a looser match than TimezoneOffset#==, not requiring that
      # the utc_offset and std_offset both match (which have to be derived for
      # transitions, but are known for rules.
      def offset_matches_rule?(offset, rule_offset)
        offset[:utc_total_offset] == rule_offset.utc_total_offset &&
          offset[:is_dst] == rule_offset.dst? &&
          offset[:abbr] == rule_offset.abbreviation.to_s
      end

      # Determins if the offset from a transition exactly matches the offset
      # from a rule.
      def offset_equals_rule?(offset, rule_offset)
        offset_matches_rule?(offset, rule_offset) &&
          (offset[:utc_offset] || (offset[:is_dst] ? offset[:utc_total_offset] - 3600 : offset[:utc_total_offset])) == rule_offset.utc_offset
      end

      # Finds an offset hash that is an exact match to the rule offset specified.
      def find_existing_offset_index(offsets, rule_offset)
        offsets.find_index {|o| offset_equals_rule?(o, rule_offset) }
      end

      # Gets an existing matching offset index or adds a new offset hash for a
      # rule offset.
      def get_rule_offset_index(offsets, offset)
        index = find_existing_offset_index(offsets, offset)
        unless index
          index = offsets.length
          offsets << {:utc_total_offset => offset.utc_total_offset, :utc_offset => offset.utc_offset, :is_dst => offset.dst?, :abbr => offset.abbreviation}
        end
        index
      end

      # Gets a hash mapping rule offsets to indexes in offsets, creating new
      # offset hashes if required.
      def get_rule_offset_indexes(offsets, annual_rules)
        {
          annual_rules.std_offset => get_rule_offset_index(offsets, annual_rules.std_offset),
          annual_rules.dst_offset => get_rule_offset_index(offsets, annual_rules.dst_offset)
        }
      end

      # Converts an array of rule transitions to hashes.
      def convert_transitions_to_hashes(offset_indexes, transitions)
        transitions.map {|t| {:at => t.at.to_i, :offset => offset_indexes[t.offset]} }
      end

      # Apply the rules from the TZ string when there were no defined
      # transitions. Checks for a matching offset. Returns the rules-based
      # constant offset or generates transitions from 1970 until 100 years into
      # the future (at the time of loading zoneinfo_timezone_info.rb) or 2037 if
      # limited to 32-bit Times.
      def apply_rules_without_transitions(file, offsets, first_offset_index, rules)
        first_offset = offsets[first_offset_index]

        if rules.kind_of?(TimezoneOffset)
          unless offset_matches_rule?(first_offset, rules)
            raise InvalidZoneinfoFile, "Constant offset POSIX-style TZ string does not match constant offset in file '#{file.path}'."
          end

          first_offset[:utc_offset] = rules.utc_offset
          []
        else
          transitions = 1970.upto(GENERATE_UP_TO).map {|y| rules.transitions(y) }.flatten
          first_transition = transitions[0]

          if offset_matches_rule?(first_offset, first_transition.previous_offset)
            # Correct the first offset if it isn't an exact match.
            first_offset[:utc_offset] = first_transition.previous_offset.utc_offset
          else
            # Not transitioning from the designated first offset.
            if offset_matches_rule?(first_offset, first_transition.offset)
              # Correct the first offset if it isn't an exact match.
              first_offset[:utc_offset] = first_transition.offset.utc_offset

              # Skip an unnecessary transition to the first offset.
              transitions.shift
            end

            # If the first offset doesn't match either the offset or previous
            # offset, then it will be retained.
          end

          offset_indexes = get_rule_offset_indexes(offsets, rules)
          convert_transitions_to_hashes(offset_indexes, transitions)
        end
      end

      # Validates the rules offset against the offset of the last defined
      # transition. Replaces the transition with an equivalent using the rules
      # offset if the rules give a different definition for the base offset.
      def replace_last_transition_offset_if_valid_and_needed(file, transitions, offsets)
        last_transition = transitions.last
        last_offset = offsets[last_transition[:offset]]
        rule_offset = yield last_offset

        unless offset_matches_rule?(last_offset, rule_offset)
          raise InvalidZoneinfoFile, "Offset from POSIX-style TZ string does not match final transition in file '#{file.path}'."
        end

        # The total_utc_offset and abbreviation must always be the same. The
        # base utc_offset and std_offset might differ. In which case the rule
        # should be used as it will be more precise.
        last_offset[:utc_offset] = rule_offset.utc_offset
        last_transition
      end

      # todo: port over validate_and_fix_last_defined_transition_offset
      # when fixing the previous offset will need to define a new one

      # Validates the offset indicated to be observed by the rules before the
      # first generated transition against the offset of the last defined
      # transition.
      #
      # Fix the last defined transition if it differ on just base/std offsets
      # (which are derived). Raise an error if the observed UTC offset or
      # abbreviations differ.
      def validate_and_fix_last_defined_transition_offset(file, offsets, last_defined, first_rule_offset)
        offset_of_last_defined = offsets[last_defined[:offset]]

        if offset_equals_rule?(offset_of_last_defined, first_rule_offset)
          last_defined
        else
          if offset_matches_rule?(offset_of_last_defined, first_rule_offset)
            # The same overall offset, but differing in the base or std
            # offset (which are derived). Correct by using the rule.

            offset_index = get_rule_offset_index(offsets, first_rule_offset)
            {:at => last_defined[:at], :offset => offset_index}
          else
            raise InvalidZoneinfoFile, "The first offset indicated by the POSIX-style TZ string did not match the final defined offset in file '#{file.path}'."
          end
        end
      end

      # Apply the rules from the TZ string when there were defined transitions.
      # Checks for a matching offset with the last transition. Redefines the
      # last transition if required and if the rules don't specific a constant
      # offset, generates transitions until 100 years into the future (at the
      # time of loading zoneinfo_timezone_info.rb) or 2037 if limited to 32-bit
      # Times.
      def apply_rules_with_transitions(file, transitions, offsets, first_offset_index, rules)
        last_defined = transitions[-1]

        if rules.kind_of?(TimezoneOffset)
          transitions[-1] = validate_and_fix_last_defined_transition_offset(file, offsets, last_defined, rules)
        else
          previous_offset_index = transitions.length > 1 ? transitions[-2][:offset] : first_offset_index
          previous_offset = offsets[previous_offset_index]
          last_year = (Time.at(last_defined[:at]).utc + previous_offset[:utc_total_offset]).year

          if last_year <= GENERATE_UP_TO
            generated = rules.transitions(last_year).find_all {|t| t.at > last_defined[:at] } +
              (last_year + 1).upto(GENERATE_UP_TO).map {|y| rules.transitions(y) }.flatten

            unless generated.empty?
              transitions[-1] = validate_and_fix_last_defined_transition_offset(file, offsets, last_defined, generated[0].previous_offset)
              rule_offset_indexes = get_rule_offset_indexes(offsets, rules)
              transitions.concat(convert_transitions_to_hashes(rule_offset_indexes, generated))
            end
          end
        end
      end

      # Defines an offset for the timezone based on the given index and offset
      # Hash.
      def define_offset(index, offset)
        utc_total_offset = offset[:utc_total_offset]
        utc_offset = offset[:utc_offset]

        if utc_offset
          # DST offset with base utc_offset derived by derive_offsets.
          std_offset = utc_total_offset - utc_offset
        elsif offset[:is_dst]
          # DST offset unreferenced by a transition (offset in use before the
          # first transition). No derived base UTC offset, so assume 1 hour
          # DST.
          utc_offset = utc_total_offset - 3600
          std_offset = 3600
        else
          # Non-DST offset.
          utc_offset = utc_total_offset
          std_offset = 0
        end

        offset index, utc_offset, std_offset, offset[:abbr].untaint.to_sym
      end
      
      # Parses a zoneinfo file and intializes the DataTimezoneInfo structures.
      def parse(file, posix_tz_parser)
        magic, version, ttisutccnt, ttisstdcnt, leapcnt, timecnt, typecnt, charcnt =
          check_read(file, 44).unpack('a4 a x15 NNNNNN')

        if magic != 'TZif'
          raise InvalidZoneinfoFile, "The file '#{file.path}' does not start with the expected header."
        end

        if version == '2' || version == '3'
          # Skip the first 32-bit section and read the header of the second
          # 64-bit section. The 64-bit section is always used even if the
          # runtime platform doesn't support 64-bit timestamps. In "slim" format
          # zoneinfo files the 32-bit section will be empty.
          file.seek(timecnt * 5 + typecnt * 6 + charcnt + leapcnt * 8 + ttisstdcnt + ttisutccnt, IO::SEEK_CUR)
          
          prev_version = version
          
          magic, version, ttisutccnt, ttisstdcnt, leapcnt, timecnt, typecnt, charcnt =
            check_read(file, 44).unpack('a4 a x15 NNNNNN')
            
          unless magic == 'TZif' && (version == prev_version)
            raise InvalidZoneinfoFile, "The file '#{file.path}' contains an invalid 64-bit section header."
          end
          
          using_64bit = true
        elsif version != '3' && version != '2' && version != "\0"
          raise InvalidZoneinfoFile, "The file '#{file.path}' contains a version of the zoneinfo format that is not currently supported."
        else
          using_64bit = false
        end
        
        unless leapcnt == 0
          raise InvalidZoneinfoFile, "The zoneinfo file '#{file.path}' contains leap second data. TZInfo requires zoneinfo files that omit leap seconds."
        end
        
        transitions = []
        
        if using_64bit
          timecnt.times do |i|
            high, low = check_read(file, 8).unpack('NN'.freeze)
            transition_time = make_signed_int64(high, low)
            transitions << {:at => transition_time}          
          end
        else
          timecnt.times do |i|
            transition_time = make_signed_int32(check_read(file, 4).unpack('N'.freeze)[0])
            transitions << {:at => transition_time}          
          end
        end
        
        timecnt.times do |i|
          localtime_type = check_read(file, 1).unpack('C'.freeze)[0]
          transitions[i][:offset] = localtime_type
        end
        
        offsets = []
        
        typecnt.times do |i|
          gmtoff, isdst, abbrind = check_read(file, 6).unpack('NCC'.freeze)
          gmtoff = make_signed_int32(gmtoff)
          isdst = isdst == 1
          offset = {:utc_total_offset => gmtoff, :is_dst => isdst, :abbr_index => abbrind}
          
          unless isdst
            offset[:utc_offset] = gmtoff
          end
          
          offsets << offset
        end
        
        abbrev = check_read(file, charcnt)

        if using_64bit
          # Skip to the POSIX-style TZ string.
          file.seek(ttisstdcnt + ttisutccnt, IO::SEEK_CUR) # + leapcnt * 8, but leapcnt is checked above and guaranteed to be 0.
          tz_string_start = check_read(file, 1)
          raise InvalidZoneinfoFile, "Expected newline starting POSIX-style TZ string in file '#{file.path}'." unless tz_string_start == "\n"
          tz_string = RubyCoreSupport.force_encoding(file.readline("\n"), 'UTF-8')
          raise InvalidZoneinfoFile, "Expected newline ending POSIX-style TZ string in file '#{file.path}'." unless tz_string.chomp!("\n")

          begin
            rules = posix_tz_parser.parse(tz_string)
          rescue InvalidPosixTimeZone => e
            raise InvalidZoneinfoFile, "Failed to parse POSIX-style TZ string in file '#{file.path}': #{e}"
          end
        else
          rules = nil
        end

        offsets.each do |o|
          abbrev_start = o[:abbr_index]         
          raise InvalidZoneinfoFile, "Abbreviation index is out of range in file '#{file.path}'" unless abbrev_start < abbrev.length
          
          abbrev_end = abbrev.index("\0", abbrev_start)
          raise InvalidZoneinfoFile, "Missing abbreviation null terminator in file '#{file.path}'" unless abbrev_end

          o[:abbr] = RubyCoreSupport.force_encoding(abbrev[abbrev_start...abbrev_end], 'UTF-8')
        end
        
        transitions.each do |t|
          if t[:offset] < 0 || t[:offset] >= offsets.length
            raise InvalidZoneinfoFile, "Invalid offset referenced by transition in file '#{file.path}'."
          end
        end
        
        # Derive the offsets from standard time (std_offset).
        first_offset_index = derive_offsets(transitions, offsets)

        # Filter out transitions that are not supported by Time on this
        # platform.
        unless transitions.empty?
          if !RubyCoreSupport.time_supports_negative
            transitions = remove_unsupported_negative_transitions(transitions, 0)
          elsif !RubyCoreSupport.time_supports_64bit
            transitions = remove_unsupported_negative_transitions(transitions, -2**31)
          else
            # Ignore transitions that occur outside of a defined window. The
            # transition index cannot handle a large range of transition times.
            #
            # This is primarily intended to ignore the far in the past
            # transition added in zic 2014c (at timestamp -2**63 in zic 2014c
            # and at the approximate time of the big bang from zic 2014d).
            #
            # Assumes MIN_TIMESTAMP is less than -2**31.
            transitions = remove_unsupported_negative_transitions(transitions, MIN_TIMESTAMP)
          end

          if !RubyCoreSupport.time_supports_64bit
            i = transitions.find_index {|t| t[:at] >= 2**31 }
            had_later_transition = !!i
            transitions = transitions.first(i) if i
          else
            had_later_transition = false
          end
        end

        if rules && !had_later_transition
          if transitions.empty?
            transitions = apply_rules_without_transitions(file, offsets, first_offset_index, rules)
          else
            apply_rules_with_transitions(file, transitions, offsets, first_offset_index, rules)
          end
        end

        define_offset(first_offset_index, offsets[first_offset_index])

        used_offset_indexes = transitions.map {|t| t[:offset] }.to_set

        offsets.each_with_index do |o, i|
          define_offset(i, o) if i != first_offset_index && used_offset_indexes.include?(i)
        end
        
        # Ignore transitions that occur outside of a defined window. The
        # transition index cannot handle a large range of transition times.
        transitions.each do |t|
          at = t[:at]
          break if at >= MAX_TIMESTAMP
          time = Time.at(at).utc
          transition time.year, time.mon, t[:offset], at
        end
      end
  end
end
