import docx
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_UNDERLINE
from docx.shared import Cm

doc = docx.Document()

def create_file_doc(tngc:list, plan:list, data:list):

	# Чтение файлов переноса
	# t = open('tngc.txt', 'r')
	# tngc = [line.strip() for line in t]
	# t.close()
	# p = open('plan.txt', 'r')
	# plan = [line.strip() for line in p]
	# p.close()
	# d = open('data.txt', 'r')
	# data = [line.strip() for line in d]
	# d.close()

	# Удаление пустых строк в data
	# data.remove('')

	# Формирование стиля всего документа
	style = doc.styles['Normal']
	style.font.name = 'Times New Roman'
	style.font.size = Pt(14)

	# run = doc.add_paragraph().add_run()
	# r_fmt = run.font
	# r_fmt.name = 'Times New Roman'
	# r_fmt.size = Pt(14)

	# Добавление Названия учреждения по центру
	paragraph = doc.add_paragraph(tngc[3])
	p_fmt = paragraph.paragraph_format
	p_fmt.alignment = WD_ALIGN_PARAGRAPH.CENTER

	# Отступ
	for i in range(0, 10):
		l = len(doc.paragraphs)
		doc.paragraphs[l-1].runs[0].add_break()

	# Тема по центру полужирным увеличенным шрифтом
	paragraph = doc.add_paragraph()
	p_fmt = paragraph.paragraph_format
	p_fmt.alignment = WD_ALIGN_PARAGRAPH.CENTER
	run = paragraph.add_run('Тема работы:')
	run.font.size = Pt(16)
	run.font.bold = False # Полужирный
	paragraph = doc.add_paragraph()
	p_fmt = paragraph.paragraph_format
	p_fmt.alignment = WD_ALIGN_PARAGRAPH.CENTER
	run = paragraph.add_run('"' + tngc[0] + '"')
	run.font.size = Pt(18)
	run.font.bold = True # Полужирный

	# Отступ
	for i in range(0, 8):
		l = len(doc.paragraphs)
		doc.paragraphs[l-1].runs[0].add_break()

	# Добавление информации об ученике по правому краю
	paragraph = doc.add_paragraph('Подготовил(а) студент(ка)')
	p_fmt = paragraph.paragraph_format
	p_fmt.alignment = WD_ALIGN_PARAGRAPH.RIGHT
	paragraph = doc.add_paragraph('Группы ' + tngc[2])
	p_fmt = paragraph.paragraph_format
	p_fmt.alignment = WD_ALIGN_PARAGRAPH.RIGHT
	paragraph = doc.add_paragraph(tngc[1])
	p_fmt = paragraph.paragraph_format
	p_fmt.alignment = WD_ALIGN_PARAGRAPH.RIGHT

	# Отступ
	for i in range(0, 4):
		l = len(doc.paragraphs)
		doc.paragraphs[l-1].runs[0].add_break()

	# Год по центру
	paragraph = doc.add_paragraph('2024')
	p_fmt = paragraph.paragraph_format
	p_fmt.alignment = WD_ALIGN_PARAGRAPH.CENTER

	# Разрыв страницы
	l = len(doc.paragraphs)
	doc.paragraphs[l-1].runs[0].add_break(docx.enum.text.WD_BREAK.PAGE)

	# Содержание
	paragraph = doc.add_paragraph()
	p_fmt = paragraph.paragraph_format
	p_fmt.alignment = WD_ALIGN_PARAGRAPH.CENTER
	run = paragraph.add_run('Содержание:')
	run.font.size = Pt(16)
	run.font.bold = True # Полужирный
	l = len(doc.paragraphs)
	doc.paragraphs[l-1].runs[0].add_break()
	n = 1
	for item in plan:
		doc.add_paragraph(str(n) + '. ' + item)
		n = n + 1

	# Разрыв страницы
	l = len(doc.paragraphs)
	doc.paragraphs[l-1].runs[0].add_break(docx.enum.text.WD_BREAK.PAGE)

	n = 1
	i = 0
	for item in plan:
		paragraph = doc.add_paragraph()
		run = paragraph.add_run(str(n) + '. ' + item)
		run.font.size = Pt(16)
		run.font.bold = True # Полужирный

		paragraph = doc.add_paragraph(data[i])
		p_fmt = paragraph.paragraph_format
		p_fmt.first_line_indent = Cm(1.5)
		p_fmt.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

		# Разрыв страницы
		# l = len(doc.paragraphs)
		# doc.paragraphs[l-1].runs[0].add_break(docx.enum.text.WD_BREAK.PAGE)

		n = n + 1
		i = i + 1

	doc.add_paragraph()

	doc.save('output.docx')