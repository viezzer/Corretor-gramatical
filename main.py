import os
import openai
from flask import Flask, request, flash, redirect, render_template, url_for
# import telebot

API_KEY = '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'
openai.api_key = API_KEY

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/corrigir', methods=['POST'])
def corrigir():
    texto = request.form['texto']
    resposta = openai.Completion.create(
        engine="text-davinci-003",
        prompt=(f"Corrija os erros gramaticais no seguinte texto:\n{texto}\n"),
        temperature=0.7,
        max_tokens=60,
        n = 1,
        stop=None,
        timeout=10,
    )

    correcao = resposta.choices[0].text.strip()
    print(resposta.choices)
    return render_template('index.html', texto=texto, correcao=correcao)


if __name__ == "__main__":
  app.run(debug=True)