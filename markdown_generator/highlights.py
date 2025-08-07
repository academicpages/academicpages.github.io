import argparse
import datetime as dt
import json
import os
import shutil
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import fitz  # PyMuPDF

from highlights_inputs import load_yaml, validate_schema  # type: ignore


ROOT = Path(__file__).resolve().parents[1]
IMAGES_DIR = ROOT / "images" / "highlights"
DRAFTS_DIR = ROOT / "_drafts"


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def rank_pages_by_figure_likelihood(doc: fitz.Document, max_pages: int = 3) -> List[int]:
    scores: List[Tuple[int, float]] = []
    for page_index in range(len(doc)):
        page = doc.load_page(page_index)
        text = page.get_text("text") or ""
        num_images = len(page.get_images(full=True))
        # Heuristic: images weight + presence of 'Fig'/'Figure' text
        score = num_images * 2.0
        if "figure" in text.lower() or "fig." in text.lower() or "fig " in text.lower():
            score += 1.5
        # Prefer mid/late pages slightly (avoid front-matter)
        score += (page_index / max(1, len(doc) - 1)) * 0.3
        if score > 0:
            scores.append((page_index, score))
    scores.sort(key=lambda x: x[1], reverse=True)
    top_pages = [idx for idx, _ in scores[:max_pages]]
    return top_pages


def rasterize_pages_to_images(pdf_path: Path, pages: List[int], out_dir: Path, slug: str, dpi: int = 200) -> List[Path]:
    ensure_dir(out_dir)
    image_paths: List[Path] = []
    with fitz.open(pdf_path) as doc:  # type: ignore[arg-type]
        for i, page_index in enumerate(pages, start=1):
            page = doc.load_page(page_index)
            zoom = dpi / 72.0
            mat = fitz.Matrix(zoom, zoom)
            pix = page.get_pixmap(matrix=mat, alpha=False)
            out_path = out_dir / f"{slug}-fig{i}.png"
            pix.save(out_path.as_posix())
            image_paths.append(out_path)
    return image_paths


def select_pages(doc: fitz.Document, preferred_pages: Optional[List[int]], max_images: int) -> List[int]:
    if preferred_pages:
        # Convert 1-based to 0-based indices, clamp range
        chosen = [max(0, min(len(doc) - 1, p - 1)) for p in preferred_pages]
        return chosen[:max_images]
    ranked = rank_pages_by_figure_likelihood(doc, max_pages=max_images)
    if not ranked:  # fallback to first pages
        ranked = list(range(min(max_images, len(doc))))
    return ranked[:max_images]


def emit_markdown_draft(
    slug: str,
    title: str,
    date: str,
    tags: List[str],
    images: List[Path],
    links: Dict[str, str],
    out_dir: Path,
) -> Path:
    ensure_dir(out_dir)
    front_matter: Dict[str, Any] = {
        "title": title,
        "date": date,
        "categories": ["research-highlights"],
        "tags": tags,
        "links": links,
    }

    body_lines: List[str] = []
    body_lines.append(
        "Review checklist (delete after approval):\n"
        "- Facts correct and grounded in paper/repo?\n"
        "- Selected figures representative and legible?\n"
        "- Figure credit/source included and licensing OK?\n"
        "- Tags and links correct?\n"
    )
    body_lines.append("")
    body_lines.append("TL;DR: Replace this with a concise, accurate 1–2 sentence summary.")
    body_lines.append("")
    if images:
        for img in images:
            rel = "/" + img.relative_to(ROOT).as_posix()
            body_lines.append(f"![Figure]({rel})")
            body_lines.append("")
        body_lines.append("Figure credit: Source pages/images as indicated; ensure attribution upon approval.")
        body_lines.append("")
    body_lines.append("Key points:")
    body_lines.append("- Point 1: contribution")
    body_lines.append("- Point 2: method or result")
    body_lines.append("- Point 3: impact")
    body_lines.append("")
    if links:
        link_lines = [f"- {k}: {v}" for k, v in links.items()]
        body_lines.append("Links:\n" + "\n".join(link_lines))

    fm = "---\n" + json.dumps(front_matter, indent=2).replace("\"", "\"")
    # Use YAML-like by building manually for readability
    yaml_lines = ["---"]
    yaml_lines.append(f"title: \"{title}\"")
    yaml_lines.append(f"date: {date}")
    yaml_lines.append(f"permalink: /highlights/{slug}/")
    yaml_lines.append("categories: [research-highlights]")
    if tags:
        yaml_lines.append("tags: [" + ", ".join(tags) + "]")
    if links:
        yaml_lines.append("links:")
        for k, v in links.items():
            yaml_lines.append(f"  {k}: {v}")
    yaml_lines.append("---\n")

    content = "\n".join(yaml_lines + body_lines) + "\n"
    out_path = out_dir / f"{slug}.md"
    out_path.write_text(content, encoding="utf-8")
    return out_path


