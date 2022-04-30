# frozen_string_literal: true

module HTML
  class Pipeline
    # Public: Runs a String of content through an HTML processing pipeline,
    # providing easy access to a generated DocumentFragment.
    class BodyContent
      attr_reader :result

      # Public: Initialize a BodyContent.
      #
      # body     - A String body.
      # context  - A Hash of context options for the filters.
      # pipeline - A HTML::Pipeline object with one or more Filters.
      def initialize(body, context, pipeline)
        @body = body
        @context = context
        @pipeline = pipeline
      end

      # Public: Gets the memoized result of the body content as it passed through
      # the Pipeline.
      #
      # Returns a Hash, or something similar as defined by @pipeline.result_class.
      def result
        @result ||= @pipeline.call @body, @context
      end

      # Public: Gets the updated body from the Pipeline result.
      #
      # Returns a String or DocumentFragment.
      def output
        @output ||= result[:output]
      end

      # Public: Parses the output into a DocumentFragment.
      #
      # Returns a DocumentFragment.
      def document
        @document ||= HTML::Pipeline.parse output
      end
    end
  end
end
