# paginas.py — gera as páginas de conteúdo do site.
#
# Por que existem: o site era UMA página de 817 palavras. Buscador costuma não
# indexar site fino em domínio novo — não por maldade, por economia: ele
# precisa de motivo pra gastar rastreamento. Cada página aqui responde UMA
# pergunta que alguém realmente digita ("bot de música pra discord", "como
# funciona xp por call"), com conteúdo que só quem fez o bot sabe escrever.
#
# Não são páginas de enganação: cada uma descreve de verdade como o módulo
# funciona, inclusive os limites. Página que promete o que o bot não faz volta
# como desinstalação.
#
# A lista de comandos vem do registro do próprio bot (o mesmo site-cmds.json
# que o montar.py usa), então nunca anuncia comando que não existe.
import io, json, os, re, sys

RAIZ = os.path.dirname(os.path.abspath(__file__))
def ler(n): return io.open(os.path.join(RAIZ, n), encoding='utf-8').read()

cmds_json = sys.argv[1] if len(sys.argv) > 1 else r'C:\Users\reisj\AppData\Local\Temp\site-cmds.json'
CMDS = json.load(io.open(cmds_json, encoding='utf-8'))

# O CSS do site inteiro, reaproveitado: as páginas têm que parecer o mesmo site.
_head = ler('index.head.html')
_css2 = ler('index.css2.html')
ESTILO = _head[_head.index('<style>'):] + _css2[:_css2.index('</style>') + len('</style>')]

SITE = 'https://visya.app.br'
CONVITE = ('https://discord.com/oauth2/authorize?client_id=1541625357730586756'
           '&permissions=1417774886134&scope=bot%20applications.commands')


def esc(s):
    return (str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'))


def pagina(arquivo, titulo, descricao, olho, h1, intro, corpo, atualizado='2026-09-19'):
    """Monta uma página inteira com o visual do site."""
    return f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(titulo)}</title>
<meta name="description" content="{esc(descricao)}">
<meta name="theme-color" content="#0b0b0c">
<link rel="icon" href="assets/brand/favicon.png">
<link rel="canonical" href="{SITE}/{arquivo}">
<meta property="og:title" content="{esc(titulo)}">
<meta property="og:description" content="{esc(descricao)}">
<meta property="og:image" content="{SITE}/assets/brand/visya-banner.png">
<meta property="og:type" content="article">
<meta property="og:url" content="{SITE}/{arquivo}">
<meta property="og:site_name" content="VISYA">
<meta property="og:locale" content="pt_BR">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght,SOFT,WONK@0,9..144,400;0,9..144,700;0,9..144,900;1,9..144,700&family=Space+Mono:wght@400;700&family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,600;12..96,700&display=swap">
<script type="application/ld+json">
{json.dumps({
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": titulo,
    "description": descricao,
    "inLanguage": "pt-BR",
    "url": f"{SITE}/{arquivo}",
    "dateModified": atualizado,
    "image": f"{SITE}/assets/brand/visya-banner.png",
    "author": {"@type": "Organization", "name": "VISYA", "url": f"{SITE}/"},
    "publisher": {"@type": "Organization", "name": "VISYA", "url": f"{SITE}/"},
    "isPartOf": {"@type": "WebSite", "name": "VISYA", "url": f"{SITE}/"},
}, ensure_ascii=False, indent=1)}
</script>
{ESTILO}
</head>
<body>

<svg width="0" height="0" style="position:absolute" aria-hidden="true"><symbol id="v" viewBox="0 0 1500 1067.66"><path fill="currentColor" d="M771.69,944.01c-29.55-17.73-49.39,7.48-88.66,28.1-73.57,38.63-162.36,21.98-215.5-40.61-30.54-35.97-40.23-79.57-29.06-125.24,16.19-66.19-22.79-134.12-88.1-152.59-32.88-9.3-59.79-27.32-78.12-56.33-51.99-82.32-24.91-191.95,59.95-239.9l46.91-26.51c10.34-5.84,16.39-16.82,16.71-28.85.62-23.85-1.11-47.72,1-71.25,8.38-93.18,88.72-156.15,180.14-156.22l348.62-.27c90.83-.07,168.9,66.53,176.43,157.8,1.93,23.38.59,46.44,1.09,70.27.26,12.35,6.6,23.26,17.24,29.28l49.24,27.84c89.32,50.5,107.26,159.45,57,246.14l-175.31,302.33c-48.02,82.81-156.39,109.89-238.01,60.93l-41.57-24.94ZM720.42,878.01c7.53,12.73,17.82,19.09,30.8,18.83,12.6-.25,23.02-6.78,29.98-18.71l77.22-132.51,104.56-181.48,110.69-192.37c6.22-10.82,3.92-24.89-2.14-33.92-5.82-8.68-15.69-14.86-28.54-14.87l-585.81-.18c-14.17,0-24.38,6.02-30.62,15.62-6.46,9.94-7.06,23.34-.98,33.87l60.21,104.33c16.56,28.7,44.56,45.57,75.26,53.45,72.44,18.61,111.47,90.82,91.68,161.41-9.35,33.35-2.25,68.29,14.82,97.15l52.88,89.39Z"/></symbol></svg>

