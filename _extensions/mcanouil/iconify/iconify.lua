--[[
# MIT License
#
# Copyright (c) Mickaël Canouil
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
]]

local function ensure_html_deps()
  quarto.doc.add_html_dependency({
    name = 'iconify',
    version = '2.1.0',
    scripts = {"iconify-icon.min.js"}
  })
end

local function is_empty(s)
  return s == nil or s == ''
end

local function is_valid_size(size)
  if is_empty(size) then
    return ''
  end
  local size_table = {
    ["tiny"]         = "0.5em",
    ["scriptsize"]   = "0.7em",
    ["footnotesize"] = "0.8em",
    ["small"]        = "0.9em",
    ["normalsize"]   = "1em",
    ["large"]        = "1.2em",
    ["Large"]        = "1.5em",
    ["LARGE"]        = "1.75em",
    ["huge"]         = "2em",
    ["Huge"]         = "2.5em",
    ["1x"]           = "1em",
    ["2x"]           = "2em",
    ["3x"]           = "3em",
    ["4x"]           = "4em",
    ["5x"]           = "5em",
    ["6x"]           = "6em",
    ["7x"]           = "7em",
    ["8x"]           = "8em",
    ["9x"]           = "9em",
    ["10x"]          = "10em",
    ["2xs"]          = "0.625em",
    ["xs"]           = "0.75em",
    ["sm"]           = "0.875em",
    ["lg"]           = "1.25em",
    ["xl"]           = "1.5em",
    ["2xl"]          = "2em"
  }
  for key, value in pairs(size_table) do
    if key == size then
      return 'font-size: ' .. value .. ';'
    end
  end
  return 'font-size: ' .. size .. ';'
end

return {
  ["iconify"] = function(args, kwargs)
    -- detect html (excluding epub which won't handle fa)
    if quarto.doc.is_format("html:js") then
      ensure_html_deps()
      local icon = pandoc.utils.stringify(args[1])
      local set = "fluent-emoji"

      if #args > 1 and string.find(pandoc.utils.stringify(args[2]), ":") then
        quarto.log.warning(
          'Use "set:icon" or "set icon" syntax, not both! ' ..
          'Using "set:icon" syntax and discarding first argument!'
        )
        icon = pandoc.utils.stringify(args[2])
      end

      if string.find(icon, ":") then
        set = string.sub(icon, 1, string.find(icon, ":") - 1)
        icon = string.sub(icon, string.find(icon, ":") + 1)
      elseif #args > 1 then
        set = icon
        icon = pandoc.utils.stringify(args[2])
      end

      local attributes = ' icon="' .. set .. ':' .. icon .. '"'
      local default_label = 'Icon ' .. icon .. ' from ' .. set .. ' Iconify.design set.'

      local size = is_valid_size(pandoc.utils.stringify(kwargs["size"]))
      if not is_empty(size) then
        attributes = attributes .. ' style="' .. size .. '"'
      end

      local aria_label = pandoc.utils.stringify(kwargs["label"])
      if is_empty(aria_label) then
        aria_label =  ' aria-label="' .. default_label .. '"'
      else
        aria_label =  ' aria-label="' .. aria_label .. '"'
      end

      local title = pandoc.utils.stringify(kwargs["title"])
      if is_empty(title) then
        title =  ' title="' .. default_label .. '"'
      else
        title =  ' title="' .. title .. '"'
      end

      attributes = attributes .. aria_label .. title

      local width = pandoc.utils.stringify(kwargs["width"])
      if not is_empty(width) and is_empty(size) then
        attributes = attributes .. ' width="' .. width .. '"'
      end
      local height = pandoc.utils.stringify(kwargs["height"])
      if not is_empty(height) and is_empty(size)  then
        attributes = attributes .. ' height="' .. height .. '"'
      end
      local flip = pandoc.utils.stringify(kwargs["flip"])
      if not is_empty(flip) then
        attributes = attributes .. ' flip="' .. flip.. '"'
      end
      local rotate = pandoc.utils.stringify(kwargs["rotate"])
      if not is_empty(rotate) then
        attributes = attributes .. ' rotate="' .. rotate .. '"'
      end

      return pandoc.RawInline(
        'html',
        '<iconify-icon inline=true role="img"' .. attributes .. '></iconify-icon>'
      )
    else
      return pandoc.Null()
    end
  end
}
