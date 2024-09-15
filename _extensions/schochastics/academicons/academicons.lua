-- function ensureLatexDeps()
--   quarto.doc.useLatexPackage("academicons")
-- end

local function ensureHtmlDeps()
  quarto.doc.addHtmlDependency({
    name = "academicons",
    version = "1.9.2",
    stylesheets = { "assets/css/all.css", "assets/css/size.css" }
  })
end

local function isEmpty(s)
  return s == nil or s == ''
end

local function isValidSize(size)
  local validSizes = {
    "tiny", "scriptsize", "footnotesize", "small", "normalsize",
    "large", "Large", "LARGE", "huge", "Huge",
    "1x", "2x", "3x", "4x", "5x", "6x", "7x", "8x", "9x", "10x",
    "2xs", "xs", "sm", "lg", "xl", "2xl"
  }
  for _, v in ipairs(validSizes) do
    if v == size then
      return " ai-" .. size
    end
  end
  return ""
end

return {
  ["ai"] = function(args, kwargs)
    local group = ""
    local icon = pandoc.utils.stringify(args[1])
    if #args > 1 then
      group = icon
      icon = pandoc.utils.stringify(args[2])
    end

    local size = isValidSize(pandoc.utils.stringify(kwargs["size"]))
    local color = pandoc.utils.stringify(kwargs["color"])
    if not isEmpty(color) then
      color = " style=\"color:" .. color .. "\""
      --else
      -- color = " style=\"color:" .. "black"  .. "\""
    end

    local title = pandoc.utils.stringify(kwargs["title"])
    if not isEmpty(title) then
      title = " title=\"" .. title .. "\""
    end

    -- detect html (excluding epub)
    if quarto.doc.isFormat("html:js") then
      ensureHtmlDeps()
      if isEmpty(size) then
        local csize = pandoc.utils.stringify(kwargs["size"])
        if (isEmpty(csize)) then
          csize = ""
        else
          csize = " style=\"font-size:" .. csize .. "\""
        end
        return pandoc.RawInline(
          'html',
          "<i class=\"ai " .. group .. " ai-" .. icon .. "\"" .. title .. color .. csize .. "></i>"
        )
      else
        return pandoc.RawInline(
          'html',
          "<i class=\"ai " .. group .. " ai-" .. icon .. size .. "\"" .. title .. color .. "></i>"
        )
      end
      -- detect pdf / beamer / latex / etc
      -- elseif quarto.doc.isFormat("pdf") then
      --   ensureLatexDeps()
      --   return pandoc.RawInline('tex', "\\aiIcon{" .. icon .. "}")
    else
      return pandoc.Null()
    end
  end
}
