"""
pdf_report.py

Generates a PDF report from the motion log.
"""

import csv

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph

from config import LOG_FILE
from config import PDF_REPORT


def generate_report():

    document = SimpleDocTemplate(PDF_REPORT)

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>Wildlife Motion Detection Report</b>", styles["Heading1"]))
    story.append(Paragraph("<br/>", styles["Normal"]))

    with open(LOG_FILE, "r") as csvfile:

        reader = csv.reader(csvfile)

        next(reader)

        for row in reader:

            detection = row[0]
            date = row[1]
            time = row[2]

            story.append(
                Paragraph(
                    f"<b>Detection #{detection}</b><br/>"
                    f"Date: {date}<br/>"
                    f"Time: {time}<br/><br/>",
                    styles["Normal"]
                )
            )

    document.build(story)

    print("[PDF] Report updated.")