# 1. Usa uma imagem oficial do Python, leve e baseada em Linux
FROM python:3.11-slim

# 2. Define o diretório de trabalho dentro do contentor
WORKDIR /app

# 3. Copia o ficheiro de dependências para o contentor
COPY requirements.txt .

# 4. Instala as dependências (sem usar cache para a imagem ficar mais leve)
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copia todo o restante código do projeto para dentro do contentor
COPY . .

# 6. Expõe a porta que o Uvicorn vai usar
EXPOSE 8000

# 7. O comando que será executado quando o contentor arrancar
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]