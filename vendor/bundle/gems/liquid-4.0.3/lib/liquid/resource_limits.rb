module Liquid
  class ResourceLimits
    attr_accessor :render_length, :render_score, :assign_score,
      :render_length_limit, :render_score_limit, :assign_score_limit

    def initialize(limits)
      @render_length_limit = limits[:render_length_limit]
      @render_score_limit = limits[:render_score_limit]
      @assign_score_limit = limits[:assign_score_limit]
      reset
    end

    def reached?
      (@render_length_limit && @render_length > @render_length_limit) ||
        (@render_score_limit && @render_score > @render_score_limit) ||
        (@assign_score_limit && @assign_score > @assign_score_limit)
    end

    def reset
      @render_length = @render_score = @assign_score = 0
    end
  end
end
