require 'helper.rb'

module BibTeX
  class FiltersTest < Minitest::Spec
    it 'should Filters should be singleton classes' do
      assert_equal false, Filter.respond_to?(:new)
      assert_equal Filter.instance.object_id, Filter.instance.object_id
    end

    describe 'Filters.resolve' do
      it 'should return the filter if a filter is given' do
        assert_equal Filter.instance.object_id, Filters.resolve(Filter.instance).object_id
      end

      it 'should return the parameter if it quacks like a filter' do
        f = Object.new
        def f.apply
          nil
        end
        assert_equal f.object_id, Filters.resolve(f).object_id
      end

      it 'should return the filter if there is a filter by that name' do
        class FooBar < Filter; end
        assert_equal FooBar.instance.object_id, Filters.resolve(:foobar).object_id
        assert_equal FooBar.instance.object_id, Filters.resolve('foobar').object_id
        Filter.subclasses.delete(FooBar)
      end

      it 'should return nil if there is no filter by that name' do
        assert_nil Filters.resolve(:foobar)
        assert_nil Filters.resolve('foobar')
        assert_nil Filters.resolve(nil)
      end
    end
  end
end
