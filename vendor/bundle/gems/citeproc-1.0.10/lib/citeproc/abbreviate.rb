module CiteProc
	module Abbreviate

		attr_accessor :namespace

		def abbreviations
			@abbreviations ||= { :default => {} }
		end

		def abbreviations=(abbreviations)
			@abbreviations = case abbreviations
				when ::String
					::JSON.parse(abbreviations, :symbolize_names => true)
				when ::Hash
					abbreviations.deep_copy.symbolize_keys
				else
					raise ArgumentError, "failed to set abbreviations from #{abbreviations.inspect}"
				end
		end

		# @overload abbreviate(namespace = :default, context, word)
		def abbreviate(*arguments)
			raise ArgumentError, "wrong number of arguments (#{arguments.length} for 2..3)" unless
        (2..3).include?(arguments.length)

			arguments.unshift(namespace || :default) if arguments.length < 3

      arguments[0] = arguments[0].to_sym
      arguments[1] = arguments[1].to_sym

			abbreviations.deep_fetch(*arguments)
		end
		alias abbrev abbreviate

	end
end
