Before do
  FileUtils.rm_rf(TEST_DIR) if File.exist?(TEST_DIR)
  FileUtils.mkdir_p(TEST_DIR)
  Dir.chdir(TEST_DIR)
end

After do
  if File.exist?(TEST_DIR)
    FileUtils.rm_rf(TEST_DIR)
    Dir.chdir(File.dirname(TEST_DIR))
  end
end
