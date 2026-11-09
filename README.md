# Proposal agent: your sales calls write their own proposals

After a sales call, Claude reads the transcript and the client's email, writes a 3-month plan, prices it from your rate card, drafts the proposal, and drops a ready email in your Gmail drafts. You review it and press Send. It never sends anything on its own.

## What you need
- Claude Code (claude.com/claude-code) on Mac, Windows or Linux
- A note taker that gives you the call transcript (any one: it just needs to export or save the transcript as text)
- Gmail, logged in in your browser

## Set it up (10 minutes)
1. Copy the `proposal-agent` folder anywhere, e.g. your home folder.
2. Open `rates.md` and put in your own prices.
3. After a call, save the transcript as a .txt file in `calls/` (name it with the date and client, e.g. `2026-11-09_acme_call.txt`). Save the client's email (if any) as a .txt in `inbox/`.
4. Open a terminal in the folder and run:
   `claude "Check for new sales calls and draft the proposals."`
5. A few minutes later: the proposal is in `proposals/`, and a Gmail draft opens in your browser. Read it, edit it, press Send.

## Make it check on its own
Run it on a schedule so new calls get picked up without you asking. Mac/Linux, every 30 minutes on weekdays, 9 am to 7 pm (`crontab -e`):
```
*/30 9-19 * * 1-5 cd ~/proposal-agent && claude -p "Check for new sales calls and draft the proposals." --allowedTools Read Write Edit Glob Grep "Bash(ls:*)" "Bash(python3 tools/gmail_draft.py:*)" >> log.txt 2>&1
```
If your note taker can save transcripts to a folder automatically (most can sync to Google Drive or Dropbox), point that folder at `calls/` and the whole loop runs hands-free.

## Good to know
- It only uses what the client said. Anything it had to assume is listed at the end of the proposal, so check those before sending.
- Prices come only from your `rates.md`, with the hours and math shown.
- Test it first with a made-up call (like the one in the reel) before using real client data.
