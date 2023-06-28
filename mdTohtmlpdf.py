import sys
sys.path.append(r'C:\Users\P65\AppData\Local\Programs\Python\Python311\Lib\site-packages')
import os
import tkinter as tk
from tkinter import filedialog
import pdfkit
import markdown

# 將Markdown轉換為HTML
def markdown_to_html(markdown_text):
    html_text = markdown.markdown(markdown_text)
    return html_text

# 將HTML轉換為PDF
def html_to_pdf(html_text, output_folder_path, file_path):
    options = {
        'page-size': 'A4',
        'encoding': 'UTF-8'
    }
    # 生成輸出的HTML檔案名稱
    filename_without_extension = os.path.splitext(os.path.basename(file_path))[0]
    html_filename = f"{filename_without_extension}.html"
    html_path = os.path.join(output_folder_path, html_filename)

    # 保存HTML檔案
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_text)

    # 生成輸出的PDF檔案名稱
    pdf_filename = f"{filename_without_extension}.pdf"
    pdf_path = os.path.join(output_folder_path, pdf_filename)

    # 將HTML轉換為PDF
    pdfkit.from_file(html_path, pdf_path, options=options)

# 選擇要轉換的MD檔案
def select_file():
    file_path = filedialog.askopenfilename(filetypes=[('Markdown Files', '*.md')])
    if file_path:
        convert_file(file_path)

# 轉換檔案
def convert_file(file_path):
    # 讀取Markdown文件
    with open(file_path, 'r', encoding='utf-8') as f:
        md_text = f.read()

    # 將Markdown轉換為HTML
    html_text = markdown_to_html(md_text)

    # 選擇輸出資料夾
    output_folder_path = filedialog.askdirectory()

    if output_folder_path:
        # 將HTML轉換為PDF
        html_to_pdf(html_text, output_folder_path, file_path)

# 建立UI
root = tk.Tk()
root.title("Markdown轉換程式")

# 按鈕：選擇檔案
select_button = tk.Button(root, text="選擇檔案", command=select_file)
select_button.pack()

# 啟動UI主迴圈
root.mainloop()

