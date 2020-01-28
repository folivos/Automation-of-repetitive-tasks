class Escribe_word():
    def __init__(self):
        pass
    # Formato para proyectos en desarrollo

    def desarrollo(self,doc, texto_tipo_proyecto):
        for i in range(len(texto_tipo_proyecto)):
            for j in range(len(texto_tipo_proyecto[0][:])):
                n = 1
                if j == 0 or (j - 0) % (n * 8) == 0:
                    pass
                    # doc.add_paragraph(texto_tipo_proyecto[i][j], 'Subtitle')
                if j == 1 or (j - 1) % (n * 8) == 0:
                    doc.add_paragraph(texto_tipo_proyecto[i][j], 'No Spacing')
                if j == 2 or (j - 2) % (n * 8) == 0:
                    doc.add_paragraph(texto_tipo_proyecto[i][j], 'No Spacing')
                if j == 3 or (j - 3) % (n * 8) == 0:
                    doc.add_paragraph(texto_tipo_proyecto[i][j], 'Subtitle')
                if j == 4 or (j - 4) % (n * 8) == 0:
                    doc.add_paragraph(texto_tipo_proyecto[i][j], 'No Spacing')
                if j == 5 or (j - 5) % (n * 8) == 0:
                    doc.add_paragraph(texto_tipo_proyecto[i][j], 'Subtitle')
                if j == 6 or (j - 6) % (n * 8) == 0:
                    doc.add_paragraph(texto_tipo_proyecto[i][j], 'No Spacing')
                if j == 7 or (j - 7) % (n * 8) == 0:
                    doc.add_paragraph(texto_tipo_proyecto[i][j], 'No Spacing')
                n = +1

            doc.add_paragraph('\n', 'No Spacing')



    # Formato para proyectos en estudio

    def estudios(self,doc, texto_tipo_proyecto):
        for i in range(len(texto_tipo_proyecto)):
            for j in range(len(texto_tipo_proyecto[0][:])):
                n = 1
                if j == 0 or (j - 0) % (n * 3) == 0:
                    doc.add_paragraph(texto_tipo_proyecto[i][j], 'Subtitle')
                if j == 1 or (j - 1) % (n * 3) == 0:
                    doc.add_paragraph(texto_tipo_proyecto[i][j], 'Subtitle')
                if j == 2 or (j - 2) % (n * 3) == 0:
                    doc.add_paragraph(texto_tipo_proyecto[i][j], 'No Spacing')
                n = +1

            doc.add_paragraph('\n', 'No Spacing')