import streamlit as st
import oguid

def convert(input: str, func) -> str:
    """
    テキストエリアからidのリストを受けとり、
    引数にとった関数を適用して別のテキストエリアに返す
    """
    lines = input.splitlines()
    result_lines = [func(line) for line in lines]
    result = "\n".join(result_lines)
    return result


def gen_func(input: str, convert_to:str):
    """1行目の文字からidのタイプを推測し、ユーザーの指定するタイプに変換する関数を作る

    Args:
        input (str): email, caddie, web serviceの3通り
        convert_to (str): email, caddie, web serviceの3通り

    Returns:
        func
    """    
    lines = input.splitlines()
    if lines == []:
        return passfunc

    convert_from = oguid.guess_id_type(lines[0])

    dic = {
        "email": "email",
        "OGU-Caddie": "caddie",
        "OGU Web Service": "web"
    }

    result = oguid.convert(source=dic[convert_from], target=dic[convert_to])

    if result is None:
        result = passfunc

    return result


def passfunc(input: str) -> str:
    return input


st.title("OGU email-ID Converter ")
col1, col2 = st.columns(2)

email = "email"
caddie = "OGU-Caddie"
web = "OGU Web Service"

with col1:
    input = st.text_area("input", height=465)

id_type = oguid.guess_id_type(input)

if input is None:
    input = ""

with col2:
    if id_type is None:
        id_type = ""
    
    match id_type:
        case "email":
            id_types = [caddie, web]
        case "OGU-Caddie":
            id_types = [email, web]
        case "OGU Web Service":
            id_types = [email, caddie]
        case _:
            id_types = [email, caddie, web]
    
    if id_type is "":
        bold_id_type = ""
    else:
        bold_id_type = "**" + id_type + "**"

    convert_to = st.selectbox(
        bold_id_type + " to",
        id_types 
    )
    func = gen_func(input, convert_to)
    st.text_area("output", value=convert(input, func), height=380)