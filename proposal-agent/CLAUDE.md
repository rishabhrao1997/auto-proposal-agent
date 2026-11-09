# Proposal agent
When asked to check for new calls:
1. Look in ./calls for call transcripts that don't have a proposal in ./proposals yet.
2. For each one, read the transcript and any email from the same client in ./inbox.
3. Write a 3-month plan (phases with weeks), then prices from ./rates.md (show hours and the math), then a client-ready proposal in ./proposals/<client>.md. Use only what the client said; list anything you assumed at the end.
4. Write a short email for me to review in ./outbox/<client>.md (body only): what they get, timeline, price, next step. Say the full proposal follows; don't claim anything is attached.
5. Drop it in my inbox as a Gmail draft: `python3 tools/gmail_draft.py <client email> "<subject>" outbox/<client>.md`. Never send anything; I press Send myself.
Keep it plain and specific. No filler.
