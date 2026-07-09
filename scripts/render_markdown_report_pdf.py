#!/usr/bin/env python3
"""Render a Korean markdown report to PDF using ReportLab.

This lightweight renderer is for curated HIRA reports where dashboard sync requires a PDF.
It intentionally supports only the markdown constructs used in these reports.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfbase.ttfonts import TTFont, TTFError
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)

FONT_FAMILY = {
    "regular": "ReportKorean-Regular",
    "semibold": "ReportKorean-SemiBold",
    "bold": "ReportKorean-Bold",
}

NOTO_STATIC = Path("/opt/data/fonts/noto-static")
FONT_CANDIDATE_SETS = [
    {
        "regular": NOTO_STATIC / "NotoSansKR-400.ttf",
        "semibold": NOTO_STATIC / "NotoSansKR-600.ttf",
        "bold": NOTO_STATIC / "NotoSansKR-700.ttf",
    },
]
FONT_CANDIDATES = [
    Path("/usr/share/fonts/opentype/ipafont-gothic/ipag.ttf"),
    Path("/usr/share/fonts/truetype/fonts-japanese-gothic.ttf"),
    Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
]


def register_fonts() -> dict[str, str]:
    """Register Korean fonts and return regular/semibold/bold font names.

    HIRA leadership PDFs should match the accepted 약평위 D+1 style: embedded
    NotoSansKR Regular/SemiBold/Bold when available, not ReportLab's minimal
    HYGothic CID fallback.
    """
    for font_set in FONT_CANDIDATE_SETS:
        if all(path.exists() for path in font_set.values()):
            try:
                pdfmetrics.registerFont(TTFont(FONT_FAMILY["regular"], str(font_set["regular"])))
                pdfmetrics.registerFont(TTFont(FONT_FAMILY["semibold"], str(font_set["semibold"])))
                pdfmetrics.registerFont(TTFont(FONT_FAMILY["bold"], str(font_set["bold"])))
                return FONT_FAMILY.copy()
            except TTFError:
                pass

    # Fallbacks for minimal Linux images. Prefer TrueType files before the CID
    # font so headings/body use one extractable embedded font where possible.
    for path in FONT_CANDIDATES:
        if path.exists():
            try:
                pdfmetrics.registerFont(TTFont("ReportKorean", str(path)))
                return {"regular": "ReportKorean", "semibold": "ReportKorean", "bold": "ReportKorean"}
            except TTFError:
                continue
    try:
        pdfmetrics.registerFont(UnicodeCIDFont("HYGothic-Medium"))
        return {"regular": "HYGothic-Medium", "semibold": "HYGothic-Medium", "bold": "HYGothic-Medium"}
    except Exception:
        return {"regular": "Helvetica", "semibold": "Helvetica-Bold", "bold": "Helvetica-Bold"}


def esc(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace("`", "")
    )


def inline_md(text: str) -> str:
    text = esc(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    return text


def split_table_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def table_col_widths(rows: list[list[str]], avail_width: float) -> list[float]:
    n = max(len(r) for r in rows)
    widths = [1.0] * n
    for r in rows:
        for i, cell in enumerate(r):
            widths[i] = max(widths[i], min(4.0, max(1.0, len(cell) / 14)))
    total = sum(widths)
    return [avail_width * w / total for w in widths]


def build_story(md: str, styles: dict[str, ParagraphStyle], avail_width: float):
    story = []
    lines = md.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        if not line:
            story.append(Spacer(1, 3 * mm))
            i += 1
            continue
        if line.strip() == "---":
            story.append(Spacer(1, 5 * mm))
            i += 1
            continue
        if line.startswith("# "):
            story.append(Paragraph(inline_md(line[2:].strip()), styles["Title"]))
            story.append(Spacer(1, 4 * mm))
            i += 1
            continue
        if line.startswith("## "):
            story.append(Paragraph(inline_md(line[3:].strip()), styles["Heading2"]))
            i += 1
            continue
        if line.startswith("### "):
            story.append(Paragraph(inline_md(line[4:].strip()), styles["Heading3"]))
            i += 1
            continue
        if line.startswith("|"):
            table_lines = []
            while i < len(lines) and lines[i].startswith("|"):
                table_lines.append(lines[i])
                i += 1
            rows = []
            for tl in table_lines:
                cells = split_table_row(tl)
                if cells and all(re.fullmatch(r":?-{3,}:?", c or "") for c in cells):
                    continue
                rows.append(cells)
            if rows:
                n = max(len(r) for r in rows)
                norm = [r + [""] * (n - len(r)) for r in rows]
                data = [[Paragraph(inline_md(c), styles["TableCell"]) for c in r] for r in norm]
                tbl = Table(data, colWidths=table_col_widths(norm, avail_width), repeatRows=1)
                tbl.setStyle(TableStyle([
                    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#eef2f7")),
                    ("TEXTCOLOR", (0, 0), (-1, 0), colors.HexColor("#111827")),
                    ("GRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#cbd5e1")),
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("LEFTPADDING", (0, 0), (-1, -1), 4),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                    ("TOPPADDING", (0, 0), (-1, -1), 4),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                ]))
                story.append(tbl)
                story.append(Spacer(1, 3 * mm))
            continue
        if line.startswith("- "):
            bullet_lines = []
            while i < len(lines) and lines[i].startswith("- "):
                bullet_lines.append(lines[i][2:].strip())
                i += 1
            for bl in bullet_lines:
                story.append(Paragraph("• " + inline_md(bl), styles["Bullet"]))
            continue
        if re.match(r"^\d+\. ", line):
            story.append(Paragraph(inline_md(line), styles["Body"]))
            i += 1
            continue
        # Merge adjacent plain lines into one paragraph.
        para = [line]
        i += 1
        while i < len(lines) and lines[i].strip() and not lines[i].startswith(("#", "|", "- ")) and lines[i].strip() != "---":
            if re.match(r"^\d+\. ", lines[i]):
                break
            para.append(lines[i].strip())
            i += 1
        story.append(Paragraph(inline_md(" ".join(para)), styles["Body"]))
    return story


def footer(canvas, doc):
    canvas.saveState()
    footer_font = getattr(doc, "footer_font", "Helvetica")
    canvas.setFont(footer_font, 8)
    canvas.setFillColor(colors.HexColor("#64748b"))
    canvas.drawString(18 * mm, 10 * mm, "HIRA Market Access Intelligence | Leadership Brief")
    canvas.drawRightString(A4[0] - 18 * mm, 10 * mm, f"{doc.page}")
    canvas.restoreState()


def render(src: Path, dst: Path) -> None:
    fonts = register_fonts()
    base = getSampleStyleSheet()
    styles = {
        "Title": ParagraphStyle("Title", parent=base["Title"], fontName=fonts["bold"], fontSize=18, leading=24, alignment=TA_CENTER, textColor=colors.HexColor("#0f172a"), spaceAfter=6),
        "Heading2": ParagraphStyle("Heading2", parent=base["Heading2"], fontName=fonts["bold"], fontSize=14, leading=19, textColor=colors.HexColor("#1e3a8a"), spaceBefore=8, spaceAfter=5),
        "Heading3": ParagraphStyle("Heading3", parent=base["Heading3"], fontName=fonts["semibold"], fontSize=11.5, leading=16, textColor=colors.HexColor("#334155"), spaceBefore=6, spaceAfter=3),
        "Body": ParagraphStyle("Body", parent=base["BodyText"], fontName=fonts["regular"], boldFontName=fonts["bold"], fontSize=9.2, leading=14, alignment=TA_LEFT, spaceAfter=3),
        "Bullet": ParagraphStyle("Bullet", parent=base["BodyText"], fontName=fonts["regular"], boldFontName=fonts["bold"], fontSize=9.0, leading=13, leftIndent=8, firstLineIndent=-8, spaceAfter=2),
        "TableCell": ParagraphStyle("TableCell", parent=base["BodyText"], fontName=fonts["regular"], boldFontName=fonts["bold"], fontSize=7.3, leading=9.5),
    }
    left = right = 14 * mm
    top = 16 * mm
    bottom = 16 * mm
    doc = BaseDocTemplate(str(dst), pagesize=A4, leftMargin=left, rightMargin=right, topMargin=top, bottomMargin=bottom)
    doc.footer_font = fonts["regular"]
    frame = Frame(left, bottom, A4[0] - left - right, A4[1] - top - bottom, id="normal")
    doc.addPageTemplates([PageTemplate(id="main", frames=[frame], onPage=footer)])
    story = build_story(src.read_text(encoding="utf-8"), styles, A4[0] - left - right)
    dst.parent.mkdir(parents=True, exist_ok=True)
    doc.build(story)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("usage: render_markdown_report_pdf.py input.md output.pdf")
    render(Path(sys.argv[1]), Path(sys.argv[2]))
