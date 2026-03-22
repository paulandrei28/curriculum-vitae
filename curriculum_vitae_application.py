from flask import Flask, render_template, send_from_directory
from curriculum_vitae_content import curriculum_vitae_content

app = Flask(__name__)


@app.route('/')
def curriculum_vitae_homepage():
    return render_template('curriculum_vitae_homepage.html', curriculum_vitae=curriculum_vitae_content)


@app.route('/download/curriculum-vitae')
def download_curriculum_vitae():
    return send_from_directory(
        'static/documents',
        'paul_sipos_curriculum_vitae.pdf',
        as_attachment=True,
        download_name='Paul_Sipos_Curriculum_Vitae.pdf'
    )


if __name__ == '__main__':
    app.run(debug=True)
