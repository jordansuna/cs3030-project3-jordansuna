# GitHub Issues and Project Management

**Duration:** 60 minutes  
**Learning Outcome:** o_mod3_github_issues - Create and manage GitHub Issues with proper labels, assignments, and milestones. Link commits to issues using keywords (fixes #, closes #). Track automation script development through issue workflows and maintain audit trails for DevOps projects.

---

## Table of Contents
1. [Introduction to GitHub Issues](#introduction-to-github-issues)
2. [Creating and Managing Issues](#creating-and-managing-issues)
3. [Labels, Milestones, and Assignments](#labels-milestones-and-assignments)
4. [Linking Issues to Code](#linking-issues-to-code)
5. [Project Boards and Workflows](#project-boards-and-workflows)
6. [Automation with GitHub Actions](#automation-with-github-actions)  
7. [Best Practices for DevOps Teams](#best-practices-for-devops-teams)
8. [Industry Skills Focus](#industry-skills-focus)

---

## Introduction to GitHub Issues

### What are GitHub Issues?

GitHub Issues is an integrated tracking system for:
- **Bug reports**: Document defects and errors
- **Feature requests**: Plan new functionality
- **Tasks**: Track work items and to-dos
- **Documentation**: Record discussions and decisions
- **Project management**: Organize development workflows

**Think of Issues as:**
- A ticketing system integrated with your code
- A project management tool for development teams
- An audit trail for changes and decisions
- A communication hub for distributed teams

### Why GitHub Issues for DevOps?

**Real-world value:**

1. **Traceability**
   - Link every code change to a specific issue
   - Understand why changes were made
   - Maintain compliance and audit trails
   - Document incident response actions

2. **Collaboration**
   - Asynchronous communication across time zones
   - Knowledge sharing and documentation
   - Stakeholder updates and transparency
   - Team coordination on complex projects

3. **Workflow Management**
   - Track automation script development
   - Manage infrastructure changes
   - Coordinate deployments and releases
   - Prioritize bug fixes and improvements

4. **Integration**
   - Automatically close issues with commits
   - Trigger CI/CD pipelines on issue events
   - Connect to project management tools
   - Generate reports and metrics

**Industry Skills Focus:**
> Professional DevOps teams use issue tracking systems to manage all work. Whether it's JIRA, GitLab Issues, or GitHub Issues, the concepts are universal. GitHub Issues is particularly valuable because it's integrated directly with your code repository, creating seamless workflows from planning to deployment. Companies like Microsoft, Google (on public projects), and thousands of startups rely on GitHub Issues for project management.

---

## Creating and Managing Issues

### Creating Your First Issue

**Via Web Interface:**

1. Navigate to your repository
2. Click "Issues" tab
3. Click "New issue"
4. Fill in:
   - **Title**: Clear, concise description
   - **Description**: Detailed information
   - **Labels**: Categorize the issue
   - **Assignees**: Who will work on it
   - **Milestone**: What release it's for

**Example Issue:**

```markdown
Title: Implement log rotation for backup script

Description:
## Problem
The daily backup script (`backup_database.sh`) generates logs that grow unbounded, 
eventually filling disk space.

## Proposed Solution
Implement log rotation to:
- Keep last 30 days of logs
- Compress logs older than 7 days
- Delete logs older than 30 days

## Acceptance Criteria
- [ ] Logs rotate daily
- [ ] Old logs are compressed with gzip
- [ ] Logs older than 30 days are automatically deleted
- [ ] Log rotation is documented in README
- [ ] Testing shows no disk space issues

## Technical Details
- Location: `/var/log/backups/`
- Current size: 15 GB
- Expected size after implementation: < 500 MB

## Priority
High - disk space at 80% capacity
```

**Via GitHub CLI:**

```bash
# Install GitHub CLI
brew install gh  # macOS
sudo apt install gh  # Linux

# Authenticate
gh auth login

# Create issue
gh issue create \
  --title "Implement log rotation for backup script" \
  --body "See description above" \
  --label "enhancement,high-priority" \
  --assignee "@me"
```

### Issue Anatomy

**Essential components:**

1. **Title** (required)
   - Clear and descriptive
   - Use imperative mood: "Add feature" not "Adding feature"
   - Include context: "Fix timeout in deployment script"

2. **Description** (strongly recommended)
   - What's the problem?
   - Why does it matter?
   - What's the solution?
   - How to verify it's fixed?

3. **Labels** (categorization)
   - Type: bug, enhancement, documentation
   - Priority: high, medium, low
   - Status: in-progress, blocked, ready
   - Area: backend, frontend, infrastructure

4. **Assignees** (ownership)
   - Who's responsible?
   - Multiple people can be assigned

5. **Milestone** (grouping)
   - Which release/sprint?
   - Helps with planning and tracking

6. **Projects** (organization)
   - Which project board?
   - Enables kanban workflows

### Managing Issues

**List issues:**
```bash
gh issue list

# Filter by state
gh issue list --state open
gh issue list --state closed

# Filter by label
gh issue list --label bug
gh issue list --label "high-priority"

# Filter by assignee
gh issue list --assignee @me
gh issue list --assignee username
```

**View issue:**
```bash
gh issue view 42

# View in browser
gh issue view 42 --web
```

**Edit issue:**
```bash
gh issue edit 42 --title "New title"
gh issue edit 42 --add-label "bug"
gh issue edit 42 --remove-label "enhancement"
gh issue edit 42 --add-assignee username
gh issue edit 42 --milestone "v2.0"
```

**Close issue:**
```bash
gh issue close 42
gh issue close 42 --comment "Fixed in commit abc123"
```

**Reopen issue:**
```bash
gh issue reopen 42
```

**Add comment:**
```bash
gh issue comment 42 --body "Working on this now"
```

---

## Labels, Milestones, and Assignments

### Labels

Labels categorize and filter issues.

**Default labels:**
- `bug` - Something isn't working
- `documentation` - Improvements or additions to documentation
- `duplicate` - This issue or pull request already exists
- `enhancement` - New feature or request
- `good first issue` - Good for newcomers
- `help wanted` - Extra attention is needed
- `invalid` - This doesn't seem right
- `question` - Further information is requested
- `wontfix` - This will not be worked on

**Custom labels for DevOps:**

```bash
# Create labels via GitHub CLI
gh label create "infrastructure" --description "Infrastructure related" --color "0052CC"
gh label create "deployment" --description "Deployment issues" --color "D93F0B"
gh label create "monitoring" --description "Monitoring and alerting" --color "FBCA04"
gh label create "security" --description "Security concerns" --color "B60205"
gh label create "performance" --description "Performance optimization" --color "BFD4F2"
gh label create "high-priority" --description "Urgent work" --color "D93F0B"
gh label create "low-priority" --description "Can wait" --color "C5DEF5"
```

**Or via web interface:**
1. Go to Issues tab
2. Click "Labels"
3. Click "New label"

**Label strategy:**

Organize by multiple dimensions:

**Type:**
- `bug` - Defects
- `enhancement` - New features
- `task` - General work items
- `documentation` - Docs updates

**Priority:**
- `critical` - Production down
- `high` - Urgent but not emergency
- `medium` - Normal priority
- `low` - Nice to have

**Component:**
- `backend` - Server-side code
- `frontend` - Client-side code
- `infrastructure` - Servers, deployment
- `database` - Data layer
- `api` - API endpoints

**Status:**
- `in-progress` - Actively being worked on
- `blocked` - Waiting on dependency
- `needs-review` - Ready for review
- `ready` - Ready to be worked on

**Example: Multi-label issue:**
```
Issue #42: Database connection timeout in production

Labels:
- bug (type)
- high-priority (priority)
- infrastructure (component)
- database (component)
```

### Milestones

Milestones group issues for releases or sprints.

**Create milestone:**
```bash
gh api repos/:owner/:repo/milestones \
  -f title="v2.0 Release" \
  -f description="Features for version 2.0" \
  -f due_on="2026-03-01T00:00:00Z"
```

**Or via web interface:**
1. Go to Issues tab
2. Click "Milestones"
3. Click "New milestone"
4. Set title, description, due date

**Assign issue to milestone:**
```bash
gh issue edit 42 --milestone "v2.0 Release"
```

**Milestone benefits:**
- Track progress toward release
- Group related work
- Set deadlines and goals
- Generate release notes

**Example milestones:**
- `v1.0` - Initial release
- `v1.1` - Bug fix release
- `Sprint 12` - Two-week sprint
- `Q1 2026` - Quarterly planning

### Assignments

**Assign issue:**
```bash
# Assign to yourself
gh issue edit 42 --assignee @me

# Assign to others
gh issue edit 42 --assignee username

# Multiple assignees
gh issue edit 42 --add-assignee user1 --add-assignee user2
```

**Assignment best practices:**

1. **Clear ownership**: One primary assignee
2. **Collaborators**: Add others as needed
3. **Reassignment**: Update if work transfers
4. **Accountability**: Assignee responsible for closure

---

## Linking Issues to Code

### Issue References

**Mention issues in commits, PRs, and comments:**

```bash
# Simple reference (creates link)
git commit -m "Improve error handling, see #42"

# Context in body
git commit -m "Add retry logic

Implements exponential backoff for failed requests.
Related to #42 and #38"
```

**Issue mention syntax:**
- `#123` - Links to issue 123 in current repo
- `owner/repo#123` - Links to issue in different repo
- `GH-123` - Alternative syntax

### Automatic Issue Closing

**Close issues automatically with commit keywords:**

```bash
# Close single issue
git commit -m "Fix database timeout, fixes #42"

# Alternative keywords
git commit -m "Implement log rotation, closes #42"
git commit -m "Add monitoring, resolves #42"

# Close multiple issues
git commit -m "Refactor auth system

Closes #42, closes #43, fixes #44"
```

**Keywords that close issues:**
- `close`, `closes`, `closed`
- `fix`, `fixes`, `fixed`
- `resolve`, `resolves`, `resolved`

**Important:** Only closes when merged to default branch (usually `main`)

### Issue Closing Workflow

**Example workflow:**

```bash
# 1. Create issue
gh issue create --title "Add health check endpoint" --label "enhancement"
# Created issue #42

# 2. Create branch
git checkout -b feature/health-check-42

# 3. Develop with context
git commit -m "Add /health endpoint, progress on #42"
git commit -m "Add tests for health check, refs #42"

# 4. Final commit closes issue
git commit -m "Complete health check implementation

Adds /health endpoint that returns:
- API status
- Database connectivity  
- Disk space available

Fixes #42"

# 5. Push and create PR
git push origin feature/health-check-42
gh pr create --title "Add health check endpoint" --body "Closes #42"

# 6. Merge PR - issue automatically closes
```

### Cross-Repository References

**Reference issues across repositories:**

```bash
git commit -m "Update config to match myorg/infra-config#42"
```

**Use cases:**
- Infrastructure changes affecting application
- Shared library updates
- Documentation updates in separate repo

---

## Project Boards and Workflows

### GitHub Projects (Beta)

Modern project management integrated with GitHub.

**Create project:**

1. Go to repository or organization
2. Click "Projects" tab
3. Click "New project"
4. Choose template:
   - **Kanban**: To-do, In Progress, Done
   - **Bug tracking**: New, Triage, In Progress, Done
   - **Roadmap**: Timeline view

**Or use GitHub CLI:**
```bash
gh project create --owner "@me" --title "Automation Scripts"
```

### Classic Project Boards

**Create board:**

1. Repository → Projects → New project
2. Choose template:
   - Automated kanban
   - Automated kanban with reviews
   - Bug triage
3. Name and describe

**Columns (example kanban):**
- **To Do**: Planned work
- **In Progress**: Active work
- **Review**: Awaiting review
- **Done**: Completed work

**Add issues to board:**
```bash
# Via web: Drag issues to columns

# Via automation: Configure column presets
# - "To Do" for newly created issues
# - "In Progress" when assigned
# - "Done" when closed
```

### Workflow Example: Automation Script Development

**Setup:**

```
Project: "Backup Automation"

Columns:
1. Backlog
2. Ready
3. In Progress
4. Testing
5. Done

Labels:
- script (type)
- bug (type)
- enhancement (type)
- high-priority (priority)
```

**Workflow:**

```bash
# 1. Create issue for new backup feature
gh issue create \
  --title "Add MySQL backup to daily script" \
  --label "enhancement,high-priority" \
  --body "Need to include MySQL in nightly backups"
# Auto-added to "Backlog" column

# 2. Ready to work - move to "Ready", assign
gh issue edit 45 --assignee @me
# Move card to "Ready" column

# 3. Start work - move to "In Progress"
git checkout -b feature/mysql-backup-45
# Move card to "In Progress"

# 4. Develop and commit
git commit -m "Add MySQL backup function, refs #45"
git commit -m "Add error handling for MySQL backup, refs #45"

# 5. Push and create PR
git push origin feature/mysql-backup-45
gh pr create --title "Add MySQL backup" --body "Closes #45"
# Move card to "Testing"

# 6. Merge PR
gh pr merge 45
# Issue closes, card moves to "Done"
```

### Automation Rules

**Built-in automations:**

1. **When issue created** → Add to "To Do"
2. **When issue assigned** → Move to "In Progress"
3. **When PR opened** → Move linked issue to "Review"
4. **When issue closed** → Move to "Done"

**Custom automations with GitHub Actions:**

```yaml
# .github/workflows/issue-automation.yml
name: Issue Automation

on:
  issues:
    types: [labeled]

jobs:
  auto-assign:
    if: contains(github.event.issue.labels.*.name, 'high-priority')
    runs-on: ubuntu-latest
    steps:
      - name: Assign to on-call engineer
        uses: actions/github-script@v6
        with:
          script: |
            github.rest.issues.addAssignees({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              assignees: ['oncall-engineer']
            })
```

---

## Automation with GitHub Actions

### Issue-Based Workflows

**Trigger workflows on issue events:**

```yaml
# .github/workflows/issue-labeled.yml
name: Issue Labeled Actions

on:
  issues:
    types: [labeled]

jobs:
  infrastructure-alert:
    if: contains(github.event.issue.labels.*.name, 'infrastructure')
    runs-on: ubuntu-latest
    steps:
      - name: Notify infrastructure team
        env:
          SLACK_WEBHOOK: ${{ secrets.SLACK_WEBHOOK }}
        run: |
          curl -X POST $SLACK_WEBHOOK \
            -H 'Content-Type: application/json' \
            -d "{\"text\":\"New infrastructure issue: ${{ github.event.issue.html_url }}\"}"
```

### Scheduled Issue Creation

**Automatically create recurring task issues:**

```yaml
# .github/workflows/weekly-tasks.yml
name: Create Weekly Maintenance Issue

on:
  schedule:
    - cron: '0 9 * * 1'  # Every Monday at 9 AM

jobs:
  create-issue:
    runs-on: ubuntu-latest
    steps:
      - name: Create maintenance issue
        uses: actions/github-script@v6
        with:
          script: |
            const issue = await github.rest.issues.create({
              owner: context.repo.owner,
              repo: context.repo.repo,
              title: `Weekly Maintenance - ${new Date().toISOString().slice(0, 10)}`,
              body: `## Weekly Maintenance Tasks
              
              - [ ] Review backup logs
              - [ ] Check disk space on all servers
              - [ ] Update dependencies
              - [ ] Review monitoring alerts
              - [ ] Security patches
              
              Due: Friday EOD`,
              labels: ['maintenance', 'weekly-task']
            })
            console.log(`Created issue: ${issue.data.html_url}`)
```

### Issue Templates

**Create standardized issue forms:**

**`.github/ISSUE_TEMPLATE/bug_report.yml`:**
```yaml
name: Bug Report
description: File a bug report for automation scripts
title: "[Bug]: "
labels: ["bug", "needs-triage"]
assignees:
  - devops-team

body:
  - type: markdown
    attributes:
      value: |
        Thanks for taking the time to fill out this bug report!

  - type: input
    id: script
    attributes:
      label: Script Name
      description: Which script has the bug?
      placeholder: backup_database.sh
    validations:
      required: true

  - type: textarea
    id: what-happened
    attributes:
      label: What happened?
      description: Describe the bug
      placeholder: Script failed with timeout error
    validations:
      required: true

  - type: textarea
    id: expected
    attributes:
      label: Expected Behavior
      description: What should have happened?
    validations:
      required: true

  - type: textarea
    id: steps
    attributes:
      label: Steps to Reproduce
      description: How can we reproduce this?
      value: |
        1. 
        2. 
        3. 
    validations:
      required: true

  - type: textarea
    id: logs
    attributes:
      label: Relevant Logs
      description: Paste relevant log output
      render: shell

  - type: dropdown
    id: severity
    attributes:
      label: Severity
      options:
        - Critical (Production Down)
        - High (Major Feature Broken)
        - Medium (Feature Partially Works)
        - Low (Minor Issue)
    validations:
      required: true

  - type: checkboxes
    id: terms
    attributes:
      label: Checklist
      options:
        - label: I have searched existing issues
          required: true
        - label: I have included relevant logs
          required: false
```

**`.github/ISSUE_TEMPLATE/feature_request.yml`:**
```yaml
name: Feature Request  
description: Suggest an enhancement for automation scripts
title: "[Feature]: "
labels: ["enhancement"]

body:
  - type: textarea
    id: problem
    attributes:
      label: Problem Statement
      description: What problem does this solve?
    validations:
      required: true

  - type: textarea
    id: solution
    attributes:
      label: Proposed Solution
      description: How should we solve this?
    validations:
      required: true

  - type: textarea
    id: alternatives
    attributes:
      label: Alternatives Considered
      description: What other approaches did you consider?

  - type: dropdown
    id: priority
    attributes:
      label: Priority
      options:
        - High
        - Medium
        - Low
    validations:
      required: true
```

**Configure templates:**

Create `.github/ISSUE_TEMPLATE/config.yml`:
```yaml
blank_issues_enabled: false
contact_links:
  - name: Documentation
    url: https://github.com/owner/repo/wiki
    about: Check documentation first
  - name: Discussion Forum
    url: https://github.com/owner/repo/discussions
    about: Ask questions here
```

---

## Best Practices for DevOps Teams

### Issue Creation Standards

**Write good issue titles:**

❌ Bad:
- "Bug"
- "Fix thing"
- "Enhancement"

✅ Good:
- "Database connection times out after 30 seconds"
- "Add automatic log rotation to backup script"
- "Implement rate limiting for API endpoints"

**Write comprehensive descriptions:**

```markdown
## Problem
[What's wrong or what's needed?]

## Current Behavior
[What happens now?]

## Expected Behavior
[What should happen?]

## Proposed Solution
[How to fix or implement?]

## Acceptance Criteria
- [ ] Clear, testable conditions
- [ ] Specific success metrics
- [ ] Definition of "done"

## Additional Context
- Screenshots
- Log excerpts
- Related issues
- External references
```

### Linking Strategy

**Every commit should reference an issue:**

```bash
# Good commits
git commit -m "Add retry logic for API calls, refs #42"
git commit -m "Refactor error handling, fixes #42"

# Bad commits
git commit -m "Fix stuff"
git commit -m "Update files"
```

**Why?**
- Provides context for changes
- Creates audit trail
- Enables traceability
- Facilitates code review

### Label Organization

**Consistent label taxonomy:**

```
Type (mutually exclusive):
- bug
- enhancement
- task
- documentation

Priority (mutually exclusive):
- critical
- high
- medium
- low

Component (can have multiple):
- backend
- frontend
- infrastructure
- database
- api

Status (mutually exclusive):
- needs-triage
- ready
- in-progress
- blocked
- needs-review
```

**Color coding:**
- Red: Critical/bugs
- Orange: High priority
- Yellow: Warnings/monitoring
- Green: Enhancements/features
- Blue: Infrastructure/deployment
- Purple: Documentation
- Gray: Closed/wontfix

### Milestone Management

**Use milestones for:**
- Releases: "v1.0", "v1.1", "v2.0"
- Sprints: "Sprint 1", "Sprint 2"
- Quarters: "Q1 2026", "Q2 2026"
- Deadlines: "Security Audit 2026"

**Don't overload:**
- Not every issue needs a milestone
- Use backlog for unprioritized work
- Adjust milestones as priorities change

### Team Workflows

**Daily stand-up:**
```bash
# What I worked on yesterday
gh issue list --assignee @me --state closed --json number,title --jq '.[] | "#\(.number) \(.title)"'

# What I'm working on today
gh issue list --assignee @me --state open --json number,title --jq '.[] | "#\(.number) \(.title)"'
```

**Sprint planning:**
```bash
# View milestone progress
gh issue list --milestone "Sprint 12" --json number,title,state,assignees

# Assign issues
gh issue edit 42 --assignee engineer1 --milestone "Sprint 12"
```

**Release preparation:**
```bash
# List all issues in milestone
gh issue list --milestone "v1.0" --state all

# Generate release notes
gh issue list --milestone "v1.0" --state closed --json number,title --jq '.[] | "- \(.title) (#\(.number))"'
```

---

## Industry Skills Focus

### Why Issue Tracking Matters in DevOps

**Professional requirements:**

1. **Documentation and Compliance**
   - SOC 2 compliance requires change tracking
   - Security audits need issue audit trails
   - Regulatory compliance demands traceability

2. **Incident Management**
   - Track incidents from detection to resolution
   - Document root cause analysis
   - Create follow-up tasks for improvements

3. **Change Management**
   - Request and approval workflows
   - Impact assessment documentation
   - Rollback procedures

4. **Knowledge Management**
   - Organizational memory
   - Onboarding new team members
   - Historical context for decisions

### Real Company Practices

**Stripe:**
- Every production change linked to issue
- Automated issue creation from monitoring
- Incident issues with standardized format

**Shopify:**
- Feature development tracked through issues
- Post-incident review issues
- Technical debt tracked and prioritized

**GitLab:**
- Dogfooding: Uses GitLab issues extensively
- Public issue tracker for open source
- Transparent roadmap via milestones

### Career Skills

**Demonstrable competencies:**
- Professional communication
- Project management
- Technical documentation
- Workflow automation
- Team collaboration

**Interview preparation:**
- Show your GitHub projects with issues
- Demonstrate workflow understanding
- Explain traceability importance
- Discuss automation strategies

---

## Advanced Features

### Issue Forms vs YAML Templates

**Markdown templates (older):**
```markdown
---
name: Bug report
about: Create a report to help us improve
---

**Describe the bug**
A clear and concise description.

**To Reproduce**
Steps to reproduce the behavior.
```

**YAML forms (recommended):**
- Form validation
- Dropdown selections
- Required fields
- Better structure

### Saved Replies

**Create reusable responses:**

1. Go to GitHub Settings → Saved replies
2. Create templates for common responses:

```markdown
Title: "Need more information"
Body:
Thanks for reporting this! To help us investigate, could you provide:

- [ ] Script name and version
- [ ] Complete error message
- [ ] Steps to reproduce
- [ ] Environment details (OS, shell version)
```

### Issue Search Syntax

**Advanced filtering:**

```bash
# Find issues
is:issue is:open label:bug assignee:@me

# Find by author
is:issue author:username

# Find by mention
is:issue mentions:username

# Date ranges
is:issue created:>2026-01-01

# Find issues without labels
is:issue no:label

# Find issues in milestone
is:issue milestone:"v1.0"

# Combine filters
is:issue is:open label:bug,high-priority no:assignee
```

### Bulk Operations

**Via GitHub CLI:**

```bash
# Close multiple issues
gh issue list --label "wontfix" --json number --jq '.[].number' | xargs -I {} gh issue close {}

# Add label to multiple issues
gh issue list --search "database in:title" --json number --jq '.[].number' | xargs -I {} gh issue edit {} --add-label "database"

# Assign milestone to multiple issues
for issue in 42 43 44 45; do
  gh issue edit $issue --milestone "v1.0"
done
```

---

## Summary

### Key Takeaways

1. **Issues are essential** for professional development workflows
2. **Link everything**: Commits, PRs, and issues connected
3. **Use automation**: Templates, labels, project boards
4. **Maintain consistency**: Standardized processes and naming
5. **Track everything**: From bugs to features to incidents
6. **Enable collaboration**: Asynchronous communication and transparency

### Essential Commands Reference

**GitHub CLI:**
```bash
gh issue list                           # List issues
gh issue create                         # Create issue
gh issue view 42                        # View issue
gh issue edit 42                        # Modify issue
gh issue close 42                       # Close issue
gh issue comment 42 --body "text"       # Add comment
```

**Git commit keywords:**
```bash
git commit -m "Fix bug, closes #42"     # Close issue
git commit -m "Work on feature, refs #42"  # Reference issue
```

**Search syntax:**
```
is:issue is:open label:bug              # Filter issues
is:issue assignee:@me                   # Your issues
is:issue milestone:"v1.0"               # By milestone
```

---

## Next Steps

1. **Create issue templates** for your repository
2. **Establish labeling system** with your team
3. **Set up project board** for workflow visualization
4. **Configure automations** with GitHub Actions
5. **Train team** on consistent practices
6. **Link commits to issues** going forward
7. **Review and refine** your process regularly

### Additional Resources

- GitHub Issues documentation: https://docs.github.com/en/issues
- GitHub CLI manual: https://cli.github.com/manual/
- GitHub Actions for issues: https://github.com/marketplace?type=actions&query=issues
- Project management with GitHub: https://github.com/features/issues
- Issue templates: https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests

---

**Remember:** Professional DevOps engineers maintain comprehensive issue tracking. It's not overhead—it's organizational memory, compliance documentation, and team coordination. Master issue management to demonstrate professional-level project management skills.
