#!/usr/bin/env python3
import os

OUT = os.path.dirname(os.path.abspath(__file__))

STYLE = """
@font-face{ font-family:"Fraunces"; font-weight:600; src:url("fonts/fraunces-600.woff2") format("woff2"); }
@font-face{ font-family:"Inter"; font-weight:700; src:url("fonts/inter-700.woff2") format("woff2"); }
:root{
  --forest:#20301F; --forest-dark:#141E13; --cream:#F5F1E6;
  --blush:#DDBBAE; --gold:#C7C05E; --oxblood:#5C2331;
  --font-display:"Fraunces", Georgia, serif;
  --font-body:"Inter", -apple-system, "Segoe UI", sans-serif;
}
*{ margin:0; padding:0; box-sizing:border-box; }
html,body{ width:1080px; height:1350px; }
body{ font-family: var(--font-body); color: var(--cream); position: relative; overflow: hidden; background: {{BG}}; }
.photo{ position:absolute; inset:0; background-image:url('{{PHOTO}}'); background-size:cover; background-position:{{POS}}; }
.scrim{ position:absolute; left:0; right:0; bottom:0; height:62%; background: linear-gradient(180deg, {{BG_T}} 0%, {{BG}} 68%); }
.mark{ position:absolute; top:44px; left:52px; font-family:var(--font-display); font-weight:600; font-size:22px; color:var(--cream); z-index:5; }
.mark span{ color:var(--gold); }
.counter{ position:absolute; top:48px; right:52px; font-weight:700; font-size:15px; letter-spacing:0.08em; color:var(--blush); z-index:5; }
.bottom{ position:absolute; left:0; right:0; bottom:0; padding:0 60px 88px; z-index:5; }
.eyebrow{ font-weight:700; font-size:14px; letter-spacing:0.2em; text-transform:uppercase; color:var(--gold); margin-bottom:14px; }
.name{ font-weight:700; font-size:52px; line-height:1.05; letter-spacing:-0.01em; color:var(--cream); }
.title{ font-weight:700; font-size:23px; color:var(--gold); margin-top:10px; }
.divider{ width:64px; height:4px; background:var(--gold); margin:20px 0; }
.tagline{ font-family:var(--font-display); font-style:italic; font-weight:500; font-size:22px; line-height:1.35; color:var(--blush); max-width:820px; }
.swipe{ position:absolute; left:0; right:0; bottom:36px; text-align:center; font-weight:700; font-size:13px; letter-spacing:0.14em; text-transform:uppercase; color:var(--blush); opacity:0.75; z-index:5; }

.cover{ position:absolute; inset:0; display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center; padding:0 80px; z-index:5; }
.cover .eyebrow{ margin-bottom:0; }
.cover .headline{ font-family:var(--font-display); font-weight:600; font-style:italic; font-size:62px; line-height:1.14; color:var(--cream); margin-top:16px; }
.cover .subline{ margin-top:20px; font-weight:700; font-size:17px; letter-spacing:0.14em; text-transform:uppercase; color:var(--blush); }
.cover .rule{ width:120px; height:3px; background:var(--gold); margin:28px auto 0; }
.cover .names{ margin-top:40px; font-weight:600; font-size:19px; line-height:1.9; color:var(--gold); }
"""

COVER_TMPL = """<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><style>{style}</style></head>
<body>
  <div class="mark">BW<span>R</span></div>
  <div class="counter">1 / 6</div>
  <div class="cover">
    <div class="eyebrow">A Historic Night For</div>
    <div class="headline">Black Women in Leadership</div>
    <div class="subline">U.S. Elections &middot; November 3, 2026</div>
    <div class="rule"></div>
    <div class="names">Keisha Lance Bottoms &middot; Juliana Stratton &middot; Stacey Plaskett<br>Letitia Plummer &middot; Letitia James</div>
  </div>
  <div class="swipe">Swipe &rarr;</div>
</body></html>
"""

SLIDE_TMPL = """<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><style>{style}</style></head>
<body>
  <div class="photo"></div>
  <div class="scrim"></div>
  <div class="mark">BW<span>R</span></div>
  <div class="counter">{num} / 6</div>
  <div class="bottom">
    <div class="eyebrow">{eyebrow}</div>
    <div class="name">{name}</div>
    <div class="title">{title}</div>
    <div class="divider"></div>
    <div class="tagline">{tagline}</div>
  </div>
</body></html>
"""

people = [
  dict(num=2, bg="var(--forest-dark)", bg_t="rgba(20,30,19,0)", photo="photos/keisha-official.jpg", pos="center 16%",
       eyebrow="First In The Nation", name="Keisha Lance Bottoms", title="Governor of Georgia",
       tagline="First Black woman elected governor of a U.S. state."),
  dict(num=3, bg="var(--oxblood)", bg_t="rgba(92,35,49,0)", photo="photos/stratton-official.jpg", pos="center 18%",
       eyebrow="Fifth In History", name="Juliana Stratton", title="U.S. Senator — Illinois",
       tagline="Fifth Black woman ever elected to the U.S. Senate."),
  dict(num=4, bg="var(--forest-dark)", bg_t="rgba(20,30,19,0)", photo="photos/plaskett-official.jpg", pos="center 10%",
       eyebrow="First In The Nation", name="Stacey Plaskett", title="Governor of the U.S. Virgin Islands",
       tagline="First Black woman elected governor of a U.S. territory."),
  dict(num=5, bg="var(--oxblood)", bg_t="rgba(92,35,49,0)", photo="photos/plummer-official.png", pos="center 13%",
       eyebrow="First In Harris County", name="Letitia Plummer", title="Harris County Judge — Texas",
       tagline="First Black woman elected Harris County judge."),
  dict(num=6, bg="var(--forest-dark)", bg_t="rgba(20,30,19,0)", photo="photos/james-official.png", pos="center 2%",
       eyebrow="Three Terms Strong", name="Letitia James", title="New York Attorney General",
       tagline="Won reelection to a third term as Attorney General."),
]

def style_for(bg, bg_t, photo, pos):
    return STYLE.replace("{{BG}}", bg).replace("{{BG_T}}", bg_t).replace("{{PHOTO}}", photo).replace("{{POS}}", pos)

with open(os.path.join(OUT, "carousel-1-cover.html"), "w") as f:
    f.write(COVER_TMPL.format(style=style_for("var(--oxblood)", "rgba(0,0,0,0)", "", "center")))

for p in people:
    html = SLIDE_TMPL.format(
        style=style_for(p["bg"], p["bg_t"], p["photo"], p["pos"]),
        num=p["num"], eyebrow=p["eyebrow"], name=p["name"], title=p["title"], tagline=p["tagline"])
    with open(os.path.join(OUT, f"carousel-{p['num']}-{p['name'].split()[-1].lower()}.html"), "w") as f:
        f.write(html)

print("done")
