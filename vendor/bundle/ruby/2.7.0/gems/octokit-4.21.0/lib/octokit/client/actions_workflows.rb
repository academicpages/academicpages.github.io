module Octokit
  class Client
    # Methods for the Actions Workflows API
    #
    # @see https://developer.github.com/v3/actions/workflows
    module ActionsWorkflows

      # Get the workflows in a repository
      #
      # @param repo [Integer, String, Repository, Hash] A GitHub repository
      #
      # @return [Sawyer::Resource] the total count and an array of workflows
      # @see https://developer.github.com/v3/actions/workflows/#list-repository-workflows
      def workflows(repo, options = {})
        paginate "#{Repository.path repo}/actions/workflows", options
      end
      alias list_workflows workflows

      # Get single workflow in a repository
      #
      # @param repo [Integer, String, Repository, Hash] A GitHub repository
      # @param id [Integer, String] Id or file name of the workflow
      #
      # @return [Sawyer::Resource] A single workflow
      # @see https://developer.github.com/v3/actions/workflows/#get-a-workflow
      def workflow(repo, id, options = {})
        get "#{Repository.path repo}/actions/workflows/#{id}", options
      end

      # Create a workflow dispatch event
      #
      # @param repo [Integer, String, Repository, Hash] A GitHub repository
      # @param id [Integer, String] Id or file name of the workflow
      # @param ref [String] A SHA, branch name, or tag name
      #
      # @return [Boolean] True if event was dispatched, false otherwise
      # @see https://docs.github.com/en/rest/reference/actions#create-a-workflow-dispatch-event
      def workflow_dispatch(repo, id, ref, options = {})
        boolean_from_response :post, "#{Repository.path repo}/actions/workflows/#{id}/dispatches", options.merge({ ref: ref })
      end
    end
  end
end
