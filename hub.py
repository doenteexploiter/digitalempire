#!/usr/bin/env python3
"""
    ,----------------,              ,---------,           
        ,-----------------------,          ,"        ,"|           
      ,"                      ,"|        ,"        ,"  |           
     +-----------------------+  |      ,"        ,"    |           
     |  .-----------------.  |  |     +---------+      |           
     |  |                 |  |  |     | -==----'|      |           
     |  |  I LOVE FEMBOYS!   |  |     |         |      |              
     |  |  Bad command or |  |  |/----|`---=    |      |           
     |  |  C:\&gt;_          |  |  |   ,/|==== ooo     |      ;           
     |  |                 |  |  |  // |(((( [33]|    ,"            
     |  `-----------------'  |," .;'| |((((     |  ,"              
     +-----------------------+  ;;  | |         |,"     
        /_)______________(_/  //'   | +---------+                  
   ___________________________/___  `,                             
  /  oooooooooooooooo  .o.  oooo /,   \,"-----------               
 / ==ooooooooooooooo==.o.  ooo= //   ,`\--{)B     ,"               
/_==__==========__==_ooo__ooo=_/'   /___________,"                 
`-----------------------------'

Instagram DM Bot - Envio automático de mensagens diretas
"""

import os
import sys
import time
import random
import threading
from colorama import init, Fore, Style

# Inicializa colorama no Windows
init(autoreset=True)

# ─── ARTE ASCII ───────────────────────────────────────────────────────────────

ASCII_ART = r"""
             ,----------------,              ,---------,           
        ,-----------------------,          ,"        ,"|           
      ,"                      ,"|        ,"        ,"  |           
     +-----------------------+  |      ,"        ,"    |           
     |  .-----------------.  |  |     +---------+      |           
     |  |                 |  |  |     | -==----'|      |           
     |  |  I LOVE FEMBOYS!   |  |     |         |      |              
     |  |  Bad command or |  |  |/----|`---=    |      |           
     |  |  C:\&gt;_          |  |  |   ,/|==== ooo     |      ;           
     |  |                 |  |  |  // |(((( [33]|    ,"            
     |  `-----------------'  |," .;'| |((((     |  ,"              
     +-----------------------+  ;;  | |         |,"     
        /_)______________(_/  //'   | +---------+                  
   ___________________________/___  `,                             
  /  oooooooooooooooo  .o.  oooo /,   \,"-----------               
 / ==ooooooooooooooo==.o.  ooo= //   ,`\--{)B     ,"               
/_==__==========__==_ooo__ooo=_/'   /___________,"                 
`-----------------------------'
"""

# ─── MENSAGENS ────────────────────────────────────────────────────────────────

MENSAGENS = [
    "Olá! Tudo bem?\nMeu nome é Isaac e sou programador especializado na criação de sites modernos para academias e negócios fitness.",
    "Percebi que hoje ter uma presença profissional na internet faz muita diferença para atrair novos alunos e fortalecer a marca da academia. Por isso, desenvolvo sites modernos, rápidos e totalmente responsivos, com visual premium e integração com Instagram, WhatsApp, planos, avaliações e muito mais.",
    "Posso criar um site personalizado para sua academia com design profissional, versão para celular e computador, divulgação dos planos e serviços, visual premium para atrair mais alunos.",
    "Isso faz total diferença no perfil de vocês. Entrego ele agora se você quiser, cobro apenas R$30,00 e entrego primeiro pra provar que não é golpe nem nada do tipo.",
    "Obrigado pela atenção!"
]

# ─── ANIMAÇÃO DE CORES ────────────────────────────────────────────────────────

CORES = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
animacao_ativa = True

def animacao_ascii():
    """Faz a arte ASCII mudar de cor em loop."""
    while animacao_ativa:
        for cor in CORES:
            if not animacao_ativa:
                break
            sys.stdout.write('\033[H\033[J')  # limpa terminal
            sys.stdout.write(cor + ASCII_ART + Style.RESET_ALL)
            sys.stdout.write(f"\n{Fore.WHITE}Instagram DM Bot - v1.0{Style.RESET_ALL}\n")
            sys.stdout.flush()
            time.sleep(0.8)

# ─── FUNÇÃO PRINCIPAL ─────────────────────────────────────────────────────────

