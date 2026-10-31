"""learn-robot-valuechain 정답 스크립트 — Block 1~4 산출물과 대시보드를 만든다.

사용: 작업 폴더(안에 data/facts.csv 가 있는 곳)에서 실행한다.
    python build_answers.py
만드는 것: output/market_cards.md, cost_calc.md, fact_check.md, entry_case.md,
          my_company_map.md·my_entry.md(빈 틀), index.html, expected.json
"""
import csv
import html
import json
import re
from pathlib import Path

DATA, OUT = Path("data"), Path("output")
OUT.mkdir(exist_ok=True)
expected = {}


def put(key, value, block, decimals=None):
    expected[key] = {"value": value, "decimals": decimals, "block": block}


with open(DATA / "facts.csv", encoding="utf-8-sig", newline="") as f:
    facts = {r["id"]: r for r in csv.DictReader(f)}


def num(fid, i=0):
    """값(원문)에서 i번째 숫자를 꺼낸다. 'million'이 붙으면 백만을 곱한다."""
    raw = facts[fid]["값(원문)"]
    found = re.findall(r"(\d[\d,]*(?:\.\d+)?)\s*(million)?", raw)
    n, mil = found[i]
    v = float(n.replace(",", ""))
    return v * 1_000_000 if mil else v


def cite(fid):
    return f"[{facts[fid]['출처']}]"


# ───────── Block 0 ─────────
put("lab_file_count", len([p for p in DATA.iterdir() if p.is_file()]), 0, 0)
put("facts_rows", len(facts), 0, 0)

# ───────── Block 1 · 시장 카드 ─────────
world_installs, world_stock, korea_installs, density = num("F01"), num("F02"), num("F04"), num("F05")
korea_share = round(korea_installs / world_installs * 100, 1)
cards = [("F01", "세계 산업용 로봇 신규 설치"), ("F02", "세계 산업용 로봇 가동 대수"), ("F05", "한국 로봇 밀도")]
md = ["# 시장 카드 (facts.csv 원문 그대로)", ""]
for fid, title in cards:
    r = facts[fid]
    md += [f"## {title}", f"- 값: {r['값(원문)']} {r['단위']}", f"- 기준연도: {r['기준연도']}", f"- 출처: {cite(fid)}", ""]
md += [f"한국 신규 설치 비중 = {korea_installs:,.0f} ÷ {world_installs:,.0f} × 100 = **{korea_share}%** (2024) {cite('F04')}{cite('F01')}"]
(OUT / "market_cards.md").write_text("\n".join(md) + "\n", encoding="utf-8")
(OUT / "my_company_map.md").write_text(
    "# 우리 회사 지도 (회사 내부용 — 공개 저장소에 올리지 않는다)\n\n"
    "| 로봇의 부분 | 우리 회사의 관련 제품·기술 | 가치사슬 층 | 비고 |\n|---|---|---|---|\n"
    "| 센서 | | | |\n| 제어기·AI | | | |\n| 액추에이터 | | | |\n| 엔드이펙터 | | | |\n", encoding="utf-8")
put("world_installs", world_installs, 1, 0)
put("world_stock", world_stock, 1, 0)
put("korea_density", density, 1, 0)
put("korea_share", korea_share, 1, 1)

# ───────── Block 2 · 원가·출하 계산 ─────────
bom25, bom30 = num("F06"), num("F07")
drop = round((bom25 - bom30) / bom25 * 100, 1)
cagr_bom = round((1 - (bom30 / bom25) ** (1 / 5)) * 100, 1)
ship25, ship30, ship35 = num("F14"), num("F15", 0), num("F15", 1)
multiple = round(ship30 / ship25)
cagr_ship = round(((ship35 / ship25) ** (1 / 10) - 1) * 100, 1)
md = ["# 원가·출하 계산 (BofA 추정 기반, E = 추정)", "",
      "| 항목 | 계산식 | 결과 | 출처 |", "|---|---|---|---|",
      f"| BOM 하락률 2025 → 2030E | (35,000 − 17,000) ÷ 35,000 | {drop}% 이상 | {cite('F06')} |",
      f"| BOM 연평균 하락률 | 1 − (17,000 ÷ 35,000)^(1/5) | {cagr_bom}% 이상 | {cite('F07')} |",
      f"| 출하 배수 2025E → 2030E | 1,200,000 ÷ 20,000 | {multiple}배 | {cite('F15')} |",
      f"| 출하 연평균 증가율 2025E → 2035E | (10,000,000 ÷ 20,000)^(1/10) − 1 | {cagr_ship}% | {cite('F15')} |", "",
      f"BofA 원문의 \"86% CAGR\"과 비교: 계산값 {cagr_ship}% → 일치(반올림 차이).", "",
      "대당 원가는 2030E까지 절반 이상 내려가지만 출하는 같은 기간 60배로 늘 전망이라, 부품 시장 전체 지출은 커질 수 있다. "
      "다만 단가가 해마다 최소 13%대씩 내려가므로 더 싸게 더 많이 만드는 능력이 이익을 가른다(모두 BofA 추정)."]
