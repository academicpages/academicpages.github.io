// FILE: assets/graph-data.js
const graphData = {
  nodes: [
    {
      id: "domain-cs",
      label: "Computer Science",
      group: "cs",
      kind: "domain",
      description: "Algorithms, systems, machine learning, security, networking, and design practice.",
      details: [
        "Acts as the hub for CS coursework.",
        "Connects low-level systems, applied ML, and interface thinking."
      ]
    },
    {
      id: "domain-math",
      label: "Mathematics",
      group: "math",
      kind: "domain",
      description: "Quantitative reasoning, calculus, linear methods, probability, and scientific foundations.",
      details: [
        "Provides the modelling layer behind ML and computational neuroscience.",
        "Supports analytical thinking across experiments and simulations."
      ]
    },
    {
      id: "domain-bio",
      label: "Biology and Neuroscience",
      group: "bio",
      kind: "domain",
      description: "Behaviour, biology, psychology, and computational neuroscience as one connected cluster.",
      details: [
        "Anchors research interests in neuroethology and neural systems.",
        "Links coursework directly to current lab and modelling work."
      ]
    },
    {
      id: "domain-humanities",
      label: "Humanities and Practice",
      group: "humanities",
      kind: "domain",
      description: "Critical reading, context-building, environmental thinking, design sensitivity, and applied practice.",
      details: [
        "Adds writing, interpretation, and interdisciplinary breadth.",
        "Supports communication and design judgement across the portfolio."
      ]
    },
    {
      id: "cs-intro",
      label: "Introduction to Computer Science",
      group: "cs",
      kind: "course",
      description: "Foundational programming fluency and computational problem-solving.",
      details: ["Course code: CS-1102", "Introduced abstraction, logic, and disciplined debugging."]
    },
    {
      id: "cs-dsa",
      label: "Data Structures and Algorithms",
      group: "cs",
      kind: "course",
      description: "Classical data structures, graph traversal, recursion, and efficiency reasoning.",
      details: ["Course code: CS-1204", "Built algorithmic thinking for scale and representation."]
    },
    {
      id: "cs-systems",
      label: "Computer Organization and Systems",
      group: "cs",
      kind: "course",
      description: "Machine structure, memory, instruction flow, and hardware-software abstraction.",
      details: ["Course code: CS-2710", "Strengthened low-level systems reasoning."]
    },
    {
      id: "cs-ml",
      label: "Introduction to Machine Learning",
      group: "cs",
      kind: "course",
      description: "Regression, classification, optimization, and model evaluation.",
      details: ["Course code: CS-3410 / MAT-3211", "Connects statistical learning to research tooling."]
    },
    {
      id: "cs-security",
      label: "Information Security",
      group: "cs",
      kind: "course",
      description: "Threat modelling, cryptography, secure communication, and system trust.",
      details: ["Course code: CS-3610", "Added security-oriented systems reasoning."]
    },
    {
      id: "cs-networks",
      label: "Computer Networks",
      group: "cs",
      kind: "course",
      description: "Protocols, routing, transport, and reliability in networked systems.",
      details: ["Course code: CS-3620", "Expanded distributed systems vocabulary."]
    },
    {
      id: "cs-design",
      label: "Design Practices in CS",
      group: "cs",
      kind: "course",
      description: "User-centred design, prototyping, critique, and iterative problem solving.",
      details: ["Course code: CS-3810", "Supports interface and product judgement."]
    },
    {
      id: "cs-geometry",
      label: "Computational Geometry",
      group: "cs",
      kind: "course",
      description: "Spatial algorithms, convexity, intersections, and geometric reasoning in computation.",
      details: ["Course code: CS-4232", "Connects spatial modelling to algorithm design."]
    },
    {
      id: "math-qrmt",
      label: "Quantitative Reasoning and Mathematical Thinking",
      group: "math",
      kind: "course",
      description: "Estimation, modelling, and communicating quantitative arguments.",
      details: ["Course code: FC-0306", "Established a formal reasoning habit."]
    },
    {
      id: "math-calculus",
      label: "Calculus",
      group: "math",
      kind: "course",
      description: "Continuous change, rates, accumulation, and optimization.",
      details: ["Course code: MAT-1000", "Underpins modelling in science and engineering."]
    },
    {
      id: "math-discrete",
      label: "Discrete Mathematics",
      group: "math",
      kind: "course",
      description: "Logic, sets, combinatorics, proof methods, and formal structure.",
      details: ["Course code: CS-1104", "Built rigor for theoretical CS."]
    },
    {
      id: "math-linear",
      label: "Linear Algebra",
      group: "math",
      kind: "course",
      description: "Vectors, matrices, transformations, eigensystems, and state representations.",
      details: ["Course code: MAT-1001 / CS-2210", "Supports modelling and ML."]
    },
    {
      id: "math-probability",
      label: "Probability and Statistics",
      group: "math",
      kind: "course",
      description: "Distributions, inference, variance, uncertainty, and evidence under noise.",
      details: ["Course code: MAT-2020 / CS-1209 / PHY-1208", "Critical for ML and data interpretation."]
    },
    {
      id: "math-physics",
      label: "A Physics Primer",
      group: "math",
      kind: "course",
      description: "Physical intuition, approximation, and quantitative model building.",
      details: ["Course code: PHY-1220", "Reinforced scientific simplification."]
    },
    {
      id: "math-science",
      label: "Principles of Science",
      group: "math",
      kind: "course",
      description: "Scientific method, evidence, explanation, and experiment logic.",
      details: ["Course code: FC-0801", "Frames how empirical questions are structured."]
    },
    {
      id: "bio-mind-behaviour",
      label: "Mind and Behaviour",
      group: "bio",
      kind: "course",
      description: "Behavioural explanation as a bridge between action and mechanism.",
      details: ["Course code: FC-0503", "Helps frame neuroethology questions."]
    },
    {
      id: "bio-psychology",
      label: "Introduction to Psychology",
      group: "bio",
      kind: "course",
      description: "Cognitive, social, developmental, and experimental psychology.",
      details: ["Course code: PSY-1001", "Expands behaviour analysis beyond one system."]
    },
    {
      id: "bio-neuro-intro",
      label: "Introduction to Neuroscience",
      group: "bio",
      kind: "course",
      description: "Neurons, synapses, circuits, sensation, and motor control.",
      details: ["Course code: BIO-IS-2009", "Introduced the systems-level language of neuroscience."]
    },
    {
      id: "bio-evolution",
      label: "Biology I: Genetics and Evolution",
      group: "bio",
      kind: "course",
      description: "Genetics, inheritance, variation, and evolutionary reasoning.",
      details: ["Course code: BIO-1200", "Anchors biological questions in evolution."]
    },
    {
      id: "bio-comp-neuro",
      label: "Computational Neuroscience",
      group: "bio",
      kind: "course",
      description: "Neural coding, spiking models, dynamics, and simulation-oriented thinking.",
      details: ["Course code: BIO-IS-3024", "Directly links math and neuroscience."]
    },
    {
      id: "bio-advanced-neuro",
      label: "Advanced Neuroscience",
      group: "bio",
      kind: "course",
      description: "Research-facing neuroscience, literature synthesis, and mechanistic argumentation.",
      details: ["Course code: PSY-3011 / BIO-3114 / BIO-4114 / BIO-6114", "Deepened reading of primary work."]
    },
    {
      id: "hum-critical",
      label: "Introduction to Critical Thinking",
      group: "humanities",
      kind: "course",
      description: "Argument analysis, critique, evidence, and logical clarity.",
      details: ["Course code: CT-0001", "Sharpens analytical writing and evaluation."]
    },
    {
      id: "hum-civilisations",
      label: "Indian Civilisations",
      group: "humanities",
      kind: "course",
      description: "Historical context, traditions, and interpretive breadth.",
      details: ["Course code: FC-0201", "Adds long-range contextual reading."]
    },
    {
      id: "hum-great-books",
      label: "Great Books",
      group: "humanities",
      kind: "course",
      description: "Close reading, discussion, long-form interpretation, and textual care.",
      details: ["Course code: FC-0601", "Strengthens seminar-style thinking."]
    },
    {
      id: "hum-environment",
      label: "Environmental Studies",
      group: "humanities",
      kind: "course",
      description: "Ecology, sustainability, scale, and interdisciplinary environmental systems thinking.",
      details: ["Course code: FC-0102", "Connects science to public questions."]
    },
    {
      id: "hum-handmade",
      label: "HANDMADE: Sub-Continental Crafts",
      group: "humanities",
      kind: "course",
      description: "Material awareness, making, craft traditions, and embodied design judgement.",
      details: ["Course code: CVA-0046", "Adds tactile sensitivity to design practice."]
    },
    {
      id: "hum-internship",
      label: "Internship",
      group: "humanities",
      kind: "course",
      description: "Applied work, ownership, and adapting theory to real-world constraints.",
      details: ["Course code: INT-2004", "Extends classroom learning into practice."]
    },
    {
      id: "concept-grid-cells",
      label: "Grid Cells",
      group: "concept",
      kind: "concept",
      description: "Spatial coding, internal representations, and navigation.",
      details: ["Central concept in the reward-distortion model."]
    },
    {
      id: "concept-research-tooling",
      label: "Research Tooling",
      group: "concept",
      kind: "concept",
      description: "Software that directly improves analysis, annotation, and experiment workflows.",
      details: ["Recurs across zebrafish, systems, and imaging work."]
    },
    {
      id: "concept-scientific-imaging",
      label: "Scientific Imaging",
      group: "concept",
      kind: "concept",
      description: "Microscopy, imaging analysis, and visual interpretation in biological research.",
      details: ["A shared thread between wet-lab and computational work."]
    },
    {
      id: "concept-behaviour-analysis",
      label: "Behavioural Analysis",
      group: "concept",
      kind: "concept",
      description: "Quantifying and interpreting behaviour from experiments and recordings.",
      details: ["Connects neuroethology to computer vision and protocol design."]
    },
    {
      id: "concept-rl",
      label: "Reinforcement Learning",
      group: "concept",
      kind: "concept",
      description: "Learning from reward structure and action outcomes.",
      details: ["Links ML to grid-cell modelling and behavioural decision-making."]
    },
    {
      id: "project-zebrafish",
      label: "Automated Zebrafish Analysis",
      group: "project",
      kind: "project",
      description: "Computer-vision pipeline for movement analysis in zebrafish experiments.",
      details: ["Designed to reduce manual annotation.", "Supports cleaner behavioural workflows and numerical cognition studies."],
      links: [{ label: "About", url: "about.html" }]
    },
    {
      id: "project-grid",
      label: "Grid Cell Distortion Model",
      group: "project",
      kind: "project",
      description: "A reward-sensitive modelling project examining distortions in spatial coding.",
      details: ["Combines attractor reasoning with reinforcement-driven behaviour."]
    },
    {
      id: "project-disk",
      label: "Disk Analysis Tool",
      group: "project",
      kind: "project",
      description: "Asynchronous Rust and Tauri application for file-system traversal and duplicate detection.",
      details: ["Represents the systems engineering side of the portfolio."]
    },
    {
      id: "project-knot",
      label: "Knot Theory and Biology",
      group: "project",
      kind: "project",
      description: "Mathematical structure and molecular biology linked through expository and exploratory work.",
      details: ["Developed through the Math Apprenticeship Program."]
    },
    {
      id: "project-plash",
      label: "PLASH Materials Project",
      group: "project",
      kind: "project",
      description: "Early interdisciplinary work on materials, microscopy, and prototyping at IIT Bhubaneswar.",
      details: ["Used SEM, optical microscopy, and X-ray diffraction."]
    }
  ],
  edges: [
    { source: "domain-cs", target: "cs-intro", relation: "contains" },
    { source: "domain-cs", target: "cs-dsa", relation: "contains" },
    { source: "domain-cs", target: "cs-systems", relation: "contains" },
    { source: "domain-cs", target: "cs-ml", relation: "contains" },
    { source: "domain-cs", target: "cs-security", relation: "contains" },
    { source: "domain-cs", target: "cs-networks", relation: "contains" },
    { source: "domain-cs", target: "cs-design", relation: "contains" },
    { source: "domain-cs", target: "cs-geometry", relation: "contains" },
    { source: "domain-math", target: "math-qrmt", relation: "contains" },
    { source: "domain-math", target: "math-calculus", relation: "contains" },
    { source: "domain-math", target: "math-discrete", relation: "contains" },
    { source: "domain-math", target: "math-linear", relation: "contains" },
    { source: "domain-math", target: "math-probability", relation: "contains" },
    { source: "domain-math", target: "math-physics", relation: "contains" },
    { source: "domain-math", target: "math-science", relation: "contains" },
    { source: "domain-bio", target: "bio-mind-behaviour", relation: "contains" },
    { source: "domain-bio", target: "bio-psychology", relation: "contains" },
    { source: "domain-bio", target: "bio-neuro-intro", relation: "contains" },
    { source: "domain-bio", target: "bio-evolution", relation: "contains" },
    { source: "domain-bio", target: "bio-comp-neuro", relation: "contains" },
    { source: "domain-bio", target: "bio-advanced-neuro", relation: "contains" },
    { source: "domain-humanities", target: "hum-critical", relation: "contains" },
    { source: "domain-humanities", target: "hum-civilisations", relation: "contains" },
    { source: "domain-humanities", target: "hum-great-books", relation: "contains" },
    { source: "domain-humanities", target: "hum-environment", relation: "contains" },
    { source: "domain-humanities", target: "hum-handmade", relation: "contains" },
    { source: "domain-humanities", target: "hum-internship", relation: "contains" },
    { source: "cs-intro", target: "cs-dsa", relation: "related" },
    { source: "cs-intro", target: "cs-systems", relation: "related" },
    { source: "cs-intro", target: "cs-ml", relation: "related" },
    { source: "cs-intro", target: "cs-security", relation: "related" },
    { source: "cs-intro", target: "cs-networks", relation: "related" },
    { source: "cs-intro", target: "cs-design", relation: "related" },
    { source: "cs-intro", target: "cs-geometry", relation: "related" },
    { source: "cs-dsa", target: "cs-systems", relation: "related" },
    { source: "cs-dsa", target: "cs-ml", relation: "related" },
    { source: "cs-dsa", target: "cs-security", relation: "related" },
    { source: "cs-dsa", target: "cs-networks", relation: "related" },
    { source: "cs-dsa", target: "cs-design", relation: "related" },
    { source: "cs-dsa", target: "cs-geometry", relation: "related" },
    { source: "cs-systems", target: "cs-ml", relation: "related" },
    { source: "cs-systems", target: "cs-security", relation: "related" },
    { source: "cs-systems", target: "cs-networks", relation: "related" },
    { source: "cs-systems", target: "cs-design", relation: "related" },
    { source: "cs-systems", target: "cs-geometry", relation: "related" },
    { source: "cs-ml", target: "cs-security", relation: "related" },
    { source: "cs-ml", target: "cs-networks", relation: "related" },
    { source: "cs-ml", target: "cs-design", relation: "related" },
    { source: "cs-ml", target: "cs-geometry", relation: "related" },
    { source: "cs-security", target: "cs-networks", relation: "related" },
    { source: "cs-security", target: "cs-design", relation: "related" },
    { source: "cs-security", target: "cs-geometry", relation: "related" },
    { source: "cs-networks", target: "cs-design", relation: "related" },
    { source: "cs-networks", target: "cs-geometry", relation: "related" },
    { source: "cs-design", target: "cs-geometry", relation: "related" },
    { source: "math-qrmt", target: "math-calculus", relation: "related" },
    { source: "math-qrmt", target: "math-discrete", relation: "related" },
    { source: "math-qrmt", target: "math-linear", relation: "related" },
    { source: "math-qrmt", target: "math-probability", relation: "related" },
    { source: "math-qrmt", target: "math-physics", relation: "related" },
    { source: "math-qrmt", target: "math-science", relation: "related" },
    { source: "math-calculus", target: "math-discrete", relation: "related" },
    { source: "math-calculus", target: "math-linear", relation: "related" },
    { source: "math-calculus", target: "math-probability", relation: "related" },
    { source: "math-calculus", target: "math-physics", relation: "related" },
    { source: "math-calculus", target: "math-science", relation: "related" },
    { source: "math-discrete", target: "math-linear", relation: "related" },
    { source: "math-discrete", target: "math-probability", relation: "related" },
    { source: "math-discrete", target: "math-physics", relation: "related" },
    { source: "math-discrete", target: "math-science", relation: "related" },
    { source: "math-linear", target: "math-probability", relation: "related" },
    { source: "math-linear", target: "math-physics", relation: "related" },
    { source: "math-linear", target: "math-science", relation: "related" },
    { source: "math-probability", target: "math-physics", relation: "related" },
    { source: "math-probability", target: "math-science", relation: "related" },
    { source: "math-physics", target: "math-science", relation: "related" },
    { source: "bio-mind-behaviour", target: "bio-psychology", relation: "related" },
    { source: "bio-mind-behaviour", target: "bio-neuro-intro", relation: "related" },
    { source: "bio-mind-behaviour", target: "bio-evolution", relation: "related" },
    { source: "bio-mind-behaviour", target: "bio-comp-neuro", relation: "related" },
    { source: "bio-mind-behaviour", target: "bio-advanced-neuro", relation: "related" },
    { source: "bio-psychology", target: "bio-neuro-intro", relation: "related" },
    { source: "bio-psychology", target: "bio-evolution", relation: "related" },
    { source: "bio-psychology", target: "bio-comp-neuro", relation: "related" },
    { source: "bio-psychology", target: "bio-advanced-neuro", relation: "related" },
    { source: "bio-neuro-intro", target: "bio-evolution", relation: "related" },
    { source: "bio-neuro-intro", target: "bio-comp-neuro", relation: "related" },
    { source: "bio-neuro-intro", target: "bio-advanced-neuro", relation: "related" },
    { source: "bio-evolution", target: "bio-comp-neuro", relation: "related" },
    { source: "bio-evolution", target: "bio-advanced-neuro", relation: "related" },
    { source: "bio-comp-neuro", target: "bio-advanced-neuro", relation: "related" },
    { source: "hum-critical", target: "hum-civilisations", relation: "related" },
    { source: "hum-critical", target: "hum-great-books", relation: "related" },
    { source: "hum-critical", target: "hum-environment", relation: "related" },
    { source: "hum-critical", target: "hum-handmade", relation: "related" },
    { source: "hum-critical", target: "hum-internship", relation: "related" },
    { source: "hum-civilisations", target: "hum-great-books", relation: "related" },
    { source: "hum-civilisations", target: "hum-environment", relation: "related" },
    { source: "hum-civilisations", target: "hum-handmade", relation: "related" },
    { source: "hum-civilisations", target: "hum-internship", relation: "related" },
    { source: "hum-great-books", target: "hum-environment", relation: "related" },
    { source: "hum-great-books", target: "hum-handmade", relation: "related" },
    { source: "hum-great-books", target: "hum-internship", relation: "related" },
    { source: "hum-environment", target: "hum-handmade", relation: "related" },
    { source: "hum-environment", target: "hum-internship", relation: "related" },
    { source: "hum-handmade", target: "hum-internship", relation: "related" },
    { source: "project-zebrafish", target: "domain-bio", relation: "belongs to" },
    { source: "project-zebrafish", target: "bio-comp-neuro", relation: "draws on" },
    { source: "project-zebrafish", target: "concept-behaviour-analysis", relation: "uses" },
    { source: "project-zebrafish", target: "concept-scientific-imaging", relation: "uses" },
    { source: "project-zebrafish", target: "concept-research-tooling", relation: "builds" },
    { source: "project-grid", target: "domain-bio", relation: "belongs to" },
    { source: "project-grid", target: "domain-math", relation: "belongs to" },
    { source: "project-grid", target: "concept-grid-cells", relation: "models" },
    { source: "project-grid", target: "concept-rl", relation: "uses" },
    { source: "project-grid", target: "bio-comp-neuro", relation: "extends" },
    { source: "project-grid", target: "math-linear", relation: "draws on" },
    { source: "project-disk", target: "domain-cs", relation: "belongs to" },
    { source: "project-disk", target: "cs-systems", relation: "extends" },
    { source: "project-disk", target: "cs-design", relation: "extends" },
    { source: "project-disk", target: "concept-research-tooling", relation: "embodies" },
    { source: "project-knot", target: "domain-math", relation: "belongs to" },
    { source: "project-knot", target: "domain-bio", relation: "belongs to" },
    { source: "project-knot", target: "math-discrete", relation: "draws on" },
    { source: "project-knot", target: "bio-evolution", relation: "connects to" },
    { source: "project-plash", target: "domain-humanities", relation: "bridges" },
    { source: "project-plash", target: "concept-scientific-imaging", relation: "uses" },
    { source: "project-plash", target: "hum-handmade", relation: "echoes" },
    { source: "domain-cs", target: "concept-research-tooling", relation: "supports" },
    { source: "domain-bio", target: "concept-behaviour-analysis", relation: "supports" },
    { source: "domain-bio", target: "concept-scientific-imaging", relation: "supports" },
    { source: "domain-math", target: "concept-rl", relation: "supports" },
    { source: "domain-bio", target: "concept-grid-cells", relation: "supports" }
  ]
};

export default graphData;
