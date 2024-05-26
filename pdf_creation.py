from fpdf import FPDF
from datetime import date


class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Deployment Steps', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(10)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()


pdf = PDF()
pdf.add_page()

# Title page
pdf.set_font('Arial', 'B', 16)
pdf.cell(0, 10, 'Data Science Internship Submission', 0, 1, 'C')
pdf.ln(20)

# Details
pdf.set_font('Arial', '', 12)
pdf.cell(0, 10, f'Name: Glen Miasnychenko', 0, 1)
# pdf.cell(0, 10, f'Batch code: [Your Batch Code]', 0, 1)
pdf.cell(0, 10, f'Submission date: {date.today().strftime("%B %d, %Y")}', 0, 1)
pdf.cell(0, 10, f'Submitted to: Data Glacier', 0, 1)
pdf.ln(20)

# Step 1
pdf.chapter_title('Step 1: Load and Train Model')
pdf.chapter_body('We used the Iris dataset and trained a RandomForestClassifier. The model was saved using joblib.')

# Step 2
pdf.chapter_title('Step 2: Deploy Model using Flask')
pdf.chapter_body('We created a Flask app to serve the trained model and handle prediction requests.')

# Save the PDF
pdf.output('deployment_steps.pdf')
