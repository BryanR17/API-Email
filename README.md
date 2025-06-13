
# 📬 API de Contato 

Esta é uma API simples desenvolvida com Flask para receber dados de um formulário de contato e enviar por e-mail para o endereço que voce deseja

---

## 🚀 Funcionalidades

- ✅ Retorna mensagem padrão na rota principal (`/`)
- 📩 Recebe dados de formulário via POST (`/enviar`)
- ✉️ Envia e-mail automático com os dados do formulário
- 🌐 Suporte a requisições CORS (ideal para integração com frontend hospedado externamente)

---

## 🛠️ Tecnologias Utilizadas

- Python 3.x
- Flask
- Flask-CORS
- smtplib (SMTP via Gmail)
- EmailMessage (módulo `email`)

---

## 📥 Instalação e Execução

1. **Clone o repositório:**

```bash
git clone https://github.com/BryanR17/API-Email
cd API-Email
```

2. **Crie um ambiente virtual (opcional, mas recomendado):**

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

4. **Execute a aplicação:**

```bash
python app.py
```

---

## 📡 Rotas da API

### `GET /`
Retorna uma mensagem indicando que a API está online.

**Resposta:**
```json
{
  "message": "API está online"
}
```

---

### `POST /enviar`
Recebe um JSON com os dados do formulário:

**Corpo da requisição:**
```json
{
  "nome": "João Silva",
  "email": "joao@email.com",
  "telefone": "(64) 99999-9999",
  "mensagem": "Gostaria de contratar um site."
}
```

**Resposta de sucesso:**
```json
{
  "success": true,
  "message": "Mensagem enviada com sucesso!"
}
```

**Resposta de erro:**
```json
{
  "success": false,
  "message": "Erro ao enviar mensagem."
}
```

---

## ⚠️ Observações de Segurança

- 🔐 O arquivo contém credenciais sensíveis (e-mail e senha de app). Em produção, utilize variáveis de ambiente para manter esses dados seguros.
- 🔒 Ative a autenticação em 2 fatores no Gmail e utilize senhas de app (como feito aqui) para enviar e-mails com segurança.

