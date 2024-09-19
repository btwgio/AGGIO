import streamlit as st
import pandas as pd
from view import View
import time

class ManterAgiotaUI:
  def main():
    st.header("Cadastro de Agiotas")
    tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
    with tab1: ManterAgiotaUI.listar()
    with tab2: ManterAgiotaUI.inserir()
    with tab3: ManterAgiotaUI.atualizar()
    with tab4: ManterAgiotaUI.excluir()

  def listar():
    agiotas = View.agiota_listar()
    if len(agiotas) == 0:
      st.write("Nenhum agiota cadastrado")
    else:
      dic = [] # lista de dicionários, onde cada dicionário é um cliente
      for obj in agiotas: dic.append(obj.__dict__)
      df = pd.DataFrame(dic)
      st.dataframe(df)

  def inserir():
    nome = st.text_input("Informe o nome")
    celular = st.text_input("Informe o celular")
    endereco = st.text_input("Informe o endereco")
    credito = st.text_input("Informe o credito disponível")
    if st.button("Inserir"):
      try:
        View.agiota_inserir(nome, celular, endereco, credito) #, senha)
        st.success("Agiota inserido com sucesso")
        time.sleep(2)
        st.rerun()
      except ValueError:
        st.write("Nome e/ou celular inválidos")  

  def atualizar():
    agiotas = View.agiota_listar()
    if len(agiotas) == 0:
      st.write("Nenhum cliente cadastrado")
    else:
      op = st.selectbox("Atualização de Clientes", agiotas)
      nome = st.text_input("Informe o novo nome", op.get_nome())
      celular = st.text_input("Informe o novo celular", op.get_celular())
      endereco = st.text_input("Informe o novo endereco", op.get_endereco())
      credito = st.text_input("Informe o credito disponível", op.get_credito())
      if st.button("Atualizar"):
        id = op.get_id()
        View.agiota_atualizar(id, nome, celular, endereco, credito) #, senha)
        st.success("Dados do Agiota atualizados com sucesso")
        time.sleep(2)
        st.rerun()

  def excluir():
    agiotas = View.agiota_listar()
    if len(agiotas) == 0:
      st.write("Nenhum agiota cadastrado")
    else:
      op = st.selectbox("Exclusão de Agiotas", agiotas)
      if st.button("Excluir"):
        id = op.get_id()
        View.agiota_excluir(id)
        st.success("Agiota excluído com sucesso")
        time.sleep(2)
        st.rerun()