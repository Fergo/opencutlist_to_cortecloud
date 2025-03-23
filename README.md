## OpenCutList to CorteCloud ##

Utilitário de conversão do OpenCutList do SketchUp para o padrão do CorteCloud.

O script espera que o CSV exportado pelo OpenCutList possua as seguintes colunas na seguinte ordem (essa opções podem ser configuradas na tela de exportação do OCL):

1. Quantity
2. Length - raw
3. Width - raw
4. Designation
5. Edge Length 1
6. Edge Length 2
7. Edge Width 1
8. Edge Width 2
9. Material
10. Type

O resultado é um segundo arquivo CSV (porém com tabulações separando as colunas) que pode ser colado diretamente na tela de importação do CorteCloud.

## Uso ##

`python opencutlist_to_cortecloud.py csv_input csv_output`
