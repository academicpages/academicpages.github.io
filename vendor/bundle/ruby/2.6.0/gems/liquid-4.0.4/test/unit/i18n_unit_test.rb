require 'test_helper'

class I18nUnitTest < Minitest::Test
  include Liquid

  def setup
    @i18n = I18n.new(fixture("en_locale.yml"))
  end

  def test_simple_translate_string
    assert_equal "less is more", @i18n.translate("simple")
  end

  def test_nested_translate_string
    assert_equal "something wasn't right", @i18n.translate("errors.syntax.oops")
  end

  def test_single_string_interpolation
    assert_equal "something different", @i18n.translate("whatever", something: "different")
  end

  # def test_raises_translation_error_on_undefined_interpolation_key
  #   assert_raises I18n::TranslationError do
  #     @i18n.translate("whatever", :oopstypos => "yes")
  #   end
  # end

  def test_raises_unknown_translation
    assert_raises I18n::TranslationError do
      @i18n.translate("doesnt_exist")
    end
  end

  def test_sets_default_path_to_en
    assert_equal I18n::DEFAULT_LOCALE, I18n.new.path
  end
end