<div class="prompt">
  <div class="prompt-in">
    <span class="cifrao">$</span>
    <a class="marca" href="./" aria-label="VISYA — início"><svg aria-hidden="true"><use href="#v"/></svg>VISYA</a>
    <nav class="caminho" aria-label="Páginas">
      <a href="./">/início</a>
      <a href="musica.html">/música</a>
      <a href="niveis.html">/níveis</a>
      <a href="economia.html">/economia</a>
      <a href="moderacao.html">/moderação</a>
      <a href="comandos.html">/comandos</a>
    </nav>
  </div>
</div>

<main id="topo">
<section class="secao">
  <div class="env cantos" data-canto="visya ▷" data-canto2="//// {esc(olho)}">
    <div class="olho">{esc(olho)}</div>
    <h1>{h1}</h1>
    <p class="sub">{intro}</p>
  </div>
</section>

{corpo}

<section class="secao risco">
  <div class="env">
    <div class="olho">adicionar</div>
    <h2>Põe o VISYA<br>no seu servidor</h2>
    <p class="sub">É grátis, e os módulos que você não usar ficam desligados.</p>
    <p style="margin-top:22px">
      <a class="btn p" href="{CONVITE}">Adicionar ao Discord</a>
      <a class="btn" href="https://painel.visya.app.br">Abrir o painel</a>
    </p>
  </div>
</section>
</main>

<footer>
  <div class="env pe">
    <div style="display:flex;align-items:center;gap:9px">
      <svg width="16" height="16" aria-hidden="true"><use href="#v"/></svg>
      VISYA · 2026
    </div>
    <nav>
      <a href="./">Início</a>
      <a href="comandos.html">Comandos</a>
      <a href="https://painel.visya.app.br" target="_blank" rel="noopener">Painel ↗</a>
      <a href="termos.html">Termos</a>
      <a href="privacidade.html">Privacidade</a>
    </nav>
    <div>feito no Brasil · pt-BR</div>
  </div>
</footer>
</body>
</html>
"""


def secao(olho, titulo, html):
    return f"""<section class="secao">
  <div class="env">
    <div class="olho">{esc(olho)}</div>
    <h2>{titulo}</h2>
    {html}
  </div>
