#!/usr/bin/env python3
"""Build a standalone animated gallery and a static first-frame contact sheet."""

from __future__ import annotations

import html
import hashlib
import json
from pathlib import Path
import textwrap

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
SITE_BG = (251, 249, 246, 255)
PAPER = (255, 255, 255, 255)
INK = (30, 29, 28, 255)
MUTED = (105, 99, 94, 255)
BORDER = (230, 224, 216, 255)
CORAL = (227, 66, 60, 255)

STORIES = [
    (
        "01-helping-build-the-future.png",
        "Helping build the future",
        "Instagram Story: I’m helping build the future of real estate.",
    ),
    (
        "02-levelling-up-with-ai.png",
        "Levelling up with AI",
        "Instagram Story: I’m levelling up my business with AI.",
    ),
    (
        "03-my-business-got-an-ai-team.png",
        "My business got an AI team",
        "Instagram Story: My business just got an AI team.",
    ),
    (
        "04-purpose-built-for-real-estate.png",
        "Purpose-built for real estate",
        "Instagram Story: AI, purpose-built for real estate.",
    ),
    (
        "05-less-admin-more-agent.png",
        "Less admin. More agent.",
        "Instagram Story: Less admin. More agent.",
    ),
    (
        "06-the-work-moves-i-move-up.png",
        "The work moves. I move up.",
        "Instagram Story: The work moves. I move up.",
    ),
    (
        "07-powerful-ai-team.png",
        "A powerful AI team",
        "Instagram Story: A powerful AI team, built for real estate.",
    ),
    (
        "08-helping-shape-what-comes-next.png",
        "Helping shape what comes next",
        "Instagram Story: I’m helping shape what comes next.",
    ),
]


def versioned_asset(relative_path: str) -> str:
    """Add a content fingerprint so browsers never reuse an older animation."""
    path = ROOT / relative_path
    digest = hashlib.sha256(path.read_bytes()).hexdigest()[:12]
    return f"{relative_path}?v={digest}"


def versioned_runtime_pack() -> str:
    """Fingerprint runtime inputs without depending on the ZIP being rebuilt first."""
    paths = [
        ROOT / "README.md",
        ROOT / "SHARE.md",
        ROOT / "PROMPT_TEMPLATE.md",
        *sorted(ROOT.glob("GENERATION_PROMPTS-*.md")),
        ROOT / "manifest.json",
        ROOT / "browser-preview.png",
        ROOT / "vercel-live.png",
        *sorted((ROOT / "gifs").rglob("*.gif")),
        *sorted((ROOT / "references").glob("*.png")),
        *sorted((ROOT / "scripts").glob("*")),
    ]
    digest = hashlib.sha256()
    for path in paths:
        if not path.is_file() or path.name == "__pycache__":
            continue
        digest.update(str(path.relative_to(ROOT)).encode("utf-8"))
        digest.update(path.read_bytes())
    return f"homie-loaders-runtime.zip?v={digest.hexdigest()[:12]}"


def build_story_section() -> str:
    figures = []
    for index, (filename, label, alt_text) in enumerate(STORIES, start=1):
        asset_url = versioned_asset(f"stories/{filename}")
        figures.append(
            f"""
                <figure class="story-item">
                  <a class="story-art-link" href="{html.escape(asset_url)}">
                    <img src="{html.escape(asset_url)}" alt="{html.escape(alt_text)}" width="1080" height="1920" loading="lazy" decoding="async">
                  </a>
                  <figcaption><span><strong>{index:02d}</strong> / {html.escape(label)}</span><a href="{html.escape(asset_url)}" download>Download PNG</a></figcaption>
                </figure>
            """
        )

    archive_url = versioned_asset("stories/homies-beta-instagram-stories.zip")
    return f"""
            <section class="stories-section" id="beta-stories" aria-labelledby="beta-stories-title">
              <header>
                <div>
                  <div class="eyebrow">Beta tester social kit</div>
                  <h2 id="beta-stories-title">Built to stop the scroll.</h2>
                  <p>Eight ready-to-post Instagram Stories for the agents helping shape Homies. Every design appears below at its full 1080 × 1920 size.</p>
                  <div class="actions">
                    <a class="primary" href="{html.escape(archive_url)}" download>Download all 8 Stories</a>
                  </div>
                </div>
              </header>
              <div class="story-list">{''.join(figures)}</div>
            </section>
    """


def font(size: int, bold: bool = False) -> ImageFont.ImageFont:
    candidates = [
        Path("/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else
             "/System/Library/Fonts/Supplemental/Arial.ttf"),
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else
             "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
    ]
    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size)
    return ImageFont.load_default()


