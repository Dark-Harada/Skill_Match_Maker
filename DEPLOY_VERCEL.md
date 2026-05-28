# Deploy na Vercel

## 1. Criar MongoDB Atlas
- Crie um cluster gratuito no MongoDB Atlas.
- Copie sua string de conexão.

## 2. Variáveis de ambiente
Na Vercel:

Settings -> Environment Variables

Adicione:

MONGO_URL=sua_string_do_mongodb_atlas

## 3. Deploy
- Faça upload do projeto na Vercel.
- Framework: Other
- Root Directory: Skill_Match_Maker

## 4. Rodar localmente
Instale:

pip install -r requirements.txt

Depois:

uvicorn backend.main:app --reload