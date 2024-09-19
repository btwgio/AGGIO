import streamlit as st
import pandas as pd
from view import View
import time

class ManterCobradorUI:
  def main():
    st.header("Cadastro de Cobradores")
    tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
    with tab1: ManterCobradorUI.listar()
    with tab2: ManterCobradorUI.inserir()
    with tab3: ManterCobradorUI.atualizar()
    with tab4: ManterCobradorUI.excluir()

  def listar():
    cobradores = View.cobrador_listar()
    if len(cobradores) == 0:
      st.write("Nenhum cobrador cadastrado")
    else:
      dic = [] # lista de dicionários, onde cada dicionário é um cliente
      for obj in cobradores: dic.append(obj.__dict__)
      df = pd.DataFrame(dic)
      st.dataframe(df)

  def inserir():
    nome = st.text_input("Informe o nome")
    celular = st.text_input("Informe o celular")
    endereco = st.text_input("Informe o endereço")
    placa = st.text_input("Informe a placa do veículo")
    View.cobrador_listar()
    id_agiota = st.text_input("Informe o ID para qual agiota o cobrador trabalha ")
    if st.button("Inserir"):
      try:
        View.cobrador_inserir(nome, celular, endereco, placa, id_agiota) #, senha)
        st.success("Cobrador inserido com sucesso")
        time.sleep(2)
        st.rerun()
      except ValueError:
        st.write("Nome e/ou endereço inválidos")  

  def atualizar():
    cobradores = View.cobrador_listar()
    if len(cobradores) == 0:
      st.write("Nenhum cobrador cadastrado")
    else:
      op = st.selectbox("Atualização de Clientes", cobradores)
      nome = st.text_input("Informe o novo nome", op.get_nome())
      celular = st.text_input("Informe o novo celular", op.get_celular())
      endereco = st.text_input("Informe o novo endereço", op.get_endereco())
      placa = st.text_input("Informe a nova placa do veículo", op.get_placa_veiculo())
      Id_agiota = st.text_input("Informe o novo id do agiota para qual o cobrador trabalha")
      if st.button("Atualizar"):
        id = op.get_id()
        View.agiota_atualizar(id, nome, celular, endereco, placa, Id_agiota) #, senha)
        st.success("Dados do Cobrador atualizados com sucesso")
        time.sleep(2)
        st.rerun()

  def excluir():
    cobradores = View.cobrador_listar()
    if len(cobradores) == 0:
      st.write("Nenhum cobrador cadastrado")
    else:
      op = st.selectbox("Exclusão de Cobradores", cobradores)
      if st.button("Excluir"):
        id = op.get_id()
        View.cobrador_excluir(id)
        st.success("Cobrador excluído com sucesso")
        time.sleep(2)
        st.rerun()