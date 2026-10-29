
# Test Results — Phishing URL Awareness Checker

| # | Input | Expected | Actual | Result |
|---|---|---|---|---|
| 1 | `https://secure-login.demo.invalid/account` | No listed warning signs | No listed warning signs found | PASS |
| 2 | `http://192.0.2.10/verify` | IP address and HTTP warnings | 2 warnings: IP address, HTTP | PASS |
| 3 | `http://paypal.com@fake-login.invalid/signin` | @ symbol and HTTP warnings | 2 warnings: @ symbol, HTTP | PASS |
| 4 | `http://xn--e1afmkfd.invalid/login` | Punycode and HTTP warnings | 2 warnings: punycode, HTTP | PASS |
| 5 | `http://login.verify.account.security.portal.invalid/confirm` | 5+ hostname segments and HTTP warning | 2 warnings: hostname segments, HTTP | PASS |

## Test Notes

- All five sample inputs were tested.
- The URLs were treated as text only and were never opened.
- No warning signs does not prove a URL is safe.
