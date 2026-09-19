# montar.py — junta as partes em index.html.
#
# A pagina e um arquivo so (e o que a Discloud serve), mas escrever 40 KB de
# HTML+CSS+JS num arquivo unico e o caminho curto pra editar a coisa errada.
# As partes ficam separadas aqui e o build cola.
#
# A lista de comandos NAO e escrita a mao: vem do registro do bot, gerada por
#   node -e "... paraApi() ..."  ->  site-cmds.json
# A versao anterior do site anunciava /abraco, /roleta e /paineljogos, que
# sumiram quando os comandos foram agrupados pra caber no teto de 100.
import io, json, os, re, sys

RAIZ = os.path.dirname(os.path.abspath(__file__))
def ler(n): return io.open(os.path.join(RAIZ, n), encoding='utf-8').read()

CORES = ['#c8ff2e', '#ff8a3d', '#ff5a5f', '#3ddad7', '#b39dff', '#ffd166', '#7bd389', '#f78ca0']


def _esc(s):
    return (str(s).replace('&', '&amp;').replace('<', '&lt;')
            .replace('>', '&gt;').replace('"', '&quot;'))


def _lista(js, nome):
    """Le um `const NOME = [ ['a','b'], ... ];` do arquivo de script."""
    bloco = re.search(r'const ' + nome + r' = \[(.*?)\n\];', js, re.S)
    if not bloco:
        return []
    linhas = []
    for linha in re.findall(r'\[(.*?)\],', bloco.group(1)):
        linhas.append(re.findall(r"'((?:[^'\\]|\\.)*)'", linha))
    return [[c.replace("\\'", "'") for c in l] for l in linhas if l]


def pre_renderizar(corpo, js):
    """
    Escreve no HTML o que o script escreveria no navegador.

    Os cartoes de recursos e de jogos nasciam de `innerHTML` na carga. Pra
    quem visita nao muda nada, mas pra um buscador muda tudo: ele le o HTML
    primeiro e so depois, as vezes, executa o script. Medido: a home tinha
    799 palavras no HTML estatico, e o resto dependia de o robo rodar JS.
    O script continua rodando e reescrevendo o mesmo conteudo — nao ha
    divergencia possivel, porque os dois lados saem da MESMA lista.
    """
    recs = _lista(js, 'RECURSOS')
    if recs:
        html = ''.join(
            '<article class="rec" style="--c:' + CORES[i % len(CORES)] + '">'
            + '<div class="num"><span>/' + str(i + 1).zfill(2) + '</span><em>////</em></div>'
            + '<h3>' + _esc(t) + '</h3><p>' + _esc(d) + '</p></article>'
            for i, (t, d) in enumerate(recs))
        corpo = corpo.replace('<div class="recursos" id="grade-recursos"></div>',
                              '<div class="recursos" id="grade-recursos">' + html + '</div>')

    jogos = _lista(js, 'JOGOS')
    if jogos:
        html = ''.join(
            '<article class="jogo" style="--c:' + CORES[i % len(CORES)] + '">'
            + '<div class="topo"><span>' + str(i + 1).zfill(3) + '</span><span>////</span></div>'
            + '<div class="palavra">' + _esc(p) + '</div>'
            + '<div class="ds">' + _esc(d) + '</div>'
            + '<div class="cmd">' + _esc(c) + '</div></article>'
            for i, (p, d, c) in enumerate(jogos))
        corpo = corpo.replace('<div class="trilho" id="trilho"></div>',
                              '<div class="trilho" id="trilho">' + html + '</div>')
    return corpo


cmds_json = sys.argv[1] if len(sys.argv) > 1 else r'C:\Users\reisj\AppData\Local\Temp\site-cmds.json' 
cmds = json.load(io.open(cmds_json, encoding='utf-8'))

dados = ('<script>window.__CMDS__=' +
         json.dumps(cmds, ensure_ascii=False, separators=(',', ':')) +
         ';</script>\n')

js = ler('index.js.html')
corpo = pre_renderizar(ler('index.body.html'), js)

html = ler('index.head.html') + ler('index.css2.html') + corpo + dados + js
io.open(os.path.join(RAIZ, 'index.html'), 'w', encoding='utf-8').write(html)

texto = re.sub(r'<script.*?</script>', '', html[html.index('<main'):], flags=re.S)
palavras = len(re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', texto)).split())
print('index.html:', len(html.encode('utf-8')), 'bytes ·', len(cmds), 'comandos ·',
      palavras, 'palavras no HTML estatico')
