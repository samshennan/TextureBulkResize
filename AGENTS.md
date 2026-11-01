# Codex Token Routing

Use Codex/GPT-5.5 as the primary engineer model for this repo. Keep judgment-heavy work here: architecture, planning, debugging, security/privacy reasoning, refactors, and anything that lands in the diff.

If the local or cheap worker tool is unavailable, do not simulate routing. Continue on Codex and mention that worker routing is unavailable if it matters to the task.

## Route To Worker

When a local or cheap worker tool such as `ollamaLocalWorker` / `local_worker` backed by Ollama/Qwen is available, use it for bounded, reviewable janitor work:

- Bulk reformatting or text normalization
- Single-field or multi-field extraction from docs, logs, changelogs, or command output
- Classification, tagging, or triage that will be manually reviewed
- Templated rewrites where tone, style, shortening, or expansion is explicitly requested
- Deterministic transforms such as JSON/CSV cleanup, table shaping, label mapping, or Markdown conversion
- First-pass summarization for human or Codex review

## Keep On Codex

Never route these tasks to the worker:

- Architecture, planning, system design, or product judgment
- Shipping code changes, refactors, migrations, or anything that directly modifies repo files
- Work in unfamiliar or high-risk parts of the codebase
- Security, privacy, credentials, auth, billing, or policy-sensitive reasoning
- Ambiguous debugging, root-cause analysis, or investigation where subtle mistakes matter
- Final prose sent to users, clients, public channels, or production systems without Codex review

## Worker Checklist

Only route if all are true:

- Inputs are explicit and bounded
- Output format is explicit and easy to check
- No architectural or cross-repo implications
- Result can be reviewed in 3 minutes or less
- Required context is already in the prompt or attached artifact

Guardrails:

- Max 2 sequential worker calls per parent task
- Prefer one consolidated worker prompt over many tiny calls
- Escalate back to Codex after any unclear, failed, or low-confidence worker result
- Treat worker output as untrusted draft text
