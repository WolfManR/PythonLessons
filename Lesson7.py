from docxtpl import DocxTemplate
import csv
import json

directory_path = "Lesson7Files\\"
data_file = directory_path + 'data.txt'
template_file = directory_path + 'template.docx'
docx_result_file = directory_path + 'result.docx'
csv_result_file = directory_path + 'result.csv'
json_result_file = directory_path + 'result.json'

template_values = {'brand': '', 'model': '', 'fuel_cons': '', 'price': ''}

# Вручную создайте текстовый файл с данными (например, марка авто, модель авто, расход топлива, стоимость).
with open(data_file) as text:
    template_values['brand'] = text.readline().replace('\n', '')
    template_values['model'] = text.readline().replace('\n', '')
    template_values['fuel_cons'] = text.readline().replace('\n', '')
    template_values['price'] = text.readline().replace('\n', '')

print(template_values)

# Создайте шаблон документа doc
# Внесите данные из файла в шаблон
template = DocxTemplate(template_file)
template.render(template_values)
template.save(docx_result_file)

# Создайте csv-файл с данными о машине.
with open(csv_result_file, 'w') as csv_file:
    writer = csv.DictWriter(csv_file, delimiter=';', fieldnames=template_values.keys())
    writer.writeheader()
    writer.writerow(template_values)

# Создайте json-файл с данными о машине.
with open(json_result_file, 'w') as json_file:
    json.dump(template_values, json_file)
