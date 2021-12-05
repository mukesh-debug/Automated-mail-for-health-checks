#!/usr/bin/env python3

import health_checks
import emails

sender='max007master@gmail.com'
recipient='mukeshmaxkumar2000@gmail.com'
subject=health_checks.error_identification(health_checks.cpu_usage(), health_checks.disk_free(), health_checks.free_memory(), health_checks.resolve_host())
if subject:
    message=emails.generate(sender, recipient, subject)
    print("message: ",message)
    emails.send(message)
else:
    print('No-Error identified, and thus no email sent.')
