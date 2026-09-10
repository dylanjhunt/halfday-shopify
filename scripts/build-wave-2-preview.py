"""Build local email review artifacts. No network, profiles, tracking or sending.

The HTML under klaviyo/ contains native template tags, but still needs Klaviyo
rendering and approved inbox tests. preview/ replaces ONLY those footer tags
with visibly non-deliverable placeholders; it is not a Klaviyo renderer.
"""
import json
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "docs/wave-2"
CONTENT = json.loads((ROOT / "content.json").read_text())
for folder in ("preview", "klaviyo", "plain-text"):
    (ROOT / folder).mkdir(exist_ok=True)

def email(message, preview=False):
    p = "".join(f'<p style="margin:0 0 20px">{escape(t)}</p>' for t in message['paragraphs'])
    footer = ('<p>Halfday · Company mailing address appears here after account verification.</p>'
              '<p>Manage preferences · Unsubscribe<br>Preview labels only. No subscription actions.</p>') if preview else (
        '<p>{{ organization.name }}<br>{{ organization.full_address }}</p>'
        '<p><a href="{% manage_preferences_link %}" style="color:#004600">Manage preferences</a>'
        ' · <a href="{% unsubscribe_link %}" style="color:#004600">Unsubscribe</a></p>')
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{escape(message['subject'])}</title>
<style>body{{margin:0;padding:0}}a:focus-visible{{outline:3px solid #ff5528;outline-offset:4px}}@media(max-width:480px){{.pad{{padding:28px 24px!important}}h1{{font-size:42px!important}}}}</style></head>
<body style="background:#f4f0e4;color:#004600;font-family:Verdana,Geneva,sans-serif">
<div style="display:none;font-size:1px;line-height:1px;max-height:0;max-width:0;opacity:0;overflow:hidden;mso-hide:all">{escape(message['preheader'])}</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr><td align="center" style="padding:24px 0">
<!--[if mso]><table role="presentation" width="600"><tr><td><![endif]-->
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="max-width:600px;background:#fffdf5">
<tr><td class="pad" style="padding:30px 40px;border-bottom:2px solid #004600"><a href="https://drinkhalfday.com/" style="color:#004600;text-decoration:none;font:900 36px Georgia,serif;letter-spacing:-2px" aria-label="Halfday home">Halfday</a><p style="margin:5px 0 0;font-size:11px;letter-spacing:3px">PREBIOTIC ICED TEA</p></td></tr>
<tr><td class="pad" style="padding:38px 40px;background:#ffe700"><p style="margin:0 0 18px;font-size:12px;font-weight:bold;letter-spacing:2px;text-transform:uppercase">{escape(message['eyebrow'])}</p><h1 style="margin:0;font:700 54px/1.04 Georgia,serif;letter-spacing:-2px">{escape(message['heading'])}</h1></td></tr>
<tr><td class="pad" style="padding:36px 40px;font-size:16px;line-height:1.7">{p}
<table role="presentation" cellpadding="0" cellspacing="0" style="margin:28px 0"><tr><td bgcolor="#004600" style="text-align:center;mso-padding-alt:14px"><a href="{escape(message['url'],quote=True)}" style="display:inline-block;padding:14px;background:#004600;color:#ffffff;text-decoration:none;font-size:16px;font-weight:bold;line-height:22px">{escape(message['cta'])}</a></td></tr></table>
<p style="margin:0 0 28px"><a href="{escape(message['secondary_url'],quote=True)}" style="color:#004600;text-decoration:underline">{escape(message['secondary'])}</a></p><p style="margin:0">See you at tea time,<br>The Halfday team</p></td></tr>
<tr><td class="pad" style="padding:24px 40px;border-top:2px solid #004600;font-size:12px;line-height:1.6">{footer}<p>Questions? <a href="mailto:hey@drinkhalfday.com" style="color:#004600">hey@drinkhalfday.com</a></p></td></tr></table>
<!--[if mso]></td></tr></table><![endif]-->
</td></tr></table></body></html>'''

cards = []
for message in CONTENT['messages']:
    ident = message['id']
    (ROOT / 'klaviyo' / f'{ident}.html').write_text(email(message))
    (ROOT / 'preview' / f'{ident}.html').write_text(email(message, True))
    plain = f"Subject: {message['subject']}\nPreheader: {message['preheader']}\n\n{message['heading']}\n\n" + '\n\n'.join(message['paragraphs'])
    plain += f"\n\n{message['cta']}: {message['url']}\n{message['secondary']}: {message['secondary_url']}\n\nSee you at tea time,\nThe Halfday team\n\n{{{{ organization.name }}}}\n{{{{ organization.full_address }}}}\nManage preferences: {{% manage_preferences_link %}}\nUnsubscribe: {{% unsubscribe_link %}}\nQuestions? hey@drinkhalfday.com\n"
    (ROOT / 'plain-text' / f'{ident}.txt').write_text(plain)
    cards.append(f'<article><p class="kicker">{escape(message["name"])}</p><h2>{escape(message["subject"])}</h2><p>{escape(message["preheader"])}</p><a href="{ident}.html">Open full email →</a><iframe title="{escape(message["name"])}" src="{ident}.html" loading="lazy"></iframe></article>')

style = '''*{box-sizing:border-box}body{margin:0;background:#f4f0e4;color:#004600;font:16px/1.6 Verdana,sans-serif}header,main{max-width:1320px;margin:auto;padding:32px}header{border-bottom:2px solid #004600}h1,h2,h3{font-family:Georgia,serif;line-height:1.1}h1{font-size:clamp(40px,7vw,76px);letter-spacing:-2px;max-width:850px;margin:12px 0 24px}h2{font-size:28px}a{color:#004600;text-underline-offset:4px}a:focus-visible{outline:3px solid #ff5528;outline-offset:4px}.kicker{font-size:12px;font-weight:bold;letter-spacing:2px;text-transform:uppercase}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,350px),1fr));gap:28px}article{min-width:0}iframe{display:block;width:100%;height:1070px;border:1px solid #004600;margin-top:24px;background:#fffdf5}.note{max-width:850px}.sample{background:#ffe700;border:2px solid #004600;padding:32px;margin:28px 0}.sample h2{font-size:42px;max-width:500px;margin:0 0 20px}.sample input{width:100%;max-width:360px;padding:16px;border:1px solid #004600;background:#fffdf5;font:inherit}.sample button{padding:17px 24px;border:0;background:#004600;color:white;font:700 16px Verdana,sans-serif}.sample small{display:block;margin-top:16px;max-width:500px}nav{display:flex;gap:24px;flex-wrap:wrap}@media(max-width:480px){header,main{padding:24px}.sample{padding:24px}.sample button{display:block;margin-top:12px}.sample h2{font-size:36px}}'''
index = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Halfday · Wave 2 review</title><style>{style}</style></head><body><header><p class="kicker">Halfday / Wave 2 / Local drafts</p><h1>A clearer path from signup to tea time.</h1><p class="note">Five email drafts and a signup direction for review. No discount promises, no disputed nutrition numbers, and no live forms or tracking. These previews show browser layout, not verified inbox rendering.</p><nav><a href="#signup">Signup direction</a><a href="#emails">Email drafts</a><a href="../implementation-outline.md">Implementation outline</a><a href="../signup-and-offer.md">Both offer options</a></nav></header><main><section id="signup"><p class="kicker">Proposed email signup / no offer</p><div class="sample"><h2>Your next tea break starts here.</h2><p>Get flavor news and more from Halfday in your inbox.</p><label for="preview-email">Email address</label><br><input id="preview-email" type="email" placeholder="Your email address" disabled><button type="button" disabled>Keep me in the loop</button><small>By signing up, you agree to receive marketing emails from Halfday. You can unsubscribe at any time. <a href="https://drinkhalfday.com/policies/privacy-policy">Privacy policy</a>.</small></div><p><strong>Success copy:</strong> Thanks for joining us. Take a look at the flavors while you wait for your first email.</p><p>This is a static email-step concept. Input and button are disabled. SMS and existing consent configuration are outside this preview.</p></section><section id="emails"><h2>The email sequence</h2><p>Text comes first. Existing approved artwork can be added as supporting images during Klaviyo staging, with explicit dimensions and descriptive alt text.</p><div class="grid">{''.join(cards)}</div></section></main></body></html>'''
(ROOT / 'preview/index.html').write_text(index)
print('Built five email HTML sources, five plain-text versions, five browser previews and review index.')
