import path from 'path'
export default function getMapfile(options) {
  if (options.map && typeof options.map.annotation === 'string') {
    return `${path.dirname(options.to)}/${options.map.annotation}`
  }
  return `${options.to}.map`
}
