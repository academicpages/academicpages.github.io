import path from 'path'
import { DepGraph } from 'dependency-graph'

export default function createDependencyGraph() {
  const graph = new DepGraph()
  return {
    add(message) {
      message.parent = path.resolve(message.parent)
      graph.addNode(message.parent)

      if (message.type === 'dir-dependency') {
        message.dir = path.resolve(message.dir)
        graph.addNode(message.dir)
        graph.addDependency(message.parent, message.dir)
      } else {
        message.file = path.resolve(message.file)
        graph.addNode(message.file)
        graph.addDependency(message.parent, message.file)
      }

      return message
    },
    dependantsOf(node) {
      node = path.resolve(node)

      if (graph.hasNode(node)) return graph.dependantsOf(node)
      return []
    },
  }
}
