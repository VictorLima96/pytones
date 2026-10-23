from pathlib import Path

ARQUIVO = Path("agenda.txt")

def carregar():
    """Lê o arquivo e retorna o dicionário de contatos."""
    if not ARQUIVO.exists(): return {}
    contatos = {}
    for linha in ARQUIVO.read_text(encoding="utf-8").splitlines():
        if len(dados := linha.split("|")) == 4:
            n, s, t, e = dados
            contatos[n.lower()] = {"nome": n, "sobrenome": s, "telefone": t, "email": e}
    return contatos

def salvar(contatos):
    """Grava o dicionário de volta no arquivo."""
    linhas = [f"{c['nome']}|{c['sobrenome']}|{c['telefone']}|{c['email']}\n" for c in contatos.values()]
    ARQUIVO.write_text("".join(linhas), encoding="utf-8")

def gerenciar_contato(contatos, acao):
    """Agrupa as operações de busca, atualização e exclusão para evitar repetição."""
    nome = input(f"\nDigite o nome para {acao}: ").strip().lower()
    if nome not in contatos:
        return print("Contato não encontrado.")
    
    c = contatos[nome]
    if acao == "buscar":
        print(f"\nNome: {c['nome']} {c['sobrenome']}\nTel: {c['telefone']}\nE-mail: {c['email']}")
    elif acao == "atualizar":
        c['sobrenome'] = input(f"Novo Sobrenome [{c['sobrenome']}]: ").strip() or c['sobrenome']
        c['telefone'] = input(f"Novo Telefone [{c['telefone']}]: ").strip() or c['telefone']
        c['email'] = input(f"Novo E-mail [{c['email']}]: ").strip() or c['email']
        salvar(contatos)
        print("Contato atualizado!")
    elif acao == "apagar" and input(f"Apagar {c['nome']}? (s/n): ").strip().lower() == 's':
        del contatos[nome]
        salvar(contatos)
        print("Contato apagado!")

def criar_contato(contatos):
    """Cria um novo contato na agenda."""
    if not (nome := input("\nNome: ").strip()): return print("O nome não pode ser vazio.")
    if nome.lower() in contatos: return print("Esse contato já existe!")
    
    contatos[nome.lower()] = {
        "nome": nome,
        "sobrenome": input("Sobrenome: ").strip(),
        "telefone": input("Telefone: ").strip(),
        "email": input("E-mail: ").strip()
    }
    salvar(contatos)
    print(f"Contato '{nome}' salvo!")

def menu_principal():
    contatos = carregar()
    acoes = {"1": lambda: criar_contato(contatos), "2": lambda: gerenciar_contato(contatos, "buscar"),
             "3": lambda: gerenciar_contato(contatos, "atualizar"), "4": lambda: gerenciar_contato(contatos, "apagar")}
    
    while True:
        opcao = input("\n1-Novo | 2-Procura | 3-Atualiza | 4-Apaga | 0-Sair\nEscolha: ").strip()
        if opcao == "0": break
        acoes.get(opcao, lambda: print("Opção inválida!"))()

if __name__ == "__main__":
    menu_principal()
