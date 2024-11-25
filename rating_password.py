import urwid

POSITIVE = 2
NEGATIVE = 0


def is_very_long(password: str) -> int:
    return POSITIVE if len(password) >= 12 else NEGATIVE


def has_digit(password: str) -> int:
    return POSITIVE if any(elem.isdigit() for elem in password) else NEGATIVE


def has_letters(password: str) -> int:
    return POSITIVE if any(elem.isalpha() for elem in password) else NEGATIVE


def has_upper_letters(password: str) -> int:
    return POSITIVE if any(elem.isupper() for elem in password) else NEGATIVE


def has_lower_letters(password: str) -> int:
    return POSITIVE if any(elem.islower() for elem in password) else NEGATIVE


def has_symbols(password: str) -> int:
    return POSITIVE if any((elem == '#' or elem == '%')
                           for elem in password) else NEGATIVE


def on_ask_change(edit: urwid.Edit, text: str) -> None:
    rating_password = sum([
        is_very_long(text),
        has_digit(text),
        has_letters(text),
        has_upper_letters(text),
        has_lower_letters(text),
        has_symbols(text),
        ]
    )
    reply.set_text("Рейтинг этого пароля: %s" % rating_password)


def on_ask_exit(key: str) -> None:
    if key in 'esc':
        raise urwid.ExitMainLoop()


ask = urwid.Edit('Введите пароль: ', mask='*')
reply = urwid.Text("")
menu = urwid.Pile([ask, reply])
menu = urwid.Filler(menu, valign='top')
urwid.connect_signal(ask, 'change', on_ask_change)
urwid.MainLoop(menu, unhandled_input=on_ask_exit).run()
