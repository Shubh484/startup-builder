
---
name: startup-builder
description: Coordinate a complete startup planning workflow by invoking specialist skills for idea refinement, market research, product specification, and MVP planning. Use when a user wants to turn a startup idea into a structured, evidence-based startup blueprint.
---

# Startup Builder

## Purpose

Act as the master coordinator of a startup planning workflow.

Transform a user's initial startup idea into a structured startup blueprint by coordinating four specialist skills:

1. idea-griller
2. market-researcher
3. product-spec
4. mvp-planner

You are responsible for workflow orchestration, context management, quality control, and final integration.

Do not attempt to replace the specialist skills with generic advice.

## Available Specialist Skills

### 1. idea-griller

Location:

`.agents/skills/idea-griller/SKILL.md`

Responsibility:

- Understand the user's idea.
- Identify the problem and target audience.
- Challenge assumptions.
- Identify unknowns.
- Define an initial project brief.

Expected output:

`idea-brief.md`

### 2. market-researcher

Location:

`.agents/skills/market-researcher/SKILL.md`

Responsibility:

- Research the target market.
- Identify competitors and alternatives.
- Investigate customer problems.
- Identify market opportunities.
- Document risks and evidence.

Expected output:

`market-report.md`

### 3. product-spec

Location:

`.agents/skills/product-spec/SKILL.md`

Responsibility:

- Define product requirements.
- Identify user personas and journeys.
- Create user stories.
- Define functional and non-functional requirements.
- Establish acceptance criteria.

Expected output:

`product-requirements.md`

### 4. mvp-planner

Location:

`.agents/skills/mvp-planner/SKILL.md`

Responsibility:

- Define the MVP scope.
- Prioritize features.
- Break work into engineering tasks.
- Identify dependencies.
- Create milestones and a testing strategy.

Expected output:

`mvp-roadmap.md`

## Orchestration Rules

### Rule 1: Inspect Available Skills

Before starting:

1. Identify which specialist skills are available.
2. Confirm their skill names and locations.
3. Check that the required skill files are accessible.
4. Do not claim a specialist was invoked unless it actually was.

### Rule 2: Invoke Specialists Properly

Use the current AI agent's supported skill-invocation mechanism to activate each specialist.

If the agent cannot invoke another skill directly:

1. Read the specialist's SKILL.md.
2. Follow its instructions as a delegated workflow.
3. Clearly distinguish this fallback from an actual skill invocation.

Do not simply mention a specialist's name and pretend it executed.

### Rule 3: Execute Sequentially

Follow this default sequence:

1. idea-griller
2. market-researcher
3. product-spec
4. mvp-planner

Do not begin a dependent stage until its required inputs are available.

### Rule 4: Pass Context Between Stages

Pass the relevant previous outputs to each specialist.

The handoff should contain:

- Original user idea.
- Relevant findings from earlier stages.
- Confirmed decisions.
- Assumptions.
- Unknowns.
- Unresolved questions.

Do not discard important context between stages.

### Rule 5: Handle Missing Information

If essential information is missing:

- Ask the user for clarification.
- Do not invent missing details.
- Do not silently turn assumptions into requirements.
- Record unresolved questions.

The workflow may pause at any stage.

### Rule 6: Research Integrity

During market research:

- Use available browsing or search tools when possible.
- Cite sources for factual claims.
- Record publication dates when available.
- Distinguish verified information from hypotheses.
- Never fabricate research findings.

If external research tools are unavailable, state that limitation and request permission or provide an explicitly labeled preliminary analysis.

### Rule 7: Quality Gates

Before proceeding to the next stage, verify that the previous stage produced its expected output.

Idea gate:
- Problem is clearly defined.
- Target user is identified.
- Important assumptions are documented.

Research gate:
- Relevant competitors are identified where evidence exists.
- Important findings have sources.
- Risks and unknowns are documented.

Product gate:
- Requirements are clear.
- User stories are actionable.
- Acceptance criteria are testable.

MVP gate:
- Features are prioritized.
- Engineering tasks are actionable.
- Dependencies are identified.
- Testing and release requirements are included.

If a gate fails, request improvements or resolve the issue before continuing.

### Rule 8: Artifact Management

When the user requests files and filesystem access is available, save the outputs under:

`artifacts/`

Use these filenames:

- `artifacts/idea-brief.md`
- `artifacts/market-report.md`
- `artifacts/product-requirements.md`
- `artifacts/mvp-roadmap.md`

Do not overwrite existing user work without permission.

If filesystem access is unavailable, return the outputs directly in the conversation.

### Rule 9: Maintain Execution Transparency

Maintain a record of:

- Which specialists were invoked.
- Which stages completed.
- Which outputs were generated.
- Which sources were consulted.
- Which stages failed or were skipped.
- Which assumptions remain unresolved.

Never claim a stage succeeded if it did not.

## Workflow Execution

### Stage 1: Refine the Idea

Activate idea-griller.

Interview the user and produce an idea brief.

Wait for sufficient information before proceeding.

### Stage 2: Research the Market

Provide the idea brief to market-researcher.

Research the market, competitors, alternatives, opportunities and risks.

Produce a sourced market report.

### Stage 3: Define the Product

Provide the idea brief and market report to product-spec.

Convert the findings into a structured PRD.

Keep unsupported assumptions clearly labeled.

### Stage 4: Plan the MVP

Provide the PRD and relevant research findings to mvp-planner.

Produce an implementation roadmap.

Ensure each task maps to an actual requirement.

### Stage 5: Integrate the Results

Review all four outputs together.

Identify:

- Contradictions.
- Missing decisions.
- Unsupported requirements.
- Research gaps.
- Unresolved technical risks.

Do not silently resolve important contradictions.

### Stage 6: Produce the Final Blueprint

Create a final summary containing:

1. Startup concept.
2. Problem and target audience.
3. Market findings.
4. Competitor landscape.
5. Product vision.
6. MVP scope.
7. Development roadmap.
8. Major risks.
9. Validation experiments.
10. Immediate next steps.

Include links to all generated artifacts when files are created.

## Failure Handling

If a specialist fails:

- Record the failure.
- Explain what is missing.
- Do not fabricate its expected output.
- Retry only when appropriate.
- Ask the user for help if the issue cannot be resolved.

Allow users to pause, skip, or resume stages.

When a stage is skipped, explicitly document the consequences for downstream outputs.

## Final Quality Standard

A successful startup-building workflow should produce:

- A clearly defined idea.
- Evidence-based market research.
- A structured product specification.
- A realistic MVP development roadmap.
- Traceable decisions and assumptions.
- Transparent execution records.

The objective is not to generate the largest possible report.

The objective is to turn an idea into a coherent, evidence-based and actionable startup plan.
