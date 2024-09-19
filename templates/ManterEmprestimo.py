import streamlit as st
import pandas as pd
from view import View
import time

class ManterEmprestimoUI:
  def main():
    st.header("Cadastro de Empréstimos")
    tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
    with tab1: ManterEmprestimoUI.listar()
    with tab2: ManterEmprestimoUI.inserir()
    with tab3: ManterEmprestimoUI.atualizar()
    with tab4: ManterEmprestimoUI.excluir()

  def listar():
    emprestimos = View.emprestimo_listar()
    if len(emprestimos) == 0:
      st.write("Nenhum Empréstimo cadastrado")
    else:
      dic = [] # lista de dicionários, onde cada dicionário é um cliente
      for obj in emprestimos: dic.append(obj.__dict__)
      df = pd.DataFrame(dic)
      st.dataframe(df)

  def inserir():
    valor = st.text_input("Informe o valor do empréstimo")
    data = st.text_input("Informe a data do empréstimo")
    duracao = st.text_input("Informe o tempo de duração do empréstimo")
    juros = st.text_input("Informe o juros")
    if st.button("Inserir"):
      try:
        View.emprestimo_inserir(valor, data, duracao, juros) #, senha)
        st.success("Empréstimo inserido com sucesso")
        time.sleep(2)
        st.rerun()
      except ValueError:
        st.write("Data inválida")  

  def atualizar():
    emprestimos = View.emprestimo_listar()
    if len(emprestimos) == 0:
      st.write("Nenhum Empréstimo cadastrado")
    else:
      op = st.selectbox("Atualização de Emprestimos", emprestimos)
      valor = st.text_input("Informe o novo valor", op.get_valor())
      data = st.text_input("Informe nova data", op.get_data())
      duracao = st.text_input("Informe a duração do empéstimo", op.get_duracao())
      juros = st.text_input("Informe o juros", op.get_juros())
      if st.button("Atualizar"):
        id = op.get_id()
        View.emprestimo_atualizar(id, valor, data, duracao, juros) #, senha)
        st.success("Dados do Emprestimo atualizados com sucesso")
        time.sleep(2)
        st.rerun()

  def excluir():
    emprestimos = View.emprestimo_listar()
    if len(emprestimos) == 0:
      st.write("Nenhum empréstimo cadastrado")
    else:
      op = st.selectbox("Exclusão de Empréstimos", emprestimos)
      if st.button("Excluir"):
        id = op.get_id()
        View.emprestimo_excluir(id)
        st.success("Empréstimo excluído com sucesso")
        time.sleep(2)
        st.rerun()