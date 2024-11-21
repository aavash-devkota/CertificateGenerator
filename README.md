# Certificate Generator

Automate the creation of personalized certificates using Python. This tool reads participant names from an Excel file and generates certificates by overlaying the names onto a template image.

## 🎉 Features

- Generate certificates with custom fonts, colors, and positions.
- Supports Excel input for participant names.
- Outputs high-quality images for certificates.
- Simple setup and easy customization.

## 🛠️ Requirements

- Python 3.x
- Libraries: `Pillow`, `pandas`, `openpyxl`

## 📂 Project Structure

```
CertificateGenerator/
├── certificates/         # Generated certificates
├── fonts/                # Custom fonts
├── templates/            # Certificate templates
├── name_list.xlsx        # Input Excel file with participant names
├── generate_certificates.py  # Main Python script
└── README.md             # Project documentation
```

## 🚀 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/CertificateGenerator.git
   cd CertificateGenerator
   ```

2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Add your certificate template to the `templates/` folder and the font file to the `fonts/` folder.

4. Place your participant list in `name_list.xlsx` with a column named `Name`.

## 🖥️ Usage

Run the script:
```bash
python3 generate_certificates.py
```

Certificates will be saved in the `certificates/` directory.

## 🖋️ Customization

- **Font**: Replace the font in the `fonts/` folder and update the font path in the script.
- **Template**: Use your custom certificate template by replacing the file in `templates/`.
- **Name Position**: Adjust the `name_position` coordinates in the script to fit your template.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
