import streamlit as st
import oguid

def convert(input: str, func) -> str:
    lines = input.splitlines()
    result_lines = [func(line) for line in lines]
    result = "\n".join(result_lines)
    return result

def gen_func(input: str, convert_to:str):
    lines = input.splitlines()
    if lines == []:
        return passfunc

    convert_from = oguid.guess_id_type(lines[0])

    select = (convert_from, convert_to)
    match select:
        case ("email", "OGU-Caddie"):
            result = oguid.email_to_caddie
        case ("email", "OGU Web Service"):
            result =  oguid.email_to_webservice
        case ("OGU-Caddie", "email"):
            result =  oguid.caddie_to_email
        case ("OGU-Caddie", "OGU Web Service"):
            result =  oguid.caddie_to_webservice
        case ("OGU Web Service", "email"):
            result = oguid.webservice_to_email
        case ("OGU Web Service", "OGU-Caddie"):
            result = oguid.webservice_to_caddie
        case (_, _):
            result = passfunc
    return result

st.title("OGU email-ID Converter ")
col1, col2 = st.columns(2)

email = email2 = "email"
caddie = caddie2 = "OGU-Caddie"
web = web2 = "OGU Web Service"

with col1:
    input = st.text_area("input (ctrl + enter)", height=465)
    id_type = oguid.guess_id_type(input)


def passfunc(input: str) -> str:
    return input

if input is None:
    input = ""

with col2:
    if id_type is None:
        id_type = ""
    
    l = [email, caddie, web]

    convert_to = st.selectbox(
        id_type + " to",
        l
    )
    func = gen_func(input, convert_to)
    st.text_area("output", value=convert(input, func), height=380)