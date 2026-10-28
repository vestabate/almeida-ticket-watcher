# Almeida ticket watcher: initial access test

Target: Golden Boy, Saturday 31 October 2026, 7:30pm. One ticket, maximum GBP 100 including fees. Any seat.

Status: manual diagnostic only. No scheduled monitoring, alerts, login, reservations or purchases.

## Run the access test
Open Actions, select Test booking page, then Run workflow on main. When it finishes, open the run and download booking-page-diagnostic. Inspect page.png and page.txt. A successful workflow only confirms script execution; it does not confirm ticket availability.

The diagnostic uses an unauthenticated browser and does not bypass CAPTCHA or queues. Its artifacts contain public booking-page content and are retained for three days. Do not add credentials or payment details to this public repository.

Next: verify the rendered booking page before implementing availability checks, price verification, notification delivery and a hard stop before the performance.
