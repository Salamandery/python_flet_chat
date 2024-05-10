import flet as ft

def main(pagina):
    def mensagem_tunnel(mensagem):
        print("mensagem enviada para todos")
        print(mensagem)
        chat.controls.append(ft.Text(mensagem))
        pagina.update()

    pagina.pubsub.subscribe(mensagem_tunnel)

    def enviar_msg(evento):
        texto_mensagem = campo_mensagem.value
        usuario_mensagem = usuario.value
        campo_mensagem.value = ""
        mensagem = f"# {usuario_mensagem}: {texto_mensagem}"
        print("enviou")
        print(mensagem)
        pagina.pubsub.send_all(mensagem)
        pagina.update()

    def entrar_chat(evento):
        print("entrou")
        pagina.remove(titulo)
        pagina.remove(botao_iniciar)
        popup.open = False
        pagina.add(chat)
        pagina.add(linha_mensagem)
        mensagem = f"- entrou {usuario.value}"
        pagina.pubsub.send_all(mensagem)
        pagina.update()


    def iniciar_chat(evento):
        print("site")
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    titulo = ft.Text("Hashzap")
    titulo_popup = ft.Text("Bem vindo ao Hashzap")
    usuario = ft.TextField(label="Digite seu nome")
    botao_popup = ft.ElevatedButton("Entrar", on_click=entrar_chat)

    
    popup = ft.AlertDialog(title=titulo_popup,
                           content=usuario,
                           actions=[botao_popup])
    
    chat = ft.Column()
    campo_mensagem = ft.TextField(label="Digite sua Mensagem")
    botao_enviar = ft.ElevatedButton("Enviar", 
                                     on_click=enviar_msg)  

    botao_iniciar = ft.ElevatedButton("Iniciar", 
                                      on_click=iniciar_chat)
    
    linha_mensagem = ft.Row([campo_mensagem, botao_enviar])

    pagina.add(titulo)
    pagina.add(botao_iniciar)

#ft.app(main)
#ABRIR NO NAVEGADOR
ft.app(main, view=ft.WEB_BROWSER)