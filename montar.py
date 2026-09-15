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
import io, json, os, sys

RAIZ = os.path.dirname(os.path.abspath(__file__))
def ler(n): return io.open(os.path.join(RAIZ, n), encoding='utf-8').read()

cmds_json = sys.argv[1] if len(sys.argv) > 1 else r'C:\Users\reisj\AppData\Local\Temp\site-cmds.json'
cmds = json.load(io.open(cmds_json, encoding='utf-8'))

dados = ('<script>window.__CMDS__=' +
         json.dumps(cmds, ensure_ascii=False, separators=(',', ':')) +
         ';</script>\n')

html = ler('index.head.html') + ler('index.css2.html') + ler('index.body.html') + dados + ler('index.js.html')
io.open(os.path.join(RAIZ, 'index.html'), 'w', encoding='utf-8').write(html)

print('index.html:', len(html.encode('utf-8')), 'bytes ·', len(cmds), 'comandos')
