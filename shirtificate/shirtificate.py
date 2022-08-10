def main():
    '''
    1. Ask for name input
    2. Format the PDF at the right orientation, size, texts, etc.
    3. Combine name input w/ 'took CS50'
    4. Add text to PDF
    '''
    shirtificate()


def shirtificate():
    from fpdf import FPDF

    name = input('Name: ')
    title = 'CS50 Shirtificate'
    cs_name = name + ' ' + 'took CS50'

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", "B", 36)
    pdf.cell(190, 10, title, align='C')
    pdf.ln()
    pdf.ln()
    pdf.ln()
    pdf.image('shirtificate.png', w=190)
    pdf.set_xy(10, 100)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("helvetica", "B", 24)
    pdf.cell(190, 10, cs_name, align='C')
    pdf.output("shirtificate.pdf")


if __name__ == '__main__':
    main()