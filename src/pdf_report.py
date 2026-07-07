"""
pdf_report.py

Generates a PDF report from the motion log.
"""

import csv
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph

from config import LOG_FILE, PDF_REPORT


def generate_report():

    document = SimpleDocTemplate(PDF_REPORT)

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph(
            "<b>Wildlife Motion Detection Report</b>",
            styles["Heading1"]
        )
    )

    story.append(Paragraph("<br/>", styles["Normal"]))

    with open(LOG_FILE, "r") as csvfile:

        reader = csv.reader(csvfile)

        next(reader)

        for row in reader:

            detection = row[0]
            date = row[1]
            time = row[2]

            if len(row) >= 4:
                session = row[3]
            else:
                session = "N/A"

            text = (
                f"<b>Detection #{detection}</b><br/>"
                f"Date: {date}<br/>"
                f"Time: {time}<br/>"
                f"Session Duration: {session}<br/><br/>"
            )

            story.append(
                Paragraph(text, styles["Normal"])
            )

    document.build(story)

    print("[PDF] Report updated.")