def enviar_mensagens(cl, usuario_alvo):
    """Envia as 5 mensagens em sequência para o usuário alvo."""
    try:
        # Resolve o user_id a partir do @
        user_id = cl.user_id_from_username(usuario_alvo.replace("@", ""))
        print(f"\n{Fore.CYAN}[✓] Usuário @{usuario_alvo.replace('@', '')} encontrado!{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[*] Iniciando envio de 5 mensagens...{Style.RESET_ALL}\n")

        for i, msg in enumerate(MENSAGENS, 1):
            print(f"{Fore.GREEN}[{i}/5] Enviando: {msg[:60]}...{Style.RESET_ALL}")
            cl.direct_send(msg, [user_id])
            
            if i < 5:
                delay = random.uniform(2.0, 4.0)
                print(f"{Fore.BLUE}    Aguardando {delay:.1f}s...{Style.RESET_ALL}")
                time.sleep(delay)

        print(f"\n{Fore.GREEN}{'='*60}")
        print(f"[✓] TODAS AS 5 MENSAGENS ENVIADAS COM SUCESSO!")
        print(f"{'='*60}{Style.RESET_ALL}")

    except Exception as e:
        print(f"\n{Fore.RED}[✗] ERRO: {e}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Dicas: verifique se o @ existe e se sua conta não está bloqueada.{Style.RESET_ALL}")

# ─── MAIN ─────────────────────────────────────────────────────────────────────

def main():
    global animacao_ativa

    # Inicia animação em thread separada
    thread_anim = threading.Thread(target=animacao_ascii, daemon=True)
    thread_anim.start()

    time.sleep(2)  # deixa a animação rodar um pouco

    # Para a animação para mostrar os inputs
    animacao_ativa = False
    time.sleep(0.3)
    sys.stdout.write('\033[H\033[J')
    sys.stdout.flush()

    # Mostra a arte estática em branco
    print(Fore.WHITE + ASCII_ART + Style.RESET_ALL)
    print(f"{Fore.CYAN}{'='*60}")
    print("  BOT DE MENSAGEM DIRETA - INSTAGRAM")
    print(f"{'='*60}{Style.RESET_ALL}\n")

    # ─── CREDENCIAIS ──────────────────────────────────────────────────────────
    try:
        from instagrapi import Client
    except ImportError:
        print(f"{Fore.RED}[!] Biblioteca 'instagrapi' não encontrada.")
        print(f"[!] Instale com: pip install instagrapi{Style.RESET_ALL}")
        sys.exit(1)

    meu_user = input(f"{Fore.YELLOW}[?] Seu @ do Instagram: {Style.RESET_ALL}").strip()
    minha_senha = input(f"{Fore.YELLOW}[?] Sua senha: {Style.RESET_ALL}").strip()
    alvo = input(f"{Fore.YELLOW}[?] @ da empresa que você quer mandar mensagem: {Style.RESET_ALL}").strip()

    print(f"\n{Fore.CYAN}[*] Fazendo login como @{meu_user}...{Style.RESET_ALL}")

    cl = Client()

    # ─── SESSÃO PERSISTENTE (opcional) ────────────────────────────────────────
    sessao_arquivo = f"sessao_{meu_user}.json"
    if os.path.exists(sessao_arquivo):
        try:
            cl.load_settings(sessao_arquivo)
            cl.login(meu_user, minha_senha)
            print(f"{Fore.GREEN}[✓] Login via sessão salva!{Style.RESET_ALL}")
        except Exception:
            print(f"{Fore.YELLOW}[!] Sessão expirada, fazendo login normal...{Style.RESET_ALL}")
            cl.login(meu_user, minha_senha)
    else:
        cl.login(meu_user, minha_senha)
        print(f"{Fore.GREEN}[✓] Login realizado com sucesso!{Style.RESET_ALL}")

    # Salva sessão para não precisar logar toda vez
    cl.dump_settings(sessao_arquivo)
    print(f"{Fore.BLUE}[i] Sessão salva em: {sessao_arquivo}{Style.RESET_ALL}")

    # ─── ENVIA AS MENSAGENS ───────────────────────────────────────────────────
    enviar_mensagens(cl, alvo)

    print(f"\n{Fore.MAGENTA}Finalizado. Pressione Enter para sair...{Style.RESET_ALL}")
    input()

if __name__ == "__main__":
    main()