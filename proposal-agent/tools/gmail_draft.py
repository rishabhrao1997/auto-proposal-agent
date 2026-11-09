#!/usr/bin/env python3
"""Open a Gmail draft in your browser with the email filled in. It never sends: you review and press Send yourself.
usage: python3 tools/gmail_draft.py <to> <subject> <body_file>"""
import subprocess, sys, urllib.parse, pathlib
to, subject, body_file = sys.argv[1], sys.argv[2], sys.argv[3]
body = pathlib.Path(body_file).read_text()
url = "https://mail.google.com/mail/?view=cm&fs=1&" + urllib.parse.urlencode({"to": to, "su": subject, "body": body}, quote_via=urllib.parse.quote)
opener = {"darwin": ["open"], "win32": ["cmd", "/c", "start", ""]}.get(sys.platform, ["xdg-open"])
subprocess.run(opener + [url], check=True)
print("Draft opened in Gmail for", to, "(not sent)")
