# Graphify-Claude Integration Methods

## Method A: Local MCP Server
- Best for: private/proprietary codebases
- Code privacy: stays on local machine
- Transport: stdio
- Setup: graphify update . then claude mcp add graphify -- graphify-mcp --graph graphify-out/graph.json
- Tools exposed: query_graph, graph_impact, shortest_path, god_nodes

## Method B: Hosted Cloud Service
- Best for: teams sharing remote repositories
- Transport: HTTP (Streamable)
- Endpoint: https://api.graphify.com/mcp
- Auth: OAuth via app.graphify.com
- Setup: claude mcp add --transport http --scope user graphify https://api.graphify.com/mcp

## Method C: Quick Install via graphify install
- Best for: Claude Code CLI users
- Auto-detects: Claude Code, writes CLAUDE.md hooks
- Trigger: /graphify command inside Claude Code
- Privacy: local Tree-sitter parse, nothing leaves machine

## graphify install --platform options
claude, codex, opencode, kilo, aider, copilot, claw, droid, trae, hermes, kiro, pi, codebuddy, antigravity, antigravity-windows, cursor, gemini, amp, devin

## Graphify Signup Options
- Sign up with Google
- Sign up with GitHub  
- Sign up with GitLab
- Sign up with Email
- URL: https://app.graphify.com/signup
