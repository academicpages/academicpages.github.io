#!/usr/bin/env python3
"""Build a SiGMA talk PowerPoint from Notion notes content and local images."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Iterable
from urllib.parse import unquote, urlparse

import requests
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.util import Emu, Inches, Pt

ROOT = Path(__file__).resolve().parents[1]
OUT_PPTX = ROOT / "files" / "talk_geoml_sigma.pptx"
IMG_DIR = Path("/tmp/sigma_slides/images")
URLS_JSON = Path("/tmp/sigma_slides/urls.json")

TITLE_COLOR = RGBColor(0x15, 0x65, 0xC0)
BODY_COLOR = RGBColor(0x33, 0x33, 0x33)


def strip_html(text: str) -> str:
    """Remove simple HTML tags and unescape common entities.

    Args:
        text: Raw HTML-ish text from Notion export.

    Returns:
        Plain text suitable for PowerPoint.
    """
    cleaned = re.sub(r"<br\\s*/?>", "\n", text, flags=re.I)
    cleaned = re.sub(r"</?[^>]+>", "", cleaned)
    cleaned = cleaned.replace("&gt;", ">").replace("&lt;", "<").replace("&amp;", "&")
    return re.sub(r"\n{3,}", "\n\n", cleaned).strip()


def download_images(url_map: dict[str, str]) -> dict[str, Path]:
    """Download Notion images keyed by short filename.

    Args:
        url_map: Mapping from short name to signed download URL.

    Returns:
        Mapping from short name to local path.
    """
    IMG_DIR.mkdir(parents=True, exist_ok=True)
    local: dict[str, Path] = {}
    for name, url in url_map.items():
        path = IMG_DIR / name
        response = requests.get(url, timeout=60)
        response.raise_for_status()
        path.write_bytes(response.content)
        local[name] = path
        print(f"downloaded {name} ({len(response.content)} bytes)")
    return local


def set_run(paragraph, text: str, *, size: int = 18, bold: bool = False) -> None:
    """Configure a paragraph's text run.

    Args:
        paragraph: python-pptx paragraph object.
        text: Text content.
        size: Font size in points.
        bold: Whether text is bold.
    """
    paragraph.clear()
    run = paragraph.add_run()
    run.text = text
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = BODY_COLOR
    run.font.name = "Calibri"


def add_title_slide(prs: Presentation, title: str, subtitle: str) -> None:
    """Add a title slide.

    Args:
        prs: Presentation object.
        title: Main title.
        subtitle: Subtitle lines.
    """
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    box = slide.shapes.add_textbox(Inches(0.7), Inches(2.2), Inches(12), Inches(2))
    tf = box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    set_run(p, title, size=32, bold=True)
    p.font.color.rgb = TITLE_COLOR
    p2 = tf.add_paragraph()
    set_run(p2, subtitle, size=18)
    p2.space_before = Pt(18)


def add_bullets_slide(
    prs: Presentation,
    title: str,
    bullets: Iterable[str],
    image: Path | None = None,
) -> None:
    """Add a content slide with optional image.

    Args:
        prs: Presentation object.
        title: Slide title.
        bullets: Bullet strings.
        image: Optional local image path.
    """
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.3), Inches(12.3), Inches(0.8))
    tp = title_box.text_frame.paragraphs[0]
    set_run(tp, title, size=26, bold=True)
    tp.font.color.rgb = TITLE_COLOR

    width = Inches(6.2) if image else Inches(12.3)
    body = slide.shapes.add_textbox(Inches(0.5), Inches(1.2), width, Inches(5.5))
    tf = body.text_frame
    tf.word_wrap = True
    first = True
    for bullet in bullets:
        paragraph = tf.paragraphs[0] if first else tf.add_paragraph()
        first = False
        set_run(paragraph, bullet, size=16)
        paragraph.level = 0
        paragraph.space_after = Pt(8)

    if image and image.exists():
        slide.shapes.add_picture(str(image), Inches(7.0), Inches(1.3), width=Inches(5.7))


def add_image_slide(prs: Presentation, title: str, image: Path, caption: str = "") -> None:
    """Add an image-focused slide.

    Args:
        prs: Presentation object.
        title: Slide title.
        image: Local image path.
        caption: Optional caption under the image.
    """
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.25), Inches(12.3), Inches(0.7))
    set_run(title_box.text_frame.paragraphs[0], title, size=24, bold=True)
    title_box.text_frame.paragraphs[0].font.color.rgb = TITLE_COLOR
    if image.exists():
        slide.shapes.add_picture(str(image), Inches(1.2), Inches(1.1), width=Inches(11))
    if caption:
        cap = slide.shapes.add_textbox(Inches(0.5), Inches(6.7), Inches(12.3), Inches(0.4))
        set_run(cap.text_frame.paragraphs[0], caption, size=12)


def build(local_images: dict[str, Path]) -> Path:
    """Assemble the SiGMA deck.

    Args:
        local_images: Mapping of short image names to paths.

    Returns:
        Path to the written PPTX.
    """
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    add_title_slide(
        prs,
        "SiGMA: Learning under Graph-Level Heterogeneity\nwith Gated Message-Passing and Attention",
        "Raphael Pellegrin — 11/06/2026 — Harvard GeoML group meeting",
    )

    add_bullets_slide(
        prs,
        "Punchline",
        [
            "Within one dataset, different graphs need different computation.",
            "Standard GNNs still apply a fixed template to every graph.",
            "SiGMA keeps MP heads and attention heads in parallel.",
            "Sigmoid gates let each graph emphasize, downweight, or skip heads — and even skip layers.",
        ],
    )

    add_bullets_slide(
        prs,
        "Background: node-level heterogeneity",
        [
            "Most heterogeneity work is node-level (homophily / heterophily).",
            "Methods redesign aggregation for heterophilic nodes.",
            "Literature rarely asks: across a collection of graphs, do whole graphs prefer different operators or depths?",
            "Node-level heterophily: who to aggregate from.",
            "Graph-level heterogeneity: which computational recipe a whole graph needs.",
        ],
    )

    add_bullets_slide(
        prs,
        "Graph-level heterogeneity",
        [
            "Some graphs are consistently easy; others are consistently hard.",
            "Difficulty is model-dependent (hard for GCN can be easier for GIN).",
            "Datasets look homogeneous at the task level, but architectures use one fixed template.",
            "Claim: heterogeneity is an interaction between input and architecture — route per graph.",
        ],
    )

    add_image_slide(
        prs,
        "Heterogeneity profiles — ENZYMES (GAT)",
        local_images["enzymes_gat.png"],
    )
    add_image_slide(
        prs,
        "Heterogeneity profiles — ENZYMES (GIN)",
        local_images["enzymes_gin.png"],
    )
    add_image_slide(
        prs,
        "Heterogeneity profiles — ENZYMES (GCN / GPS)",
        local_images["enzymes_smooth_CGN_GPS.png"],
    )

    add_bullets_slide(
        prs,
        "Preference of MPGNN operator",
        [
            "Compare GCN / GIN / GatedGCN under the same protocol.",
            "No operator dominates every graph in a dataset.",
            "“Best MP for this dataset” is really the best average MP.",
            "A hybrid with multiple MP heads is a natural response.",
        ],
        image=local_images.get("operator_pref.png"),
    )

    add_bullets_slide(
        prs,
        "Preference of depth",
        [
            "Not all graphs want the same number of MP layers.",
            "Depth preferences are spread, not concentrated.",
            "Picking one global depth is a compromise.",
            "We want models that can use or skip layers.",
        ],
        image=local_images.get("depth_pref.png"),
    )

    add_bullets_slide(
        prs,
        "Inspiration: gated attention",
        [
            "Extra capacity without control can waste compute and hurt optimization.",
            "Sigmoid gates let a block contribute continuously between 0 and 1.",
            "Without gates, every head is always on and can interfere.",
            "With gates, a graph can open needed heads and approximately skip layers.",
        ],
        image=local_images.get("gated_attn.png"),
    )

    add_bullets_slide(
        prs,
        "Background: GraphGPS",
        [
            "Hybrid layer = local MP + global attention.",
            "GPS does not run multiple heterogeneous MP operators in parallel.",
            "GPS lacks explicit per-head sigmoid gates.",
            "SiGMA keeps the local+global idea, then generalizes with gated heads.",
        ],
    )

    add_image_slide(
        prs,
        "SiGMA architecture",
        local_images["sigma_arch.png"],
        caption="Sigmoid Gated Message-Passing and Attention",
    )

    add_bullets_slide(
        prs,
        "SiGMA design principle",
        [
            "Per layer: attention heads (global) + MP heads (local; e.g. GCN + GIN).",
            "Each head produces an update and a gate logit.",
            "Head output is multiplied by σ(gate).",
            "Concatenate gated heads → project → residual → FFN.",
            "Multiple operators address operator preference; gates + residual give soft depth.",
        ],
    )

    add_image_slide(
        prs,
        "MMA: same hybrid without gating",
        local_images["MMA.png"],
        caption="MMA = Mixture of Message-Passing and Attention (ungated)",
    )

    add_bullets_slide(
        prs,
        "Synthetic operator routing",
        [
            "Rooted star graphs; label rule chosen by type τ at the root.",
            "τ=0 favors degree-normalized (GCN-like) sums; τ=1 favors unnormalized (GIN-like) sums.",
            "Opposite-sign pairs force graph-specific routing.",
            "Success: high accuracy on both types, and gates that open the matching head.",
        ],
    )

    add_image_slide(prs, "Example graphs in the synthetic experiment", local_images["ex_gin1.png"])
    add_image_slide(prs, "Example graphs in the synthetic experiment", local_images["ex_gin2.png"])
    add_image_slide(prs, "SiGMA can route to the right operator", local_images["routing_acc.png"])
    add_image_slide(prs, "Gates align with generative type", local_images["routing_gates.png"])

    add_bullets_slide(
        prs,
        "Experiments: real datasets",
        [
            "Benchmarks from Dwivedi / LRGB families.",
            "ZINC, MNIST, CIFAR10, PATTERN, CLUSTER, Peptides, VOC-SP, COCO-SP, …",
            "Competitive / strong gains, especially CIFAR10 and PATTERN.",
        ],
        image=local_images.get("real1.png"),
    )
    add_image_slide(prs, "Real-dataset results", local_images["real2.png"])

    add_bullets_slide(
        prs,
        "Theory",
        [
            "Prop. 1: SiGMA is at least as expressive as its strongest MP component.",
            "Prop. 2: gated residuals allow near-identity layers — no forced oversmoothing from depth alone.",
            "Depth preference across graphs is real; gating gives selective depth use.",
        ],
    )

    add_bullets_slide(
        prs,
        "Takeaways",
        [
            "Graph-level heterogeneity is real: graphs disagree on depth and MP operator.",
            "Fixed templates are a dataset-level compromise.",
            "SiGMA: GPS-style hybrid + multiple heads + sigmoid gates.",
            "Synthetic routing shows gates track operator need.",
            "Recipe: strong GNN baselines → multiple operators → attention → gate them.",
            "Code: https://github.com/Weber-GeoML/SiGMA",
        ],
    )

    add_title_slide(prs, "Thank you", "Questions?")

    add_image_slide(prs, "Appendix: gate values are per-node", local_images["mutag_gates.png"])
    add_image_slide(prs, "Appendix: gates — ENZYMES", local_images["enzymes_gates.png"])
    add_image_slide(prs, "Appendix: gates — IMDB", local_images["imdb_gates.png"])
    add_image_slide(
        prs,
        "Appendix: heterogeneity profiles (MUTAG)",
        local_images["mutag_profile.png"],
    )

    OUT_PPTX.parent.mkdir(parents=True, exist_ok=True)
    prs.save(OUT_PPTX)
    return OUT_PPTX


def main() -> None:
    """Build the PPTX from local images (optionally refresh via urls.json)."""
    if URLS_JSON.exists():
        url_map: dict[str, str] = json.loads(URLS_JSON.read_text())
        local = download_images(url_map)
    else:
        local = {path.name: path for path in IMG_DIR.glob("*.png")}
        if not local:
            raise SystemExit(f"No images in {IMG_DIR} and no {URLS_JSON}.")
    path = build(local)
    print(f"wrote {path} ({path.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
