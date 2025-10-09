from docx import Document

# Load the .docx file
doc = Document("C:/Users/matte/Documents/testdocreader.docx") #specify the path to your .docx file here

# Extract all text
full_text = []
for para in doc.paragraphs:
    full_text.append(para.text)

# Join all paragraphs into a single string
text = "\n".join(full_text)
print(text)
