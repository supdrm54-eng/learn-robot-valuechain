# Block 5: 공개와 공유 — GitHub Pages

> **Phase A 시작 시 그대로 출력한다:**
> ```
> 📖 공식 문서: https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site · https://cli.github.com/manual/gh_repo_create · https://code.claude.com/docs/en/skills
> ```

## EXPLAIN

### 1. 용어

| 용어 | 뜻 |
|---|---|
| 저장소 | GitHub에 올린 폴더. 파일과 바뀐 기록(커밋)이 함께 남는다 |
| GitHub Pages | 저장소의 `index.html`을 `https://내아이디.github.io/저장소이름/` 주소로 보여 주는 무료 기능 |
| 공개 전 점검 | 비밀값·개인정보·**회사 자료**가 섞였는지, 출처와 'E' 표시가 있는지 확인하는 것 |
| .gitignore | 저장소에 올리지 않을 파일 목록 — Block 0에서 `my_*.md`를 넣어 두었다 |

### 2. 무엇을 공개하고 무엇을 남기나

| 공개해도 되는 것 | 공개하면 안 되는 것 |
|---|---|
| 대시보드(공개 숫자·출처), 계산표, 출처 검증표, 현대모비스 판단표 | `my_company_map.md`, `my_entry.md` — 우리 회사 제품·고객·약점 |
| facts.csv·sources.md (공개 자료 정리) | 회사 내부 원가·수주·전략 문서 |

### 3. 보안 수칙

- GitHub 로그인은 Claude Code가 보여 주는 **일회용 코드**를 브라우저 `github.com/login/device`에 넣고 **Authorize**까지 누른다. 코드는 약 15분 뒤 만료된다. 비밀번호·토큰은 채팅이나 파일에 쓰지 않는다.
- 커밋 작성자는 개인 이메일 대신 GitHub noreply 주소를 쓴다.
- 공개는 되돌리기 어렵다. 점검 결과를 보고 내가 "공개해"라고 말한 뒤에만 올린다.

## EXECUTE

아래 프롬프트를 붙여 넣으라고 안내한다.

```
robot-vc-lab 폴더를 GitHub Pages로 공개할 준비를 해 줘. 공개는 내가 "공개해"라고 말한 뒤에만 해.

1. 공개 전 점검: ① 비밀번호·토큰·이메일·전화번호 패턴 ② .gitignore 에 my_*.md 와 env_check.txt 가 있고 실제로 올라갈 목록에서 빠지는지 ③ index.html 에 "공개 자료 기반 · E는 추정" 표시와 [S#] 출처가 있는지 ④ 올라갈 파일 목록. 결과를 output/publish_check.md 에 적고 요약해 줘.
2. README.md 를 만들어 줘: 무엇을 했는지 3줄, 대시보드 주소 자리, 데이터 출처(data/sources.md 요약), 이 수업 learn-robot-valuechain 을 따랐다는 한 줄.
3. 동료에게 보낼 공유 메시지를 output/share_message.md 에 써 줘: 대시보드 주소 자리, 핵심 숫자 3줄(출처 포함), 같은 수업을 설치하는 방법.
4. 여기까지 하고 멈춰서 점검 결과를 보여 줘. 내가 "공개해"라고 하면 그때:
   - gh 로그인을 확인하고, 안 되어 있으면 브라우저 로그인용 일회용 코드만 알려 줘. 로그인되면 gh auth setup-git 을 해 줘.
   - git 작성자가 비어 있으면 GitHub noreply 주소를 이 저장소에만 설정해 줘.
   - git 저장소로 만들고 커밋한 뒤, public 저장소 robot-vc-dashboard 를 만들어 올리고 Pages(main, /)를 켜서 주소가 열릴 때까지 확인해 줘.
   - README.md 와 share_message.md 의 주소 자리를 실제 주소로 바꿔 커밋해 줘.
```

### 확인할 것 (Phase B)

- `output/publish_check.md`: 비밀값·개인정보 패턴 0건, 올라갈 목록에 `my_*.md`·`env_check.txt`가 없다, `data/` 자료 3개.
- 수강생이 "공개해"라고 답한 경우에만: `gh repo view robot-vc-dashboard`가 public이고, Pages 주소에서 시장 카드·BOM 차트·판단표가 보인다.
- 공개하지 않기로 했다면 저장소를 만들지 않았다.

