
## flask
flask flask flask


# 📚 CSRF (Cross-Site Request Forgery) 강의 자료

---

## ✅ 1. 개념 소개

- **정의**: CSRF는 사용자가 인증된 상태에서 공격자가 의도한 요청을 **피해자 대신** 특정 웹 서버에 보내는 공격 기법이다.
- **예시 상황**:
  - 사용자가 웹사이트 `example.com`에 로그인한 상태
  - 공격자가 만든 악성 웹사이트를 방문하면 사용자의 쿠키를 이용해 `example.com`에 요청이 전송됨

---

## 🎯 2. 공격 조건

CSRF가 성공하려면 다음과 같은 조건이 필요하다:

| 조건 | 설명 |
|------|------|
| 1. 사용자가 로그인 상태여야 함 | 예: 세션 쿠키 유지 중 |
| 2. 요청이 자동으로 전송될 수 있어야 함 | `<img src=...>`, `<form>`, JS 자동 요청 등 |
| 3. 서버가 요청의 출처(origin)를 확인하지 않아야 함 | Referer 또는 Origin header 미검사 |

---

## 🧪 3. 공격 시나리오 예시

### 💥 예제: 비밀번호 변경

```html
<!-- 공격자의 사이트에 있는 코드 -->
<img src="http://example.com/change-password?pw=hacked1234">
```

### 💥 예제: 자동 전송 form

```html
<form action="http://example.com/change-email" method="POST">
  <input type="hidden" name="email" value="hacker@example.com">
  <input type="submit" value="Click me">
</form>
<script>
  document.forms[0].submit();
</script>
```

---

## 🛡️ 4. 방어 방법

| 방어법 | 설명 |
|--------|------|
| ✅ CSRF Token 사용 | 서버가 발급한 랜덤 토큰을 모든 중요 요청에 포함시켜야 함 |
| ✅ SameSite 쿠키 설정 | `SameSite=Strict` 또는 `Lax` 설정으로 외부 요청 차단 |
| ✅ Referer / Origin 검사 | 요청의 출처가 본인의 도메인인지 확인 |
| ✅ 사용자 확인 절차 추가 | 비밀번호 재입력, CAPTCHA 등 |

---

## 🔍 5. 실습 아이디어 (CTF 또는 내부 서버 기반)

- 로그인한 상태에서 CSRF 공격 HTML을 만들어 이메일 변경 시도
- CSRF Token이 적용된 경우, 어떻게 공격이 실패하는지 확인
- Burp Suite를 통해 요청 조작 실습

---

## 📝 6. 요약

- CSRF는 **인증된 사용자의 권한을 탈취**하는 공격
- 서버는 반드시 **CSRF Token**, **출처 확인**, **SameSite 쿠키** 등을 통해 방어해야 함
- 실습을 통해 자동 요청이 어떻게 동작하는지 눈으로 확인해보자!
