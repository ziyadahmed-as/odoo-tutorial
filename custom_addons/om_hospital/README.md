# Hospital Management: Data Architecture

This is the `om_hospital` custom Odoo module created for the Module 2 Project.

## Selection Field vs Char Field for Gender

A `Selection` field was chosen for the `gender` field instead of a `Char` field for the following reasons:

1. **Data Integrity**: Using a selection field enforces valid options (Male, Female, Other). If a Char field were used, users could input typos (e.g., "Mlae"), inconsistent casing ("male", "Male", "MALE"), or invalid entries.
2. **User Experience**: The selection field generates a convenient dropdown list in the Odoo user interface, making it easier and faster for the user to select the appropriate value without having to type it out.
3. **Database Optimization**: Selection fields map keys to labels. In the database, only the key (a predictable string) is stored, making querying, grouping, and filtering by gender much more efficient and reliable compared to unstructured text.
4. **Localization/Translation**: Selection field labels can easily be translated into different languages within Odoo, while the underlying key remains consistent for logic and reporting.
