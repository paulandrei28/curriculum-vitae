from flask import Blueprint, render_template_string
from curriculum_vitae_data import (
    full_name,
    role,
    location,
    phone,
    email,
    github_url,
    github_handle,
    professional_summary,
    technical_stack,
    internships_and_early_experience,
    professional_experience,
    education,
    languages,
    additional_strengths,
)
from curriculum_vitae_template import curriculum_vitae_template

curriculum_vitae = Blueprint('curriculum_vitae', __name__)


@curriculum_vitae.route('/')
def curriculum_vitae_page():
    return render_template_string(
        curriculum_vitae_template,
        full_name=full_name,
        role=role,
        location=location,
        phone=phone,
        email=email,
        github_url=github_url,
        github_handle=github_handle,
        professional_summary=professional_summary,
        technical_stack=technical_stack,
        internships_and_early_experience=internships_and_early_experience,
        professional_experience=professional_experience,
        education=education,
        languages=languages,
        additional_strengths=additional_strengths,
    )