</section>
"""


# ------------------------------------------------------------------ MÚSICA
musica = secao('como funciona', 'Ele procura a música<br>antes de tocar', """
    <p class="sub">A maior parte dos bots de música manda o nome que você digitou direto pra fonte de
    áudio e toca o primeiro resultado. É por isso que tanta gente pede Eagles e ouve banda cover,
    ou pede uma música e recebe a versão acelerada.</p>
    <p class="sub">O VISYA faz em duas etapas. Primeiro descobre <strong>qual é a gravação</strong>
    num catálogo de música, que devolve artista, título e duração certos. Só depois procura essa
    gravação específica pra tocar, conferindo o nome e a duração. Versão que foge do tempo da
    gravação original não entra: remix, acelerado e ao vivo quase nunca batem no mesmo segundo.</p>""") + \
secao('o detalhe chato', 'Prévia de 30 segundos<br>não passa', """
    <p class="sub">Parte das gravações oficiais é publicada como prévia: o catálogo anuncia a
    duração cheia, o áudio entregue tem trinta segundos, e acaba como se a música tivesse
    terminado. Sem erro, sem aviso.</p>
    <p class="sub">O VISYA confere isso antes de tocar e descarta. Quando a única versão inteira
    disponível não é a do artista, ele toca assim mesmo e <strong>avisa no aviso de "tocando
    agora"</strong> que aquela versão foi enviada por outra pessoa. Um cover que toca inteiro é
    melhor que o original que para no meio, mas você merece saber qual é qual.</p>
    <p class="sub">Se a versão escolhida não abrir, ele desce pra próxima da mesma música em vez de
    desistir e sair da chamada.</p>""") + \
secao('o resto', 'Fila, controles<br>e nó próprio', """
    <p class="sub">O áudio roda num nó dedicado, separado do bot. Isso importa na prática: uma
    reinicialização do bot não derruba a música, e a sessão é retomada.</p>
    <ul class="lista">
      <li><strong>Fila</strong> com nome ou link, playlist inteira e ordem visível.</li>
      <li><strong>Controles</strong> de pausar, retomar, pular, volume, repetir e parar.</li>
      <li><strong>Sai sozinho</strong> quando fica sem ninguém na chamada, ou depois de um tempo parado que você define.</li>
      <li><strong>Vigia</strong> que detecta música travada e destrava, em vez de ficar com "tocando agora" na tela sem som.</li>
    </ul>
    <p class="sub">Tudo em um comando só, <code>/musica</code>, com subcomandos.</p>""")

# ------------------------------------------------------------------ NÍVEIS
niveis = secao('como se pontua', 'Mensagem conta,<br>call conta mais', """
    <p class="sub">Cada mensagem rende experiência, com um intervalo mínimo entre elas pra que
    escrever cinquenta linhas seguidas não valha mais que conversar. Cada minuto de chamada rende
    também, e é aí que mora a diferença: comunidade viva é comunidade que fica em call.</p>
    <p class="sub">Os dois valores são configuráveis por servidor, e podem ser zerados
    independentemente. Dá para premiar só call, só chat, ou os dois.</p>""") + \
secao('anti-AFK', 'O relógio para<br>quando você não está lá', """
    <p class="sub">Contar do momento em que a pessoa entra até sair é o jeito fácil e errado.
    Bastaria entrar mudo e dormir. Exigir companhia também não resolve, porque dois AFKs na mesma
    chamada se fazem companhia.</p>
    <p class="sub">No VISYA o relógio liga e desliga conforme o estado muda. <strong>Não
    conta</strong> quem está com o microfone desligado por escolha própria, quem está com o som
    desligado, e quem está no canal de ausente do servidor. <strong>Conta</strong> quem foi
    silenciado pela moderação, porque ali a pessoa está presente, só foi calada.</p>
    <p class="sub">Além disso há teto de minutos por hora. Com o teto em vinte, uma chamada de
    cinco horas rende como uma hora e quarenta. Continua premiando quem fica, sem transformar
    dormir na chamada em estratégia.</p>""") + \
secao('a curva', 'Os primeiros níveis vêm rápido,<br>os últimos custam caro', """
    <p class="sub">O nível é a raiz da experiência dividida por cinco. Na prática:</p>
    <div class="tabela-wrap"><table class="tabela">
      <thead><tr><th>Nível</th><th>Experiência</th></tr></thead>
      <tbody>
        <tr><td>5</td><td>625</td></tr>
        <tr><td>10</td><td>2.500</td></tr>
        <tr><td>20</td><td>10.000</td></tr>
        <tr><td>40</td><td>40.000</td></tr>
        <tr><td>100</td><td>250.000</td></tr>
      </tbody>
    </table></div>
    <p class="sub">Isso é de propósito. Quem chega hoje vê progresso na primeira semana, e quem
    está há um ano continua tendo o que perseguir.</p>""") + \
secao('cargos', 'O cargo chega sozinho', """
    <p class="sub">Você diz quais cargos valem quais níveis e o bot troca sozinho quando a pessoa
    sobe, tirando o anterior pra ninguém acumular a escada inteira. Se você não configurar nada,
    ele reconhece cargos que já tenham o nível no nome, como "Nível 5" ou "Ativo 〔10+〕".</p>
    <p class="sub">Tem cartão de perfil com imagem, ranking do servidor e ranking separado de
    tempo em chamada.</p>""")

# ------------------------------------------------------------------ ECONOMIA
economia = secao('a moeda', 'O nome é seu', """
    <p class="sub">A moeda tem nome, plural e emoji definidos por você. Pode ser coins, pode ser
    gemas, pode ser o nome da piada interna do servidor. O bot escreve o que você escolheu em
    todos os lugares onde fala de dinheiro.</p>""") + \
secao('como se ganha', 'Conversando, ficando em call<br>e subindo de nível', """
    <ul class="lista">
      <li><strong>Mensagem</strong> — cada mensagem pontuada rende moeda, com o mesmo intervalo do sistema de níveis.</li>
      <li><strong>Chamada</strong> — cada minuto rende, usando o mesmo minuto já limitado pelas regras anti-AFK e pelo teto por hora.</li>
      <li><strong>Nível</strong> — subir de nível paga um bônus proporcional ao nível alcançado.</li>
      <li><strong>Diária e trabalho</strong> — dois comandos com tempo de espera próprio.</li>
      <li><strong>Jogos</strong> — acertar nos jogos do chat rende, e o cassino arrisca.</li>
    </ul>
    <p class="sub">Todos os valores são ajustáveis, inclusive para zero. É o que evita a inflação
    que mata economia de servidor: se o dinheiro entra sozinho sem parar, ninguém dá valor.</p>""") + \
secao('onde se gasta', 'Cargos, cores<br>e itens', """
    <p class="sub">A loja é montada pela equipe do servidor. Cada item tem nome e preço, e pode
    entregar um cargo que já existe.</p>
    <p class="sub">Cor é um tipo próprio de item: você informa a cor em hexadecimal e o bot cria o
    cargo colorido na primeira compra. <strong>Cor é troca, não coleção</strong> — comprar uma tira
    a anterior, porque no Discord vale a cor do cargo mais alto, e acumular deixaria a pessoa
    exibindo uma cor que não foi a que ela comprou.</p>
    <p class="sub">Tem ainda inventário com itens consumíveis, transferência entre membros com teto
    configurável, ranking dos mais ricos e ajuste manual pela equipe.</p>""")

# ------------------------------------------------------------------ MODERAÇÃO
moderacao = secao('hierarquia', 'O bot não passa<br>por cima de ninguém', """
    <p class="sub">A regra mais importante de um bot de moderação não é o que ele faz, é o que ele
    se recusa a fazer. O VISYA confere a hierarquia antes de qualquer ação: não age sobre quem está
    acima de quem pediu, nem sobre quem está acima dele próprio, e não mexe em cargo gerenciado por
    integração.</p>
    <p class="sub">Isso vale inclusive quando a ordem vem pela inteligência artificial. Pedir ao
    bot em linguagem natural para remover alguém não pula a checagem de permissão.</p>""") + \
secao('automático', 'O que roda sem<br>ninguém olhando', """
    <ul class="lista">
      <li><strong>Filtros</strong> de conteúdo, com listas e exceções por servidor.</li>
      <li><strong>Advertências</strong> com histórico, para a decisão não depender da memória de quem está de plantão.</li>
      <li><strong>Registros</strong> do que acontece: entradas, saídas, mensagens apagadas e editadas, mudanças de canal, cargo e voz.</li>
      <li><strong>Cargo automático</strong> na entrada e verificação por botão.</li>
    </ul>
    <p class="sub">Os registros são o que transforma discussão em fato. Quase toda briga de
    servidor termina em "eu não disse isso" — e o histórico responde.</p>""") + \
secao('tickets', 'Atendimento<br>em canal privado', """
    <p class="sub">Quem precisa de ajuda abre um chamado por botão e ganha um canal privado com a
    equipe. Ao fechar, a conversa inteira é salva em transcrição.</p>
    <p class="sub">Serve para suporte de comunidade, mas também para venda: a maior parte dos
    servidores de loja usa o chamado como balcão.</p>""")

# ------------------------------------------------------------------ COMANDOS
por_cat = {}
for nome, cat, desc, subs in CMDS:
    por_cat.setdefault(cat, []).append((nome, desc, subs))

blocos = []
for cat in sorted(por_cat, key=lambda c: (-len(por_cat[c]), c)):
    linhas = []
    for nome, desc, subs in sorted(por_cat[cat]):
        sub = ''
        if subs:
            sub = '<br><span class="mini">' + ' · '.join(esc(s) for s in subs) + '</span>'
        linhas.append(f'<tr><td><code>{esc(nome)}</code>{sub}</td><td>{esc(desc)}</td></tr>')
    blocos.append(f"""<section class="secao">
  <div class="env">
    <div class="olho">{esc(cat.lower())} — {len(por_cat[cat])} comandos</div>
    <h2>{esc(cat)}</h2>
    <div class="tabela-wrap"><table class="tabela">
      <thead><tr><th>Comando</th><th>O que faz</th></tr></thead>
      <tbody>{''.join(linhas)}</tbody>
    </table></div>
  </div>
