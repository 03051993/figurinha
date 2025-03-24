import streamlit as st
from PIL import Image
import io

st.title("Criador de Figurinhas para WhatsApp")

uploaded_file = st.file_uploader("Envie uma foto para criar a figurinha", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Abrir a imagem enviada
    image = Image.open(uploaded_file)

    # Redimensionar a imagem para 512x512 (tamanho ideal para figurinhas do WhatsApp)
    sticker_size = (512, 512)
    image = image.resize(sticker_size, Image.ANTIALIAS)

    # Exibir a imagem redimensionada
    st.image(image, caption="Pré-visualização da Figurinha", use_column_width=False)

    # Botão para baixar a figurinha
    buf = io.BytesIO()
    image.save(buf, format="PNG")
    byte_im = buf.getvalue()

    st.download_button(
        label="Baixar Figurinha",
        data=byte_im,
        file_name="figurinha.png",
        mime="image/png"
    )