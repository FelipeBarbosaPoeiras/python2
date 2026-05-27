import math
from flask import render_template, request

def calcular():
    num1 = float(request.form["num1"])
    operacao = request.form["operacao"]

    # Operações que usam apenas o primeiro número
    if operacao == "sqrt":
        if num1 < 0:
            resultado = "Erro: número negativo"
            etapas = f"Não existe raiz real de {num1}."
        else:
            resultado = math.sqrt(num1)
            etapas = f"√{num1} = {resultado}"
            
    elif operacao == "log":
        if num1 <= 0:
            resultado = "Erro: valor inválido"
            etapas = f"Não existe logaritmo base 10 de {num1} (deve ser maior que zero)."
        else:
            resultado = math.log10(num1)
            etapas = f"log10({num1}) = {resultado}"
            
    # Operações que exigem o segundo número
    else:
        num2_valor = request.form.get("num2", "").strip()
        if not num2_valor:
            return render_template(
                "calculadora.html",
                etapas="Informe o segundo número para esta operação.",
                resultados="",
            )
        num2 = float(num2_valor)

        if operacao == "+":
            resultado = num1 + num2
            etapas = f"{num1} + {num2} = {resultado}"
            
        elif operacao == "-":
            resultado = num1 - num2
            etapas = f"{num1} - {num2} = {resultado}"
            
        elif operacao == "*":
            resultado = num1 * num2
            etapas = f"{num1} × {num2} = {resultado}"
            
        elif operacao == "/":
            if num2 == 0:
                resultado = "Erro: divisão por zero"
                etapas = f"{num1} / {num2} não é permitido."
            else:
                resultado = num1 / num2
                etapas = f"{num1} ÷ {num2} = {resultado}"
                
        elif operacao == "**":
            resultado = math.pow(num1, num2)
            etapas = f"{num1} ^ {num2} = {resultado}"
            
        else:
            resultado = "Erro"
            etapas = "Operação inválida."

    return render_template(
        "calculadora.html",
        etapas=etapas,
        resultados=resultado
    )
