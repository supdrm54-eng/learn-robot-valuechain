"""덱의 글자 크기·숫자를 검사한다.
- 16pt 미만 글자: chrome(12pt: nav칩·과목명·푸터·쪽번호)과 표지 설명(14.5pt) 외에는 없어야 한다.
- 슬라이드의 숫자가 forge/facts.csv 에 있는지 본다(구조 숫자·출처 번호·쪽번호 제외).
사용: python qa_fonts.py <deck.pptx> <facts.csv>
"""
import re
import sys
from pptx import Presentation
from pptx.util import Pt

deck, facts_path = sys.argv[1], sys.argv[2]
facts = open(facts_path, encoding="utf-8").read()
NUM = re.compile(r"\d[\d,]*(?:\.\d+)?")
allowed = {n.replace(",", "") for n in NUM.findall(facts)} | {"1", "2", "3", "4", "5", "01", "02", "03"}
prs = Presentation(deck)
small, unknown = [], []


def runs(shape):
    if shape.has_text_frame:
        for para in shape.text_frame.paragraphs:
            for r in para.runs:
                yield r
    if getattr(shape, "has_table", False) and shape.has_table:
        for row in shape.table.rows:
            for cell in row.cells:
                for para in cell.text_frame.paragraphs:
                    for r in para.runs:
                        yield r


for i, sl in enumerate(prs.slides, 1):
    for sh in sl.shapes:
        for r in runs(sh):
            t = r.text.strip()
            if not t:
                continue
            size = r.font.size.pt if r.font.size else None
            chrome = size in (12, 13) or (i == 1 and size == 14.5)
            if size is not None and size < 16 and not chrome:
                small.append((i, size, t[:30]))
            if i == 1 or t.isdigit() and len(t) <= 2:      # 표지·쪽번호 제외
                continue
            body = re.sub(r"\[S\d+\]|\d{4}-\d{2}-\d{2}|①|②|③|④|⑤|Q\d|\d장|\d+기준", "", t)
            for n in NUM.findall(body):
                if n.replace(",", "") not in allowed:
                    unknown.append((i, n, t[:40]))

print(f"슬라이드 {len(prs.slides)}장")
print(f"16pt 미만 본문 글자: {len(small)}건")
for x in small:
    print("  ", x)
print(f"facts.csv 에 없는 숫자: {len(unknown)}건")
for x in unknown:
    print("  ", x)
