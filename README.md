# fimdosemestrebot
Bot que conta quantos dias faltam pra acabar/começar o semestre de aulas da UFSC.

# Como usar?
http://t.me/fimdosemestrebot  
Pode ser usado tanto no chat privado com o bot indo até @fimdosemestrebot através da busca e lhe mandando um `/start` ou através do modo inline digitando `@fimdosemestrebot ` (em qualquer chat) e clicando na caixa de resultado que aparecer.

# Como executar/configurar o bot
Criar um arquivo `.env` com as variáveis presentes no `example.env` alterando seus valores.

FDS_TOKEN é o token do seu bot, você consegue esse token no [@BotFather](https://t.me/BotFather) no telegram.

MANTAINER é o seu id no telegram. Ele pode ser obtido pelo próprio comando `/set` do bot. Se você ainda não tiver permissão para realizar a operação ele exibe o seu id no chat.

```
poetry install
poetry shell
python -m fimdosemestrebot
```

## Como configurar no telegram:
Utilizar o comando `/set` seguido da data e hora do início do semestre e do final do semestre.

`/set 02-10-2021 00:00 01-12-2021 22:00`