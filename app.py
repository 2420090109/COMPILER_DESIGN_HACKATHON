import streamlit as st
import pandas as pd
import re
from parse_tree import generate_parse_tree
# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(
    page_title="Compiler Visualization Tool",
    page_icon="⚙️",
    layout="wide"
)

# ---------------------------
# Custom CSS
# ---------------------------
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}

h1 {
    text-align: center;
    color: #1E3A8A;
}

.stButton > button {
    width: 100%;
    height: 50px;
    font-size: 18px;
}

.metric-card {
    text-align:center;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------
# Header
# ---------------------------
st.markdown("""
<h1>⚙️ Compiler Visualization Tool</h1>
<p style='text-align:center'>
Interactive Demonstration of Compiler Design Phases
</p>
""", unsafe_allow_html=True)

# ---------------------------
# Sidebar
# ---------------------------
st.sidebar.title("Compiler Phases")

st.sidebar.info("""
1. Lexical Analysis
2. Syntax Analysis
3. Symbol Table
4. Three Address Code
5. Code Optimization
6. Target Code Generation
""")

# ---------------------------
# Input Area
# ---------------------------
col1, col2 = st.columns([3, 1])

with col1:
    code = st.text_area(
    "Enter Source Code",
    "",
    height=250,
    placeholder="Type your code here..."
)

with col2:
    st.info("""
### Instructions
Enter C-style declarations:

```c
int a = 10;
int b = 20;
int c = a + b;""")

#---------------------------
#Compile Button
#---------------------------

if st.button("Compile"):

    st.subheader("Source Code")
    st.code(code, language="c")

# ---------------------------
# Lexical Analysis
# ---------------------------
token_specification = [
    ('KEYWORD', r'\b(int|float|char)\b'),
    ('NUMBER', r'\b\d+\b'),
    ('IDENTIFIER', r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'),
    ('OPERATOR', r'[+\-*/=]'),
    ('SEMICOLON', r';'),
    ('SKIP', r'[ \t\n]+'),
    ('MISMATCH', r'.')
]

tok_regex = '|'.join(
    '(?P<%s>%s)' % pair
    for pair in token_specification
)

tokens = []

for mo in re.finditer(tok_regex, code):
    kind = mo.lastgroup
    value = mo.group()

    if kind == "SKIP":
        continue

    if kind == "MISMATCH":
        continue

    tokens.append([value, kind])

token_df = pd.DataFrame(
    tokens,
    columns=["Lexeme", "Token Type"]
)

# ---------------------------
# Syntax Analysis
# ---------------------------
lines = [
    line.strip()
    for line in code.splitlines()
    if line.strip()
]

syntax_ok = True

declaration_pattern = (
    r'^int\s+[a-zA-Z_]\w*'
    r'\s*=\s*[a-zA-Z0-9_+\-*/ ]+;$'
)

for line in lines:
    if not re.match(declaration_pattern, line):
        syntax_ok = False
        break

# ---------------------------
# Symbol Table
# ---------------------------
symbol_table = []

for line in lines:

    match = re.match(
        r'int\s+(\w+)\s*=\s*(.+);',
        line
    )

    if match:
        variable = match.group(1)
        value = match.group(2)

        symbol_table.append(
            [variable, "int", value]
        )

symbol_df = pd.DataFrame(
    symbol_table,
    columns=["Variable", "Type", "Value"]
)

# ---------------------------
# TAC
# ---------------------------
tac = []

for line in lines:

    match = re.match(
        r'int\s+(\w+)\s*=\s*(.+);',
        line
    )

    if match:

        lhs = match.group(1)
        rhs = match.group(2).strip()

        if '+' in rhs:

            op1, op2 = [
                x.strip()
                for x in rhs.split('+')
            ]

            tac.append(f"t1 = {op1} + {op2}")
            tac.append(f"{lhs} = t1")

        else:
            tac.append(f"{lhs} = {rhs}")

# ---------------------------
# Optimization
# ---------------------------
optimized = []

for line in tac:

    match = re.match(
        r'(\w+)\s*=\s*(\d+)\s*\+\s*(\d+)',
        line
    )

    if match:

        var = match.group(1)
        a = int(match.group(2))
        b = int(match.group(3))

        optimized.append(
            f"{var} = {a+b}"
        )

    else:
        optimized.append(line)

# ---------------------------
# Assembly
# ---------------------------
assembly = []

for line in lines:

    match = re.match(
        r'int\s+(\w+)\s*=\s*(.+);',
        line
    )

    if match:

        lhs = match.group(1)
        rhs = match.group(2).strip()

        if '+' in rhs:

            op1, op2 = [
                x.strip()
                for x in rhs.split('+')
            ]

            assembly.append(f"MOV R1, {op1}")
            assembly.append(f"ADD R1, {op2}")
            assembly.append(f"MOV {lhs}, R1")

        else:

            assembly.append(f"MOV {lhs}, {rhs}")

# ---------------------------
# Metrics
# ---------------------------
m1, m2, m3 = st.columns(3)

m1.metric("Tokens", len(tokens))
m2.metric("Variables", len(symbol_table))
m3.metric("TAC Instructions", len(tac))

# ---------------------------
# Tabs
# ---------------------------
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "Lexical Analysis",
    "Syntax Analysis",
    "Symbol Table",
    "Parse Tree",
    "TAC",
    "Optimization",
    "Assembly"
])

with tab1:
    st.subheader("Tokens")
    st.table(token_df)

with tab2:
    st.subheader("Syntax Result")

    if syntax_ok:
        st.success("Syntax Valid")
    else:
        st.error("Syntax Error")

with tab3:
    st.subheader("Symbol Table")
    st.table(symbol_df)
with tab4:
    st.subheader("Parse Tree")

    tree = generate_parse_tree()

    st.graphviz_chart(tree)

with tab5:
    st.subheader("Three Address Code")

    for instruction in tac:
        st.code(instruction)

with tab6:
    st.subheader("Optimized Code")

    for line in optimized:
        st.code(line)

with tab7:
    st.subheader("Assembly Code")

    for inst in assembly:
        st.code(inst)