# 🚀 Startup Builder

An AI-powered multi-skill toolkit that transforms startup ideas into actionable product and development plans.

Startup Builder is an open-source collection of AI Agent Skills designed to help founders, developers, and entrepreneurs move from an initial idea to a structured startup blueprint.

Instead of relying on one giant prompt, Startup Builder uses a master orchestrator and four specialist skills.

## ✨ Features

- 💡 Idea refinement and assumption validation
- 🔎 Evidence-based market and competitor research
- 📋 Product Requirements Document (PRD) generation
- 🛠️ MVP planning and engineering task breakdown
- 🔗 Multi-skill orchestration
- 📁 Markdown artifact generation
- ✅ Automated artifact evaluation
- 📊 Execution tracking and quality gates

## 🧠 Architecture

```text
                  USER IDEA
                      |
                      v
               STARTUP-BUILDER
                ORCHESTRATOR
                      |
          +-----------+-----------+
          |           |           |
          v           v           v
     IDEA-GRILLER  MARKET-RESEARCHER
          |           |
          v           v
      IDEA BRIEF   MARKET REPORT
          |           |
          +-----+-----+
                |
                v
            PRODUCT-SPEC
                |
                v
        PRODUCT REQUIREMENTS
                |
                v
            MVP-PLANNER
                |
                v
           MVP ROADMAP
                |
                v
        STARTUP BLUEPRINT
```

## 📦 Included Skills

| Skill | Responsibility |
|---|---|
| startup-builder | Coordinates the complete workflow |
| idea-griller | Refines and challenges startup ideas |
| market-researcher | Researches markets and competitors |
| product-spec | Creates product requirements |
| mvp-planner | Creates development roadmaps |

## 🚀 Installation

**Clone the repository:**

```bash
git clone https://github.com/Shubh484/startup-builder.git
```

**Navigate to your existing project:**

```bash
cd your-project
```

**Copy the skills into your project:**

```bash
mkdir -p .agents
cp -r /path/to/startup-builder/.agents/skills .agents/
```

Alternatively, copy the skills using the full path to your cloned repository.

**Open the project using Codex and check available skills:**

```text
/skills
```

**Invoke the complete workflow:**

```text
$startup-builder
```

I want to build a startup that solves a real customer problem.

Help me refine the idea, research the market, define the product,
and create an MVP development roadmap.

## 📁 Project Structure

```text
startup-builder/
│
├── .agents/
│   └── skills/
│       ├── startup-builder/
│       │   └── SKILL.md
│       ├── idea-griller/
│       │   └── SKILL.md
│       ├── market-researcher/
│       │   └── SKILL.md
│       ├── product-spec/
│       │   └── SKILL.md
│       └── mvp-planner/
│           └── SKILL.md
│
├── artifacts/
├── tests/
│   └── test_artifacts.py
│
├── README.md
└── LICENSE
```

## 🧪 Testing

Run the artifact evaluation script:

```bash
python3 tests/test_artifacts.py
```

The script checks the presence of expected output files and basic content requirements.

Note: These are structural checks, not a complete evaluation of AI reasoning or specialist invocation.

## 🛠️ Technology

- AI Agent Skills
- Markdown
- Codex
- Python 3
- Git and GitHub

## 🤝 Contributing

Contributions, suggestions, bug reports, and improvements are welcome.

Feel free to fork the repository and submit a pull request.

## 📄 License

MIT License.
