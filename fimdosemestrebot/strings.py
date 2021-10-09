from datetime import date

CONFETTI = u'\U0001F38A'
HORN = u'\U0001F389'
PALM_TREE = u'\U0001F334'

TODAY = date.today()
HELP_TXT = """/start - Mostra os dias restantes
/help - Aparece este texto super útil e sobre como contribuir
GitHub: https://www.github.com/abarichello/fimdosemestrebot"""
DENIED = 'Unauthorized acess! :/'
INLINE = (
    'Este bot está disponível em modo inline, digite @fimdosemestrebot em QUALQUER chat para usar. '
    + CONFETTI
)

START_STRINGS = ['começou', 'começa', 'seguinte']
END_STRINGS = ['terminou', 'termina', 'atual']
