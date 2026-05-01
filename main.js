// FILE: main.js
import graphData from "./assets/graph-data.js";

const groupLabels = {
  cs: "Computer Science",
  math: "Mathematics",
  bio: "Biology and Neuroscience",
  humanities: "Humanities and Practice",
  concept: "Concepts",
  project: "Projects"
};

const graphPalette = {
  cs: "#1d1d1f",
  math: "#4f5561",
  bio: "#375f4f",
  humanities: "#8b7254",
  concept: "#5d5b88",
  project: "#8b6046"
};

function setupNav() {
  const nav = document.querySelector(".site-nav");
  const toggle = document.querySelector(".nav-toggle");
  if (!nav || !toggle) {
    return;
  }

  toggle.addEventListener("click", () => {
    const expanded = toggle.getAttribute("aria-expanded") === "true";
    toggle.setAttribute("aria-expanded", String(!expanded));
    toggle.setAttribute("aria-label", expanded ? "Open navigation menu" : "Close navigation menu");
    nav.classList.toggle("is-open", !expanded);
  });
}

function setupLightbox() {
  const dialog = document.getElementById("lightbox-dialog");
  const triggers = Array.from(document.querySelectorAll("[data-lightbox-index]"));
  if (!dialog || !triggers.length) {
    return;
  }

  const image = dialog.querySelector(".lightbox-dialog__image");
  const closeButton = dialog.querySelector(".lightbox-dialog__close");
  const prevButton = dialog.querySelector(".lightbox-dialog__nav--prev");
  const nextButton = dialog.querySelector(".lightbox-dialog__nav--next");
  let activeIndex = 0;

  const items = triggers.map((trigger) => ({
    src: trigger.getAttribute("data-lightbox-src"),
    alt: trigger.getAttribute("data-lightbox-alt")
  }));

  function render(index) {
    const item = items[index];
    if (!item) {
      return;
    }
    activeIndex = index;
    image.src = item.src;
    image.alt = item.alt;
  }

  function open(index) {
    render(index);
    if (!dialog.open) {
      dialog.showModal();
    }
  }

  function close() {
    if (dialog.open) {
      dialog.close();
    }
  }

  function step(delta) {
    const nextIndex = (activeIndex + delta + items.length) % items.length;
    render(nextIndex);
  }

  triggers.forEach((trigger, index) => {
    trigger.addEventListener("click", () => open(index));
  });

  closeButton.addEventListener("click", close);
  prevButton.addEventListener("click", () => step(-1));
  nextButton.addEventListener("click", () => step(1));

  dialog.addEventListener("click", (event) => {
    if (event.target === dialog) {
      close();
    }
  });

  dialog.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      close();
    }
    if (event.key === "ArrowLeft") {
      event.preventDefault();
      step(-1);
    }
    if (event.key === "ArrowRight") {
      event.preventDefault();
      step(1);
    }
  });
}