(OUT / "cost_calc.md").write_text("\n".join(md) + "\n", encoding="utf-8")
put("bom_drop_pct", drop, 2, 1)
put("bom_cagr", cagr_bom, 2, 1)
put("ship_multiple", multiple, 2, 0)
put("ship_cagr", cagr_ship, 2, 1)

# ───────── Block 3 · 출처 검증 ─────────
status = {fid: r["상태"].split()[0] for fid, r in facts.items()}
cond = [fid for fid, s in status.items() if s == "조건부"]
confirmed = sum(1 for s in status.values() if s == "확인")
md = ["# 출처 검증", "", f"- 확인: {confirmed}개 · 조건부: {len(cond)}개", "",
      "## 조건부 숫자와 인용 문장", "", "| id | 항목 | 값 | 기준연도 | 인용 예 |", "|---|---|---|---|---|"]
for fid in cond:
    r = facts[fid]
    md.append(f"| {fid} | {r['항목']} | {r['값(원문)']} | {r['기준연도']} | {r['값(원문)']}({r['기준연도']}, BofA 추정) {cite(fid)} |")
sources = (DATA / "sources.md").read_text(encoding="utf-8")
missing = [ln for ln in sources.splitlines() if "**미확보**" in ln and ln.startswith("|")]   # 굵게 표시한 '미확보'만
md += ["", "## 미확보 자료", ""] + [f"- {html.unescape(ln.split('|')[2].strip())}" for ln in missing]
md += ["", "## 같은 손, 다른 숫자", "", "| 질문 | 원본 강의 덱 [S6] | BofA [S5] |", "|---|---|---|",
       "| 값 | 약 30% | 19% |", "| ① 기준연도 | 덱 기준(연도 미표기) | 2030E |",
       "| ② 나누는 방식 | 부위별(단일 부위 최대 가능성) | 모듈별 |", "| ③ 추정 주체 | 원본 강의 | BofA 고유 추정 |"]
(OUT / "fact_check.md").write_text("\n".join(md) + "\n", encoding="utf-8")
put("confirmed_count", confirmed, 3, 0)
put("conditional_count", len(cond), 3, 0)
put("conditional_ids", "·".join(cond), 3)

# ───────── Block 4 · 진입 판단표 ─────────
cap, inhouse = num("F16"), num("F17")
share = round(inhouse / cap * 100, 1)
case = [("① 기술 거리", "자동차 부품 → 로봇 액추에이터. 구체적 기술 이전 내용은 공개 자료로 확인되지 않음", "[S9]"),
        ("② 원가 비중", "공급 품목 액추에이터가 로봇 원가에서 가장 큰 몫", "[S5][S9]"),
        ("③ 첫 고객", "같은 그룹 보스턴다이내믹스 — 로보틱스 첫 고객", "[S9][S18]"),
        ("④ 양산 일정", "아틀라스 양산 시점에 맞춘 공급. 수요 쪽은 2028년 연 30,000대 생산 체계 목표(발표)", "[S9][S13]"),
        ("⑤ 원가 하락 대응", "공개 자료로 확인되지 않음", "—")]
md = ["# 진입 판단표 — 현대모비스 사례 (공개 자료)", "",
      f"현대차그룹 생산 체계 목표 중 자사 공장 투입 비중 = {inhouse:,.0f} ÷ {cap:,.0f} × 100 = **{share}%** (발표된 목표) {cite('F17')}", "",
      "| 기준 | 현대모비스 사례 | 출처 |", "|---|---|---|"] + [f"| {a} | {b} | {c} |" for a, b, c in case]
(OUT / "entry_case.md").write_text("\n".join(md) + "\n", encoding="utf-8")
(OUT / "my_entry.md").write_text(
    "# 우리 회사 진입 판단표 (회사 내부용 — 공개 저장소에 올리지 않는다)\n\n"
    "| 기준 | 우리 회사 평가(상·중·하) | 근거 한 줄 |\n|---|---|---|\n"
    "| ① 기술 거리 | | |\n| ② 원가 비중 | | |\n| ③ 첫 고객 | | |\n| ④ 양산 일정 | | |\n| ⑤ 원가 하락 대응 | | |\n", encoding="utf-8")
put("hmg_capacity", cap, 4, 0)
put("hmg_inhouse", inhouse, 4, 0)
put("hmg_inhouse_share", share, 4, 1)

# ───────── 대시보드 ─────────
def card(v, unit, cap_, src):
    return f'<div class="card"><b>{v}</b><span>{unit}</span><small>{cap_} {src}</small></div>'


