import json
import os

ARQUIVO = "metas.json"

# Função para carregar as metas do arquivo


def carregar():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    return []

# Função para salvar metas no arquivo


def salvar(metas):
    with open(ARQUIVO, "w") as f:
        json.dump(metas, f, indent=4)

# Função para criar meta


def criar_meta():
    nome = input("Digite o nome da meta: ")
    descricao = input("Digite uma descrição: ")

    metas = carregar()  # pega todas as metas existentes
    nova = {
        "id": len(metas) + 1,
        "nome": nome,
        "descricao": descricao,
        "status": "em andamento"
    }
    metas.append(nova)  # adiciona a nova meta
    salvar(metas)       # salva no arquivo
    print(f"✅ Meta '{nome}' criada com sucesso!")

# Função para listar metas


def listar_metas():
    metas = carregar()
    if not metas:
        print("⚠️ Nenhuma meta cadastrada ainda.")
        return

    print("\n=== LISTA DE METAS ===")
    for meta in metas:
        print(f"[{meta['id']}] {meta['nome']} - {meta['status']}")
        print(f"   Descrição: {meta['descricao']}")


def atualizar_meta():
    listar_metas()
    try:
        id_meta = int(input("Digite o ID da meta para atualizar: "))
    except ValueError:
        print("⚠️ Digite um número válido.")
        return

    novo_status = input(
        "Novo status (em andamento/concluído): ").strip().lower()
    if novo_status not in ["em andamento", "concluído"]:
        print("⚠️ Status inválido.")
        return

    metas = carregar()
    for meta in metas:
        if meta["id"] == id_meta:
            meta["status"] = novo_status
            salvar(metas)
            print("✅ Meta atualizada com sucesso!")
            return

    print("⚠️ Meta não encontrada.")


def deletar_meta():
    listar_metas()  # mostra as metas para o usuário escolher
    try:
        id_meta = int(input("Digite o ID da meta para excluir: "))
    except ValueError:
        print("⚠️ Digite um número válido.")
        return

    metas = carregar()
    novas_metas = [m for m in metas if m["id"] != id_meta]

    if len(novas_metas) == len(metas):
        print("⚠️ Meta não encontrada.")
        return

    # Reorganizar IDs
    for i, meta in enumerate(novas_metas, start=1):
        meta["id"] = i

    salvar(novas_metas)
    print("✅ Meta excluída com sucesso!")


# Menu principal
def menu():
    while True:
        print("\n=== GERENCIADOR DE METAS ===")
        print("1 - Criar meta")
        print("2 - Listar metas")
        print("3 - Atualizar meta (em breve)")
        print("4 - Excluir meta (em breve)")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_meta()
        elif opcao == "2":
            listar_metas()
        elif opcao == "3":
            atualizar_meta()
        elif opcao == "4":
            deletar_meta()
        elif opcao == "5":
            print("Saindo... até mais!")
            break
        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    menu()
