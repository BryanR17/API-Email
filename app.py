@app.route('/enviar', methods=['POST'])
def enviar():
    try:
        if not request.is_json:
            return jsonify({'success': False, 'message': 'Requisição deve estar no formato JSON'}), 400

        data = request.get_json()
        nome = data.get('nome')
        email_usuario = data.get('email')
        telefone = data.get('telefone')
        mensagem = data.get('mensagem')

        # Configuração do e-mail
        remetente = 'rodeksolucaoemti@gmail.com'
        senha = 'cloc urzk mrew ibkg'
        destinatario = ['bryanrodrigues3002@gmail.com', 'paulianecardoso@gmail.com']

        conteudo = f"""
        Novo formulário recebido:

        Nome: {nome}
        Email: {email_usuario}
        Telefone: {telefone}
        Mensagem: {mensagem}
        """

        msg = EmailMessage()
        msg['Subject'] = 'Formulário do site'
        msg['From'] = remetente
        msg['To'] = ', '.join(destinatario)
        msg.set_content(conteudo)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(remetente, senha)
            smtp.send_message(msg)

        return jsonify({'success': True, 'message': 'Mensagem enviada com sucesso!'})
    
    except Exception as e:
        print(f"Erro interno: {e}")
        return jsonify({'success': False, 'message': 'Erro ao enviar mensagem.'}), 500

