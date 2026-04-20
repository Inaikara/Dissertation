import fitz  # PyMuPDF
import re

def count_pdf_words(file_path):
    try:
        # 打开 PDF 文件
        doc = fitz.open(file_path)
        full_text = ""

        # 逐页提取文本
        for page in doc:
            full_text += page.get_text()

        doc.close()

        # --- 统计逻辑 ---
        
        # 1. 统计中文字符 (匹配所有中文字符区间)
        chinese_chars = re.findall(r'[\u4e00-\u9fa5]', full_text)
        chinese_count = len(chinese_chars)

        # 2. 统计英文单词 (按空格和标点切分的连续字母)
        english_words = re.findall(r'[a-zA-Z]+', full_text)
        english_count = len(english_words)

        # 3. 统计数字
        numbers = re.findall(r'\d+', full_text)
        number_count = len(numbers)

        # 4. 统计标点及其他字符 (可选)
        # 如果你只想看传统意义上的“字数”，通常是 中文数 + 英文单词数
        total_word_count = chinese_count + english_count

        print(f"--- 统计结果 ---")
        print(f"文件路径: {file_path}")
        print(f"中文字符数: {chinese_count}")
        print(f"英文单词数: {english_count}")
        print(f"数字出现次数: {number_count}")
        print(f"总字数 (中+英): {total_word_count}")
        print(f"----------------")

        return {
            "chinese": chinese_count,
            "english": english_count,
            "total": total_word_count
        }

    except Exception as e:
        print(f"读取文件出错: {e}")
        return None

# --- 使用示例 ---
if __name__ == "__main__":
    path = "盲审版本.pdf"  # 替换为你的 PDF 文件路径
    count_pdf_words(path)