막히면 원인을 Claude Code에게 찾게 하는 후속 프롬프트를 준다. 정답은 "정답 보기" 요청이 있을 때만 연다.

```
my_entry.md 가 git 에 올라갈 목록에 들어 있다. .gitignore 내용과 git status 를 보여 주고, 이미 커밋됐다면 원격에 올리기 전에 기록에서 빼는 방법을 먼저 설명해 줘. 실행은 내 허락을 받고 해.
```

## QUIZ

### Quiz 1 — 판단표까지 공개하자는 동료

```json
AskUserQuestion({
  "questions": [{
    "question": "동료가 \"우리 회사 진입 판단표(my_entry.md)도 대시보드에 같이 올리면 더 설득력 있겠다\"고 한다. 판단표에는 우리 제품, 고객 후보, 가장 약한 기준이 적혀 있다. 어떻게 답할까?",
    "header": "Quiz 1",
    "options": [
      {"label": "회사명만 지우고 올린다", "description": "회사 이름을 빼면 누구 것인지 모른다"},
      {"label": "올려도 된다", "description": "공개 저장소라도 아무도 찾아보지 않는다"},
      {"label": "공개 저장소에는 올리지 않는다", "description": "제품·고객 후보·약점은 회사 정보다. 공개 대시보드는 공개 숫자와 공개 사례만 담고, 판단표는 사내에서 공유한다"}
    ],
    "multiSelect": false
  }]
})
```

정답: 3번. ① 판단표의 '약한 기준'과 '고객 후보'는 경쟁사가 가장 알고 싶어 하는 정보다. 공개 저장소는 누구나 내려받고 기록이 남는다. ② 1번은 제품·고객 후보만으로도 회사를 특정할 수 있다는 점을 놓쳤다. 2번은 공개가 되돌리기 어렵다는 점을 놓쳤다. ③ 그래서 Block 0에서 `.gitignore`로 `my_*.md`를 처음부터 막아 두었다.

### Quiz 2 — 동료의 대시보드 숫자가 다르다

```json
AskUserQuestion({
  "questions": [{
    "question": "같은 수업을 들은 동료의 대시보드에는 \"BOM 연평균 하락 13.4%\" 대신 \"BOM 하락 2030년 $17,000\"만 있고, 출하 연평균 증가율은 86.2%가 아니라 117.5%로 나와 있다. 가장 먼저 확인할 것은?",
    "header": "Quiz 2",
    "options": [
      {"label": "계산의 처음 값·끝 값·햇수", "description": "출하 증가율은 2025E→2035E 10년으로 계산해야 한다. 햇수를 다르게 넣었는지부터 본다"},
      {"label": "동료 PC 성능", "description": "컴퓨터에 따라 계산 결과가 달라질 수 있다"},
      {"label": "내 결과가 공개됐으니 내가 맞다", "description": "먼저 공개한 쪽이 정답이다"}
    ],
    "multiSelect": false
  }]
})
```

정답: 1번. ① 연평균 증가율은 처음 값·끝 값·햇수 세 가지로 정해진다. 20,000 → 10 million을 10년으로 계산하면 86.2%로 BofA 원문 86%와 맞지만, 8년으로 잘못 넣으면 117.5%가 나온다. 같은 facts.csv에서 다른 숫자가 나오면 계산 조건부터 대조한다. ② 2번은 근거 없는 추측이고, 3번은 공개 여부와 정답 여부를 혼동했다. ③ 저장소에 계산표(cost_calc.md)가 함께 있으면 이 대조가 몇 분이면 끝난다 — 공개의 진짜 가치다.

## 과제와 다음

1. **우리 회사 진입 판단표 완성** — `my_entry.md`의 5기준을 채우고 가장 약한 기준 하나와 그 보완 방법을 한 단락으로 쓴다. 제출물: 사내 공유용 1쪽(공개 저장소 금지).
2. **원문 맞춰 보기 하나 더** — facts.csv의 '확인' 숫자 하나를 골라 sources.md의 원문 주소를 열고, 원문 표현·단위·기준연도가 facts.csv와 같은지 확인한다. 제출물: 확인 결과 3줄.
3. **내 강의 하나 더** — `/course-forge`를 다시 실행해 다른 Day(예: Day4 업무 자동화)나 내 업무 주제로 learn 스킬을 하나 더 만든다. 제출물: 새 learn 스킬 저장소 주소.
