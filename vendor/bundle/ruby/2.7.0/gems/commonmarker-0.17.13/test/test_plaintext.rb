require 'test_helper'

class TestPlaintext < Minitest::Test
  def setup
    @markdown = <<-MD
Hi *there*!

1. I am a numeric list.
2. I continue the list.
* Suddenly, an unordered list!
* What fun!

Okay, _enough_.

| a   | b   |
| --- | --- |
| c   | d   |
    MD
  end

  def render_doc(doc)
    CommonMarker.render_doc(doc, :DEFAULT, %i[table])
  end

  def test_to_commonmark
    compare = render_doc(@markdown).to_plaintext

    assert_equal <<-PLAINTEXT, compare
Hi there!

1.  I am a numeric list.
2.  I continue the list.

  - Suddenly, an unordered list!
  - What fun!

Okay, enough.

| a | b |
| --- | --- |
| c | d |
      PLAINTEXT
  end
end
