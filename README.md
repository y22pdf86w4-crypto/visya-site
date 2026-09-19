# VISYA — site oficial

Página única do **VISYA**, um bot para Discord em português.

**Site:** <https://visya.app.br/>
**Painel de configuração:** <https://painel.visya.app.br>
**Adicionar ao seu servidor:** [link de convite](https://discord.com/oauth2/authorize?client_id=1541625357730586756&permissions=1417774886134&scope=bot%20applications.commands)
**Ficha na vitrine do Discord:** <https://discord.com/discovery/applications/1541625357730586756>

## O que é o VISYA

Bot verificado pela Discord, com 103 comandos em português e 104 modelos de
servidor prontos. Moderação, níveis por mensagem e por tempo em call, economia
com moeda própria e loja de cargos, tickets de atendimento, jogos no chat e
música com nó de áudio próprio. A configuração é feita por painel web, sem
precisar decorar comando.

Serve comunidade, loja, time de jogo ou empresa — os módulos ligam e desligam
por servidor.

## Este repositório

Só o site. O bot e o painel ficam em repositórios separados e privados.

```
index.head.html   <head>, metadados e o começo do CSS
index.css2.html   o resto do CSS
index.body.html   o conteúdo da página
index.js.html     o script
montar.py         cola as partes em index.html
```

A página servida é o `index.html`, um arquivo só. As partes existem porque
editar 50 KB de HTML, CSS e JS num arquivo único é o caminho curto pra mexer
na coisa errada.

A lista de comandos não é escrita à mão: vem do registro do próprio bot na API
do Discord.

### Build

```bash
python3 montar.py caminho/para/site-cmds.json
```

O deploy é automático: push na branch principal publica no
[Discloud](https://discloud.com/).

## Páginas

| Arquivo | Endereço |
|---|---|
| `index.html` | <https://visya.app.br/> |
| `termos.html` | <https://visya.app.br/termos.html> |
| `privacidade.html` | <https://visya.app.br/privacidade.html> |

Contato: `reisjoaog@hotmail.com`
