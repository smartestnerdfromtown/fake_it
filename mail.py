from typing import Optional
import random as rn

domains = [
    "gmail.com", "yahoo.com", "outlook.com", "hotmail.com",
    "icloud.com", "mail.com", "protonmail.com", "yandex.ru",
    "yandex.com", "mail.ru", "bk.ru", "inbox.ru", "list.ru",
    "rambler.ru", "zoho.com", "gmx.com", "gmx.de", "aol.com",
    "live.com", "msn.com", "fastmail.com", "tutanota.com"
]

def generate_email(
    name: str,
    surname: str,
    random_domain: bool,
    specific_domain: Optional[str] = None,
    nickname: Optional[str] = None,
) -> str:

    if nickname:
        username = nickname.lower()
    else:
        username = f"{name}.{surname}".lower()

    if random_domain:
        domain = rn.choice(domains)
    elif specific_domain:
        domain = specific_domain
    else:
        raise ValueError("Either random_domain=True or specific_domain must be provided")

    return f"{username}@{domain}"
