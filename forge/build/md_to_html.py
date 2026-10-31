"""교재 마크다운(ch1~3.md)을 Word가 열 수 있는 HTML 한 파일로 묶는다.

사용: python md_to_html.py <textbook 폴더> <출력 html>
지원 범위: 제목(#~###), 표, 번호·글머리 목록, 인용(>), 그림, 굵게·기울임·코드, 가로줄.
"""
import html
import re
import sys
from pathlib import Path

src = Path(sys.argv[1])
out = Path(sys.argv[2])


def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"(?<![\w*])\*([^*]+)\*(?![\w*])", r"<i>\1</i>", s)
    s = re.sub(r"\[(S\d+)\]", r'<span class="cite">[\1]</span>', s)
    s = re.sub(r"(https?://[^\s<)]+)", r'<a href="\1">\1</a>', s)
    return s


def convert(md, img_dir):
    lines, out_html, i = md.splitlines(), [], 0
    while i < len(lines):
        ln = lines[i]
        if not ln.strip():
            i += 1
            continue
        if ln.startswith("---"):
            out_html.append('<p class="rule"></p>')
            i += 1
            continue
        m = re.match(r"^(#{1,3}) (.*)", ln)
        if m:
            lvl = len(m.group(1))
            out_html.append(f"<h{lvl}>{inline(m.group(2))}</h{lvl}>")
            i += 1
            continue
        m = re.match(r"^!\[(.*?)\]\((.*?)\)", ln)
        if m:
            p = (img_dir / m.group(2)).resolve()
            if p.with_suffix(".png").exists():           # Word용으로 렌더한 PNG가 있으면 그것을 쓴다
                p = p.with_suffix(".png")
            path = p.as_uri()
            out_html.append(f'<p class="fig"><img src="{path}" alt="{html.escape(m.group(1))}" width="620"></p>')
            i += 1
            continue
        if ln.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                if not re.match(r"^\|[-| :]+\|$", lines[i]):
                    rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            t = ["<table>"]
            for r, row in enumerate(rows):
                tag = "th" if r == 0 else "td"
                t.append("<tr>" + "".join(f"<{tag}>{inline(c)}</{tag}>" for c in row) + "</tr>")
            t.append("</table>")
            out_html.append("".join(t))
            continue
        if ln.startswith(">"):
            buf = []
            while i < len(lines) and lines[i].startswith(">"):
                buf.append(lines[i].lstrip("> ").rstrip())
                i += 1
            paras = "<br>".join(inline(b) for b in buf if b)
            out_html.append(f'<div class="callout">{paras}</div>')
            continue
        if re.match(r"^\d+\. ", ln) or ln.startswith("- "):
            ordered = bool(re.match(r"^\d+\. ", ln))
            tag = "ol" if ordered else "ul"
            items = []
            while i < len(lines) and (re.match(r"^\d+\. ", lines[i]) if ordered else lines[i].startswith("- ")):
                items.append(re.sub(r"^(\d+\. |- )", "", lines[i]))
                i += 1
            out_html.append(f"<{tag}>" + "".join(f"<li>{inline(x)}</li>" for x in items) + f"</{tag}>")
            continue
        cls = ' class="caption"' if ln.startswith("*") and ln.endswith("*") else ""
        out_html.append(f"<p{cls}>{inline(ln)}</p>")
        i += 1
    return "\n".join(out_html)


CSS = """
@page { size: 210mm 297mm; margin: 22mm 20mm 22mm 20mm; }
body { font-family: 'Malgun Gothic', sans-serif; font-size: 10.5pt; line-height: 1.6; color: #2A2F3A; }
h1 { font-size: 20pt; color: #1B2C5E; border-bottom: 2.5pt solid #1B2C5E; padding-bottom: 4pt; margin-top: 0; page-break-before: always; }
h2 { font-size: 14pt; color: #1B2C5E; margin-top: 18pt; border-left: 5pt solid #2E5BAA; padding-left: 6pt; }
h3 { font-size: 12pt; color: #2E5BAA; margin-top: 12pt; }
table { border-collapse: collapse; width: 100%; margin: 6pt 0 10pt 0; font-size: 9.5pt; }
th { background: #1B2C5E; color: #FFFFFF; font-weight: bold; padding: 4pt 6pt; border: 0.75pt solid #1B2C5E; text-align: left; }
td { padding: 4pt 6pt; border: 0.75pt solid #C9CFDA; vertical-align: top; }
.callout { background: #EAF1FB; border-left: 4pt solid #2E5BAA; padding: 6pt 10pt; margin: 8pt 0; }
.caption { font-size: 9pt; color: #5B6270; }
.fig { text-align: center; margin: 8pt 0 2pt 0; }
.cite { color: #2E5BAA; font-size: 8.5pt; }
.rule { border-bottom: 0.75pt solid #C9CFDA; margin: 6pt 0; }
code { font-family: Consolas, monospace; font-size: 9pt; color: #3B4252; }
a { color: #2E5BAA; text-decoration: none; }
.cover h1 { page-break-before: auto; border: none; font-size: 28pt; margin-top: 140pt; }
.cover p { font-size: 12pt; color: #5B6270; }
"""

COVER = """<div class="cover">
<h1>로봇 밸류체인 — 자동차 부품사의 진입 기회</h1>
<p><b>교재 3장</b> · 대상: 자동차 부품사 재직자</p>
<p>이 교재가 답할 질문 — 휴머노이드 원가의 절반이 액추에이터에 몰린 로봇 밸류체인에서, 우리 자동차 부품사는 어떤 기존 역량을 옮겨 어느 부품부터 들어갈 수 있는가?</p>
<p>1장. 로봇을 해부하면 밸류체인이 보인다<br>2장. 돈은 어디에 있나 — 휴머노이드 원가 구조<br>3장. 부품사는 어디로 들어가나 — 진입 전략</p>
<p class="caption">숫자의 출처는 각 장 끝 [S#] 목록에 있다. 'E'가 붙은 연도는 기관의 추정·전망이다. 원본 강의: KMA 자동차특화 AI 융합 전문가 과정 로봇과 스마트팩토리 특강.</p>
</div>"""

body = [COVER]
for ch in sorted(src.glob("ch*.md")):
    body.append(convert(ch.read_text(encoding="utf-8"), src))
doc = f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>로봇 밸류체인 교재</title><style>{CSS}</style></head><body>{"".join(body)}</body></html>'
out.write_text(doc, encoding="utf-8")
print("html:", out)
