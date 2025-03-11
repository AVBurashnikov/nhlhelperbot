from typing import Tuple

from helpers.constants import TROPHY_LIST
from helpers.formatters import bold, italic, underline
from helpers.message_cutter import split_message
from helpers.text_builder import text as _


def trophy_help_builder() -> Tuple[str, ...]:
    trophy_list = [
        _("Список наград NHL (AHL)", pre="🏆", fmt_func=bold, new_line=2)
    ]

    for trophy, value in TROPHY_LIST.items():
        trophy_list.append(
            _([
                _(f"• {trophy} ", fmt_func=(bold, underline)),
                _(value['descr'], fmt_func=italic, new_line=1),
                _(f"Вручается с: ", fmt_func=bold),
                _(f"{value['since']} г.", new_line=1)
            ])
        )
        if "stopped" in value:
            trophy_list.append(
                _([
                    _(f"Не вручается с: ", fmt_func=bold),
                    _(f"{value['stopped']} г.", new_line=1),
                    _(f"Последний обладатель: ", fmt_func=bold),
                    _(f"{value['last']} г.", new_line=1)
                ])
            )
        trophy_list.append(_(new_line=1))

    message = _(trophy_list)

    return split_message(message)
