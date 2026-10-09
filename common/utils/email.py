from django.core.mail import EmailMessage

def send_email(to, subject, content, sender='admin@example.com'):
    # If a single email string is passed, wrap it in a list
    if isinstance(to, str):
        to = [to]
        
    email = EmailMessage(
        subject=subject,
        body=content,
        from_email=sender,
        to=to,
    )
    # Set the content subtype to HTML so it renders correctly
    email.content_subtype = 'html'

    return email.send()