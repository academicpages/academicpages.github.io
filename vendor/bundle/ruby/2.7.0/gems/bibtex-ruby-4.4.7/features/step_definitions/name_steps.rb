When /^I parse the name "(.*)"$/ do |string|
  @name = BibTeX::Name.parse(string)
end

When /^I parse the names "(.*)"$/ do |string|
  @names = BibTeX::Names.parse(string)
end


Then /^the parts should be:$/ do |table|
  table.hashes.each do |row|
    assert_equal [row['first'], row['von'], row['last'], row['jr']],
      [@name.first, @name.von, @name.last, @name.jr].map(&:to_s)
    # row.each do |k,v|
    #   assert_equal v, @name.send(k).to_s
    # end
  end
end
