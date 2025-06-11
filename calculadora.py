import streamlit as st

# Título da aplicação
st.title("🧮 Calculadora Simples")

# Entrada de números
num1 = st.number_input("Digite o primeiro número", format="%.2f")
num2 = st.number_input("Digite o segundo número", format="%.2f")

# Seleção da operação
operacao = st.selectbox("Escolha a operação", ["Soma", "Subtração", "Multiplicação", "Divisão"])

# Botão de calcular
if st.button("Calcular"):
    if operacao == "Soma":
        resultado = num1 + num2
        st.success(f"Resultado: {resultado}")
    elif operacao == "Subtração":
        resultado = num1 - num2
        st.success(f"Resultado: {resultado}")
    elif operacao == "Multiplicação":
        resultado = num1 * num2
        st.success(f"Resultado: {resultado}")
    elif operacao == "Divisão":
        if num2 != 0:
            resultado = num1 / num2
            st.success(f"Resultado: {resultado}")
        else:
            st.error("Erro: Divisão por zero não é permitida.")