</section>""")

n_sub = sum(len(x[3]) for x in CMDS)
comandos_corpo = ''.join(blocos)

# ------------------------------------------------------------------ escrita
CSS_TABELA = """
<style>
.tabela-wrap{overflow-x:auto;margin-top:22px;}
.tabela{border-collapse:collapse;width:100%;font-size:.93rem;}
.tabela th,.tabela td{text-align:left;padding:11px 14px;border-bottom:1px solid var(--line2);vertical-align:top;}
.tabela th{font-family:var(--mono);font-size:.68rem;letter-spacing:.14em;text-transform:uppercase;color:var(--ink3);}
.tabela td code{font-family:var(--mono);color:var(--lim);}
.tabela td:first-child{white-space:nowrap;}
ul.lista{margin:20px 0 0;padding-left:20px;color:var(--ink2);}
ul.lista li{margin:9px 0;max-width:62ch;}
</style>
"""

PAGINAS = [
    ('musica.html',
     'Bot de música para Discord — VISYA',
     'Como o VISYA toca música no Discord: acha a gravação certa antes de tocar, descarta prévia de 30 segundos e avisa quando a versão não é a do artista.',
     'módulo de música', 'Música no Discord<br>sem tocar a versão errada',
     'Fila, controles e nó de áudio próprio. E, principalmente, a parte que ninguém conta: como o bot decide qual gravação vai tocar.',
     musica),
    ('niveis.html',
     'Sistema de níveis e XP no Discord — VISYA',
     'XP por mensagem e por tempo em call com regra anti-AFK de verdade: mudo, surdo e canal de ausente não contam, e há teto de minutos por hora.',
     'módulo de níveis', 'Níveis que premiam<br>quem aparece de verdade',
     'Experiência por mensagem e por tempo em chamada, com as travas que impedem dormir na call de virar estratégia.',
     niveis),
    ('economia.html',
     'Economia, moeda e loja de cargos no Discord — VISYA',
     'Moeda com nome próprio, ganha conversando e ficando em call, gasta em cargos, cores e itens. Todos os valores configuráveis por servidor.',
     'módulo de economia', 'Uma economia que<br>o seu servidor controla',
     'Moeda com o nome que você escolher, ganha na conversa e na chamada, gasta em cargo, cor e item.',
     economia),
    ('moderacao.html',
     'Moderação automática e tickets no Discord — VISYA',
     'Filtros, advertências com histórico, registros completos e tickets com transcrição. O bot nunca age sobre quem está acima de quem pediu.',
     'módulo de moderação', 'Moderação que respeita<br>a hierarquia',
     'Filtros, advertências, registros e chamados. E uma regra que vale mais que todas: o bot não passa por cima de ninguém.',
     moderacao),
    ('comandos.html',
     f'Todos os {len(CMDS)} comandos do VISYA — bot de Discord em português',
     f'Lista completa dos {len(CMDS)} comandos e {n_sub} subcomandos do VISYA, com o que cada um faz. Gerada do registro do próprio bot.',
     'referência', f'{len(CMDS)} comandos,<br>{n_sub} subcomandos',
     'A lista sai do registro do próprio bot na API do Discord, então não anuncia comando que não existe. Free Fire vem desligado por padrão.',
     comandos_corpo),
]

for arquivo, titulo, desc, olho, h1, intro, corpo in PAGINAS:
    html = pagina(arquivo, titulo, desc, olho, h1, intro, corpo)
    html = html.replace('</head>', CSS_TABELA + '</head>')
    io.open(os.path.join(RAIZ, arquivo), 'w', encoding='utf-8').write(html)
    texto = re.sub(r'<[^>]+>', ' ', html[html.index('<main'):])
    print(f'{arquivo:18} {len(html.encode("utf-8")):>7} bytes · {len(texto.split()):>4} palavras')

# sitemap com tudo
hoje = '2026-09-19'
urls = [('', '1.0', 'weekly')] + [(a, '0.8', 'monthly') for a, *_ in PAGINAS] \
     + [('termos.html', '0.3', 'yearly'), ('privacidade.html', '0.3', 'yearly')]
sm = ['<?xml version="1.0" encoding="UTF-8"?>',
      '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for loc, pri, freq in urls:
    sm.append(f'  <url>\n    <loc>{SITE}/{loc}</loc>\n    <lastmod>{hoje}</lastmod>\n'
              f'    <changefreq>{freq}</changefreq>\n    <priority>{pri}</priority>\n  </url>')
sm.append('</urlset>')
io.open(os.path.join(RAIZ, 'sitemap.xml'), 'w', encoding='utf-8').write('\n'.join(sm) + '\n')
print(f'sitemap.xml        {len(urls)} endereços')
