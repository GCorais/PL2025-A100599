import re

def markdown_to_html(md_text):
    # Headers
    md_text = re.sub(r'^#\s+(.*)$', r'<h1>\1</h1>', md_text)
    md_text = re.sub(r'^##\s+(.*)$', r'<h2>\1</h2>', md_text)
    md_text = re.sub(r'^###\s+(.*)$', r'<h3>\1</h3>', md_text)
    md_text = re.sub(r'^####\s+(.*)$', r'<h4>\1</h4>', md_text)
    md_text = re.sub(r'^#####\s+(.*)$', r'<h5>\1</h5>', md_text)
    md_text = re.sub(r'^######\s+(.*)$', r'<h6>\1</h6>', md_text)

    # Bold
    md_text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', md_text)
    
    # Italic
    md_text = re.sub(r'\*(.*?)\*', r'<i>\1</i>', md_text)
    
    # Imagens
    md_text = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1"/>', md_text)

    # Links
    md_text = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', md_text)

    # Unordered Lists
    def process_ul(match):
        items = re.findall(r'(?m)^\s*-\s*(.+)$', match.group(0))
        list_html = "<ul>\n"
        for item in items:
            list_html += f"<li>{item}</li>\n"
        list_html += "</ul>"
        return list_html

    md_text = re.sub(r'(?m)(?:^\s*-\s*.+\n?)+', process_ul, md_text)

    # Ordered Lists
    def process_ol(match):
        items = re.findall(r'(?m)^\s*\d+\.\s*(.+)$', match.group(0))
        list_html = "<ol>\n"
        for item in items:
            list_html += f"<li>{item}</li>\n"
        list_html += "</ol>"
        return list_html

    md_text = re.sub(r'(?m)(?:^\s*\d+\.\s*.+\n?)+', process_ol, md_text)

    md_text = re.sub(r'\n\s*\n', '\n', md_text)
        
    return md_text

if __name__ == "__main__":
    print("Digite o texto Markdown (pressione Enter duas vezes para finalizar):")
    md_input = "\n".join(iter(input, ""))
    html_output = markdown_to_html(md_input)
    
    with open("resultados.txt", "w", encoding="utf-8") as f:
        f.write(html_output)
    
    print("Conversão concluída! Resultado salvo em 'resultados.txt'.")