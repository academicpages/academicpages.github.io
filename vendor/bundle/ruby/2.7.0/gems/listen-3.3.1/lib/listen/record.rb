# frozen_string_literal: true

require 'thread'
require 'listen/record/entry'
require 'listen/record/symlink_detector'

module Listen
  class Record
    # TODO: one Record object per watched directory?
    # TODO: deprecate

    attr_reader :root
    def initialize(directory)
      @tree = _auto_hash
      @root = directory.to_s
    end

    def add_dir(rel_path)
      return if [nil, '', '.'].include? rel_path
      @tree[rel_path] ||= {}
    end

    def update_file(rel_path, data)
      dirname, basename = Pathname(rel_path).split.map(&:to_s)
      _fast_update_file(dirname, basename, data)
    end

    def unset_path(rel_path)
      dirname, basename = Pathname(rel_path).split.map(&:to_s)
      _fast_unset_path(dirname, basename)
    end

    def file_data(rel_path)
      dirname, basename = Pathname(rel_path).split.map(&:to_s)
      if [nil, '', '.'].include? dirname
        tree[basename] ||= {}
        tree[basename].dup
      else
        tree[dirname] ||= {}
        tree[dirname][basename] ||= {}
        tree[dirname][basename].dup
      end
    end

    def dir_entries(rel_path)
      subtree =
        if [nil, '', '.'].include? rel_path.to_s
          tree
        else
          _sub_tree(rel_path)
        end

      result = {}
      subtree.each do |key, values|
        # only get data for file entries
        result[key] = values.key?(:mtime) ? values : {}
      end
      result
    end

    def _sub_tree(rel_path)
      tree.each_with_object({}) do |(path, meta), result|
        next unless path.start_with?(rel_path)

        if path == rel_path
          result.merge!(meta)
        else
          sub_path         = path.sub(%r{\A#{rel_path}/?}, '')
          result[sub_path] = meta
        end
      end
    end

    def build
      @tree = _auto_hash
      # TODO: test with a file name given
      # TODO: test other permissions
      # TODO: test with mixed encoding
      symlink_detector = SymlinkDetector.new
      remaining = ::Queue.new
      remaining << Entry.new(root, nil, nil)
      _fast_build_dir(remaining, symlink_detector) until remaining.empty?
    end

    private

    def _auto_hash
      Hash.new { |h, k| h[k] = Hash.new }
    end

    attr_reader :tree

    def _fast_update_file(dirname, basename, data)
      if [nil, '', '.'].include? dirname
        tree[basename] = (tree[basename] || {}).merge(data)
      else
        tree[dirname] ||= {}
        tree[dirname][basename] = (tree[dirname][basename] || {}).merge(data)
      end
    end

    def _fast_unset_path(dirname, basename)
      # this may need to be reworked to properly remove
      # entries from a tree, without adding non-existing dirs to the record
      if [nil, '', '.'].include? dirname
        return unless tree.key?(basename)
        tree.delete(basename)
      else
        return unless tree.key?(dirname)
        tree[dirname].delete(basename)
      end
    end

    def _fast_build_dir(remaining, symlink_detector)
      entry = remaining.pop
      children = entry.children # NOTE: children() implicitly tests if dir
      symlink_detector.verify_unwatched!(entry)
      children.each { |child| remaining << child }
      add_dir(entry.record_dir_key)
    rescue Errno::ENOTDIR
      _fast_try_file(entry)
    rescue SystemCallError, SymlinkDetector::Error
      _fast_unset_path(entry.relative, entry.name)
    end

    def _fast_try_file(entry)
      _fast_update_file(entry.relative, entry.name, entry.meta)
    rescue SystemCallError
      _fast_unset_path(entry.relative, entry.name)
    end
  end
end
