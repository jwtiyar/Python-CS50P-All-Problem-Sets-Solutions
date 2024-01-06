from fpdf import FPDF


class Shirtificate:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        self.name = input("Write Your Name: ")
        return self.name

    def make_pdf(self):
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()
        pdf.set_auto_page_break(auto=False, margin=0)
        pdf.set_font("helvetica", "B", 16)
        pdf.cell(200, 20, "CS50 Shirtificate", align="C")
        pdf.image("shirtificate.png", h=260, w=160, x=30, y=30)
        pdf.set_text_color(r=255, g=255, b=255)
        pdf.cell(-200, 170, txt=f"{self.name} took CS50", align="C")
        pdf.output("shirtificate.pdf")


def main():
    anjam = Shirtificate(None)
    anjam.name = anjam.get_name()
    anjam.make_pdf()


if __name__ == "__main__":
    main()