function setupGraph() {
  const root = document.getElementById("knowledge-graph");
  if (!root || !window.d3) {
    return;
  }

  const { d3 } = window;
  const searchInput = document.getElementById("graph-search");
  const resetButton = document.getElementById("graph-reset");
  const filterButtons = Array.from(document.querySelectorAll("[data-filter]"));
  const panelTitle = document.getElementById("graph-panel-title");
  const panelMeta = document.getElementById("graph-panel-meta");
  const panelDescription = document.getElementById("graph-panel-description");
  const panelDetails = document.getElementById("graph-panel-details");
  const panelLinks = document.getElementById("graph-panel-links");
  const panelConnections = document.getElementById("graph-panel-connections");

  const state = {
    activeId: null,
    hoverId: null,
    searchVisible: null,
    activeGroups: new Set(Object.keys(groupLabels)),
    adjacency: new Map(),
    width: 0,
    height: 540,
    simulation: null,
    svg: null,
    viewport: null,
    zoom: null,
    nodes: [],
    links: [],
    nodeSelection: null,
    linkSelection: null,
    groupLabelSelection: null
  };

  function nodeId(value) {
    return typeof value === "string" ? value : value.id;
  }

  function buildAdjacency() {
    state.adjacency = new Map();
    state.nodes.forEach((node) => {
      state.adjacency.set(node.id, []);
    });
    state.links.forEach((link) => {
      state.adjacency.get(nodeId(link.source)).push(nodeId(link.target));
      state.adjacency.get(nodeId(link.target)).push(nodeId(link.source));
    });
  }

  function neighborsOf(id) {
    return state.adjacency.get(id) || [];
  }

  function wrapLabel(label) {
    const words = label.split(" ");
    const lines = [];
    let line = "";
    words.forEach((word) => {
      const next = line ? `${line} ${word}` : word;
      if (next.length > 18 && line) {
        lines.push(line);
        line = word;
      } else {
        line = next;
      }
    });
    if (line) {
      lines.push(line);
    }
    return lines.slice(0, 3);
  }

  function defaultPanel() {
    panelTitle.textContent = "Select a node";
    panelMeta.textContent = "Hover to preview. Click to pin a node and inspect how it connects to the rest of the portfolio.";
    panelDescription.textContent = "The graph supports drag, zoom, pan, hover highlighting, and click-based detail views. It is driven by JSON and rendered with D3 from a CDN, so it remains GitHub Pages-friendly.";
    panelDetails.innerHTML = [
      "<li>Drag nodes to perturb the layout.</li>",
      "<li>Use search to focus the graph in context.</li>",
      "<li>Click a connection chip to follow relationships.</li>"
    ].join("");
    panelLinks.innerHTML = '<a class="button button--ghost" href="about.html">About</a><a class="button button--ghost" href="blog.html">Blog</a>';
    panelConnections.innerHTML = '<span class="chip">No node selected</span>';
  }

  function updatePanel(node) {
    if (!node) {
      defaultPanel();
      return;
    }

    panelTitle.textContent = node.label;
    panelMeta.textContent = `${node.kind.charAt(0).toUpperCase() + node.kind.slice(1)} · ${groupLabels[node.group] || node.group}`;
    panelDescription.textContent = node.description || "";
    panelDetails.innerHTML = (node.details || []).map((detail) => `<li>${detail}</li>`).join("");
    panelLinks.innerHTML = (node.links && node.links.length)
      ? node.links.map((link) => `<a class="button button--ghost" href="${link.url}">${link.label}</a>`).join("")
      : '<a class="button button--ghost" href="about.html">About</a>';

    const related = neighborsOf(node.id)
      .map((id) => state.nodes.find((entry) => entry.id === id))
      .filter(Boolean);

    if (!related.length) {
      panelConnections.innerHTML = '<span class="chip">No direct connections</span>';
      return;
    }

    panelConnections.innerHTML = "";
    related.forEach((entry) => {
      const button = document.createElement("button");
      button.type = "button";
      button.className = "graph-connection";
      button.textContent = entry.label;
      button.addEventListener("click", () => {
        selectNode(entry, true);
      });
      panelConnections.appendChild(button);
    });
  }

  function groupAnchor(group) {
    const anchors = {
      cs: { x: state.width * 0.22, y: state.height * 0.24 },
      math: { x: state.width * 0.78, y: state.height * 0.24 },
      bio: { x: state.width * 0.22, y: state.height * 0.74 },
      humanities: { x: state.width * 0.78, y: state.height * 0.74 },
      concept: { x: state.width * 0.5, y: state.height * 0.48 },
      project: { x: state.width * 0.5, y: state.height * 0.84 }
    };
    return anchors[group] || anchors.concept;
  }

  function computeVisibility(node) {
    if (!state.activeGroups.has(node.group)) {
      return false;
    }
    if (state.searchVisible && !state.searchVisible.has(node.id)) {
      return false;
    }
    return true;
  }

  function updateGraphState() {
    const focusId = state.activeId || state.hoverId;
    const focusSet = new Set();
    if (focusId) {
      focusSet.add(focusId);
      neighborsOf(focusId).forEach((id) => focusSet.add(id));
    }

    state.nodeSelection
      .classed("is-active", (node) => node.id === state.activeId)
      .classed("is-hovered", (node) => node.id === state.hoverId && node.id !== state.activeId)
      .classed("is-dimmed", (node) => {
        if (!computeVisibility(node)) {
          return true;
        }
        if (focusSet.size && !focusSet.has(node.id)) {
          return true;
        }
        return false;
      });

    state.linkSelection
      .classed("is-active", (link) => {
        const source = nodeId(link.source);
        const target = nodeId(link.target);
        return !!focusId && (source === focusId || target === focusId);
      })
      .classed("is-dimmed", (link) => {
        const sourceNode = state.nodes.find((node) => node.id === nodeId(link.source));
        const targetNode = state.nodes.find((node) => node.id === nodeId(link.target));
        if (!sourceNode || !targetNode) {
          return true;
        }
        if (!computeVisibility(sourceNode) || !computeVisibility(targetNode)) {
          return true;
        }
        if (focusSet.size && (!focusSet.has(sourceNode.id) || !focusSet.has(targetNode.id))) {
          return true;
        }
        return false;
      });

    state.groupLabelSelection.classed("is-dimmed", (node) => {
      if (!computeVisibility(node)) {
        return true;
      }
      if (focusSet.size && !focusSet.has(node.id)) {
        return true;
      }
      return false;
    });
  }

  function applySearch(term) {
    const query = term.trim().toLowerCase();
    if (!query) {
      state.searchVisible = null;
      updateGraphState();
      return;
    }

    const visible = new Set();
    state.nodes.forEach((node) => {
      const haystack = [node.label, node.description, node.kind, groupLabels[node.group] || node.group]
        .concat(node.details || [])
        .join(" ")
        .toLowerCase();
      if (haystack.includes(query)) {
        visible.add(node.id);
        neighborsOf(node.id).forEach((neighbor) => visible.add(neighbor));
      }
    });
    state.searchVisible = visible;
    updateGraphState();
  }

  function measureNodes() {
    state.nodeSelection.each(function each(node) {
      const group = d3.select(this);
      const text = group.select("text");
      const box = text.node().getBBox();
      node.boxWidth = Math.max(box.width + 20, node.kind === "domain" ? 124 : 108);
      node.boxHeight = Math.max(box.height + 16, 40);
      node.collisionRadius = Math.max(node.boxWidth, node.boxHeight) * 0.58;
      group.select("rect")
        .attr("x", -node.boxWidth / 2)
        .attr("y", -node.boxHeight / 2)
        .attr("width", node.boxWidth)
        .attr("height", node.boxHeight)
        .attr("rx", 14)
        .attr("ry", 14);
    });
  }

  function ticked() {
    state.linkSelection
      .attr("x1", (link) => link.source.x)
      .attr("y1", (link) => link.source.y)
      .attr("x2", (link) => link.target.x)
      .attr("y2", (link) => link.target.y);

    state.nodeSelection.attr("transform", (node) => `translate(${node.x},${node.y})`);

    state.groupLabelSelection
      .attr("x", (node) => node.x)
      .attr("y", (node) => node.y - (node.boxHeight || 40) / 2 - 10);
  }

  function selectNode(node, pin = false) {
    state.activeId = node.id;
    updatePanel(node);
    if (pin) {
      state.nodes.forEach((entry) => {
        if (entry.id !== node.id && entry._pinnedByClick) {
          entry.fx = null;
          entry.fy = null;
          entry._pinnedByClick = false;
        }
      });
      node.fx = node.x;
      node.fy = node.y;
      node._pinnedByClick = true;
    }
    updateGraphState();
  }

  function buildGraph() {
    root.innerHTML = "";
    state.width = Math.max(root.clientWidth, 640);
    state.nodes = graphData.nodes.map((node) => ({
      ...node,
      x: groupAnchor(node.group).x + (Math.random() - 0.5) * 80,
      y: groupAnchor(node.group).y + (Math.random() - 0.5) * 80
    }));
    state.links = graphData.edges.map((edge) => ({ ...edge }));
    buildAdjacency();

    state.svg = d3.select(root).append("svg")
      .attr("viewBox", `0 0 ${state.width} ${state.height}`)
      .attr("role", "img")
      .attr("aria-label", "Interactive knowledge graph");

    state.viewport = state.svg.append("g");
    state.zoom = d3.zoom().scaleExtent([0.6, 2.3]).on("zoom", (event) => {
      state.viewport.attr("transform", event.transform);
    });
    state.svg.call(state.zoom);

    state.linkSelection = state.viewport.append("g")
      .selectAll("line")
      .data(state.links)
      .join("line")
      .attr("class", "graph-link");

    state.nodeSelection = state.viewport.append("g")
      .selectAll("g")
      .data(state.nodes)
      .join("g")
      .attr("class", "graph-node")
      .on("mouseenter", (_, node) => {
        state.hoverId = node.id;
        updateGraphState();
      })
      .on("mouseleave", () => {
        state.hoverId = null;
        updateGraphState();
      })
      .on("click", (event, node) => {
        event.stopPropagation();
        selectNode(node, true);
      })
      .call(
        d3.drag()
          .on("start", (event, node) => {
            if (!event.active) {
              state.simulation.alphaTarget(0.25).restart();
            }
            node.fx = node.x;
            node.fy = node.y;
          })
          .on("drag", (event, node) => {
            node.fx = event.x;
            node.fy = event.y;
          })
          .on("end", (event) => {
            if (!event.active) {
              state.simulation.alphaTarget(0);
            }
          })
      );

    state.nodeSelection.append("rect");

    state.nodeSelection.append("text").each(function each(node) {
      const text = d3.select(this);
      const lines = wrapLabel(node.label);
      text.selectAll("tspan")
        .data(lines)
        .join("tspan")
        .attr("x", 0)
        .attr("dy", (_, index) => (index === 0 ? `${-(lines.length - 1) * 0.55}em` : "1.1em"))
        .text((line) => line);
    });

    measureNodes();

    state.groupLabelSelection = state.viewport.append("g")
      .selectAll("text")
      .data(state.nodes.filter((node) => node.kind === "domain"))
      .join("text")
      .attr("class", "graph-node-label")
      .text((node) => groupLabels[node.group] || node.label);

    state.simulation = d3.forceSimulation(state.nodes)
      .force("link", d3.forceLink(state.links).id((node) => node.id).distance((link) => {
        if (link.relation === "contains") return 90;
        if (link.relation === "related") return 72;
        return 100;
      }).strength((link) => {
        if (link.relation === "contains") return 0.24;
        if (link.relation === "related") return 0.12;
        return 0.18;
      }))
      .force("charge", d3.forceManyBody().strength((node) => {
        if (node.kind === "domain") return -1000;
        if (node.kind === "project") return -650;
        return -400;
      }))
      .force("collide", d3.forceCollide().radius((node) => node.collisionRadius || 60).iterations(2))
      .force("x", d3.forceX().x((node) => groupAnchor(node.group).x).strength((node) => node.kind === "domain" ? 0.28 : 0.12))
      .force("y", d3.forceY().y((node) => groupAnchor(node.group).y).strength((node) => node.kind === "domain" ? 0.28 : 0.12))
      .force("center", d3.forceCenter(state.width / 2, state.height / 2))
      .on("tick", ticked);

    state.svg.on("click", () => {
      state.activeId = null;
      state.nodes.forEach((node) => {
        if (node._pinnedByClick) {
          node.fx = null;
          node.fy = null;
          node._pinnedByClick = false;
        }
      });
      defaultPanel();
      updateGraphState();
      state.simulation.alpha(0.5).restart();
    });

    defaultPanel();
    updateGraphState();
  }

  filterButtons.forEach((button) => {
    button.addEventListener("click", () => {
      const key = button.getAttribute("data-filter");
      if (state.activeGroups.has(key)) {
        state.activeGroups.delete(key);
        button.classList.remove("is-active");
        button.setAttribute("aria-pressed", "false");
      } else {
        state.activeGroups.add(key);
        button.classList.add("is-active");
        button.setAttribute("aria-pressed", "true");
      }
      updateGraphState();
    });
  });

  searchInput.addEventListener("input", () => {
    applySearch(searchInput.value);
  });

  resetButton.addEventListener("click", () => {
    state.activeId = null;
    state.hoverId = null;
    state.searchVisible = null;
    searchInput.value = "";
    state.activeGroups = new Set(Object.keys(groupLabels));
    filterButtons.forEach((button) => {
      button.classList.add("is-active");
      button.setAttribute("aria-pressed", "true");
    });
    state.nodes.forEach((node) => {
      node.fx = null;
      node.fy = null;
      node._pinnedByClick = false;
    });
    defaultPanel();
    updateGraphState();
    state.svg.transition().duration(300).call(state.zoom.transform, d3.zoomIdentity);
    state.simulation.alpha(0.9).restart();
  });

  buildGraph();

  let resizeTimer = null;
  window.addEventListener("resize", () => {
    clearTimeout(resizeTimer);
    resizeTimer = window.setTimeout(() => {
      buildGraph();
    }, 120);
  });
}

setupNav();
setupLightbox();
setupGraph();