def ingest_papers(items: List[Dict[str, Any]], limit: Optional[int] = None, only_ids: Optional[List[str]] = None) -> None:
    created = 0
    report: List[Dict[str, Any]] = []
    for item in items:
        if item.get("type") != "paper":
            continue
        item_id = str(item["id"])  # slug
        if only_ids and item_id not in only_ids:
            continue
        title = str(item.get("title", item_id))
        tags = list(item.get("tags", []))
        links: Dict[str, str] = {}
        if item.get("arxiv"):
            links["arXiv"] = f"https://arxiv.org/abs/{item['arxiv']}"
        if item.get("doi"):
            links["DOI"] = f"https://doi.org/{item['doi']}"

        pdf_path = item.get("pdf")
        if not pdf_path:
            print(f"[WARN] {item_id}: no local PDF specified; skipping (MVP requires 'pdf')")
            report.append({"id": item_id, "status": "skipped", "reason": "no pdf"})
            continue
        pdf_file = ROOT / str(pdf_path)
        if not pdf_file.exists():
            print(f"[WARN] {item_id}: PDF not found at {pdf_file}; skipping")
            report.append({"id": item_id, "status": "skipped", "reason": "pdf missing"})
            continue

        with fitz.open(pdf_file) as doc:  # type: ignore[arg-type]
            preferred = None
            if item.get("preferred_figures"):
                preferred = [int(p.get("page")) for p in item["preferred_figures"] if "page" in p]
            pages = select_pages(doc, preferred_pages=preferred, max_images=2)

        out_dir = IMAGES_DIR / item_id
        images = rasterize_pages_to_images(pdf_file, pages, out_dir, slug=item_id)
        draft_path = emit_markdown_draft(
            slug=item_id,
            title=title,
            date=dt.date.today().isoformat(),
            tags=tags,
            images=images,
            links=links,
            out_dir=DRAFTS_DIR,
        )

        created += 1
        report.append({"id": item_id, "status": "created", "draft": str(draft_path), "images": [str(p) for p in images]})
        print(f"[OK] Draft created: {draft_path}")
        if limit and created >= limit:
            break

    (ROOT / "markdown_generator" / "highlights_report.json").write_text(
        json.dumps(report, indent=2), encoding="utf-8"
    )
    print(f"Report written with {len(report)} entries")


def is_image_file(path: Path) -> bool:
    return path.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".webp"}


def is_pdf_file(path: Path) -> bool:
    return path.suffix.lower() == ".pdf"


def copy_or_render_asset(src: Path, out_dir: Path, slug: str, index: int) -> Optional[Path]:
    ensure_dir(out_dir)
    if not src.exists():
        print(f"[WARN] asset not found: {src}")
        return None
    if is_image_file(src):
        dst = out_dir / f"{slug}-fig{index}.png"
        try:
            shutil.copyfile(src, dst)
            return dst
        except Exception as e:
            print(f"[WARN] failed to copy image {src} -> {dst}: {e}")
            return None
    if is_pdf_file(src):
        try:
            with fitz.open(src) as doc:  # type: ignore[arg-type]
                page = doc.load_page(0)
                mat = fitz.Matrix(200 / 72.0, 200 / 72.0)
                pix = page.get_pixmap(matrix=mat, alpha=False)
                dst = out_dir / f"{slug}-fig{index}.png"
                pix.save(dst.as_posix())
                return dst
        except Exception as e:
            print(f"[WARN] failed to rasterize PDF {src}: {e}")
            return None
    print(f"[WARN] unsupported asset type: {src}")
    return None


def ingest_repos(items: List[Dict[str, Any]], limit: Optional[int] = None, only_ids: Optional[List[str]] = None) -> None:
    created = 0
    report: List[Dict[str, Any]] = []
    for item in items:
        if item.get("type") != "repo":
            continue
        item_id = str(item["id"]).strip()
        if only_ids and item_id not in only_ids:
            continue
        title = str(item.get("title", item_id))
        tags = list(item.get("tags", []))
        github_url = str(item.get("github", "")).strip()
        links: Dict[str, str] = {}
        if github_url:
            links["GitHub"] = github_url

        out_dir = IMAGES_DIR / item_id
        ensure_dir(out_dir)
        images: List[Path] = []

        preferred = item.get("preferred_images", [])
        for idx, rel in enumerate(preferred, start=1):
            # Treat as local path relative to repo root for MVP
            src = ROOT / str(rel)
            saved = copy_or_render_asset(src, out_dir, slug=item_id, index=idx)
            if saved:
                images.append(saved)
            if len(images) >= 2:
                break

        if not images:
            print(f"[WARN] {item_id}: no images extracted; skipping draft (MVP requires preferred_images)")
            report.append({"id": item_id, "status": "skipped", "reason": "no images"})
            continue

        draft_path = emit_markdown_draft(
            slug=item_id,
            title=title,
            date=dt.date.today().isoformat(),
            tags=tags,
            images=images,
            links=links,
            out_dir=DRAFTS_DIR,
        )
        created += 1
        report.append({"id": item_id, "status": "created", "draft": str(draft_path), "images": [str(p) for p in images]})
        print(f"[OK] Draft created: {draft_path}")
        if limit and created >= limit:
            break

    # Append or overwrite a report for repos as well
    (ROOT / "markdown_generator" / "highlights_report.json").write_text(
        json.dumps(report, indent=2), encoding="utf-8"
    )
    print(f"Report written with {len(report)} entries")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Research highlights generator (MVP)")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_ingest = sub.add_parser("ingest", help="Ingest and draft content")
    p_ingest.add_argument("what", choices=["papers", "repos"], help="Type to ingest")
    p_ingest.add_argument("--input", default="markdown_generator/highlights.yml")
    p_ingest.add_argument("--limit", type=int, default=None)
    p_ingest.add_argument("--only", default=None, help="Comma-separated ids to process")

    return parser.parse_args()


def main() -> int:
    args = parse_args()
    data = load_yaml(Path(args.input))
    validate_schema(data)
    items: List[Dict[str, Any]] = data["items"]

    if args.cmd == "ingest" and args.what == "papers":
        only_ids = args.only.split(",") if args.only else None
        ingest_papers(items, limit=args.limit, only_ids=only_ids)
        return 0
    if args.cmd == "ingest" and args.what == "repos":
        only_ids = args.only.split(",") if args.only else None
        ingest_repos(items, limit=args.limit, only_ids=only_ids)
        return 0

    return 0


if __name__ == "__main__":
    raise SystemExit(main())