bar_h = lambda v: round(v / bom25 * 180)
rows = "".join(f"<tr><td>{html.escape(a)}</td><td>{html.escape(b)}</td><td>{c}</td></tr>" for a, b, c in case)
page = f"""<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>로봇 밸류체인 대시보드</title><style>
:root{{--bg:#f7f7f5;--card:#fff;--ink:#1d1d1b;--muted:#6b6b66;--navy:#1B2C5E;--blue:#2E5BAA;--border:#e3e2dd;--soft:#EAF1FB}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#161615;--card:#21211f;--ink:#ecebe6;--muted:#a3a29c;--navy:#9db8e8;--blue:#7fb0e0;--border:#33332f;--soft:#1f2a3a}}}}
:root[data-theme="dark"]{{--bg:#161615;--card:#21211f;--ink:#ecebe6;--muted:#a3a29c;--navy:#9db8e8;--blue:#7fb0e0;--border:#33332f;--soft:#1f2a3a}}
*{{box-sizing:border-box}} body{{margin:0;background:var(--bg);color:var(--ink);font:15px/1.55 system-ui,-apple-system,"Malgun Gothic","Apple SD Gothic Neo",sans-serif}}
main{{max-width:1000px;margin:0 auto;padding:24px 16px 48px}} h1{{font-size:1.5rem;margin:4px 0}} h2{{font-size:1.1rem;margin:28px 0 10px}}
.note{{font-size:.8rem;padding:2px 8px;border:1px solid var(--border);border-radius:99px;color:var(--muted)}}
.grid{{display:grid;gap:12px;grid-template-columns:repeat(auto-fit,minmax(min(100%,220px),1fr))}}
.card{{background:var(--card);border:1px solid var(--border);border-radius:10px;padding:14px;min-width:0}}
.card b{{display:block;font-size:1.6rem;color:var(--navy)}} .card span{{color:var(--muted)}} .card small{{display:block;color:var(--muted);margin-top:4px}}
.bars{{display:flex;gap:28px;align-items:flex-end;height:220px;padding:10px 0}} .bar{{width:90px;background:var(--navy);border-radius:4px 4px 0 0}}
.bar.up{{background:transparent;border:2px dashed var(--blue)}} .col{{text-align:center;font-size:.9rem}}
.wrap{{overflow-x:auto}} table{{width:100%;border-collapse:collapse;font-size:.92rem}} th,td{{text-align:left;padding:6px 8px;border-bottom:1px solid var(--border)}} th{{color:var(--muted);font-weight:500}}
footer{{margin-top:28px;font-size:.84rem;color:var(--muted)}} a{{color:var(--blue)}}
</style></head><body><main>
<span class="note">공개 자료 기반 · 연도 뒤 E는 추정</span>
<h1>로봇 밸류체인 대시보드</h1>
<p>자동차 부품사 관점 — 시장은 얼마나 크고, 돈은 어디에 몰리며, 어디로 들어가나</p>
<h2>시장 카드</h2><div class="grid">
{card(f"{world_installs:,.0f}", "대", "세계 산업용 로봇 신규 설치 (2024)", cite("F01"))}
{card(f"{world_stock:,.0f}", "대", "세계 가동 대수 (2024, +9%)", cite("F02"))}
{card(f"{density:,.0f}", "대/종업원 1만 명", "한국 로봇 밀도 (2022 데이터)", cite("F05"))}
{card(f"{korea_share}%", "", "한국 신규 설치의 세계 비중 (2024, 계산값)", cite("F04"))}
</div>
<h2>휴머노이드 1대 BOM (BofA 추정, 중국 생산 기준)</h2>
<div class="card"><div class="bars">
<div class="col">$35,000<div class="bar" style="height:{bar_h(bom25)}px"></div>2025 {cite("F06")}</div>
<div class="col">below $17,000<div class="bar up" style="height:{bar_h(bom30)}px"></div>2030E (상한) {cite("F07")}</div>
</div><p>하락률 {drop}% 이상 · 연평균 {cagr_bom}% 이상 하락 (계산값)</p></div>
<h2>휴머노이드 연간 출하 (BofA 추정)</h2>
<div class="card wrap"><table><tr><th>연도</th><th>출하</th><th>출처</th></tr>
<tr><td>2025E</td><td>20,000대</td><td>{cite("F14")}</td></tr><tr><td>2030E</td><td>1.2 million대</td><td>{cite("F15")}</td></tr><tr><td>2035E</td><td>10 million대</td><td>{cite("F15")}</td></tr></table>
<p>2025E → 2030E {multiple}배 · 2025E → 2035E 연평균 {cagr_ship}% (계산값, BofA 원문 86%와 일치)</p></div>
<h2>진입 판단표 — 현대모비스 사례</h2>
<div class="card wrap"><p>현대차그룹 2028년 연 {cap:,.0f}대 생산 체계 목표 중 자사 공장 투입 {inhouse:,.0f}대 = {share}% (발표된 목표) {cite("F17")}</p>
<table><tr><th>기준</th><th>사례</th><th>출처</th></tr>{rows}</table></div>
<footer>숫자: 교재 『로봇 밸류체인 — 자동차 부품사의 진입 기회』 검증 자료(facts.csv). 출처 번호는 data/sources.md. 회사 내부 판단표는 이 페이지에 없다. 만든 방법: Claude Code 수업 learn-robot-valuechain.</footer>
</main></body></html>"""
Path("index.html").write_text(page, encoding="utf-8")
Path("expected.json").write_text(json.dumps({"values": expected}, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"완료: 계산값 {len(expected)}개, 출하 CAGR {cagr_ship}%, BOM 하락 {drop}%")
