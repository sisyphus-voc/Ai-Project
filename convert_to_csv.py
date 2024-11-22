import csv
from dataset import faq_dataset  # Import faq_dataset directly

csv_file = 'faq_dataset.csv'

with open(csv_file, mode='w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    # Write the header
    writer.writerow(['Category', 'Question', 'Answer'])

    # Write each FAQ entry
    for faq in faq_dataset:
        writer.writerow([faq['category'], faq['question'], faq['answer']])

print(f"CSV file '{csv_file}' has been created.")
