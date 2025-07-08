import streamlit as st
from PyPDF2 import PdfMerger

st.set_page_config(page_title="Merge de PDFs", page_icon="📄", layout="centered")

st.title("📑 *** Junte Arquivos de PDFs *** ")

with st.sidebar:
    st.header("ℹ️ Instruções")
    st.write("1. Faça upload dos arquivos PDF.")
    st.write("2. Clique no botão para gerar.")
    st.write("3. Baixe o PDF final.")
    st.markdown("---")
    st.write("🛠️ Por L. Paz - DIY Edition 😎")

uploaded_files = st.file_uploader(
    "Selecione os PDFs para juntar:",
    accept_multiple_files=True,
    type="pdf"
)
output_name = st.text_input(
    "Nome do arquivo final (sem .pdf):",
    value="Resultado_Final"
)
if uploaded_files:
    st.markdown("### Arquivos selecionados:")
    for file in uploaded_files:
        st.write(f"✔️ {file.name}")

    if st.button("🔗 Juntar PDFs Agora"):
        merger = PdfMerger()
        for pdf_file in uploaded_files:
            merger.append(pdf_file)

        output_filename = f"{output_name}.pdf"

        with open(output_filename, "wb") as f_out:
            merger.write(f_out)
        merger.close()

        st.success(f"✅ Sucesso! {len(uploaded_files)} PDFs foram unidos.")
        st.balloons()

        with open(output_filename, "rb") as f_out:
            st.download_button(
                label="📥 Baixar Resultado Final",
                data=f_out,
                file_name=output_filename,
                mime="application/pdf"
            )