import urwid


def is_very_long(password: str) -> bool:
    return len(password) >= 12


def has_digit(password: str) -> bool:
    return any(elem.isdigit() for elem in password)


def has_letters(password: str) -> bool:
    return any(elem.isalpha() for elem in password)


def has_upper_letters(password: str) -> bool:
    return any(elem.isupper() for elem in password)


def has_lower_letters(password: str) -> bool:
    return any(elem.islower() for elem in password)


def has_symbols(password: str) -> bool:
    return any(not char.isalnum() for char in password)


def on_ask_change(edit: urwid.Edit, text: str) -> None:
    rating_password = sum([
        is_very_long(text),
        has_digit(text),
        has_letters(text),
        has_upper_letters(text),
        has_lower_letters(text),
        has_symbols(text),
    ])*2
    reply.set_text("Рейтинг этого пароля: %s" % rating_password)


def on_ask_exit(key: str) -> None:
    if key in 'esc':
        raise urwid.ExitMainLoop()


def main() -> None:
    global reply
    ask = urwid.Edit('Введите пароль: ', mask='*')
    reply = urwid.Text("")
    menu = urwid.Pile([ask, reply])
    menu = urwid.Filler(menu, valign='top')
    urwid.connect_signal(ask, 'change', on_ask_change)
    urwid.MainLoop(menu, unhandled_input=on_ask_exit).run()


if __name__ == '__main__':
    main()
