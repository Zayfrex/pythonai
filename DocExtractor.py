from docx import Document

# Load the .docx file
doc = Document("C:/Users/Matteo/Documents/ThisIsAI.docx")

# Extract all text
full_text = []
for para in doc.paragraphs:
    full_text.append(para.text)

# Join all paragraphs into a single string
text = "\n".join(full_text)
print(text)