def build_html(data: dict) -> None:
    total_animations = sum(len(homie["animations"]) for homie in data["homies"])
    sections: list[str] = []
    for homie in data["homies"]:
        cards = []
        for animation in homie["animations"]:
            asset_url = versioned_asset(animation["asset"])
            cards.append(
                f"""
                <article class="card">
                  <img src="{html.escape(asset_url)}" alt="" width="128" height="128" loading="lazy" decoding="async">
                  <div class="label">{html.escape(animation['label'])}</div>
                  <div class="phrase">{html.escape(animation['loadingText'])}</div>
                  <code>{html.escape(animation['slug'])}</code>
                </article>
                """
            )
        jobs = " · ".join(homie["jobs"])
        reference_url = versioned_asset(homie["reference"])
        sections.append(
            f"""
            <section>
              <header>
                <div>
                  <div class="eyebrow">{html.escape(homie['roleLabel'])}</div>
                  <h2>{html.escape(homie['name'])}</h2>
                  <p>{html.escape(homie['description'])}</p>
                  <small>{html.escape(jobs)}</small>
                </div>
                <img class="reference" src="{html.escape(reference_url)}" alt="" loading="lazy" decoding="async">
              </header>
              <div class="grid">{''.join(cards)}</div>
            </section>
            """
        )

    story_section = build_story_section()

    output = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" href="data:,">
  <title>Homies AI loading animations</title>
  <style>
    :root {{ color-scheme: light; --canvas:#fbf9f6; --paper:#fff; --surface:#f4f1ea;
      --border:#e6e0d8; --ink:#1e1d1c; --muted:#69635e; --coral:#e3423c; }}
    * {{ box-sizing:border-box; }}
    body {{ margin:0; color:var(--ink); background:var(--canvas);
      font:15px/1.45 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif; }}
    main {{ width:min(1540px,calc(100% - 40px)); margin:0 auto; padding:56px 0 96px; }}
    .hero {{ max-width:760px; margin-bottom:60px; }}
    h1 {{ font-size:clamp(36px,6vw,68px); letter-spacing:-.045em; line-height:.95; margin:0 0 22px; }}
    .hero p {{ color:var(--muted); font-size:18px; }}
    .actions {{ display:flex; flex-wrap:wrap; gap:10px; margin-top:24px; }}
    .actions a {{ display:inline-flex; min-height:42px; align-items:center; justify-content:center;
      padding:0 16px; border:1px solid var(--border); border-radius:999px; color:var(--ink);
      background:var(--paper); font-weight:700; text-decoration:none; }}
    .actions a.primary {{ color:#fff; border-color:var(--coral); background:var(--coral); }}
    .actions a.gamification {{ color:var(--coral); border-color:rgba(227,66,60,.35); background:#fff7f4; }}
    .actions a:hover {{ transform:translateY(-1px); }}
    section {{ margin:64px 0; }}
    header {{ display:flex; justify-content:space-between; gap:24px; align-items:end; margin:0 0 22px; }}
    h2 {{ font-size:30px; letter-spacing:-.025em; margin:2px 0 6px; }}
    header p {{ color:var(--muted); max-width:680px; margin:0 0 8px; }}
    header small {{ color:var(--muted); }}
    .eyebrow {{ color:var(--coral); font-size:12px; font-weight:700; letter-spacing:.12em; text-transform:uppercase; }}
    .reference {{ width:92px; height:92px; object-fit:contain; }}
    .grid {{ display:grid; grid-template-columns:repeat(5,minmax(0,1fr)); gap:12px; }}
    .card {{ min-width:0; background:rgba(255,255,255,.76); border:1px solid var(--border);
      border-radius:20px; padding:16px; text-align:center; }}
    .card img {{ width:128px; height:128px; object-fit:contain; display:block; margin:0 auto 10px; }}
    .label {{ font-weight:700; }}
    .phrase {{ min-height:42px; color:var(--muted); font-family:Georgia,serif; font-style:italic; }}
    code {{ display:block; overflow:hidden; text-overflow:ellipsis; color:#8b8179; font-size:11px; }}
    .stories-section {{ margin:112px 0 0; padding:clamp(32px,5vw,72px);
      border-radius:36px; color:#f4f1ea; background:#1a1714; overflow:hidden; }}
    .stories-section > header {{ align-items:flex-start; margin-bottom:0; }}
    .stories-section h2 {{ max-width:820px; margin:5px 0 12px;
      font-size:clamp(42px,6vw,76px); letter-spacing:-.045em; line-height:.95; }}
    .stories-section header p {{ max-width:780px; color:#bdb5ab; font-size:18px; }}
    .stories-section .eyebrow {{ color:#ea5536; }}
    .stories-section .actions a {{ color:#f4f1ea; border-color:#504a44; background:#28231f; }}
    .stories-section .actions a.primary {{ color:#1a1714; border-color:#ea5536; background:#ea5536; }}
    .story-list {{ display:grid; gap:clamp(64px,8vw,120px); max-width:1080px;
      margin:clamp(42px,6vw,80px) auto 0; }}
    .story-item {{ min-width:0; margin:0; content-visibility:auto;
      contain-intrinsic-size:1080px 1995px; }}
    .story-art-link {{ display:block; overflow:hidden; border:0;
      border-radius:26px; background:#28231f; box-shadow:0 28px 80px rgba(0,0,0,.34); }}
    .story-item img {{ display:block; width:100%; max-width:1080px; height:auto; }}
    .story-item figcaption {{ display:flex; align-items:center; justify-content:space-between;
      gap:20px; padding:16px 4px 0; color:#bdb5ab; }}
    .story-item figcaption strong {{ color:#f4f1ea; }}
    .story-item figcaption a {{ flex:none; color:#f1977a; font-weight:700; text-decoration:none; }}
    .story-item figcaption a:hover {{ color:#fff; text-decoration:underline; }}
    @media (max-width:1000px) {{ .grid {{ grid-template-columns:repeat(3,minmax(0,1fr)); }} }}
    @media (max-width:640px) {{ main {{ width:min(100% - 24px,1540px); padding-top:32px; }}
      header {{ align-items:start; }} .reference {{ width:64px; height:64px; }}
      .grid {{ grid-template-columns:repeat(2,minmax(0,1fr)); gap:8px; }}
      .card {{ padding:10px 6px; }} .card img {{ width:96px; height:96px; }}
      .stories-section {{ margin-top:88px; padding:28px 12px 34px; border-radius:24px; }}
      .stories-section > header {{ display:block; padding:0 8px; }}
      .stories-section h2 {{ font-size:clamp(40px,14vw,60px); }}
      .story-list {{ gap:64px; margin-top:42px; }}
      .story-art-link {{ border-radius:16px; }}
      .story-item figcaption {{ align-items:flex-start; padding:12px 4px 0; font-size:13px; }}
      .story-item figcaption span {{ max-width:70%; }} }}
    @media (prefers-reduced-motion:reduce) {{ .card img {{ animation-play-state:paused; }} }}
  </style>
</head>
<body>
  <main>
    <div class="hero">
      <div class="eyebrow">{total_animations} transparent loading loops</div>
      <h1>Meet the team<br>doing the work.</h1>
      <p>A growing set of job-specific loaders for every Homie. The funny status
      copy is live text, not baked into the art, so it remains accessible and
      easy to rotate.</p>
      <div class="actions">
        <a class="primary" href="{html.escape(versioned_runtime_pack())}" download>Download runtime pack</a>
        <a href="https://drive.google.com/drive/folders/19x9h9uso4AAFRUsz_PSOzw4mufi6JfKp">Open Google Drive package</a>
        <a class="gamification" href="gamification/">View gamification concept</a>
        <a href="{html.escape(versioned_asset('manifest.json'))}">View implementation manifest</a>
      </div>
    </div>
    {''.join(sections)}
    {story_section}
  </main>
</body>
</html>
"""
    (ROOT / "preview.html").write_text(output)


def build_contact_sheet(data: dict) -> None:
    columns = 10
    cell_w, cell_h = 164, 176
    header_h = 72
    margin = 24
    width = margin * 2 + columns * cell_w
    row_counts = [
        max(1, (len(homie["animations"]) + columns - 1) // columns)
        for homie in data["homies"]
    ]
    height = margin * 2 + sum(
        header_h + rows * cell_h for rows in row_counts
    )
    sheet = Image.new("RGBA", (width, height), SITE_BG)
    draw = ImageDraw.Draw(sheet)
    title_font = font(24, bold=True)
    role_font = font(12, bold=True)
    label_font = font(12, bold=True)
    phrase_font = font(10)

    y = margin
    for homie, animation_rows in zip(data["homies"], row_counts):
        draw.text((margin, y), homie["name"], font=title_font, fill=INK)
        draw.text((margin, y + 32), homie["roleLabel"].upper(), font=role_font, fill=CORAL)
        y += header_h
        for index, animation in enumerate(homie["animations"]):
            column = index % columns
            row = index // columns
            x = margin + column * cell_w
            cell_y = y + row * cell_h
            box = (x + 4, cell_y, x + cell_w - 4, cell_y + cell_h - 8)
            draw.rounded_rectangle(box, radius=16, fill=PAPER, outline=BORDER, width=1)
            gif = Image.open(ROOT / animation["asset"])
            gif.seek(0)
            frame = gif.convert("RGBA")
            frame.thumbnail((112, 112), Image.Resampling.LANCZOS)
            px = x + (cell_w - frame.width) // 2
            py = cell_y + 4
            sheet.alpha_composite(frame, (px, py))
            draw.text((x + 12, cell_y + 118), animation["label"], font=label_font, fill=INK)
            phrase = textwrap.shorten(animation["loadingText"], width=28, placeholder="…")
            draw.text((x + 12, cell_y + 139), phrase, font=phrase_font, fill=MUTED)
        y += animation_rows * cell_h
    sheet.convert("RGB").save(ROOT / "contact-sheet.jpg", quality=90, optimize=True)


def main() -> None:
    data = json.loads((ROOT / "manifest.json").read_text())
    build_html(data)
    build_contact_sheet(data)
    print(f"wrote {ROOT / 'preview.html'}")
    print(f"wrote {ROOT / 'contact-sheet.jpg'}")


if __name__ == "__main__":
    main()
