---
title: "Auditing 200+ WordPress Sites for WCAG 2.1 in 6 Weeks – A Playbook"
excerpt: "How I used Siteimprove and Python scripts to audit and remediate hundreds of WordPress sites."
collection: portfolio
---

Accessibility audits can be daunting, especially when faced with hundreds of websites. At the University of Texas at Arlington, I successfully audited and remediated WCAG 2.1 AA issues across 266 departmental WordPress sites in just six weeks. Here’s my step-by-step playbook to streamline your audit process.

## Week 1: Strategy & Tooling

### Identify Scope & Goals
- Clearly define WCAG 2.1 AA standards as your target.
- List and categorize all WordPress sites involved (departments, research units, events).

### Tool Setup
- Choose an auditing tool (I recommend Siteimprove for detailed reporting and automated checks).
- Set up scripts for bulk crawling and reporting.
- Integrate Python scripts to aggregate results for easy analysis.

## Week 2: Initial Audit & Categorization

### Automated Bulk Scanning
- Run Siteimprove audits across all sites.
- Extract reports on accessibility violations (alt text, color contrast, semantic HTML).

### Prioritize Issues
- Categorize issues by severity and frequency.
- Create a priority matrix focusing first on critical blockers (navigation, color contrast, screen-reader compatibility).

## Week 3: Outreach & Education

### Stakeholder Communication
- Inform site owners about upcoming changes via clear, concise emails.
- Provide simple guidelines on why WCAG compliance matters (legal, ethical, and practical perspectives).

### Training Sessions
- Host virtual workshops or Q&A sessions demonstrating common fixes (adding alt text, fixing heading hierarchies, color adjustments).

## Week 4: Mass Remediation

### Template & Theme Adjustments
- Push global CSS fixes for contrast and typography issues.
- Update common templates (navigation bars, footers) to address semantic issues.

### Script-Assisted Content Fixes
- Write and deploy Python scripts to automatically remediate repetitive issues (adding alt attributes, correcting broken ARIA tags).

## Week 5: Manual Checks & Iterative Fixes

### Human Review
- Manually audit critical user journeys (e.g., navigation, forms, multimedia content).
- Correct nuanced issues missed by automation (contextual alt text, video captioning).

### Continuous Communication
- Provide weekly update emails highlighting progress and outstanding issues.
- Celebrate compliance milestones publicly to motivate teams.

## Week 6: Final Validation & Documentation

### Re-Audit & Verify
- Run comprehensive final scans on all sites to confirm WCAG 2.1 AA compliance.
- Manually verify a random selection of pages for robust quality assurance.

### Documentation & Handoff
- Prepare comprehensive documentation summarizing audit results and remediations.
- Offer maintenance guidelines to prevent future accessibility regressions.

## Results & Learnings
- Achieved 80% compliance across 266 sites in just six weeks.
- Automation drastically accelerated remediation.
- Transparent communication was critical for stakeholder buy-in.

## Key Takeaways for Your Audit
- Leverage powerful automated tools paired with scripting.
- Early stakeholder engagement is vital.
- Balance automated and manual audits for robust accessibility.

Following this structured approach can dramatically streamline your WCAG audit, ensuring your web presence is inclusive and compliant efficiently.
