# Terminal Multiplexing with tmux

**Duration:** 60 minutes  
**Learning Outcome:** o_mod3_tmux - Use tmux to create persistent terminal sessions with window and pane management. Implement session detachment/reattachment workflows for long-running tasks. Configure custom layouts and leverage tmux for remote work and pair programming.

---

## Table of Contents
1. [Introduction to Terminal Multiplexing](#introduction-to-terminal-multiplexing)
2. [tmux Fundamentals](#tmux-fundamentals)
3. [Session Management](#session-management)
4. [Window and Pane Management](#window-and-pane-management)
5. [Practical Workflows](#practical-workflows)
6. [Configuration and Customization](#configuration-and-customization)
7. [Industry Skills Focus](#industry-skills-focus)

---

## Introduction to Terminal Multiplexing

### What is a Terminal Multiplexer?

A terminal multiplexer allows you to:
- Run multiple terminal sessions within a single window
- Detach from sessions and reattach later (session persistence)
- Split your terminal into multiple panes
- Manage multiple windows within a single session
- Keep processes running even after disconnection

### Why tmux for DevOps?

**Real-world scenarios where tmux is essential:**

1. **Remote Server Management**
   - Start a long-running deployment, detach, go home, reattach later
   - Keep monitoring dashboards running 24/7
   - Maintain SSH connections that survive network interruptions

2. **Development Workflows**
   - Editor in one pane, tests in another, server logs in a third
   - Monitor multiple log files simultaneously
   - Pair programming with shared sessions

3. **Production Incident Response**
   - Monitor multiple services simultaneously
   - Keep investigation commands visible while researching
   - Share your screen with other engineers during incidents

**Industry Skills Focus:**
> System administrators, DevOps engineers, and SREs use tmux daily. It's a fundamental productivity tool for anyone managing remote servers or complex deployments. Companies like Netflix, Google, and Amazon expect engineers to be proficient with terminal multiplexers.

---

## tmux Fundamentals

### Installation

**macOS:**
```bash
brew install tmux
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install tmux
```

**Linux (RHEL/CentOS):**
```bash
sudo yum install tmux
```

### Basic Concepts

tmux has a hierarchical structure:

```
Session (named collection of work)
  └── Window (like a tab in a browser)
        └── Pane (split section within a window)
```

**Terminology:**
- **Session**: A collection of windows, can be detached and reattached
- **Window**: Like a tab, each window occupies the full terminal
- **Pane**: A split section within a window
- **Prefix Key**: The key combination that tells tmux you're issuing a command (default: `Ctrl+b`)

### The Prefix Key

All tmux commands start with the **prefix key** (default `Ctrl+b`), followed by another key.

**Example:** To split a pane horizontally:
1. Press `Ctrl+b` (hold Ctrl, press b)
2. Release both keys
3. Press `%`

We write this as: `Ctrl+b %`

---

## Session Management

### Creating Sessions

**Start a new session:**
```bash
tmux
```

**Start a named session:**
```bash
tmux new -s development
tmux new -s deployment
tmux new -s monitoring
```

**Why name sessions?**
- Easy to identify and reconnect
- Professional organization of different tasks
- Essential when managing multiple projects

### Detaching and Attaching

**Detach from current session:**
- `Ctrl+b d` (detach)
- Or: `Ctrl+b D` (choose which session to detach)

**List running sessions:**
```bash
tmux ls
# or
tmux list-sessions
```

**Output example:**
```
development: 3 windows (created Sat Feb 8 10:30:15 2026)
deployment: 1 window (created Sat Feb 8 11:45:22 2026)
monitoring: 2 windows (created Sat Feb 8 09:15:08 2026) (attached)
```

**Attach to a session:**
```bash
tmux attach -t development
# or shorthand:
tmux a -t development
```

**Attach to most recent session:**
```bash
tmux attach
```

### Session Management Commands

**Kill a session:**
```bash
tmux kill-session -t development
```

**Kill all sessions except current:**
```bash
tmux kill-session -a
```

**Rename current session:**
- `Ctrl+b $` (then type new name)

### Real-World Session Workflow

**Example: Starting a workday**

```bash
# Create project-specific sessions
tmux new -s webapp-dev
# In this session: run your editor, tests, dev server

# Detach with Ctrl+b d

tmux new -s log-monitoring
# In this session: tail log files, run monitoring tools

# Detach again

tmux new -s database-admin
# In this session: database console, backup scripts

# List all sessions
tmux ls
```

**Later, reconnect to specific work:**
```bash
tmux a -t webapp-dev
```

---

## Window and Pane Management

### Window Management

Windows are like tabs in a browser.

**Create new window:**
- `Ctrl+b c` (create)

**Navigate between windows:**
- `Ctrl+b n` (next window)
- `Ctrl+b p` (previous window)
- `Ctrl+b 0-9` (jump to window number)
- `Ctrl+b w` (list all windows, choose one)

**Rename current window:**
- `Ctrl+b ,` (comma)

**Close current window:**
- `Ctrl+b &` (prompts for confirmation)
- Or: Type `exit` in the shell

**Find window:**
- `Ctrl+b f` (search by window name)

### Pane Management

Panes divide a window into multiple sections.

**Split panes:**
- `Ctrl+b %` (split vertically - left/right)
- `Ctrl+b "` (split horizontally - top/bottom)

**Navigate between panes:**
- `Ctrl+b ←` (move to left pane)
- `Ctrl+b →` (move to right pane)
- `Ctrl+b ↑` (move to pane above)
- `Ctrl+b ↓` (move to pane below)
- `Ctrl+b o` (cycle through panes)
- `Ctrl+b ;` (toggle between current and previous pane)

**Resize panes:**
- `Ctrl+b Ctrl+←` (shrink pane left)
- `Ctrl+b Ctrl+→` (grow pane right)
- `Ctrl+b Ctrl+↑` (grow pane up)
- `Ctrl+b Ctrl+↓` (shrink pane down)

**Pane layouts:**
- `Ctrl+b Space` (cycle through preset layouts)
- `Ctrl+b Alt+1` (even horizontal layout)
- `Ctrl+b Alt+2` (even vertical layout)
- `Ctrl+b Alt+3` (main horizontal layout)
- `Ctrl+b Alt+4` (main vertical layout)
- `Ctrl+b Alt+5` (tiled layout)

**Close pane:**
- `Ctrl+b x` (prompts for confirmation)
- Or: Type `exit` in the shell

**Zoom pane (full screen toggle):**
- `Ctrl+b z` (zoom in/out on current pane)

**Convert pane to window:**
- `Ctrl+b !` (break pane into its own window)

---

## Practical Workflows

### Workflow 1: Full-Stack Development

**Setup:**
```bash
tmux new -s fullstack

# Create windows for each service
Ctrl+b c    # New window for frontend
Ctrl+b ,    # Rename to "frontend"
# Start: npm run dev

Ctrl+b c    # New window for backend
Ctrl+b ,    # Rename to "backend"
# Start: python app.py

Ctrl+b c    # New window for database
Ctrl+b ,    # Rename to "database"
# Start: mysql -u root -p

Ctrl+b c    # New window for logs
Ctrl+b ,    # Rename to "logs"
Ctrl+b %    # Split vertically
# Left pane: tail -f frontend.log
# Right pane: tail -f backend.log
```

**Navigate:**
- `Ctrl+b w` to see all windows
- Jump between windows with `Ctrl+b 0-3`

### Workflow 2: System Monitoring

**Setup:**
```bash
tmux new -s monitoring

# Split into 4 panes
Ctrl+b %    # Split vertically
Ctrl+b "    # Split top pane horizontally
Ctrl+b →    # Move to right pane
Ctrl+b "    # Split bottom-right horizontally

# In each pane, run:
# Top-left: htop
# Top-right: tail -f /var/log/syslog
# Bottom-left: watch -n 5 df -h
# Bottom-right: watch -n 5 ss -tuln
```

### Workflow 3: Remote Deployment

**Scenario:** Deploy an application to production server

```bash
# Local machine
tmux new -s production-deploy

# Window 1: SSH to production server
ssh user@production.example.com
cd /var/www/app
sudo systemctl stop app

# Detach to work on something else
Ctrl+b d

# Later: reattach
tmux a -t production-deploy

# Continue deployment
git pull origin main
sudo systemctl start app
sudo systemctl status app

# Monitor logs in a new pane
Ctrl+b %
sudo tail -f /var/log/app/error.log
```

**If SSH connection drops:**
- Session stays alive on remote server
- Reconnect via SSH
- `tmux a -t production-deploy`
- All processes still running!

### Workflow 4: Pair Programming

**Setup shared session:**

```bash
# Partner 1 creates session
tmux new -s pairing

# Partner 2 connects to same machine and attaches
tmux a -t pairing
```

**Both users see the same screen and can type simultaneously.**

**Industry use:**
- Remote pair programming
- Debugging production issues together
- Training new team members
- Live demonstrations

---

## Configuration and Customization

### The tmux Configuration File

tmux reads configuration from `~/.tmux.conf`

**Create your configuration:**
```bash
touch ~/.tmux.conf
```

### Recommended Configuration

**Create a functional `.tmux.conf`:**

```bash
# ~/.tmux.conf

# ==========================================
# Basic Settings
# ==========================================

# Change prefix from Ctrl+b to Ctrl+a (easier to reach)
unbind C-b
set-option -g prefix C-a
bind-key C-a send-prefix

# Start window and pane numbering at 1 (not 0)
set -g base-index 1
setw -g pane-base-index 1

# Renumber windows when one is closed
set -g renumber-windows on

# Increase scrollback buffer size
set -g history-limit 10000

# Enable mouse support (click to select panes, resize, scroll)
set -g mouse on

# ==========================================
# Key Bindings
# ==========================================

# Reload config file
bind r source-file ~/.tmux.conf \; display "Config reloaded!"

# Split panes with more intuitive keys
bind | split-window -h  # Vertical split with |
bind - split-window -v  # Horizontal split with -
unbind '"'
unbind %

# Navigate panes with vim-style keys
bind h select-pane -L
bind j select-pane -D
bind k select-pane -U
bind l select-pane -R

# Resize panes with vim-style keys (repeatable)
bind -r H resize-pane -L 5
bind -r J resize-pane -D 5
bind -r K resize-pane -U 5
bind -r L resize-pane -R 5

# ==========================================
# Visual Settings
# ==========================================

# Enable 256 colors
set -g default-terminal "screen-256color"

# Status bar styling
set -g status-style bg=colour235,fg=colour255
set -g status-left-length 40
set -g status-left "#[fg=colour76,bold]#S #[fg=colour39]| "
set -g status-right "#[fg=colour39]%d %b %R "

# Window status styling
set -g window-status-format " #I:#W "
set -g window-status-current-format " #I:#W "
set -g window-status-current-style bg=colour39,fg=colour235,bold

# Pane border styling
set -g pane-border-style fg=colour238
set -g pane-active-border-style fg=colour39

# ==========================================
# Copy Mode (Vim-style)
# ==========================================

# Enter copy mode with Ctrl+a [
bind [ copy-mode
setw -g mode-keys vi

# Vim-style copy-paste
bind-key -T copy-mode-vi v send-keys -X begin-selection
bind-key -T copy-mode-vi y send-keys -X copy-selection-and-cancel

# ==========================================
# Plugins (Optional - requires TPM)
# ==========================================

# Plugin manager (install first: git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm)
# set -g @plugin 'tmux-plugins/tpm'
# set -g @plugin 'tmux-plugins/tmux-sensible'
# set -g @plugin 'tmux-plugins/tmux-resurrect'  # Save/restore sessions
# set -g @plugin 'tmux-plugins/tmux-continuum'  # Auto-save sessions

# Initialize plugin manager (keep at bottom)
# run '~/.tmux/plugins/tpm/tpm'
```

**Reload configuration:**
```bash
tmux source-file ~/.tmux.conf
```

Or from within tmux: `Ctrl+a r` (if you added the reload binding)

### Key Configuration Improvements

1. **Changed prefix to `Ctrl+a`**: Easier to reach on most keyboards
2. **Intuitive split keys**: `|` for vertical, `-` for horizontal
3. **Vim-style navigation**: `h j k l` for pane movement
4. **Mouse support**: Click to switch panes, scroll through history
5. **Better visual feedback**: Colored status bar, active pane highlighting

---

## Copy Mode and Scrolling

### Entering Copy Mode

**Purpose:** Scroll through terminal history and copy text

**Enter copy mode:**
- `Ctrl+b [` (or `Ctrl+a [` if you changed prefix)

**Navigate in copy mode:**
- `↑ ↓ ← →` (arrow keys)
- `Page Up` / `Page Down`
- `Ctrl+u` / `Ctrl+d` (half page up/down)
- `/` (search forward)
- `?` (search backward)
- `n` (next search result)
- `N` (previous search result)

**With vim-style configuration:**
- `h j k l` (move cursor)
- `w` / `b` (word forward/backward)
- `0` / `$` (start/end of line)
- `g` / `G` (top/bottom of buffer)

**Select and copy text:**
1. Enter copy mode: `Ctrl+b [`
2. Navigate to start position
3. Press `Space` to start selection
4. Navigate to end position
5. Press `Enter` to copy

**Paste copied text:**
- `Ctrl+b ]`

**Exit copy mode:**
- `q` or `Esc`

---

## Advanced Features

### Command Mode

**Enter command mode:**
- `Ctrl+b :`

**Useful commands:**
```
:new-window -n logs    # Create window named "logs"
:split-window -h       # Split horizontally
:select-layout tiled   # Apply tiled layout
:set mouse on          # Enable mouse
:setw synchronize-panes on   # Type in all panes simultaneously
:setw synchronize-panes off  # Disable synchronized typing
```

### Synchronized Panes

**Use case:** Run the same command on multiple servers

```bash
# Open multiple SSH connections in panes
Ctrl+b %    # Split
ssh server1.example.com

Ctrl+b %    # Split again
ssh server2.example.com

# Enable synchronized typing
Ctrl+b :
setw synchronize-panes on

# Now type once, command runs on all servers
sudo systemctl restart nginx

# Disable synchronized typing
Ctrl+b :
setw synchronize-panes off
```

### Session Switching

**Switch between sessions without detaching:**
- `Ctrl+b s` (list all sessions, use arrows to select)
- `Ctrl+b (` (switch to previous session)
- `Ctrl+b )` (switch to next session)

**Move window between sessions:**
```bash
# From command mode:
:move-window -t target-session:
```

---

## Troubleshooting

### Common Issues

**1. Nested tmux sessions**

Problem: Accidentally starting tmux inside tmux

Solution: Check for tmux:
```bash
if [ -z "$TMUX" ]; then
    echo "Not in tmux"
else
    echo "Already in tmux!"
fi
```

**2. Colors look wrong**

Solution: Add to `.tmux.conf`:
```bash
set -g default-terminal "screen-256color"
```

And to `.bashrc` or `.zshrc`:
```bash
export TERM=xterm-256color
```

**3. Can't scroll with mouse**

Solution: Enable mouse in `.tmux.conf`:
```bash
set -g mouse on
```

Then reload config.

**4. Lost sessions after reboot**

Problem: tmux sessions don't persist across reboots

Solution: Use tmux-resurrect plugin or save your layout as a script

**5. Prefix key not working**

Check if another program is intercepting the key combo. Try alternative prefix:
```bash
set -g prefix C-Space
```

---

## Industry Skills Focus

### Why tmux Matters in DevOps

**Job relevance:**

1. **System Administration**
   - Managing multiple production servers
   - Long-running maintenance tasks
   - Emergency incident response

2. **Cloud Engineering**
   - Managing containers and orchestration
   - Debugging distributed systems
   - Monitoring multiple environments simultaneously

3. **Site Reliability Engineering (SRE)**
   - On-call rotations and incident response
   - Maintaining persistent monitoring dashboards
   - Coordinating with teams during outages

### Real Company Practices

**Netflix:**
- Engineers use tmux for chaos engineering experiments
- Monitor multiple regions simultaneously during deployments

**GitHub:**
- SRE team uses shared tmux sessions during incidents
- Persistent monitoring of critical services

**Spotify:**
- Data engineers run long-running ETL jobs in tmux
- Detach and check progress throughout the day

### Career Advancement

**Skills that set you apart:**
- Efficient command-line workflows
- Professional incident response
- Remote collaboration capabilities
- System administration expertise

**Interview relevance:**
- Often tested in live coding interviews
- Shows professional-level Linux proficiency
- Demonstrates productivity optimization skills

---

## Hands-On Practice

### Exercise 1: Basic Session Management

1. Create a session named "practice"
2. Detach from it
3. List all sessions
4. Reattach to "practice"
5. Create a new window
6. Name it "experiment"
7. Kill the session

**Commands:**
```bash
tmux new -s practice
# Ctrl+b d
tmux ls
tmux a -t practice
# Ctrl+b c
# Ctrl+b , then type "experiment"
tmux kill-session -t practice
```

### Exercise 2: Pane Management

1. Start tmux
2. Split into 4 panes (2x2 grid)
3. Run different commands in each:
   - Top-left: `htop`
   - Top-right: `date` (repeating every second)
   - Bottom-left: `ls -la`
   - Bottom-right: `pwd`
4. Navigate between panes
5. Zoom into one pane and back
6. Close all panes

**Commands:**
```bash
tmux
# Ctrl+b %
# Ctrl+b "
# Ctrl+b → (move right)
# Ctrl+b "
# In each pane, run respective command
# Ctrl+b z (zoom toggle)
# Type exit in each pane or Ctrl+b &
```

### Exercise 3: Development Workflow

Simulate a full-stack development environment:

1. Create session "webapp"
2. Window 1: "editor" (run `vim` or `code .`)
3. Window 2: "server" - split into two panes
   - Top: Run a Python web server
   - Bottom: Monitor logs
4. Window 3: "database" (run `sqlite3` or MySQL client)
5. Window 4: "testing" (run test suite)
6. Practice switching between windows
7. Detach and reattach

### Exercise 4: Configuration

1. Create `~/.tmux.conf` with custom prefix
2. Add vim-style navigation
3. Change status bar colors
4. Add convenient split bindings
5. Reload configuration
6. Test new settings

---

## Summary

### Key Takeaways

1. **Session Persistence**: Work survives disconnections
2. **Multiplexed Workflows**: Multiple panes and windows increase productivity
3. **Professional Tool**: Used daily by DevOps engineers worldwide
4. **Customizable**: Configure to match your workflow
5. **Essential for Remote Work**: Manage servers and long-running tasks effectively

### Essential Commands Reference

**Sessions:**
```bash
tmux                    # Start new session
tmux new -s name        # Start named session
tmux ls                 # List sessions
tmux a -t name          # Attach to session
Ctrl+b d                # Detach from session
```

**Windows:**
```
Ctrl+b c                # Create window
Ctrl+b ,                # Rename window
Ctrl+b n/p              # Next/previous window
Ctrl+b 0-9              # Jump to window number
```

**Panes:**
```
Ctrl+b %                # Vertical split
Ctrl+b "                # Horizontal split
Ctrl+b arrow keys       # Navigate panes
Ctrl+b x                # Close pane
Ctrl+b z                # Zoom pane
```

**Other:**
```
Ctrl+b ?                # Show all key bindings
Ctrl+b :                # Command mode
Ctrl+b [                # Copy mode
```

---

## Next Steps

1. **Practice daily**: Use tmux for all your terminal work
2. **Customize**: Create your ideal `.tmux.conf`
3. **Explore plugins**: tmux Plugin Manager (TPM) adds powerful features
4. **Pair with other tools**: Combine with fzf, vim, git for maximum productivity
5. **Share knowledge**: Help teammates adopt tmux

### Additional Resources

- Official tmux wiki: https://github.com/tmux/tmux/wiki
- tmux Plugin Manager: https://github.com/tmux-plugins/tpm
- tmux cheat sheet: https://tmuxcheatsheet.com/
- Book: "tmux 2: Productive Mouse-Free Development"

---

**Remember:** tmux is a career-accelerating tool. Mastering it demonstrates professional-level command-line proficiency expected in DevOps roles.
